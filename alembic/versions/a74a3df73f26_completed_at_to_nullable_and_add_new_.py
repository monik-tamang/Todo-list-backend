"""completed_at to nullable and add new column priority on task table

Revision ID: a74a3df73f26
Revises: 5f66f3ee9c93
Create Date: 2025-07-14 18:45:43.628508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a74a3df73f26'
down_revision: Union[str, Sequence[str], None] = '5f66f3ee9c93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('tasks', 'completed_at', nullable=True)
    op.add_column('tasks', sa.Column('priority', sa.String, nullable=False, server_default="None"))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('tasks', 'completed_at', nullable=True)
    op.drop_column('tasks', 'priority')
    pass
