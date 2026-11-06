result = []


def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8: 4}

for key in data:
    try:
        if not isinstance(key, (int, float)):
            raise TypeError("Ключ не є числом")

        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError, KeyError) as err:
        print(f"Помилка: {err}")

print(result)