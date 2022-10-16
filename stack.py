class Stack:
    def __init__(self, size=0):
        self._values = []
        self.size = size

    def pop(self):
        if self._values:
            return {'val': self._values.pop()}
        return {}

    def get_size(self):
        return {'val': self.size}

    def push(self, val):
        if len(self._values) < self.size:
            self._values.append(val)
            return {'val': val}
        return {}

    def top(self):
        if self._values:
            return {'val': self._values[-1]}
        return {}

    def list(self):
        return list(self._values)

    def reset(self):
        self._values = []
        return []
