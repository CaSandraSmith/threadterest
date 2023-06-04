"""empty message

Revision ID: ca4717911fa9
Revises: 
Create Date: 2023-06-04 13:29:36.869272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca4717911fa9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('about', sa.String(length=255), nullable=True),
    sa.Column('pronouns', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.Column('cover_image', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follows',
    sa.Column('follower', sa.Integer(), nullable=False),
    sa.Column('followed', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower', 'followed')
    )
    op.create_table('pins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('alt_text', sa.String(length=255), nullable=True),
    sa.Column('destination', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('board_categories',
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], )
    )
    op.create_table('boards_pins',
    sa.Column('pin_to_board', sa.Integer(), nullable=True),
    sa.Column('board_pinned', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_pinned'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['pin_to_board'], ['pins.id'], )
    )
    op.create_table('pin_categories',
    sa.Column('pin_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['pin_id'], ['pins.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pin_categories')
    op.drop_table('boards_pins')
    op.drop_table('board_categories')
    op.drop_table('pins')
    op.drop_table('follows')
    op.drop_table('boards')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
