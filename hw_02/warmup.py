def reverse_string(s: str) -> str:
    stack = []
    for ch in s:
        stack.append(ch)

    result = []
    while stack:
        result.append(stack.pop())

    return "".join(result)


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string("Алматы"))
