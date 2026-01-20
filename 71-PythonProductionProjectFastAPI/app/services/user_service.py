import logging

from sqlalchemy.orm import Session

from app.db.schema import User

logger = logging.getLogger(__name__)

# Include business logic with database session and does things ex. get users, create users, etc called from API
# Write test without mocking endpoints
# swap persistance later on

class UserService:
    def __init__(self, session: Session):
        self._db = session

    def list_users(self) -> list[User]:
        logger.info("Fetching all users")
        return self._db.query(User).all()

    def get_user(self, user_id: int) -> User | None:
        logger.info(f"Fetching user with id: {user_id}")
        user = self._db.query(User).filter(User.id == user_id).first()
        if not user:
            logger.warning(f"User with id {user_id} not found")
        return user

    def create_user(self, name: str) -> User:
        logger.info(f"Creating user with name: {name}")
        user = User(name=name)
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)
        logger.info(f"Created user with id: {user.id}")
        return user

    def update_user(self, user_id: int, name: str) -> User | None:
        logger.info(f"Updating user {user_id} with name: {name}")
        user = self.get_user(user_id)
        if not user:
            return None
        user.name = name
        self._db.commit()
        self._db.refresh(user)
        logger.info(f"Updated user {user_id}")
        return user

    def delete_user(self, user_id: int) -> bool:
        logger.info(f"Deleting user with id: {user_id}")
        user = self.get_user(user_id)
        if not user:
            return False
        self._db.delete(user)
        self._db.commit()
        logger.info(f"Deleted user {user_id}")
        return True
