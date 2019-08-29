from sqlalchemy.orm import Session

import pr.db.session_context as sc


class DBApiSectionBase:
    def __init__(self, session_context: 'sc.SessionContext'):
        self.session_context: sc.SessionContext = session_context
        self.session: Session = self.session_context.session
