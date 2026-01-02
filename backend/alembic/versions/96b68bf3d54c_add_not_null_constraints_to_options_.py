"""add not null constraints to options tables

Revision ID: 96b68bf3d54c
Revises: f56ce0a674e3
Create Date: 2026-01-02 09:50:14.042130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96b68bf3d54c'
down_revision: Union[str, Sequence[str], None] = 'f56ce0a674e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        "BEST_COVERED_CALLS",
        "ticker",
        nullable=False,
    )

    op.alter_column(
        "BEST_COVERED_CALLS",
        "exchange",
        nullable=False,
    )

    op.alter_column(
        "BEST_COVERED_CALLS",
        "expiry_date",
        nullable=False,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "ticker",
        nullable=False,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "exchange",
        nullable=False,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "expiry_date",
        nullable=False,
    )

    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "ticker",
        nullable=False,
    )

    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "exchange",
        nullable=False,
    )

    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "expiry_date",
        nullable=False,
    )


def downgrade():
    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "expiry_date",
        nullable=True,
    )

    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "exchange",
        nullable=True,
    )

    op.alter_column(
        "BEST_SPREAD_OPTIONS",
        "ticker",
        nullable=True,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "expiry_date",
        nullable=True,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "exchange",
        nullable=True,
    )

    op.alter_column(
        "BEST_PUT_OPTIONS",
        "ticker",
        nullable=True,
    )
    
    op.alter_column(
        "BEST_COVERED_CALLS",
        "expiry_date",
        nullable=True,
    )

    op.alter_column(
        "BEST_COVERED_CALLS",
        "exchange",
        nullable=True,
    )

    op.alter_column(
        "BEST_COVERED_CALLS",
        "ticker",
        nullable=True,
    )




