class Reader:
    _readers: dict = {}

    def __init__(self, base_path: str, collection_paths: dict = None):
        if not isinstance(base_path, str):
            raise ValueError("base_path must be a string")

        self._base_path = base_path
        self.collection_paths = collection_paths or {}

    @property
    def base_path(self) -> str:
        return self._base_path

    @base_path.setter
    def base_path(self, new_base_path: str):
        if not isinstance(new_base_path, str):
            raise ValueError("base_path must be a string")
        self._base_path = new_base_path

    @property
    def collection_paths(self) -> dict:
        return self._collection_paths

    @collection_paths.setter
    def collection_paths(self, new_collection_paths: dict):
        if not isinstance(new_collection_paths, dict):
            raise ValueError("collection_paths must be a dictionary")
        self._collection_paths = new_collection_paths

    def replace_collection_paths(self, new_collection_paths: dict):
        """Replace the entire collection using the validated setter."""
        self.collection_paths = new_collection_paths

    def define_reader(self, reader_key: str, reader_function):
        self._readers[reader_key] = reader_function
        
    def reader(self, reader_key, path, *args, **kwargs):
        return self._readers[reader_key](*args, **kwargs)