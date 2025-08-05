"""add completed_at column on tasks table

Revision ID: 5f66f3ee9c93
Revises: 
Create Date: 2025-07-14 18:20:01.743050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f66f3ee9c93'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('tasks', sa.Column('completed_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tasks', 'completed_at')
    pass

