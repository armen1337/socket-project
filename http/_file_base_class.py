from utils.exceptions import FileFormatMismatchException


class BaseFile:
    def __init__(self, filepath: str):
        self._path = filepath
        with open(self._path, 'r') as f:
            self._contents = "".join(f.readlines())

    def get_contents(self) -> str:
        return self._contents

    @staticmethod
    def _verify_file_format(filepath, file_format: str) -> None:
        actual_format = filepath.split("/")[-1].split(".")[-1]
        if file_format != actual_format:
            raise FileFormatMismatchException(f"Expected '.{file_format}' but found '.{actual_format}'")
