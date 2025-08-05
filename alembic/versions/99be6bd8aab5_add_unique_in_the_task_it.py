"""add unique in the task it

Revision ID: 99be6bd8aab5
Revises: d9bfd2f1a21e
Create Date: 2025-07-16 07:36:31.749715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99be6bd8aab5'
down_revision: Union[str, Sequence[str], None] = 'd9bfd2f1a21e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint("uq_taks_id", "tasks", ["id"])
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_task_id", "tasks", type_="unique")
    pass
