"""empty message

Revision ID: 5073bea32241
Revises: e9aa743c2202
Create Date: 2022-08-08 17:56:43.883102

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5073bea32241'
down_revision = 'e9aa743c2202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'venue',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('show', 'venue',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
