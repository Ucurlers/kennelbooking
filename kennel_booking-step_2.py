# === Stage 2: Проверка полей ===
# Project: KennelBooking
from datetime import date, datetime, timedelta


def parse_date(value):
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты: '{value}'. Ожидается YYYY-MM-DD или DD.MM.YYYY.")


def validate_kennel(kennel):
    if kennel is None or kennel.strip() == "":
        raise ValueError("Вольер не может быть пустым.")
    kennel = kennel.strip()
    if len(kennel) > 20:
        raise ValueError(f"Вольер '{kennel}' слишком длинный (максимум 20 символов).")
    for char in kennel:
        if not (char.isalnum() or char in ("-", "_", "/")):
            raise ValueError(f"Вольер '{kennel}' содержит недопустимые символы.")
    return kennel


def validate_dates(start, end):
    start = parse_date(start)
    end = parse_date(end)
    if start > end:
        raise ValueError(f"Дата начала '{start}' позже даты окончания '{end}'.")
    if (end - start).days > 30:
        raise ValueError("Длительность бронирования не может превышать 30 дней.")
    return start, end


def validate_price(price):
    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError(f"Цена '{price}' должна быть числом.")
    if price <= 0:
        raise ValueError("Цена должна быть положительным числом.")
    if price != round(price, 2):
        raise ValueError("Цена должна быть указана с точностью до двух знаков.")
    return round(price, 2)


def validate_status(status):
    status = status.strip().lower()
    if status not in ("забронирована", "активна", "отменена", "завершена"):
        raise ValueError(
            f"Неизвестный статус '{status}'. Допустимые: забронирована, активна, отменена, завершена."
        )
    return status


def validate_booking(kennel, start, end, price, status):
    kennel = validate_kennel(kennel)
    start, end = validate_dates(start, end)
    price = validate_price(price)
    status = validate_status(status)
    return kennel, start, end, price, status
