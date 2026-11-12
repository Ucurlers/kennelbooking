# === Stage 4: Редактирование записей ===
# Project: KennelBooking
from datetime import date

ALLOWED_BOOKING_FIELDS = ("status", "price")


def edit_booking(booking, booking_id, changes):
    if not isinstance(changes, dict):
        raise TypeError("changes должен быть словарём")

    updated = dict(booking)
    updated["_id"] = booking_id

    for key, value in changes.items():
        if key not in ALLOWED_BOOKING_FIELDS:
            raise ValueError(
                f"Поле '{key}' не доступно для редактирования. "
                f"Допустимые: {ALLOWED_BOOKING_FIELDS}"
            )
        if key == "status":
            valid_statuses = ("pending", "confirmed", "completed", "cancelled")
            if value not in valid_statuses:
                raise ValueError(
                    f"Недопустимый статус '{value}'. "
                    f"Допустимые: {valid_statuses}"
                )
        if key == "price":
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError("Цена должна быть неотрицательным числом")
        updated[key] = value

    return updated
