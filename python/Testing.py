def balance(left: int, right:int):
    diff = right - left
    if diff < 0:
        return abs(diff), "L"
    else:
        return abs(diff), "R"

print(balance(1000, 500))