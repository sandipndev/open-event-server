"""empty message

Revision ID: 34be8a5853bd
Revises: ffbb4d4dad39
Create Date: 2016-06-29 12:03:01.736940

"""

# revision identifiers, used by Alembic.
revision = '34be8a5853bd'
down_revision = 'ffbb4d4dad39'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('storage_place', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'storage_place')
    ### end Alembic commands ###
