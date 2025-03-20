import sys, os

full_dictionary_file = open("full_dictionary.txt", "r")
modified_full_dictionary_file = open("full_dictionary_modified.txt", "a")

vowel_phonemes = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2',
                  'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2',
                  'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2', 'EY0', 'EY1', 'EY2',
                  'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'OW0', 'OW1', 'OW2',
                  'OY0', 'OY1', 'OY2', 'UH0', 'UH1', 'UH2', 'UW0', 'UW1', 'UW2']

def add_tabs_after_name_of_entry():
    for line in full_dictionary_file:
        dictionary_entry = line.split(" ", 1)
        entry = dictionary_entry[0]
        pronunciation = dictionary_entry[1][1:]

        if (len(entry) < 8):
            modified_full_dictionary_file.write(entry + "\t\t\t\t" + pronunciation)
        elif (len(entry) >= 8 and len(entry) < 16):
            modified_full_dictionary_file.write(entry + "\t\t\t" + pronunciation)
        elif (len(entry) >= 16 and len(entry) < 24):
            modified_full_dictionary_file.write(entry + "\t\t" + pronunciation)
        else:
            modified_full_dictionary_file.write(entry + "\t" + pronunciation)


def sort_words_by_last_vowel_phoneme_into_files():
    AA_file = open(os.path.join("All words sorted by last vowel phoneme", "01 AA.txt"), "w")
    AE_file = open(os.path.join("All words sorted by last vowel phoneme", "02 AE.txt"), "w")
    AH_file = open(os.path.join("All words sorted by last vowel phoneme", "03 AH.txt"), "w")
    AO_file = open(os.path.join("All words sorted by last vowel phoneme", "04 AO.txt"), "w")
    AW_file = open(os.path.join("All words sorted by last vowel phoneme", "05 AW.txt"), "w")
    AY_file = open(os.path.join("All words sorted by last vowel phoneme", "06 AY.txt"), "w")
    EH_file = open(os.path.join("All words sorted by last vowel phoneme", "07 EH.txt"), "w")
    ER_file = open(os.path.join("All words sorted by last vowel phoneme", "08 ER.txt"), "w")
    EY_file = open(os.path.join("All words sorted by last vowel phoneme", "09 EY.txt"), "w")
    IH_file = open(os.path.join("All words sorted by last vowel phoneme", "10 IH.txt"), "w")
    IY_file = open(os.path.join("All words sorted by last vowel phoneme", "11 IY.txt"), "w")
    OW_file = open(os.path.join("All words sorted by last vowel phoneme", "12 OW.txt"), "w")
    OY_file = open(os.path.join("All words sorted by last vowel phoneme", "13 OY.txt"), "w")
    UH_file = open(os.path.join("All words sorted by last vowel phoneme", "14 UH.txt"), "w")
    UW_file = open(os.path.join("All words sorted by last vowel phoneme", "15 UW.txt"), "w")


    for line in full_dictionary_file:
        dictionary_entry = line.split(" ", 1)
        entry = dictionary_entry[0]
        pronunciation = dictionary_entry[1][1:]

        last_vowel = ''
        split_by_last_space = line.rpartition(' ')
        last_vowel = split_by_last_space[2].replace("\n", "")
        leftover = split_by_last_space[0]
        while (last_vowel not in vowel_phonemes):
            split_by_last_space = leftover.rpartition(' ')
            last_vowel = split_by_last_space[2]
            leftover = split_by_last_space[0]

        match last_vowel:
            case 'AA0':
                AA_file.write(line)
            case 'AA1':
                AA_file.write(line)
            case 'AA2':
                AA_file.write(line)
            case 'AE0':
                AE_file.write(line)
            case 'AE1':
                AE_file.write(line)
            case 'AE2':
                AE_file.write(line)
            case 'AH0':
                AH_file.write(line)
            case 'AH1':
                AH_file.write(line)
            case 'AH2':
                AH_file.write(line)
            case 'AO0':
                AO_file.write(line)
            case 'AO1':
                AO_file.write(line)
            case 'AO2':
                AO_file.write(line)
            case 'AW0':
                AW_file.write(line)
            case 'AW1':
                AW_file.write(line)
            case 'AW2':
                AW_file.write(line)
            case 'AY0':
                AY_file.write(line)
            case 'AY1':
                AY_file.write(line)
            case 'AY2':
                AY_file.write(line)
            case 'EH0':
                EH_file.write(line)
            case 'EH1':
                EH_file.write(line)
            case 'EH2':
                EH_file.write(line)
            case 'ER0':
                ER_file.write(line)
            case 'ER1':
                EH_file.write(line)
            case 'ER2':
                EH_file.write(line)
            case 'EY0':
                EY_file.write(line)
            case 'EY1':
                EY_file.write(line)
            case 'EY2':
                EY_file.write(line)
            case 'IH0':
                IH_file.write(line)
            case 'IH1':
                IH_file.write(line)
            case 'IH2':
                IH_file.write(line)
            case 'IY0':
                IY_file.write(line)
            case 'IY1':
                IY_file.write(line)
            case 'IY2':
                IY_file.write(line)
            case 'OW0':
                OW_file.write(line)
            case 'OW1':
                OW_file.write(line)
            case 'OW2':
                OW_file.write(line)
            case 'OY0':
                OY_file.write(line)
            case 'OY1':
                OY_file.write(line)
            case 'OY2':
                OY_file.write(line)
            case 'UH0':
                UH_file.write(line)
            case 'UH1':
                UH_file.write(line)
            case 'UH2':
                UH_file.write(line)
            case 'UW0':
                UW_file.write(line)
            case 'UW1':
                UW_file.write(line)
            case 'UW2':
                UW_file.write(line)

def get_all_phoneme_endings_to_file():

    list_of_possible_word_endings_file = open("list of possible word endings.txt", "w")
    word_endings = []

    for line in full_dictionary_file:
        dictionary_entry = line.split(" ", 1)
        entry = dictionary_entry[0]
        pronunciation = dictionary_entry[1][1:]

        # Getting the word's ending
        last_vowel_phoneme = ''
        consonant_phonemes_after_last_vowel_phoneme = []
        split_by_last_space = line.rpartition(' ')
        last_phoneme = split_by_last_space[2].replace("\n", "")
        leftover = split_by_last_space[0]
        if (last_phoneme in vowel_phonemes):
            last_vowel_phoneme = last_phoneme
        else:
            while (last_phoneme not in vowel_phonemes):
                consonant_phonemes_after_last_vowel_phoneme.insert(0, last_phoneme)
                split_by_last_space = leftover.rpartition(' ')
                last_phoneme = split_by_last_space[2]
                leftover = split_by_last_space[0]
            last_vowel_phoneme = last_phoneme
        
        last_vowel_phoneme = last_vowel_phoneme[0:2]

        # print statement for testing
        #print(entry)
        #print(last_vowel_phoneme)
        #for phoneme in consonant_phonemes_after_last_vowel_phoneme:
        #    print(phoneme + ' ')
        #print('\n')

        word_ending = last_vowel_phoneme
        if consonant_phonemes_after_last_vowel_phoneme:
            word_ending += " " + " ".join(consonant_phonemes_after_last_vowel_phoneme)

        word_endings.append(word_ending)

    word_endings = list(set(word_endings))
    word_endings.sort()

    for word_ending in word_endings:
        list_of_possible_word_endings_file.write(word_ending + '\n')


def sort_words_by_phoneme_endings_to_file():
    for line in full_dictionary_file:
        dictionary_entry = line.split(" ", 1)
        entry = dictionary_entry[0]
        pronunciation = dictionary_entry[1][1:]

        # Getting the word's ending
        last_vowel_phoneme = ''
        consonant_phonemes_after_last_vowel_phoneme = []
        split_by_last_space = line.rpartition(' ')
        last_phoneme = split_by_last_space[2].replace("\n", "")
        leftover = split_by_last_space[0]
        if (last_phoneme in vowel_phonemes):
            last_vowel_phoneme = last_phoneme
        else:
            while (last_phoneme not in vowel_phonemes):
                consonant_phonemes_after_last_vowel_phoneme.insert(0, last_phoneme)
                split_by_last_space = leftover.rpartition(' ')
                last_phoneme = split_by_last_space[2]
                leftover = split_by_last_space[0]
            last_vowel_phoneme = last_phoneme
        
        last_vowel_phoneme = last_vowel_phoneme[0:2]

        word_ending = last_vowel_phoneme
        if consonant_phonemes_after_last_vowel_phoneme:
            word_ending += " " + " ".join(consonant_phonemes_after_last_vowel_phoneme)

        with open(os.path.join("List of rhymes sorted by phoneme endings", f"{word_ending}.txt"), 'a') as file:
            file.write(line)




# add_tabs_after_name_of_entry()
# sort_words_by_last_vowel_phoneme_into_files()
# get_all_phoneme_endings_to_file()
# sort_words_by_phoneme_endings_to_file()