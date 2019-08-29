from typing import Dict, Any

import sqlalchemy as sa
from sqlalchemy import orm

from pr.db import models


class Person(models.DeclarativeBase):
    __tablename__ = 'persons'

    id = sa.Column(sa.Integer, primary_key=True)
    vrchat_name = sa.Column(sa.String, nullable=False, index=True, unique=True)
    old_vrchat_names = sa.Column(sa.ARRAY(sa.String))
    stats = sa.Column(sa.JSON)
    description = sa.Column(sa.JSON)

    tags = orm.relationship('Tag', secondary=models.PersonTag, back_populates='persons')

    def to_web(self) -> Dict[str, Any]:
        pass
