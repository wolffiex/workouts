class File:
    name: str
    version: int = 0

    def __init__(self, initial_content):
        self._contents = [initial_content]

    @property
    def content(self):
        return self._contents[-1]

    def update(self, new_content):
        self.version += 1
        self._contents.append(new_content)
