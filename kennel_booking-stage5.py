# === Stage 5: Удаление и восстановление ===
# Project: KennelBooking
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class BookingStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Booking:
    kennel_id: str
    pet_id: str
    start_date: date
    end_date: date
    price: float
    status: BookingStatus = BookingStatus.ACTIVE
    soft_deleted: bool = False
    deleted_at: Optional[date] = None
    _restore_counter: int = field(default=0, repr=False)

    def soft_delete(self):
        if self.soft_deleted:
            raise ValueError("Уже удалена")
        self.soft_deleted = True
        self.deleted_at = date.today()
        self.status = BookingStatus.CANCELLED

    def restore(self):
        if not self.soft_deleted:
            raise ValueError("Не удалена")
        if self._restore_counter >= 1:
            raise ValueError("Восстановлена")
        self.soft_deleted = False
        self.deleted_at = None
        self.status = BookingStatus.ACTIVE
        self._restore_counter += 1

    def cancel(self):
        self.status = BookingStatus.CANCELLED
