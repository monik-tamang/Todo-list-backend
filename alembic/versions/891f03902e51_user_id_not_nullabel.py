"""user-id not nullabel)

Revision ID: 891f03902e51
Revises: 0e1ad002896a
Create Date: 2025-07-16 09:26:11.189438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891f03902e51'
down_revision: Union[str, Sequence[str], None] = '0e1ad002896a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('tasks','user_id', nullable=False)
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.alter_column('tasks', 'user_id', nullable=True)
    """Downgrade schema."""
    pass
