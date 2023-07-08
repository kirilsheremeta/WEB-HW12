"""Init

Revision ID: fd2b59033763
Revises: 57d09a6def65
Create Date: 2023-07-02 16:23:16.324851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd2b59033763'
down_revision = '57d09a6def65'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'phone_number',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'birthday',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index(op.f('ix_contacts_birthday'), 'contacts', ['birthday'], unique=False)
    op.create_index(op.f('ix_contacts_first_name'), 'contacts', ['first_name'], unique=False)
    op.create_index(op.f('ix_contacts_last_name'), 'contacts', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_last_name'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_first_name'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_birthday'), table_name='contacts')
    op.alter_column('contacts', 'birthday',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'phone_number',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###