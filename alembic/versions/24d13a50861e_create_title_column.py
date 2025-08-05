"""Create title column

Revision ID: 24d13a50861e
Revises: 891f03902e51
Create Date: 2025-07-19 17:16:35.417741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.schema import Title


# revision identifiers, used by Alembic.
revision: str = '24d13a50861e'
down_revision: Union[str, Sequence[str], None] = '891f03902e51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('tasks', sa.Column('title', sa.Enum(Title, name="title_enum"), server_default=Title.Home, nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tasks', 'title')
    pass
