def welcome():
    print("Welcome to Escape Room: The Riddle Vault!")
    print("Solve all 3 riddles to escape...\n")

def room1():
    print("Room 1: The First Riddle")
    print("Riddle: What has to be broken before you can use it?")
    answer = input("Your answer: ").strip().lower()
    normalized = answer.replace(".", "").strip()
    if "egg" in normalized:
        print("That is correct — moving to Room 2.\n")
        return True
    else:
        print("That is wrong. You're stuck in Room 1.\n")
        return False

def room2():
    print("Room 2: The Second Riddle")
    print("Riddle: What word contains 26 letters but only has three syllables?")
    answer = input("Your answer: ").strip().lower()
    normalized = answer.replace(".", "").strip()
    if normalized == "alphabet" or normalized == "the alphabet":
        print("That is correct. Room 3 awaits.\n")
        return True
    else:
        print("That is wrong. You're stuck in Room 2.\n")
        return False

def room3():
    print("Room 3: The Phonetic Lock")
    print('Riddle: How do you spell "COW" in thirteen letters?')
    answer = input("Your answer: ").strip().lower()
    normalized = answer.replace("-", " ").replace(".", "").replace(",", "").strip()

    accepted_answers = {
        "see o double you",
        "see oh double you",
        "s e e o double you",
        "s e e oh double you",
        "s-e-e o double you",
        "s-e-e oh double you"
    }

    if normalized in accepted_answers:
        print("That is correct! You’ve successfully solved all the riddles.\n")
        return True
    else:
        print("That is wrong. You're stuck in Room 3.\n")
        return False

def game():
    welcome()
    if not room1():
        return
    if not room2():
        return
    if room3():
        print("Congratulations! You have escaped the Riddle Vault.\n")

if __name__ == "__main__":
    game()