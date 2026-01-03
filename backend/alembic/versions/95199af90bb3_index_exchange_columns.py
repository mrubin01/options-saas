"""index exchange columns

Revision ID: 95199af90bb3
Revises: 8d8c4fd0a251
Create Date: 2026-01-03 10:41:35.493700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95199af90bb3'
down_revision: Union[str, Sequence[str], None] = '8d8c4fd0a251'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "ix_covered_calls_exchange",
        "BEST_COVERED_CALLS",
        ["exchange"],
    )
    op.create_index(
        "ix_put_options_exchange",
        "BEST_PUT_OPTIONS",
        ["exchange"],
    )
    op.create_index(
        "ix_spread_options_exchange",
        "BEST_SPREAD_OPTIONS",
        ["exchange"],
    )


def downgrade() -> None:
    op.drop_index("ix_covered_calls_exchange", table_name="BEST_COVERED_CALLS")
    op.drop_index("ix_put_options_exchange", table_name="BEST_PUT_OPTIONS")
    op.drop_index("ix_spread_options_exchange", table_name="BEST_SPREAD_OPTIONS")


