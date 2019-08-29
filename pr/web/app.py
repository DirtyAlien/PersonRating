from tornado.ioloop import IOLoop
from tornado.web import Application

from .handlers import *
import pr


class TornadoApp:
    def __init__(self):
        self.db_controller: 'pr.db.DBController' = pr.get_db_controller()
        handlers = [
            # users
            # (r'users/login', ApiUsersLoginHandler),
            # (r'users/logout', ApiUsersLogoutHandler),
            # (r'users/([0-9]*)', ApiUsersHandler),

            # persons
            (r'persons/([0-9]*)', ApiPersonsHandler),
            (r'persons/list', ApiPersonsListHandler),
        ]
        handlers = [(f'/api/v1/{h}', c) for h, c in handlers]

        settings = {
            'db_controller': self.db_controller
        }

        self.app: Application = Application(handlers, **settings)

    def run(self, port: int = 80):
        print(f'Running server on port {port}...')
        self.app.listen(port)
        IOLoop.current().start()
