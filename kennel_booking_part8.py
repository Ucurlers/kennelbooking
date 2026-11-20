# === Stage 8: Генерация идентификаторов ===
# Project: KennelBooking
import uuid
from datetime import datetime


PROJECT_PREFIX = "kb"


def generate_booking_id() -> str:
    booking_id = f"{PROJECT_PREFIX}-bk-{uuid.uuid4().hex[:8]}"
    if booking_id in _used_booking_ids:
        return generate_booking_id()
    _used_booking_ids.add(booking_id)
    return booking_id


def generate_pet_id() -> str:
    pet_id = f"{PROJECT_PREFIX}-pet-{uuid.uuid4().hex[:8]}"
    if pet_id in _used_pet_ids:
        return generate_pet_id()
    _used_pet_ids.add(pet_id)
    return pet_id


def is_booking_id_available(booking_id: str) -> bool:
    return booking_id not in _used_booking_ids


def is_pet_id_available(pet_id: str) -> bool:
    return pet_id not in _used_pet_ids


_used_booking_ids: set[str] = set()
_used_pet_ids: set[str] = set()


if __name__ == "__main__":
    print(generate_booking_id())
    print(generate_booking_id())
    print(generate_pet_id())
    print(generate_pet_id())
    print(is_booking_id_available("kb-bk-11111111"))
    print(is_pet_id_available("kb-pet-22222222"))
