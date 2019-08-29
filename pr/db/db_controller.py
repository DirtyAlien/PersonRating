from time import sleep

import sqlalchemy as sa
from sqlalchemy import engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

import pr
from pr.db.session_context import SessionContext
from pr.db import models


class WithSessionContextManager:
    def __init__(self, db_controller: 'DBController'):
        self.db_controller = db_controller
        self.sc: SessionContext = None

    def __enter__(self) -> SessionContext:
        self.sc = self.db_controller.make_sc()
        return self.sc

    def __exit__(self, err_type, err_value, err_traceback):
        self.sc.close()


class DBController:
    def __init__(self):
        db_config = pr.config.get('db', {})
        connection_string = db_config.pop('connection_string')
        self.__engine: 'engine.Engine' = sa.create_engine(connection_string, **db_config)

    def make_sc(self) -> SessionContext:
        while self.__engine is None:
            sleep(.01)
        return SessionContext(Session(self.__engine, expire_on_commit=False))

    def with_sc(self) -> WithSessionContextManager:
        while self.__engine is None:
            sleep(.01)
        return WithSessionContextManager(self)

    def initialize(self):
        if not database_exists(self.__engine.url):
            create_database(self.__engine.url)
        models.DeclarativeBase.metadata.drop_all(self.__engine)
        models.DeclarativeBase.metadata.create_all(self.__engine)

    def stop(self):
        self.__engine.dispose()
