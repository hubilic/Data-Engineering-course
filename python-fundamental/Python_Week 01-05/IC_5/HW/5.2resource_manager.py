class TempDir():
    def __enter__(self):
        import tempfile
        self.temp_dir = tempfile.TemporaryDirectory()
        return self.temp_dir.name

    def __exit__(self, exc_type, exc_value, traceback):
        self.temp_dir.cleanup()
        return False
