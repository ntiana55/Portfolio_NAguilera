# DSC 510
# 8.1 Programming Assignment
# Processing Files
# Nicole Aguilera
# 07/26/2020

import pprint

def add_word (word, word_count_dict):
    word_count_dict[word] = 1


def process_line (line, word_count_dict):
    line_word = line.split()
    for word in line_word:
        if word == "--":
            continue
        else:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                add_word(word, word_count_dict)


def process_file (user_filename, word_count_dict):
    with open(user_filename, 'a') as file2:
        for key, value in sorted(word_count_dict.items(), key=lambda kv: kv[1], reverse=True):
            theStr = '%-12s  %d'%(key, value)
            file2.write(theStr + '\n')
    file2.close()

def main ():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    len_dict = len(word_count_dict)
    len_header = 'Length of Dictionary: %d' % (len_dict)
    headr = '%-12s  %s' % ("Word", "Count")
    pretty_line = "-"*20
    with open(user_filename, 'w') as file2:
        file2.write( len_header + '\n' + headr + '\n' + pretty_line + '\n')
    file2.close()
    process_file(user_filename, word_count_dict)

user_filename = input("What would you like to name the file?")
main()
