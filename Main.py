from Part import Part
from Formula import Formula
import json


def process_items(items: dict) -> dict:
    ans = dict()
    for item in items:
        ans[item] = Part(item, False)
    return ans


def process_resources(resources: dict) -> dict:
    ans = dict()
    for resource in resources:
        ans[resource] = Part(resource)
    return ans


def process_recipes(items: dict, recipes: dict):
    for name, recipe in recipes.items():
        inputs, outputs = dict(), dict()
        for item_input in recipe["ingredients"]:
            inputs[items[item_input["name"]]] = item_input["amount"]
        for item_output in recipe["results"]:
            outputs[items[item_output["name"]]] = item_output["amount"]
        formula = Formula(name)
        formula.input = inputs
        formula.output = outputs
        for item_output in recipe["results"]:
            items[item_output["name"]].formula = formula


def main():
    data = json.load(open("data.json"))
    items = data["items"]
    recipes = data["recipes"]
    resources = data["resource"]
    items = process_items(items)
    items.update(process_resources(resources))
    process_recipes(items, recipes)

    required_item = "chemical-science-pack"
    items[required_item].visualize('result.png', 48)
    print(items[required_item].get_all_parts(48))


if __name__ == '__main__':
    main()
