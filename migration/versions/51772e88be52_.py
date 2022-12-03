"""empty message

Revision ID: 51772e88be52
Revises: 20eef51c4ac5
Create Date: 2022-12-03 14:34:58.220805

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '51772e88be52'
down_revision = '20eef51c4ac5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match_table', sa.Column('stage_id', sa.Integer(), nullable=True))
    op.add_column('match_table', sa.Column('team1', sa.Integer(), nullable=True))
    op.add_column('match_table', sa.Column('team2', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'match_table', 'team_table', ['team2'], ['id'])
    op.create_foreign_key(None, 'match_table', 'stage_table', ['stage_id'], ['level'])
    op.create_foreign_key(None, 'match_table', 'team_table', ['team1'], ['id'])
    op.add_column('stage_table', sa.Column('tournament_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stage_table', 'tournament_table', ['tournament_id'], ['id'])
    op.drop_column('stage_table', 'Matches')
    op.drop_column('tournament_table', 'stages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament_table', sa.Column('stages', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    op.add_column('stage_table', sa.Column('Matches', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'stage_table', type_='foreignkey')
    op.drop_column('stage_table', 'tournament_id')
    op.drop_constraint(None, 'match_table', type_='foreignkey')
    op.drop_constraint(None, 'match_table', type_='foreignkey')
    op.drop_constraint(None, 'match_table', type_='foreignkey')
    op.drop_column('match_table', 'team2')
    op.drop_column('match_table', 'team1')
    op.drop_column('match_table', 'stage_id')
    # ### end Alembic commands ###
