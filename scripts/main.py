from create_doc import create_new_document
from actions import doc_action
from revise_doc import revise_doc
from config import db_path
from datetime import datetime


if __name__ == "__main__":
    create_new_document("test1", "SOP", "albert.sevilleja", db_path)
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "SOP-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("quality.manager", "SOP-001", db_path, datetime.now().isoformat())
    revise_doc("quality.manager", "SOP-001", db_path)
    create_new_document("test2", "SOP", "albert.sevilleja", db_path)
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "SOP-002", db_path)
    document_action = doc_action("APPROVE")
    document_action("quality.manager", "SOP-002", db_path, datetime.now().isoformat())
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "SOP-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("quality.manager", "SOP-001", db_path, datetime.now().isoformat())
    revise_doc("quality.manager", "SOP-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "SOP-001", db_path)
    document_action = doc_action("REJECT")
    document_action(
        "quality.manager", "SOP-001", db_path, datetime.now().isoformat(), "misc"
    )
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "SOP-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("quality.manager", "SOP-001", db_path, datetime.now().isoformat())
    revise_doc("quality.manager", "SOP-002", db_path)
    create_new_document("test3", "WI", "albert.sevilleja", db_path)
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "WI-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("quality.manager", "WI-001", db_path, datetime.now().isoformat())
    revise_doc("quality.manager", "WI-001", db_path)
    document_action = doc_action("APPROVE")
    document_action("albert.sevilleja", "WI-001", db_path)
