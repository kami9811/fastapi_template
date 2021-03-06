"""“Changed.”

Revision ID: e88486e6113d
Revises: 
Create Date: 2021-08-23 19:29:42.436802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e88486e6113d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('hashed_password', sa.String(length=128), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_id'), 'todo', ['id'], unique=False)
    op.create_index(op.f('ix_todo_title'), 'todo', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_title'), table_name='todo')
    op.drop_index(op.f('ix_todo_id'), table_name='todo')
    op.drop_table('todo')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
