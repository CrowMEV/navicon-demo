from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%"
            "(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


# class Base(DeclarativeBase):
#     metadata = MetaData(
#         naming_convention={
#             "all_column_names": lambda constraint, table: "_".join(
#                 [column.name for column in constraint.columns.values()]
#             ),
#             "ix": "ix__%(table_name)s__%(all_column_names)s",
#             "uq": "uq__%(table_name)s__%(all_column_names)s",
#             "ck": "ck__%(table_name)s__%(constraint_name)s",
#             "fk": (
#                 "fk__%(table_name)s__%(all_column_names)s__"
#                 "%(referred_table_name)s"
#             ),
#             "pk": "pk__%(table_name)s",
#         }
#     )
