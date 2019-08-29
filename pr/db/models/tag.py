from typing import Dict, Any

from sqlalchemy import orm

from pr.db import models

import sqlalchemy as sa


class Tag(models.DeclarativeBase):
    __tablename__ = 'tags'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False, index=True, unique=True)

    persons = orm.relationship('Person', secondary=models.PersonTag, back_populates='tags')

    def to_web(self) -> Dict[str, Any]:
        pass
