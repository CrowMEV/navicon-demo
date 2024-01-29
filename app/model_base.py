import enum

# import sqlalchemy as sq
# from base_db import Base


# class Gender(enum.Enum):
#     female = "female"
#     male = "male"


# users_table = sq.Table(
#     "users",
#     Base.metadata,
#     sq.Column("user_id", sq.Integer, primary_key=True),
#     sq.Column("email", sq.String(256), nullable=False, unique=True),
#     sq.Column("name", sq.String(collation="ru-RU-x-icu"), nullable=False),
#     sq.Column("gender", sq.Enum(Gender, name="gender"), nullable=False),
#     sq.Column("floor", sq.SmallInteger, nullable=False),
#     sq.Column("seat", sq.SmallInteger, nullable=False),
# )
