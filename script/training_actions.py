from types import FunctionType
from copy import deepcopy
from datetime import datetime
from training_class import Training
from core_fn import get_training, audit_log_training, update_training


def training_actions(action: str) -> FunctionType: ...


def do_training(user_id: int, doc_num: str, score: int, db_path: str) -> None:
    old_training_obj: Training = get_training(user_id, doc_num, db_path)
    new_training_obj: Training = deepcopy(old_training_obj)
    new_training_obj.score = score
    if score > 70:
        new_training_obj.status = "COMPLETED"
        new_training_obj.completion_date = datetime.now()

    else:
        new_training_obj.status = "FAILED"
    audit_log_training(
        old_training_obj,
        new_training_obj,
        user_id,
        new_training_obj.status,
        db_path,
    )
    update_training(old_training_obj, new_training_obj, db_path)
