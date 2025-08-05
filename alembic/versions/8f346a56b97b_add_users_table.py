"""add users table

Revision ID: 8f346a56b97b
Revises: 99be6bd8aab5
Create Date: 2025-07-16 07:41:01.021340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f346a56b97b'
down_revision: Union[str, Sequence[str], None] = '99be6bd8aab5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', sa.Column('id', sa.UUID, nullable=False, unique=True, primary_key=True, server_default=sa.text('gen_random_uuid()')),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    """Downgrade schema."""
    pass
