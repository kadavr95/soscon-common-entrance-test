class CaseSwitcher:
    def __init__(self, mode):
        self.mode = mode

    def __call__(self, payload):
        if self.mode == 'upper':
            return payload.upper()
        elif self.mode == 'lower':
            return payload.lower()
        elif self.mode == 'swap':
            return payload.swapcase()
        else:
            return f"Oops unsupported mode {self.mode}"


model = CaseSwitcher('upper')
result = model('upper case')
print(result)
