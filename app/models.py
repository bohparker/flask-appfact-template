from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .app import db


class Template(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True)
    type: Mapped[Optional[str]] = mapped_column(String(32))

    def __repr__(self):
        return f'Template({self.id}, "{self.name}")'