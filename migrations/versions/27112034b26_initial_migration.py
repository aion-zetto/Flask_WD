"""initial migration

Revision ID: 27112034b26
Revises: 2edbccd4c6b
Create Date: 2015-09-28 21:32:14.718750

"""

# revision identifiers, used by Alembic.
revision = '27112034b26'
down_revision = '2edbccd4c6b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
