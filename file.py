def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("ChatBot: Goodbye!")
            break

        elif user in ["hi", "hello", "hey"]:
            print("ChatBot: Hi! How are you?")

        elif user == "i am fine" or user == "fine":
            print("ChatBot: That's great to hear!")

        elif "your name" in user:
            print("ChatBot: My name is ChatBot.")

        elif "how are you" in user:
            print("ChatBot: I am doing well. Thank you!")

        elif "thanks" in user:
            print("ChatBot: No problem")
            
        elif user == "calculate":
            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                if op == "+":
                    print("ChatBot:", num1 + num2)
                elif op == "-":
                    print("ChatBot:", num1 - num2)
                elif op == "*":
                    print("ChatBot:", num1 * num2)
                elif op == "/":
                    if num2 != 0:
                        print("ChatBot:", num1 / num2)
                    else:
                        print("ChatBot: Cannot divide by zero.")
                else:
                    print("ChatBot: Invalid operator.")
            except:
                print("ChatBot: Invalid input.")

        else:
            print("ChatBot: Sorry, I don't understand.")

chatbot()