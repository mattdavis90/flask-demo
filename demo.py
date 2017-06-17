from app import app, db
from app.models import Category, Item
from flask_migrate import Migrate


migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    context = dict(
        app=app,
        db=db,
        Category=Category,
        Item=Item,
    )

    return context
