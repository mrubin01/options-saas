"""add exchange foreign keys

Revision ID: 8d8c4fd0a251
Revises: 96b68bf3d54c
Create Date: 2026-01-03 10:19:32.862947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d8c4fd0a251'
down_revision: Union[str, Sequence[str], None] = '96b68bf3d54c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        "fk_covered_calls_exchange",
        "BEST_COVERED_CALLS",
        "EXCHANGE",
        ["exchange"],
        ["exchange_id"],
        ondelete="RESTRICT",
    )

    op.create_foreign_key(
        "fk_put_options_exchange",
        "BEST_PUT_OPTIONS",
        "EXCHANGE",
        ["exchange"],
        ["exchange_id"],
        ondelete="RESTRICT",
    )

    op.create_foreign_key(
        "fk_spread_options_exchange",
        "BEST_SPREAD_OPTIONS",
        "EXCHANGE",
        ["exchange"],
        ["exchange_id"],
        ondelete="RESTRICT",
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_covered_calls_exchange",
        "BEST_COVERED_CALLS",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_put_options_exchange",
        "BEST_PUT_OPTIONS",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_spread_options_exchange",
        "BEST_SPREAD_OPTIONS",
        type_="foreignkey",
    )
