"""Init

Revision ID: 72408a4d2999
Revises: 80e9d7ac828f
Create Date: 2023-03-28 13:04:15.170107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72408a4d2999'
down_revision = '80e9d7ac828f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('disciplines', sa.Column('name', sa.String(length=50), nullable=False))
    op.drop_column('disciplines', 'discipline_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('disciplines', sa.Column('discipline_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_column('disciplines', 'name')
    # ### end Alembic commands ###
