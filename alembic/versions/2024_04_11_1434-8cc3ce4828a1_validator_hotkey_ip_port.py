"""validator hotkey ip port

Revision ID: 8cc3ce4828a1
Revises: 88f9cfb9508a
Create Date: 2024-04-11 14:34:08.561998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8cc3ce4828a1'
down_revision: Union[str, None] = '88f9cfb9508a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('validators', sa.Column('hotkey', sa.String(), nullable=True))
    op.add_column('validators', sa.Column('ip', postgresql.INET(), nullable=True))
    op.add_column('validators', sa.Column('port', sa.Integer(), nullable=True))
    op.drop_index('ix__validators__name', table_name='validators')
    op.create_index(op.f('ix__validators__name'), 'validators', ['name'], unique=False)
    op.create_index(op.f('ix__validators__hotkey'), 'validators', ['hotkey'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__validators__hotkey'), table_name='validators')
    op.drop_index(op.f('ix__validators__name'), table_name='validators')
    op.create_index('ix__validators__name', 'validators', ['name'], unique=True)
    op.drop_column('validators', 'port')
    op.drop_column('validators', 'ip')
    op.drop_column('validators', 'hotkey')
    # ### end Alembic commands ###