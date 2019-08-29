# import sqlalchemy as sa
#
# from pr.db import models
#
#
# class User(models.DeclarativeBase):
#     __tablename__ = 'users'
#
#     id = sa.Column(sa.Integer, primary_key=True)
#     email = sa.Column(sa.String, nullable=False, index=True, unique=True)
#     name = sa.Column(sa.String, nullable=False, index=True, unique=True)
#     password = sa.Column(sa.String, nullable=False, index=True, unique=True)
