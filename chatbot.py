from agriculture import information

def chatbot():
    print("\nHello! I'm InfoBOT. Im Here to Assist You.\n")

    while True:
        user_input = input("You : ").lower()

        if user_input == 'thank you':
            print("\nHad a good conversation with you. Have a great day! Goodbye!\n")
            break

        elif "hi" in user_input:

            username = input("\nEnter Name : ")

            print("\nHi",username,". Are you from Agricultural Background?\n")

        elif "hello" in user_input:

            username = input("\nEnter Name : ")

            print("\nHi",username,". Are you from Agricultural Background?\n")

        elif "namaste" in user_input:

            username = input("\nEnter Name : ")

            print("\nHi",username,". Are you from Agricultural Background?\n")

        elif "hey" in user_input:

            username = input("\nEnter Name : ")

            print("\nHi",username,". Are you from Agricultural Background?\n")

        elif "yo" in user_input:

            username = input("\nEnter Name : ")

            print("\nHi",username,". Are you from Agricultural Background?\n")


           
        elif 'ok' in user_input:
            print("\nHello there!! Im here to assist you. Type the CROP NAME you want to know about\n")

        elif 'yes' in user_input:
            print("\nExcellent! Its good to have a knowledge on crops.Type OK to know more about crops\n")
        elif 'no' in user_input:
            print("\nI will assist you. Which crop do you want to know about??\n")

        else:
            details = information(user_input)
            if details:
                print(f"\nSure! Here's the information on {user_input}:\n")
                for crops in details:
                    print(f"{crops}")
            else:
                print("\nI'm sorry, I don't have any information on that crop. Can you ask for another crop.\n")

if __name__ == "__main__":
    chatbot()
