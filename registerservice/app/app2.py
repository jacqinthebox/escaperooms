from database import init_db, db_session
from models import User

init_db()

u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()


def shutdown_session(exception=None):
    db_session.remove()
