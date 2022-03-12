"""empty message

Revision ID: 159ad13cd386
Revises: 511cf4ce8671
Create Date: 2022-03-11 12:16:13.871272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '159ad13cd386'
down_revision = '511cf4ce8671'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'author_details', type_='foreignkey')
    op.drop_column('author_details', 'title')
    op.drop_constraint(None, 'availability', type_='foreignkey')
    op.create_foreign_key(None, 'availability', 'book', ['book_id'], ['id'])
    op.drop_column('availability', 'book_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('availability', sa.Column('book_title', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'availability', type_='foreignkey')
    op.create_foreign_key(None, 'availability', 'book', ['book_title'], ['title'])
    op.add_column('author_details', sa.Column('title', sa.VARCHAR(length=300), nullable=True))
    op.create_foreign_key(None, 'author_details', 'book', ['title'], ['title'])
    # ### end Alembic commands ###