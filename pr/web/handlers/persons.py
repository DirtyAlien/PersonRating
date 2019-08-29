from pr.web.handlers import BaseHandler


class ApiPersonsHandler(BaseHandler):
    def get(self, person_id: str):
        person = self.sc.persons.get(int(person_id))
        self.send_json(person.to_web())


class ApiPersonsListHandler(BaseHandler):
    ...
