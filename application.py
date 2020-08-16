from paste.translogger import TransLogger
from waitress import serve

from myapp import app


if __name__ == '__main__':
    serve(TransLogger(app, setup_console_handler=False),
          host="0.0.0.0", port=8088)
