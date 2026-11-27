# === Stage 11: Текстовый поиск ===
# Project: KennelBooking
def search_bookings(bookings, query):
    """Поиск по текстовым полям брони без учёта регистра с подсветкой совпадений."""
    if not query:
        return bookings

    query = query.strip().lower()
    text_fields = ("pet_name", "notes")

    def highlight(text):
        if not text:
            return text
        result = []
        text_lower = text.lower()
        start = 0
        while True:
            idx = text_lower.find(query, start)
            if idx == -1:
                result.append(text[start:])
                break
            result.append(text[start:idx])
            result.append("[" + text[idx:idx + len(query)] + "]")
            start = idx + len(query)
        return "".join(result)

    matches = []
    for booking in bookings:
        row = []
        for key in ("kennel", "pet_name", "start_date", "end_date", "price", "status", "notes"):
            value = booking.get(key, "")
            if isinstance(value, (int, float)):
                row.append(str(value))
            else:
                row.append(highlight(str(value)))
        matches.append(row)

    return matches


if __name__ == "__main__":
    sample = [
        {"kennel": "A1", "pet_name": "Барсик", "start_date": "2025-01-01",
         "end_date": "2025-01-05", "price": 1500, "status": "active", "notes": "с меткой"},
        {"kennel": "B2", "pet_name": "Рекс", "start_date": "2025-02-01",
         "end_date": "2025-02-10", "price": 2000, "status": "cancelled", "notes": ""},
    ]
    for row in search_bookings(sample, "актив"):
        print(" | ".join(row))
