from flask import render_template, abort
import jinja2
from . import web
from ..models import Category


# Handle most routes automatically
@web.route('/')
@web.route('/<string:page>/')
def view(page='index'):
    try:
        rendered = render_template('{}.html'.format(page), active=page)
    except jinja2.exceptions.TemplateNotFound:
        abort(404)

    return rendered


# Specific handler for adding items
@web.route('/add-item/')
def add_item():
    categories = [(c.id, c.name) for c in Category.query.all()]
    return render_template('add-item.html', active='add-item', categories=categories)
