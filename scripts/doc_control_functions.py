import sqlite3
from pathlib import Path
from config import storage_root_path
import os
import shutil
import json
import hashlib
from datetime import datetime

from doc_class import Document_Header, Document_Version
from config import document_types, template_map


def create_new_document(
    title: str, type: str, owner_id: int, db_path: str
) -> tuple[Document_Header, Document_Version]:
    if type not in document_types.values():
        raise (ValueError(f"Invalid type, not in valid types: '{type}'"))
    tmp_path: str = template_map.get(type.upper())  # type: ignore
    if not tmp_path:
        raise ValueError(
            f"Configuration Error: No template or mock found for type '{type}'"
        )
    with sqlite3.connect(db_path) as db:
        cursor: sqlite3.Cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM documents WHERE title = ?", (title,))
        if cursor.fetchone()[0] > 0:
            raise ValueError(f"Document title already exists: '{title}'")
        cursor.execute(
            "SELECT count(*) FROM users WHERE user_id = ? AND active_flag = 1",
            (owner_id,),
        )
        if cursor.fetchone()[0] == 0:
            raise ValueError(f"Owner ID {owner_id} does not exist or is inactive")
        cursor.execute("SELECT MAX(doc_id) FROM documents")
        last_doc_id: int | None = cursor.fetchone()[0]
        next_doc_id: int = 1 if last_doc_id is None else last_doc_id + 1

        cursor.execute("SELECT MAX(version_id) FROM versions")
        last_ver_id: int | None = cursor.fetchone()[0]
        next_ver_id: int = 1 if last_ver_id is None else last_ver_id + 1

        cursor.execute(
            "SELECT doc_num FROM documents WHERE type = ? ORDER BY doc_id DESC LIMIT 1",
            (type,),
        )
        result_num: tuple | None = cursor.fetchone()

        if result_num is None:
            next_doc_num: str = f"{type}-001"
        else:
            last_num_str: str = result_num[0]
            parts: list[str] = last_num_str.split("-")
            if len(parts) < 2:
                next_doc_num: str = f"{type}-001"
            else:
                current_seq: int = int(parts[1])
                next_seq: int = current_seq + 1
                next_doc_num: str = f"{type}-{next_seq:03d}"
    copy_path: Path = Path(tmp_path)
    extension_file: str = os.path.splitext(tmp_path)[1]
    destination_folder: Path = Path(storage_root_path) / "01_drafts"
    file_name: str = f"{next_doc_num}_V0.1_DRAFT{extension_file}"
    destination_path_root = destination_folder / file_name
    shutil.copy(copy_path, destination_path_root)
    new_document: Document_Header = Document_Header(
        next_doc_id, next_doc_num, title, owner_id, type
    )
    new_version: Document_Version = Document_Version(
        next_ver_id, next_doc_id, "0.1", "DRAFT", str(destination_path_root), None
    )
    return (new_document, new_version)


def write_new_doc(
    header: Document_Header,
    version: Document_Version,
    db_path: str,
) -> None:
    with sqlite3.connect(db_path) as db:
        try:
            db.execute(
                "INSERT INTO documents (doc_id, doc_num, title, owner_id, type) VALUES (?, ?, ?, ?, ?)",
                header.to_db_tuple(),
            )
            db.execute(
                "INSERT INTO versions (version_id, doc, version, status, file_path, effective_date) VALUES (?, ?, ?, ?, ?, ?)",
                version.to_db_tuple(),
            )
            db.commit()

        except sqlite3.Error as e:
            db.rollback()
            raise e
    audit_log_documents(header, version, db_path)


def prepare_audit_data(
    document: Document_Header,
    version: Document_Version,
    db_path: str,
) -> tuple[dict | None, dict]:  # type: ignore
    with sqlite3.connect(db_path) as db:
        cur: sqlite3.Cursor = db.cursor()
        cur.execute("SELECT count(*) FROM versions WHERE doc = ?", (document.id,))
        count_result: tuple | None = cur.fetchone()
        version_count: int = count_result[0] if count_result else 0
        if version_count <= 1:
            old_val = None
            new_val: dict = {
                "id": document.id,
                "doc_num": document.number,
                "title": document.title,
                "owner": document.owner,
                "version": version.label,
                "status": version.status,
                "path": version.file_path,
                "effective_date": version.effective_date,
            }
            return old_val, new_val
        else:
            raise (NotImplementedError)


def audit_log_documents(
    document: Document_Header,
    version: Document_Version,
    db_path: str,
) -> None:
    old_val, new_val = prepare_audit_data(document, version, db_path=db_path)
    old_val_json: str | None = json.dumps(old_val) if old_val is not None else None
    new_val_json: str = json.dumps(new_val)
    timestamp: str = datetime.now().isoformat()
    action: str = "CREATE" if not old_val else "UPDATE"
    table_affected: str = "documents"

    str_old: str = old_val_json if old_val_json else ""
    raw_str_hash: str = f"{table_affected}{document.id}{document.owner}{action}{str_old}{new_val_json}{timestamp}"
    row_hash: str = hashlib.sha256(raw_str_hash.encode("utf-8")).hexdigest()

    query_insert: str = """
        INSERT INTO audit_log (table_affected, record_id, user, action, old_val, new_val, timestamp, hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

    with sqlite3.connect(db_path) as db:
        try:
            db.execute(
                query_insert,
                (
                    table_affected,
                    document.id,
                    document.owner,
                    action,
                    old_val_json,
                    new_val_json,
                    timestamp,
                    row_hash,
                ),
            )
            db.commit()
        except sqlite3.Error as e:
            db.rollback()
            raise e
