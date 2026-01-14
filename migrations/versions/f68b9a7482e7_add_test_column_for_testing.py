"""Add test_column safely

Revision ID: f68b9a7482e7
Revises: 
Create Date: 2026-01-14 23:08:01.158782
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'f68b9a7482e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)

    # Check if the column already exists
    columns = [col['name'] for col in inspector.get_columns('attendance_sessions')]
    if 'test_column' not in columns:
        with op.batch_alter_table('attendance_sessions', schema=None) as batch_op:
            batch_op.add_column(sa.Column('test_column', sa.String(length=50), nullable=True))

    # Safe alterations to existing columns
    with op.batch_alter_table('attendance_sessions', schema=None) as batch_op:
        batch_op.alter_column('source',
               existing_type=mysql.ENUM('WEB', 'MOBILE'),
               nullable=False,
               existing_server_default=sa.text("'WEB'"))
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('current_timestamp()'))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('current_timestamp()'))


def downgrade():
    # Only drop the column if it exists
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    columns = [col['name'] for col in inspector.get_columns('attendance_sessions')]

    if 'test_column' in columns:
        with op.batch_alter_table('attendance_sessions', schema=None) as batch_op:
            batch_op.drop_column('test_column')
