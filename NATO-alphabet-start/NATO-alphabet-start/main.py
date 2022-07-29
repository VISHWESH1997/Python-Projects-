# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_frame.iterrows()}
# print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# list_word = list(user_word)
# print(list_word)
# list_nato = [row.code for (index, row) in nato_frame.iterrows() if row.letter in list_word]

# one way to do this is below
# is_true = True
# # list_nato = []
# while is_true:
#     try:
#         user_word = input("Enter a word: ").upper()
#         list_nato = [nato_dict[item] for item in user_word]
#         is_true = False
#     except KeyError:
#         print("Sorry, Only Letters in alphabet.")
#     else:
#         print(list_nato)

# second way to do this is below


def generate_phonetic():
    try:
        user_word = input("Enter a word: ").upper()
        list_nato = [nato_dict[item] for item in user_word]
    except KeyError:
        print("Sorry, Only Letters in alphabet.")
        generate_phonetic()
    else:
        print(list_nato)


generate_phonetic()
