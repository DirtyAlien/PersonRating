import json
from typing import Any, Dict

from tornado.web import RequestHandler

import pr
from pr.db.session_context import SessionContext


class BaseHandler(RequestHandler):
    json: Dict[str, Any]
    db_controller: 'pr.db.DBController'
    sc: SessionContext

    def data_received(self, chunk):
        pass

    def prepare(self):
        self.require_setting('db_controller')
        self.db_controller = self.settings['db_controller']
        self.sc = self.db_controller.make_sc()
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json = json.loads(self.request.body)

    def send_json(self, body: Dict[str, Any]):
        self.add_header('Content-Type', 'application/json')
        self.set_status(200)
        self.finish(json.dumps(body))

    def on_finish(self):
        self.sc.close()

    def write_error(self, status_code, **kwargs):
        exc_type, value, _ = kwargs['exc_info']
        self.finish(json.dumps({
            'type': str(exc_type),
            'msg': str(value),
        }))
