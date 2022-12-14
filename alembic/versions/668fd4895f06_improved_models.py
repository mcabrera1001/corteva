"""improved models

Revision ID: 668fd4895f06
Revises: 
Create Date: 2022-11-01 21:22:00.463584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "668fd4895f06"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "crop_yield",
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("crop", sa.String(length=10), nullable=True),
        sa.Column("crop_yield_1000_megatons", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("year"),
    )
    op.create_table(
        "weather",
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("date", sa.String(length=8), nullable=False),
        sa.Column("station", sa.String(length=11), nullable=False),
        sa.Column("min_temperature", sa.Float(), nullable=True),
        sa.Column("max_temperature", sa.Float(), nullable=True),
        sa.Column("precipitation", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("date", "station"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("weather")
    op.drop_table("crop_yield")
    # ### end Alembic commands ###
