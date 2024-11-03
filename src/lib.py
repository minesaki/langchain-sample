
def print_prompt(data, end: str | None = "\n"):
    END = '\033[0m'
    print(END, end='')
    print("> ", end='')
    print(data, end=end)

def print_answer(data, end: str | None = "\n"):
    GREEN = '\033[32m'
    END = '\033[0m'
    print(GREEN, end='')
    print(data, end='')
    print(END, end=end)

def print_debug(data, end: str | None = "\n"):
    GRAY = '\033[90m'
    END = '\033[0m'
    print(GRAY, end='')
    print(data, end='')
    print(END, end=end)
