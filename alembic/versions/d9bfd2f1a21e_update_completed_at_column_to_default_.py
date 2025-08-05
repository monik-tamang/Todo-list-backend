"""update completed_at column to default as None

Revision ID: d9bfd2f1a21e
Revises: a74a3df73f26
Create Date: 2025-07-14 19:20:18.970845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9bfd2f1a21e'
down_revision: Union[str, Sequence[str], None] = 'a74a3df73f26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('tasks', 'completed_at', server_default=None)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('tasks', 'completed_at', server_default=sa.text('now()'))
    pass
