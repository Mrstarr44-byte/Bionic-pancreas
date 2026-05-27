from datetime import datetime, timezone
from typing import List, Optional

from flask_login import UserMixin
import bcrypt
from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db, login


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))

    language: Mapped[str] = mapped_column(String(5), default='tr')
    telegram_id: Mapped[Optional[str]] = mapped_column(String(50), unique=True, index=True)
    avatar_filename: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    simulation_logs: Mapped[List["SimulationLog"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def set_password(self, password: str) -> None:
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        if self.password_hash is None:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self) -> str:
        return f'<User {self.username}>'


class MealPreset(db.Model):
    __tablename__ = 'meal_presets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_tr: Mapped[str] = mapped_column(String(100))
    name_en: Mapped[str] = mapped_column(String(100))
    carb_per_serving: Mapped[float] = mapped_column(Float)
    gi_value: Mapped[int] = mapped_column(Integer)
    category: Mapped[Optional[str]] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f'<MealPreset {self.name_tr}/{self.name_en} (Carbs: {self.carb_per_serving}g, GI: {self.gi_value})>'


class SimulationLog(db.Model):
    __tablename__ = 'simulation_logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    action_type: Mapped[str] = mapped_column(String(50))
    value: Mapped[float] = mapped_column(Float)
    glucose_before: Mapped[Optional[float]] = mapped_column(Float)
    glucose_after: Mapped[Optional[float]] = mapped_column(Float)
    cell_status: Mapped[Optional[str]] = mapped_column(String(50))
    mode: Mapped[Optional[str]] = mapped_column(String(50))

    timestamp: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

    user: Mapped["User"] = relationship(back_populates="simulation_logs")

    def __repr__(self) -> str:
        return f'<SimulationLog {self.action_type} - Value: {self.value}>'


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
