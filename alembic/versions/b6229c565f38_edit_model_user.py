"""edit model user

Revision ID: b6229c565f38
Revises: 1e781fe302a2
Create Date: 2022-01-07 21:45:31.593525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6229c565f38'
down_revision = '1e781fe302a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
