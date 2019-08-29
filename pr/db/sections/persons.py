from pr.db import models
from pr.db.sections.base import DBApiSectionBase


class DBApiPersonsSection(DBApiSectionBase):

    def get(self, person_id: int) -> models.Person:
        pass
