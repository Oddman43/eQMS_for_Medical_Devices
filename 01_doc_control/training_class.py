from datetime import datetime


class Training:
    def __init__(
        self,
        training_id: int,
        user_id: int,
        version_id: int,
        status: str,
        assigned_date: str,
        completion_date: str | None,
    ) -> None:
        self.id: int = training_id
        self.user_id: int = user_id
        self.version_id: int = version_id
        self.status: str = status
        self.assigned_date: datetime = datetime.fromisoformat(assigned_date)
        if completion_date:
            self.completion_date: datetime | None = datetime.fromisoformat(
                completion_date
            )
        else:
            self.completion_date = None

    def __iter__(self):
        yield "training_id", self.id
        yield "user_id", self.user_id
        yield "version_id", self.version_id
        yield "status", self.status
        yield "assigned_date", self.assigned_date.isoformat()
        if self.completion_date:
            yield "completion_date", self.completion_date.isoformat()
        else:
            yield "completion_date", None

    def to_db_tuple(self) -> tuple:
        completion_str: str | None = (
            self.completion_date.isoformat() if self.completion_date else None
        )
        return (
            self.id,
            self.user_id,
            self.version_id,
            self.status,
            self.assigned_date.isoformat,
            completion_str,
        )
