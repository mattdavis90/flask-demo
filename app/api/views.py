from flask import jsonify, request, flash, redirect
from . import api
from .. import db
from ..models import Category, Item
from ..socket import notify_sio


@api.route('/category/')
def get_categories():
    categories = Category.query.all()

    categories_json = [category.json for category in categories]

    return jsonify({'categories': categories_json})


@api.route('/category/<int:category_id>/')
def get_category(category_id=None):
    category = Category.query.get_or_404(category_id)

    return jsonify(category.json)


@api.route('/category/', methods=['POST'])
@notify_sio(Category, broadcast=True)
def add_category():
    category_data = request.form

    error = False

    if category_data is None:
        flash('Require a name', 'danger')
        error = True

    name = category_data.get('name', '')

    if name == '':
        flash("Name can't be blank", 'danger')
        error = True

    if not error:
        category = Category(name)

        db.session.add(category)
        db.session.commit()

        flash('Category created', 'success')

    return redirect('/add-category')


@api.route('/item/')
def get_items():
    items = Item.query.all()

    items_json = [item.json for item in items]

    return jsonify({'items': items_json})


@api.route('/item/<int:item_id>/')
def get_item(item_id):
    item = Item.query.get_or_404(item_id)

    return jsonify(item.json)


@api.route('/item/', methods=['POST'])
@notify_sio(Item, broadcast=True)
def add_item():
    item_data = request.form

    error = False

    if item_data is None:
        flash('Require a name and category', 'danger')
        error = True

    name = item_data.get('name', '')
    category = Category.query.filter(Category.id==item_data.get('category', -1)).first()

    if name == '':
        flash("Name can't be blank", 'danger')
        error = True

    if category is None:
        flash('Invalid category', 'danger')
        error = True

    if not error:
        item = Item(name, category)

        db.session.add(item)
        db.session.commit()

        flash('Item created', 'success')

    return redirect('/add-item')
