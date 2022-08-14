import sys

def main():
    if len(sys.args) > 1:
        print("Usage: plox [script]")
        exit(64)
    elif len(sys.args) == 1:
        run_file(sys.args[0])
    else:
        run_prompt()

def run_file(filename: str):
    pass

def run_prompt():
    pass

if __name__ == "__main__":
    main()
