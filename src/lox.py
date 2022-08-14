import sys

def main():
    if len(sys.argv) > 2:
        print("Usage: plox [script]")
        exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[0])
    else:
        run_prompt()

def run_file(filename: str):
    with open(filename) as f:
        run(f.read())

def run_prompt():
    while True:
        line = input("> ")
        if not line:
            break
        run(line)

def run(string: str):
    pass

if __name__ == "__main__":
    main()
