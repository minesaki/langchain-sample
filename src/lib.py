RESET = "\033[0m"
GREEN = "\033[32m"
GRAY = "\033[90m"


def print_prompt(data, end: str | None = "\n"):
    print(RESET, end="")
    print("> ", end="")
    print(data, end=end)


def print_answer(data, end: str | None = "\n"):
    print(GREEN, end="")
    print(data, end="")
    print(RESET, end=end)


def print_debug(*data, end: str | None = "\n"):
    print(GRAY, end="")
    for d in data:
        print(d, end="")
    print(RESET, end=end)
