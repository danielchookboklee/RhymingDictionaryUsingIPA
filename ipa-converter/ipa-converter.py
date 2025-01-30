wordlist_filename = '60000-word-frequency-list-English-list.txt'
write_to_filename = wordlist_filename[:-4] + '--converted-to-ipa.txt'
ipa_dictionary_filename = 'en_US.txt'

wordlist_file = open(wordlist_filename, encoding='utf-8', mode='r', errors='ignore')
lines = wordlist_file.readlines()
ipa_dict = open(ipa_dictionary_filename, encoding='utf-8', mode='r')
ipa_dict_entries = ipa_dict.readlines()

end_file = open(write_to_filename, encoding='utf-8', mode='w')

for line in lines:
    n = 0
    # finding the word in the ipa dictionary file
    while line[0].lower() != ipa_dict_entries[n][0]: n += 1             # some slight speed optimization
    item = line.split()[0]
    while item > ipa_dict_entries[n].split()[0]: n += 1      # finding the match between the entry in the wordlist and the ipa dictionary file
    if item != ipa_dict_entries[n].split()[0]:               # if the word is not in the ipa dictionary:
        end_file.write(item)
        end_file.write('\t\t\t')
        end_file.write('\n')
    else:
        end_file.write(item)
        end_file.write('\t' * (3 - (len(item) // 8)))
        end_file.write(ipa_dict_entries[n].split()[1].split("/")[1])
        end_file.write('\t')
        i = 1
        while ipa_dict_entries[n].split()[i][-1] == ',':
            end_file.write(ipa_dict_entries[n].split()[i+1].split("/")[1])
            end_file.write('\t')
            i += 1
        end_file.write('\n')

wordlist_file.close()
ipa_dict.close()
end_file.close()
