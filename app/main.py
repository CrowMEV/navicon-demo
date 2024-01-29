import sqlalchemy as sq

from settings import config

engine = sq.create_engine(
    config.dsn,
    echo=True,
)
