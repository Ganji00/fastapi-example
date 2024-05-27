"""Add cascading delete for orders

Revision ID: b488f275b530
Revises: da5124754da0
Create Date: 2024-05-27 19:12:38.639276

"""

from typing import Sequence, Union

import sqlalchemy as sa

# no stubs for alembic
from alembic import op  # type: ignore

# revision identifiers, used by Alembic.
revision: str = "b488f275b530"
down_revision: Union[str, None] = "da5124754da0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the existing foreign key constraint
    op.drop_constraint("order_customer_id_fkey", "order", type_="foreignkey")

    # Create a new foreign key constraint with ON DELETE CASCADE
    op.create_foreign_key(
        "order_customer_id_fkey",
        "order",
        "customer",
        ["customer_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    # Drop the foreign key constraint with ON DELETE CASCADE
    op.drop_constraint("order_customer_id_fkey", "order", type_="foreignkey")

    # Restore the original foreign key constraint
    op.create_foreign_key(
        "order_customer_id_fkey", "order", "customer", ["customer_id"], ["id"]
    )
