"""person and tag table

Revision ID: 035b7cfeb8b7
Revises: d443223c9f13
Create Date: 2019-08-29 22:39:52.071326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '035b7cfeb8b7'
down_revision = 'd443223c9f13'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'persons',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('vrchat_name', sa.String(), nullable=False),
        sa.Column('old_vrchat_names', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('stats', sa.JSON(), nullable=True),
        sa.Column('description', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_persons_vrchat_name'), 'persons', ['vrchat_name'], unique=True)
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_name'), 'tags', ['name'], unique=True)
    op.create_table(
        'persons_tags',
        sa.Column('person_id', sa.Integer(), nullable=True),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(('person_id',), ['persons.id'], ),
        sa.ForeignKeyConstraint(('tag_id',), ['tags.id'], )
    )


def downgrade():
    op.drop_table('persons_tags')
    op.drop_index(op.f('ix_tags_name'), table_name='tags')
    op.drop_table('tags')
    op.drop_index(op.f('ix_persons_vrchat_name'), table_name='persons')
    op.drop_table('persons')
