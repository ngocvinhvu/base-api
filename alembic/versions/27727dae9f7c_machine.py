"""machine

Revision ID: 27727dae9f7c
Revises: ec72685b6da9
Create Date: 2021-05-05 15:59:39.006959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '27727dae9f7c'
down_revision = 'ec72685b6da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### Create datatype in postgres
    machinestatus = postgresql.ENUM('ONLINE', 'OFFLINE', name='machinestatus')
    machinestatus.create(op.get_bind())
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine', sa.Column('access_key', sa.String(length=20), nullable=True))
    op.add_column('machine', sa.Column('agent_version', sa.String(), nullable=True))
    op.add_column('machine', sa.Column('hostname', sa.String(length=500), nullable=True))
    op.add_column('machine', sa.Column('ip_address', sa.String(), nullable=True))
    op.add_column('machine', sa.Column('operation_status', sa.Boolean(), nullable=True))
    op.add_column('machine', sa.Column('os_version', sa.String(), nullable=True))
    op.add_column('machine', sa.Column('seed_key', sa.String(length=128), nullable=True))
    op.add_column('machine', sa.Column('status', postgresql.ENUM('ONLINE', 'OFFLINE', name='machinestatus'), nullable=True))
    op.add_column('machine', sa.Column('tenant_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_unique_constraint(None, 'machine', ['access_key'])
    op.drop_column('machine', 'host_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine', sa.Column('host_name', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'machine', type_='unique')
    op.drop_column('machine', 'tenant_id')
    op.drop_column('machine', 'status')
    op.drop_column('machine', 'seed_key')
    op.drop_column('machine', 'os_version')
    op.drop_column('machine', 'operation_status')
    op.drop_column('machine', 'ip_address')
    op.drop_column('machine', 'hostname')
    op.drop_column('machine', 'agent_version')
    op.drop_column('machine', 'access_key')
    # ### end Alembic commands ###
    machinestatus = postgresql.ENUM('ONLINE', 'OFFLINE', name='machinestatus')
    machinestatus.drop(op.get_bind())
