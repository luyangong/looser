import sys

def error(line: int, message: str):
    report(line, "", message)

def report(line: int, where: str, message: str):
    print("[line " + str(line) + "] Error" + where + ": " + message)
    
def run(source):
    scanner = Scanner(source)
    tokens = scanner.scanTokens()
    for token in tokens:
        print(token)


def runFile(fn):
    with open(fn) as f:
        content = f.read()
    run(content)


def runPrompt():
    while True:
        line = input("> ")
        if not line:
            break
        run(line)


def main(args):
    if (len(args)) > 1:
        print("Usage: looser [script]")
        exit(64)
    elif len(args) == 1:
        runFile(args[0])
    else
        runPrompt()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
