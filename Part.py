from typing import *
from Utils import sum_dict, color_map
import pygraphviz as pgv


class Part:
    def __init__(self, name: str, is_primitive: bool = True, formula=None, ):
        self.name = name
        self.formula = formula
        self.is_primitive = is_primitive
        self.order = 0 if is_primitive else -1

    def get_order(self):
        if self.order != -1:
            return self.order
        # Order equals maximum order of this part's components + 1
        self.order = max([part.get_order() for part in self.formula.input]) + 1
        return self.order

    def get_all_parts(self, n: float = 1) -> dict:
        ans = {self: n}
        if self.is_primitive or n <= 0.001:
            return ans
        # Add all components' part into the total parts dict
        for part, num in self.formula.input.items():
            amount = self.formula.input[part] * n / self.formula.output[self]
            temp = part.get_all_parts(amount)
            ans = sum_dict(ans, temp)
        return ans

    def get_all_primitives(self, n: float = 1) -> dict:
        temp = self.get_all_parts(n)
        return dict(((k, v) for k, v in temp if k.get_order == 0))

    def visualize(self, output: str, n: float = 1):
        g = pgv.AGraph(directed=True, strict=True, rankdir="LR")
        # Add all part node to the graph
        parts_dict = self.get_all_parts(n)
        for part, num in parts_dict.items():
            text = f"{part} num: {num:.2f}"
            g.add_node(text, color=color_map(part.get_order()))
        # Link the node according to the formula
        for order in range(1, self.get_order()+1):
            for part, num in parts_dict.items():
                if part.get_order() != order:
                    continue
                for part_prev in part.formula.input:
                    text = f"{part} num: {num:.2f}"
                    text_prev = f"{part_prev} num: {parts_dict[part_prev]:.2f}"
                    g.add_edge(text_prev, text)
        g.layout('dot')
        g.draw(output)

    def __repr__(self):
        # {self.get_order()}
        return f"{self.name}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def main():
    iron_ore = Part("iron_ore")
    iron_plate = Part("iron_plate", False)
    iron_plate_formula = Formula("iron_plate", 3.2)
    iron_plate_formula.input = {iron_ore: 1}
    iron_plate_formula.output = {iron_plate: 1}
    iron_plate.formula = iron_plate_formula
    print(iron_plate.get_all_parts())
    iron_plate.visualize()


if __name__ == '__main__':
    from Formula import Formula
    main()
