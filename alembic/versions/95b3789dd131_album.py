"""album

Revision ID: 95b3789dd131
Revises: 9271e81ca97a
Create Date: 2024-01-29 19:22:29.352023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95b3789dd131'
down_revision: Union[str, None] = '9271e81ca97a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('published', sa.DateTime(), nullable=False),
    sa.Column('id_artist', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_artist'], ['artist.id'], name=op.f('fk_album_id_artist_artist')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_album'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('album')
    # ### end Alembic commands ###