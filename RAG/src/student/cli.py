class CLI:
    def index(self, max_chunk_size: int = 2000) -> None:
        raise NotImplementedError("")

    def search(self, query: str, k: int = 10) -> None:
        raise NotImplementedError("")
