from chatbot import chat


def main() -> None:
    print("Hello from agent!")
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            chat(user_input)
        except OSError:
            print("Error Detected, exiting...")
            exit(1)


if __name__ == "__main__":
    main()
