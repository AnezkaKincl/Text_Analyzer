import re

def registered(username, password, list_of_users):
    for user in list_of_users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def analyze_text(text):
    words = text.split()
    
    # Inicializace počítadel
    uppercase_start_count = 0
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    sum_of_numbers = 0
    
    # Vzor pro rozpoznávání čísel
    number_pattern = re.compile(r'\b\d+\b')

    for word in words:
        if word[0].isupper():
            uppercase_start_count += 1
        if word.isupper():
            uppercase_count += 1
        if word.islower():
            lowercase_count += 1

    # Vyhledávání čísel a jejich součtu
    numbers = number_pattern.findall(text)
    number_count = len(numbers)
    sum_of_numbers = sum(int(num) for num in numbers)
    
    # Výstup statistik
    print("----------------------------------------")
    print(f"Number of words starting with an uppercase letter: {uppercase_start_count}")
    print(f"Number of words written in uppercase: {uppercase_count}")
    print(f"Number of words written in lowercase: {lowercase_count}")
    print(f"Number of numbers: {number_count}")
    print(f"Sum of all numbers: {sum_of_numbers}")
    
    # Vytvoření sloupcového grafu
    word_lengths = [len(word) for word in words]
    print("----------------------------------------")
    print(f"{'LEN':5}| {'OCCURENCES':20} |{'NR.':5}")
    print("----------------------------------------")
    for length in range(max(word_lengths) + 1):
        count = word_lengths.count(length)
        if count > 0:
            print(f"{length:5}| {'*' * count:20} |{count:5}")

# Seznam registrovaných uživatelů
registered_users = [
    {'username': 'bob', 'password': '123'},
    {'username': 'ann', 'password': 'pass123'},
    {'username': 'mike', 'password': 'password123'},
    {'username': 'liz', 'password': 'pass123'}
]

# Vstupy
username = input("Username: ")
password = input("Password: ")

# Kontrola registrace
if registered(username, password, registered_users):
    # Pokud je registrovaný, vybere si číslo textu
    print(f"$ Python TextAnalyzer.py\nUsername: {username}\nPassword: {password}")
    print("----------------------------------------")
    print(f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.")
    print("----------------------------------------")
    
    # Seznam textů
    TEXTS = [
        '''
        Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.
        ''',
        '''
        At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.
        ''',
        '''
        The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present.
        '''
    ]

    # Získání vstupu od uživatele s validací
    while True:
        selected_text_number_str = input("Enter a number between 1 and 3 to select: ")
        if selected_text_number_str in ["1", "2", "3"]:
            selected_text_number = int(selected_text_number_str)
            break  # Vstup je platný, ukončujeme smyčku
        else:
            print("Invalid text number. Please enter a number between 1 and 3.")

    print()
    analyze_text(TEXTS[selected_text_number - 1])  # -1 protože indexování v seznamu začíná od 0

else:
    print(f"$ Python TextAnalyzer.py\nUsername: {username}\nPassword: {password}\nUnregistered user, terminating the program..")
