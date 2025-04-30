from sqlalchemy.orm import Session
from core.contracts.user_repository import UserRepository
from adapters.db.models.user_model import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id):
        db_user = self.session.query(UserModel).get(user_id)
        return User(
            id=db_user.id,
            email=db_user.email,
            # ... Mapp other fields
        )
