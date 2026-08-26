from readchar import readkey
from dataclasses import dataclass, field

@dataclass
class InputHandler:
    def kb(self):
        opt = readkey()
        return (opt)
