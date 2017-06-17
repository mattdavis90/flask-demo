from flask import url_for
from . import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, index=True)

    items = db.relationship('Item', backref='category', cascade='delete,delete-orphan')

    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        return url_for('api.get_category', category_id=self.id)

    @property
    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'no_items': len(self.items),
                'url': self.url,
        }

    def __repr__(self):
        return '<Category {} name: {} no_items: {}>'.format(self.id, self.name, len(self.items))


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def url(self):
        return url_for('api.get_item', item_id=self.id)

    @property
    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'category': self.category.name,
                'url': self.url,
        }

    def __repr__(self):
        return '<Item {} name: {} category: {}>'.format(self.id, self.name, self.category.name)
