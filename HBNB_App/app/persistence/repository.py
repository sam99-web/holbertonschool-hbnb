"""
Repository en mémoire (Task 0).
Implémente l'interface générique get/get_all/add/update/delete
qui sera remplacée par SQLAlchemy en Part 3 sans changer le code du Facade.
"""


class InMemoryRepository:
    def __init__(self):
        self._storage = {}  # dict { id: objet }

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data: dict):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()  # met à jour updated_at
        return obj

    def delete(self, obj_id):
        self._storage.pop(obj_id, None)

    def get_by_attribute(self, attr: str, value):
        """Recherche par attribut (ex: email unique pour User)."""
        return next(
            (obj for obj in self._storage.values() if getattr(obj, attr, None) == value),
            None,
        )
