"""empty message

Revision ID: 2db67c95f198
Revises: 51772e88be52
Create Date: 2022-12-03 14:35:47.729533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2db67c95f198'
down_revision = '51772e88be52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stage_table', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stage_table', 'id')
    # ### end Alembic commands ###
