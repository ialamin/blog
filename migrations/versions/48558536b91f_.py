"""empty message

Revision ID: 48558536b91f
Revises: None
Create Date: 2016-02-25 23:33:28.187143

"""

# revision identifiers, used by Alembic.
revision = '48558536b91f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entries', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'entries', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entries', type_='foreignkey')
    op.drop_column('entries', 'author_id')
    ### end Alembic commands ###
