from sqlalchemy.orm import Session

import pr.db.sections as sections


class SessionContext:
    def __init__(self, session: Session):
        self.__session: Session = session

        self.users: sections.DBApiUsersSection = sections.DBApiUsersSection(self)
        self.persons: sections.DBApiPersonsSection = sections.DBApiPersonsSection(self)

    @property
    def session(self) -> Session:
        return self.__session

    def close(self):
        try:
            self.session.commit()
        except Exception as ex:
            print(f'Session commit error, rollback...\n{ex}')
            self.session.rollback()
        finally:
            self.session.close()

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()
