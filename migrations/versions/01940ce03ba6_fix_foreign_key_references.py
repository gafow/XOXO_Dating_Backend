"""Fix foreign key references

Revision ID: 01940ce03ba6
Revises: 
Create Date: 2024-10-22 19:40:38.472812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01940ce03ba6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_token_jti'), ['jti'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('compatibility_score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matches')
    op.drop_table('interests')
    op.drop_table('users')
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_jti'))

    op.drop_table('token')
    # ### end Alembic commands ###
