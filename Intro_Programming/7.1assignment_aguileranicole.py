# DSC 510
# 7.1 Programming Assignment
# Reading the "Gettysburg Address" with Dictionaries
# Nicole Aguilera
# 07/19/2020

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


def pretty_print (word_count_dict):
    for key, value in sorted(word_count_dict.items(), key=lambda kv: kv[1], reverse=True):
        print('{0:12}  {1}'.format(key, value))


def main ():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    len_dict = len(word_count_dict)
    print("Length of Dictionary:", len_dict)
    print('{0:12}  {1}'.format("Word", "Count"))
    print("-"*20)
    pretty_print(word_count_dict)

main()
