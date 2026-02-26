from typing import Dict, Optional
from app.models.base_model import BaseModel

class InMemoryRepository:
    
    def __init__(self):
        self._storage: Dict[str, BaseModel] = {}  # 🗄️ "Base de données" en mémoire
        self._model_class = model_class
    
    def add(self, obj: BaseModel) -> None:
        if obj.id in self._storage:
            raise ValueError("Object already exists")
        self._storage[obj.id] = obj  # Stocke l'objet avec son ID comme clé
    
    def get(self, id: str) -> Optional[BaseModel]:
        return self._storage.get(id)  # Recherche rapide O(1)
    
    def update(self, obj_id: str, data: dict):
        obj = self._storage.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
                obj.save() # BaseModel.save() — pas obj.update()
        return obj
