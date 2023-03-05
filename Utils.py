from typing import *


def sum_dict(a: dict, b: dict) -> dict:
    ans = dict()
    for key in a.keys() | b.keys():
        ans[key] = sum([i.get(key, 0) for i in (a, b)])
    return ans


def color_map(order: int) -> str:
    color = ['#C62828', '#AD1457', '#6A1B9A', '#283593', '#1565C0', '#00838F', '#00695C',
             '#2E7D32', '#9E9D24', '#FF8F00', '#D84315', '#4E342E', '#424242', '#37474F']
    return color[order]
