import csv
wordlst = []
with open("wordlist.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        wordlst.append(row[1])


def sentence_to_token(sentence):
    def wtn(word):
        try:
            return wordlst.index(word)
        except ValueError:
            return wordlst[0]
    sentence = sentence.lower()
    words = sentence.split()
    punctuation = ".,!?;: "

    for mark in punctuation:
        sentence = sentence.replace(mark, " " + mark + " ")

    words = sentence.split()
    return [wtn(word) for word in words]




def token_to_sentence(tokens):
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

print(sentence_to_token("Hello!, how are you?"))
print(token_to_sentence(sentence_to_token("Hello!, how are you?")))