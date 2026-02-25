class InMemoryRepository(Repository):
    def __init__(self, model_class: Type[BaseModel]):
        self._storage: Dict[str, BaseModel] = {}  # 🗄️ "Base de données" en mémoire
        self._model_class = model_class
    
    def add(self, obj: BaseModel) -> None:
        if obj.id in self._storage:
            raise ValueError("Object already exists")
        self._storage[obj.id] = obj  # Stocke l'objet avec son ID comme clé
    
    def get(self, id: str) -> Optional[BaseModel]:
        return self._storage.get(id)  # Recherche rapide O(1)
    
    def update(self, id: str,  dict) -> Optional[BaseModel]:
        obj = self._storage.get(id)
        if obj is None:
            return None
        for key, value in  # Met à jour les attributs autorisés
            if hasattr(obj, key) and key not in ['id', 'created_at', 'updated_at']:
                setattr(obj, key, value)
        obj.update()  # Refresh timestamp
        return obj
