from app import create_app
from dotenv import load_dotenv
from extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

load_dotenv()
app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
