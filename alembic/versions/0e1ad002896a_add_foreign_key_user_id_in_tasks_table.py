"""add foreign key user_id in tasks table

Revision ID: 0e1ad002896a
Revises: 8f346a56b97b
Create Date: 2025-07-16 09:15:35.569627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e1ad002896a'
down_revision: Union[str, Sequence[str], None] = '8f346a56b97b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('tasks', sa.Column('user_id', sa.UUID, nullable=True))
    op.create_foreign_key('tasks_users_fk', source_table='tasks', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('tasks_users_fk', table_name='tasks')
    op.drop_column('tasks', 'user_id')
    """Downgrade schema."""
    pass
