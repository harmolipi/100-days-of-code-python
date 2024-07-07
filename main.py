# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.readlines()

print(starting_letter)

for name in names:
    print(name)
    clean_name = str.strip(name)
    new_letter = starting_letter.copy()
    new_letter[0] = str.replace(starting_letter[0], "[name]", clean_name)
    print(new_letter[0])

    with open(f"Output/ReadyToSend/letter_for_{clean_name}", "w") as file:
        file.write("".join(new_letter))
