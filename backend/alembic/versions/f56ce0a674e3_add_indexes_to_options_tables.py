"""add indexes to options tables

Revision ID: f56ce0a674e3
Revises: 2a09055d1b69
Create Date: 2026-01-01 19:40:24.848211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f56ce0a674e3'
down_revision: Union[str, Sequence[str], None] = '2a09055d1b69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    # cov calls indexes
    op.create_index(
        "ix_cc_ticker_expiry",
        "BEST_COVERED_CALLS",
        ["ticker", "expiry_date"],
    )

    op.create_index(
        "ix_cc_exchange",
        "BEST_COVERED_CALLS",
        ["exchange"],
    )

    op.create_index(
        "ix_cc_updated_at",
        "BEST_COVERED_CALLS",
        ["updated_at"],
    )

    # put options indexes
    op.create_index(
        "ix_po_ticker_expiry",
        "BEST_PUT_OPTIONS",
        ["ticker", "expiry_date"],
    )

    op.create_index(
        "ix_po_exchange",
        "BEST_PUT_OPTIONS",
        ["exchange"],
    )

    op.create_index(
        "ix_po_updated_at",
        "BEST_PUT_OPTIONS",
        ["updated_at"],
    )

    # spread options indexes
    op.create_index(
        "ix_so_ticker_expiry",
        "BEST_SPREAD_OPTIONS",
        ["ticker", "expiry_date"],
    )

    op.create_index(
        "ix_so_exchange",
        "BEST_SPREAD_OPTIONS",
        ["exchange"],
    )

    op.create_index(
        "ix_so_updated_at",
        "BEST_SPREAD_OPTIONS",
        ["updated_at"],
    )


def downgrade():
    op.drop_index("ix_cc_updated_at", table_name="BEST_COVERED_CALLS")
    op.drop_index("ix_cc_exchange", table_name="BEST_COVERED_CALLS")
    op.drop_index("ix_cc_ticker_expiry", table_name="BEST_COVERED_CALLS")

    op.drop_index("ix_po_updated_at", table_name="BEST_PUT_OPTIONS")
    op.drop_index("ix_po_exchange", table_name="BEST_PUT_OPTIONS")
    op.drop_index("ix_po_ticker_expiry", table_name="BEST_PUT_OPTIONS")

    op.drop_index("ix_so_updated_at", table_name="BEST_SPREAD_OPTIONS")
    op.drop_index("ix_so_exchange", table_name="BEST_SPREAD_OPTIONS")
    op.drop_index("ix_so_ticker_expiry", table_name="BEST_SPREAD_OPTIONS")
