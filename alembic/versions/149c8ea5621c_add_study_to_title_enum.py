"""add 'study' to title_enum

Revision ID: 149c8ea5621c
Revises: 24d13a50861e
Create Date: 2025-07-20 08:37:32.910998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '149c8ea5621c'
down_revision: Union[str, Sequence[str], None] = '24d13a50861e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TYPE title_enum ADD VALUE IF NOT EXISTS 'Study';")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
