import os

from paste.translogger import TransLogger
from waitress import serve

from myapp import app


if __name__ == '__main__':
    host = '0.0.0.0'
    port = '8088'

    if 'SERVER_HOST' in os.environ:
        host = os.environ['SERVER_HOST']
    if 'SERVER_PORT' in os.environ:
        port = os.environ['SERVER_PORT']

    serve(TransLogger(app, setup_console_handler=False),
          host=host, port=port)
