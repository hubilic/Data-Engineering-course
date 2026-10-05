class DBConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_open = False
        self.is_closed = False

    def __enter__(self):
        if self.is_closed:
            raise RuntimeError("Cannot open closed connection")

        self.is_open = True
        print(f"Connected to {self.host}:{self.port}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.is_open = False
        self.is_closed = True
        print("Connection closed")
        return False

    def execute(self, query):
        if not self.is_open:
            raise RuntimeError("Connection is not open")

        print(f"Executing query: {query}")