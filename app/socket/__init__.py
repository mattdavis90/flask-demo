from flask_socketio import emit
from flask import request
from functools import wraps, partial
from .. import sio


def notify_sio(Cls, broadcast=False):
    def decorator(func, Cls, broadcast=False):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retval = func(*args, **kwargs)

            emitter = partial(sio.emit, namespace='/socketio')
            if hasattr(request, 'namespace'):
                emitter = partial(emit, broadcast=broadcast)

            items = Cls.query.all()

            try:
                items_json = [item.json for item in items]
                items_name = '{}'.format(Cls.__tablename__.lower())
                emitter(items_name, {items_name: items_json})
            except AttributeError:
                pass

            return retval
        return wrapper
    return partial(decorator, Cls=Cls, broadcast=broadcast)


from . import views # noqa
