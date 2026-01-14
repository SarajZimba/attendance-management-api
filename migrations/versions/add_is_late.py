"""Add is_late and duration_minutes safely

Revision ID: add_is_late_duration
Revises: f68b9a7482e7
Create Date: 2026-01-14
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'add_is_late_duration'
down_revision = 'f68b9a7482e7'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)

    columns = [col['name'] for col in inspector.get_columns('attendance_sessions')]

    with op.batch_alter_table('attendance_sessions', schema=None) as batch_op:
        if 'is_late' not in columns:
            batch_op.add_column(sa.Column('is_late', sa.Boolean(), nullable=False, server_default=sa.false()))
        if 'duration_minutes' not in columns:
            batch_op.add_column(sa.Column('duration_minutes', sa.Integer(), nullable=True))


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)

    columns = [col['name'] for col in inspector.get_columns('attendance_sessions')]

    with op.batch_alter_table('attendance_sessions', schema=None) as batch_op:
        if 'is_late' in columns:
            batch_op.drop_column('is_late')
        if 'duration_minutes' in columns:
            batch_op.drop_column('duration_minutes')
