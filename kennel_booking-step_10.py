# === Stage 10: Сортировка записей ===
# Project: KennelBooking
from datetime import datetime


def get_sort_key(record, field):
    if field == "date_created":
        try:
            return datetime.strptime(record[field], "%Y-%m-%d")
        except (KeyError, ValueError, TypeError):
            return datetime.min
    return record.get(field)


def sort_bookings(bookings, field, reverse=False):
    if not isinstance(bookings, list):
        raise TypeError("Ожидается список записей")
    if field not in ("kennel", "date_created"):
        raise ValueError("Допустимые поля для сортировки: kennel, date_created")
    return sorted(bookings, key=lambda rec: get_sort_key(rec, field), reverse=reverse)


def sort_by_kennel(bookings, reverse=False):
    return sort_bookings(bookings, "kennel", reverse)


def sort_by_creation(bookings, reverse=False):
    return sort_bookings(bookings, "date_created", reverse)


if __name__ == "__main__":
    sample = [
        {"kennel": "K-03", "date_created": "2024-05-10", "price": 1500, "status": "active"},
        {"kennel": "K-01", "date_created": "2024-05-08", "price": 1200, "status": "active"},
        {"kennel": "K-02", "date_created": "2024-05-09", "price": 1350, "status": "pending"},
    ]

    print("По вольеру (возр.):")
    for b in sort_by_kennel(sample):
        print(b["kennel"], b["date_created"], b["price"])

    print("По вольеру (убыв.):")
    for b in sort_by_kennel(sample, reverse=True):
        print(b["kennel"], b["date_created"], b["price"])

    print("По дате создания (возр.):")
    for b in sort_by_creation(sample):
        print(b["date_created"], b["kennel"], b["price"])

    print("По дате создания (убыв.):")
    for b in sort_by_creation(sample, reverse=True):
        print(b["date_created"], b["kennel"], b["price"])
