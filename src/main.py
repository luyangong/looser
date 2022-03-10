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
