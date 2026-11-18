# === Stage 7: Связи между сущностями ===
# Project: KennelBooking
def get_pets_for_booking(booking, pets_by_id=None):
    """Получить всех «питомец», привязанных к заданной «бронь», и проверить целостность связи."""
    if pets_by_id is None:
        pets_by_id = {}

    booking_id = booking.get("id")
    if booking_id is None:
        raise ValueError("Бронь не имеет идентификатора")

    referenced_ids = set()
    pets = []
    for pet in pets_by_id.values():
        if pet.get("booking_id") == booking_id:
            pets.append(pet)
            referenced_ids.add(pet["id"])

    missing = referenced_ids - set(pets_by_id.keys())
    if missing:
        raise ValueError(f"Потеряна целостность связи: питомцы {sorted(missing)} не найдены среди записей")

    return pets


def validate_booking_pets_link(booking, pets_by_id):
    """Проверить, что все «питомец» для «бронь» существуют и связь не нарушена."""
    booking_id = booking.get("id")
    if booking_id is None:
        return False

    referenced_ids = {pet["id"] for pet in pets_by_id.values() if pet.get("booking_id") == booking_id}
    if referenced_ids:
        available_ids = set(pets_by_id.keys())
        if referenced_ids - available_ids:
            return False
    return True


def build_pets_for_booking(pets_by_id, booking_id):
    """Собрать список «питомец» для конкретной «бронь» по идентификатору."""
    if booking_id is None:
        raise ValueError("Бронь не имеет идентификатора")

    pets = [pet for pet in pets_by_id.values() if pet.get("booking_id") == booking_id]
    referenced_ids = {pet["id"] for pet in pets}
    missing = referenced_ids - set(pets_by_id.keys())
    if missing:
        raise ValueError(f"Нарушена целостность: не найдены питомцы {sorted(missing)}")

    return pets
