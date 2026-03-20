import os
import re

STOP_WORDS = {"the", "is", "at", "which", "on", "and", "a", "an", "to", "in", "of"}

def manual_clean(text):
# removing punctuations and turning it into lowercase
    chars_to_remove = '.,!?;:"()'
    for char in chars_to_remove:
        text = text.replace(char, "")
    return text.lower().split()


#splitting into sentences
def split_into_sentences(text):
    text = text.replace('?','.').replace('!','.')
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    return sentences

inverted_index = {}

def add_to_index(word,filename,line_num,offset):

    if word in STOP_WORDS:
         return
    #checking if word exists
    if word not in inverted_index:
            inverted_index[word] = {}

    #checking if the filename exists
    if filename not in inverted_index[word]:
        inverted_index[word][filename] = {
            "count" : 0,
            "lines" : [],
            "offsets" : []
        }
    
    inverted_index[word][filename]["count"] += 1
    inverted_index[word][filename]["lines"].append(line_num)
    inverted_index[word][filename]["offsets"].append(offset)



                        



