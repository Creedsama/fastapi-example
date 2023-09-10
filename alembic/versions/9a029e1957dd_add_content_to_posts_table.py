"""add content to posts table

Revision ID: 9a029e1957dd
Revises: 2ef3cff53c5d
Create Date: 2023-09-10 12:08:04.181482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9a029e1957dd"
down_revision: Union[str, None] = "2ef3cff53c5d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
