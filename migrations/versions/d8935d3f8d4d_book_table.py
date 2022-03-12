"""book table

Revision ID: d8935d3f8d4d
Revises: 
Create Date: 2022-03-11 09:48:04.504995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8935d3f8d4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('genre', sa.String(length=150), nullable=True),
    sa.Column('year_publication', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=True)
    op.create_index(op.f('ix_book_genre'), 'book', ['genre'], unique=True)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=True)
    op.create_index(op.f('ix_book_year_publication'), 'book', ['year_publication'], unique=False)
    op.create_table('author_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('year_of_birth', sa.Integer(), nullable=True),
    sa.Column('nationality', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['book.author'], ),
    sa.ForeignKeyConstraint(['title'], ['book.title'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('on_shelf', sa.Boolean(), nullable=True),
    sa.Column('borrower', sa.String(length=200), nullable=True),
    sa.Column('date_borrowed', sa.DateTime(), nullable=True),
    sa.Column('book_title', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_title'], ['book.title'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_availability_borrower'), 'availability', ['borrower'], unique=True)
    op.create_index(op.f('ix_availability_date_borrowed'), 'availability', ['date_borrowed'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_availability_date_borrowed'), table_name='availability')
    op.drop_index(op.f('ix_availability_borrower'), table_name='availability')
    op.drop_table('availability')
    op.drop_table('author_details')
    op.drop_index(op.f('ix_book_year_publication'), table_name='book')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_genre'), table_name='book')
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###