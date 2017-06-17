from .. import sio, db
from ..socket import notify_sio
from ..models import Item, Category


@sio.on('get_items', namespace='/socketio')
@notify_sio(Item)
def get_items(message=None):
    pass


@sio.on('remove_item', namespace='/socketio')
@notify_sio(Item, broadcast=True)
def remove_item(message):
    item_id = message['item_id']
    item = Item.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()


@sio.on('get_categories', namespace='/socketio')
@notify_sio(Category)
def get_categories(message=None):
    pass


@sio.on('remove_category', namespace='/socketio')
@notify_sio(Item, broadcast=True)
@notify_sio(Category, broadcast=True)
def remove_category(message):
    category_id = message['category_id']
    category = Category.query.get(category_id)

    if category:
        db.session.delete(category)
        db.session.commit()
