"""remove duplicate exchange foreign keys

Revision ID: 78fa906b97dc
Revises: 95199af90bb3
Create Date: 2026-01-03 16:43:02.421380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78fa906b97dc'
down_revision: Union[str, Sequence[str], None] = '95199af90bb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "BEST_PUT_OPTIONS_exchange_fkey",
        "BEST_PUT_OPTIONS",
        type_="foreignkey",
    )

    op.drop_constraint(
        "BEST_SPREAD_OPTIONS_exchange_fkey",
        "BEST_SPREAD_OPTIONS",
        type_="foreignkey",
    )


def downgrade() -> None:
    op.create_foreign_key(
        "BEST_PUT_OPTIONS_exchange_fkey",
        "BEST_PUT_OPTIONS",
        "EXCHANGE",
        ["exchange"],
        ["exchange_id"],
    )

    op.create_foreign_key(
        "BEST_SPREAD_OPTIONS_exchange_fkey",
        "BEST_SPREAD_OPTIONS",
        "EXCHANGE",
        ["exchange"],
        ["exchange_id"],
    )
    
