# === Stage 1: Каркас модуля ===
# Project: KennelBooking
from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


@dataclass
class Kennel:
    kennel_id: int
    capacity: int
    price_per_day: float


@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int


@dataclass
class Booking:
    booking_id: int
    kennel: Kennel
    pet: Pet
    start_date: date
    end_date: date
    price: float
    status: BookingStatus = BookingStatus.PENDING


def create_demo_bookings() -> list[Booking]:
    kennel = Kennel(kennel_id=1, capacity=4, price_per_day=500.0)
    pet = Pet(pet_id=1, name="Рекс", species="собака", age=3)

    start = date(2024, 6, 1)
    end = date(2024, 6, 4)
    days = (end - start).days
    price = round(kennel.price_per_day * days, 2)

    return [
        Booking(
            booking_id=1001,
            kennel=kennel,
            pet=pet,
            start_date=start,
            end_date=end,
            price=price,
            status=BookingStatus.CONFIRMED,
        ),
        Booking(
            booking_id=1002,
            kennel=kennel,
            pet=pet,
            start_date=date(2024, 6, 10),
            end_date=date(2024, 6, 12),
            price=round(kennel.price_per_day * 2, 2),
            status=BookingStatus.PENDING,
        ),
        Booking(
            booking_id=1003,
            kennel=kennel,
            pet=pet,
            start_date=date(2024, 6, 15),
            end_date=date(2024, 6, 17),
            price=round(kennel.price_per_day * 2, 2),
            status=BookingStatus.CANCELLED,
        ),
    ]


def main() -> None:
    bookings = create_demo_bookings()
    for booking in bookings:
        print(
            f"Бронь #{booking.booking_id}: вольер {booking.kennel.kennel_id}, "
            f"питомец '{booking.pet.name}', "
            f"{booking.start_date} -> {booking.end_date}, "
            f"цена {booking.price} руб., статус {booking.status.value}"
        )


if __name__ == "__main__":
    main()
