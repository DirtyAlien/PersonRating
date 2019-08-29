import sqlalchemy as sa

from pr.db import models


PersonTag = sa.Table(
    'persons_tags',
    models.DeclarativeBase.metadata,
    sa.Column('person_id', sa.Integer, sa.ForeignKey('persons.id')),
    sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.id'))
)
