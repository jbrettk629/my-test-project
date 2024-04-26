from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc))
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now(tz=timezone.utc))