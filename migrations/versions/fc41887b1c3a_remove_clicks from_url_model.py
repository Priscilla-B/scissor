"""add analytics model

Revision ID: fc41887b1c3a
Revises: ca67877b1a08
Create Date: 2023-06-22 15:43:42.326557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc41887b1c3a'
down_revision = 'ca67877b1a08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.drop_column('clicks')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clicks', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
