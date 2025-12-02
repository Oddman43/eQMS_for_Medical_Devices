from datetime import datetime
from dataclasses import dataclass
import re
from ..main import document_types, status_types


@dataclass
class Document_Header:
    id: int
    number: str
    title: str
    owner: int
    type: str

    def __post__init__(self) -> None:
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


@dataclass
class Document_Version:
    id: int
    doc: int
    lable: str
    status: str
    file_path: str
    effective_date: datetime

    def __post_init__(self) -> None:
        basic_check: str | None = self._basic_checks()

    def _basic_checks(self) -> str | None: ...


# BASIC
# label es n.n
# status dentro de status_types
# path existe

# Contextual
# si es DRAFT o IN_REVIEW solo puede haber un documento
# validacion de labels, la nueva siempre mayor que la anterior
# ojo cambio de minor version vs major
# si es RELEASED, SUPERSEDED o OBSOLETE no se puede editar
