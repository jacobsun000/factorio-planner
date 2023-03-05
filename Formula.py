from typing import *
from Part import Part


class Formula:
    def __init__(self, name: str, inputs = {}, outputs = {}):
        self.name = name
        self.time = 0
        self.input:dict[Part, float] = inputs
        self.output:dict[Part, float] = outputs
