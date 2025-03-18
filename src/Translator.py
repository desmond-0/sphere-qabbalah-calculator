import string

ones = [
    " ",
    "spiritualization",
    "purity",
    "happiness",
    "universal-love", 
    "light-fire", 
    "divine-virtue",
    "micro-macrocosm",
    "omnipresence",
    "quintessence",
]

tens = [
    " ",
    "religiosity",
    "truth",
    "mind-soul",
    "ecstasy",
    "ego-conciousness",
    "invention",
    "will-intellect-life-conciousness",
    "influence-of-divine-ideas",
    "alchemy",
]

hundreds = [
    " ",
    "equilibrium",
    "soul-body",
    "preservation",
    "love-magic",
    "abilities",
    "astral-magic",
    "four-elemental-kingdoms",
    "astral-consciousness",
    "astral-projection",
]

def custom_words(x):

    new_word = []
    for idx, x in enumerate(x):
        if idx == 0:
            new_word.insert(idx, hundreds[x])
        if idx == 1:
            new_word.insert(idx, tens[x])
        if idx == 2:
            new_word.insert(idx, ones[x])

    return new_word

def num_to_list(x):
    n = str(x)
    numbers = [int(d) for d in n]
    if len(numbers) == 4:
        print("Enter a smaller number please.")
        return None

    if len(numbers) == 2:
        numbers.insert(0,0)

    if len(numbers) == 1:
        numbers.insert(0,0)
        numbers.insert(0,0)


    return numbers

def translator(input):

    try:
        input = int(input)
        if input > 999:
            print("Enter a smaller number")
        else:
            num_list = num_to_list(input)
            return custom_words(num_list)

    except ValueError:
        print("That's not a number!")
