student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

def generate_phonetic():
    try:
        print([[alphabet[letter] for letter in word] for word in input("Enter a word: ").upper().split()])
    except KeyError:
        print('Sorry, only letters in the alphabet and spaces please.')
        generate_phonetic()
