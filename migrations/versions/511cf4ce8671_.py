"""empty message

Revision ID: 511cf4ce8671
Revises: 232c1218bd26
Create Date: 2022-03-11 12:06:19.772976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '511cf4ce8671'
down_revision = '232c1218bd26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'availability', type_='foreignkey')
    op.create_foreign_key(None, 'availability', 'book', ['book_id'], ['id'])
    op.drop_column('availability', 'book_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('availability', sa.Column('book_title', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'availability', type_='foreignkey')
    op.create_foreign_key(None, 'availability', 'book', ['book_title'], ['title'])
    # ### end Alembic commands ###
