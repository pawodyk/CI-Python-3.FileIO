def show_menu():
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")

    option = input("Enter Option: ")
    return option


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("option 1")
        elif option == "2":
            print("option 2")
        elif option == "3":
            print("option 3")
            break
        else:
            print("Invalid option")
        print("")


game_loop()
