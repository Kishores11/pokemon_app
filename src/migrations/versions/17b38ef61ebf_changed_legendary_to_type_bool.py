"""changed_legendary_to_type_bool

Revision ID: 17b38ef61ebf
Revises: 
Create Date: 2023-06-05 14:54:53.376384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b38ef61ebf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        op.execute("ALTER TABLE pokemon ALTER COLUMN legendary TYPE BOOLEAN USING legendary::boolean")


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.alter_column('legendary',
               existing_type=sa.Boolean(),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###