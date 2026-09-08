import csv
import os

filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")


def sentence_to_token(sentence):
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])

    def wtn(word):
        try:
            return wordlst.index(word)
        except ValueError:
            return 0
    sentence = sentence.lower()
    words = sentence.split()
    punctuation = ".,!?;: "

    for mark in punctuation:
        sentence = sentence.replace(mark, " " + mark + " ")

    words = sentence.split()
    return [wtn(word) for word in words]




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