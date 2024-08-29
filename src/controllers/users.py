from typing import List
import uuid
from src.supa.client import sb

from gotrue.types import UserResponse

class UserController:

    @staticmethod
    def get_user_by_id(user_id: uuid.UUID) -> UserResponse:
        user = sb.auth.admin.get_user_by_id(user_id)
        return user