import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphabet_csv = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_csv.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
print(input_word)
mapped_list = [nato_alphabet[letter] for letter in input_word]
print(mapped_list)
