# === Stage 6: Связанная сущность ===
# Project: KennelBooking
import uuid
from datetime import date

class Pet:
    def __init__(self, name, species, breed, age, photo_url=None, notes=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.photo_url = photo_url
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "photo_url": self.photo_url,
            "notes": self.notes,
        }

    @staticmethod
    def from_dict(data):
        return Pet(
            name=data["name"],
            species=data.get("species"),
            breed=data.get("breed"),
            age=data.get("age"),
            photo_url=data.get("photo_url"),
            notes=data.get("notes"),
        )


class BookingRepository:
    def __init__(self):
        self._pets = {}

    def add_pet(self, pet):
        self._pets[pet.id] = pet
        return pet

    def get_pet(self, pet_id):
        return self._pets.get(pet_id)

    def list_all(self):
        return list(self._pets.values())

    def update_pet(self, pet_id, updates):
        pet = self._pets.get(pet_id)
        if not pet:
            return None
        for key, value in updates.items():
            setattr(pet, key, value)
        return pet

    def delete_pet(self, pet_id):
        return self._pets.pop(pet_id, None)


def create_sample_pet(name="Рекс", species="собака", breed="лабрадор", age=3):
    return Pet(name=name, species=species, breed=breed, age=age)


def format_pet_summary(pet):
    return f"{pet.name} ({pet.species}, {pet.breed}, {pet.age} лет)"


def display_pets(pets):
    if not pets:
        print("Список питомцев пуст.")
        return
    for pet in pets:
        print(f"ID: {pet.id}")
        print(f"  {format_pet_summary(pet)}")
        if pet.notes:
            print(f"  Примечание: {pet.notes}")
        print()


if __name__ == "__main__":
    repo = BookingRepository()
    pet = create_sample_pet()
    repo.add_pet(pet)
    display_pets(repo.list_all())
