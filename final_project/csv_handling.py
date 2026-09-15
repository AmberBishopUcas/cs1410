import csv
import os

filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")

def sentence_to_chunk(sentence):
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])
    sentence = list(sentence)
    
        
    

def chunk_to_token(chunk):
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])
        



def sentence_to_token(sentence):
    pass




def token_to_sentence(tokens):
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])

    sentence = ""

    punctuation = ".,!?;:"

    for num in tokens:
        word = wordlst[num]

        if word in punctuation:
            sentence += word
        else:
            if sentence != "":
                sentence += " "
            sentence += word

    return sentence



print(sentence_to_chunk("hello world!"))

