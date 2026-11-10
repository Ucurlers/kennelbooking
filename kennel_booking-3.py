# === Stage 3: Хранилище в памяти ===
# Project: KennelBooking
import threading
from typing import Dict, List, Optional


class Reservation:
    """Бронь передержки."""

    def __init__(self, kennel_id: str, pet_id: str, start_date: str,
                 end_date: str, price: float, status: str = "pending"):
        self.kennel_id = kennel_id
        self.pet_id = pet_id
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.status = status

        self.id = self._generate_id()

    @staticmethod
    def _generate_id() -> str:
        counter = 1
        lock = threading.Lock()

        def _make() -> str:
            nonlocal counter
            with lock:
                counter += 1
                return f"R{counter:06d}"

        return _make()

    def __repr__(self) -> str:
        return (
            f"Reservation(id={self.id!r}, kennel_id={self.kennel_id!r}, "
            f"pet_id={self.pet_id!r}, start_date={self.start_date!r}, "
            f"end_date={self.end_date!r}, price={self.price!r}, "
            f"status={self.status!r})"
        )


class ReservationStore:
    """Память для сущностей «бронь»."""

    def __init__(self) -> None:
        self._reservations: Dict[str, Reservation] = {}
        self._lock = threading.Lock()

    def add(self, reservation: Reservation) -> Reservation:
        with self._lock:
            self._reservations[reservation.id] = reservation
            return reservation

    def get(self, reservation_id: str) -> Optional[Reservation]:
        with self._lock:
            return self._reservations.get(reservation_id)

    def list(self) -> List[Reservation]:
        with self._lock:
            return list(self._reservations.values())

    def __len__(self) -> int:
        with self._lock:
            return len(self._reservations)


if __name__ == "__main__":
    store = ReservationStore()

    r1 = Reservation("K1", "P1", "2025-01-01", "2025-01-05", 500.0)
    r2 = Reservation("K2", "P2", "2025-01-06", "2025-01-10", 700.0)

    store.add(r1)
    store.add(r2)

    print("Все брони:", store.list())
    print("Бронь R000001:", store.get("R000001"))
    print("Отсутствующая:", store.get("R000099"))
    print("Количество:", len(store))
