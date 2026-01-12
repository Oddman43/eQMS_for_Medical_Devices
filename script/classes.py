from dataclasses import dataclass
from datetime import datetime
import re
from config import document_types, status_types, training_types


@dataclass
class Document_Header:
    id: int
    number: str
    title: str
    owner: int
    type: str

    def __post_init__(self) -> None:
        check_1: str | None = self._checks()
        if check_1 is not None:
            raise (ValueError(check_1))

    def _checks(self) -> None | str:
        if not self.title or self.title == "":
            return "Title cannot be empty"
        elif self.type not in document_types.values():
            return f"Invalid document type: '{self.type}'"
        elif not re.fullmatch(r"^[a-zA-Z]{2,4}-\d{3}$", self.number):
            return f"Invalid document number format: '{self.number}'"
        elif self.type != self.number.split("-")[0]:
            return f"Mismatch: Type is '{self.type}' but Number starts with '{self.number.split('-')[0]}'"
        else:
            return None

    def __iter__(self):
        yield "doc_id", self.id
        yield "doc_num", self.number
        yield "title", self.title
        yield "owner_id", self.owner
        yield "type", self.type

    def to_db_tuple(self) -> tuple:
        return (self.id, self.number, self.title, self.owner, self.type)


@dataclass
class Document_Version:
    id: int
    doc: int
    version: str
    status: str
    file_path: str
    effective_date: str | None

    def __post_init__(self) -> None:
        basic_check: str | None = self._basic_checks()
        if basic_check is not None:
            raise (ValueError(basic_check))

    def _basic_checks(self) -> str | None:
        if not re.fullmatch(r"^\d+\.\d+$", self.version):
            return f"Invalid version major or minor is not an integer: '{self.version}'"
        if self.status not in status_types:
            return f"Invalid version status: '{self.status}'"
        if not self.file_path:
            return "File path can not be empty"
        if self.status == "RELEASED" and self.effective_date is None:
            return f"Effective date can not be empty in {self.status} documents"
        else:
            return None

    def __iter__(self):
        yield "version_id", self.id
        yield "doc", self.doc
        yield "version", self.version
        yield "status", self.status
        yield "file_path", self.file_path
        yield "effective_date", self.effective_date

    def to_db_tuple(self) -> tuple:
        return (
            self.id,
            self.doc,
            self.version,
            self.status,
            self.file_path,
            self.effective_date,
        )


@dataclass
class Training:
    id: int
    user_id: int
    version_id: int
    status: str
    assigned_date: datetime | str
    due_date: datetime | str
    completion_date: datetime | str | None = None
    score: int | None = None

    def __post_init__(self):
        if isinstance(self.assigned_date, str):
            self.assigned_date = datetime.fromisoformat(self.assigned_date)
        if isinstance(self.due_date, str):
            self.due_date = datetime.fromisoformat(self.due_date)
        if isinstance(self.completion_date, str):
            self.completion_date = datetime.fromisoformat(self.completion_date)

    def _checks(self) -> None | str:
        if self.status not in training_types:
            return "Status not valid or empty"

    def __iter__(self):
        yield "training_id", self.id
        yield "user_id", self.user_id
        yield "version_id", self.version_id
        yield "status", self.status
        yield "assigned_date", self.assigned_date.isoformat()  # type: ignore
        yield "due_date", self.due_date.isoformat()  # type: ignore
        if self.completion_date:
            yield "completion_date", self.completion_date.isoformat()  # type: ignore
        else:
            yield "completion_date", None
        yield "score", self.score

    def to_db_tuple(self) -> tuple:
        completion_str: str | None = (
            self.completion_date.isoformat() if self.completion_date else None  # type: ignore
        )
        return (
            self.id,
            self.user_id,
            self.version_id,
            self.status,
            self.assigned_date.isoformat(),  # type: ignore
            self.due_date.isoformat(),  # type: ignore
            completion_str,
            self.score,
        )


@dataclass
class Training_Review:
    tr_id: int
    version_id: int
    reviewer_id: int
    status: str
    created_at: str | datetime
    decision: str | None = None
    comment: str | None = None
    completed_at: str | datetime | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)
        if isinstance(self.completed_at, str):
            self.completed_at = datetime.fromisoformat(self.completed_at)

    def __iter__(self):
        yield "training_id", self.tr_id
        yield "version_id", self.version_id
        yield "reviewer_id", self.reviewer_id
        yield "status", self.status
        yield "decision", self.decision
        yield "comment", self.comment
        yield "created_at", self.created_at.isoformat()  # type: ignore
        if self.completed_at:
            yield "completed_at", self.completed_at.isoformat()  # type: ignore
        else:
            yield "completed_at", None

    def to_db_tuple(self) -> tuple:
        completion_at_str: str | None = (
            self.completed_at.isoformat() if self.completed_at else None  # type: ignore
        )
        return (
            self.tr_id,
            self.version_id,
            self.reviewer_id,
            self.status,
            self.decision,
            self.comment,
            self.created_at,
            completion_at_str,
        )
