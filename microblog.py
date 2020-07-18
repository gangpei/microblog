from app import create_app, db, cli
from app.models import User, Post, Notification, Message
# from gevent import pywsgi

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}


# if __name__ == '__main__':
#     server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
#     server.serve_forever()