# === Stage 9: Фильтрация записей ===
# Project: KennelBooking
from __future__ import annotations


def _parse_date(value) -> str | None:
    """Нормализовать значение поля «даты» в строку формата YYYY-MM-DD."""
    if value is None:
        return None
    if isinstance(value, str):
        candidate = value.strip()
        if not candidate:
            return None
        return candidate
    if hasattr(value, "isoformat"):
        return value.isoformat()
    if hasattr(value, "strftime"):
        return value.strftime("%Y-%m-%d")
    return str(value)


def filter_bookings_by_date(bookings, target_date):
    """Отфильтровать брони по точному значению поля «даты».

    target_date — строка YYYY-MM-DD либо объект, дающий isoformat().
    """
    target = _parse_date(target_date)
    if target is None:
        return []
    return [booking for booking in bookings if _parse_date(booking.get("даты")) == target]


def filter_bookings_by_date_range(bookings, start_date, end_date, inclusive_end=True):
    """Отфильтровать брони по диапазону значений поля «даты».

    start_date и end_date — строки YYYY-MM-DD либо объекты с isoformat().
    end_date по умолчанию включён в границу; при inclusive_end=False — нет.
    """
    start = _parse_date(start_date)
    end = _parse_date(end_date)
    if start is None or end is None:
        return []
    def to_sort_key(date_str):
        return date_str
    result = []
    for booking in bookings:
        booking_date = _parse_date(booking.get("даты"))
        if booking_date is None:
            continue
        if start <= booking_date <= end if inclusive_end else start <= booking_date < end:
            result.append(booking)
    return result
