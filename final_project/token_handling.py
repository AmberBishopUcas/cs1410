import os
from csv_handling import csv_to_list
from matrix_handling import create_matrix, randomise_matrix, save_matrix, load_matrix, hadamard_product

wrdlst_filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")
wordlist_matrix = os.path.join(os.path.dirname(__file__), "wordlist_matrix.txt")

def sentence_to_chunks(sentence):
    wordlist = csv_to_list(wrdlst_filename)
    tokens = [char for char in sentence if char != "\n"]
    while True:
        merged = False
        i = 0
        for i in range(len(tokens) - 1):
            if tokens[i] + tokens[i + 1] in wordlist:
                tokens[i] = tokens[i] + tokens[i + 1]
                del tokens[i + 1]
                merged = True
                break
        if not merged:
            break
    return tokens

def chunk_to_tokens(chunk):
    wordlist = csv_to_list(wrdlst_filename)
    tokens = []
    for token in chunk:
        if token.isspace():
            token = "<SPACE>"
        if token in wordlist:
            tokens.append(wordlist.index(token) + 1)
    return tokens

def tokens_to_matrix(tokens):
    matrix = load_matrix(wordlist_matrix)
    matrix_tokens = []
    for token in tokens:
        matrix_tokens.append(matrix[token - 1])
    return matrix_tokens

def token_to_chunk(tokens):
    wordlist = csv_to_list(wrdlst_filename)
    chunks = []
    for token in tokens:
        token = wordlist[token - 1]
        if token == "<SPACE>":
                    token = " "
        chunks.append(token)
    return chunks

def chunk_to_sentence(chunks):
    return "".join(chunks)

#def chunk_to_sentence
input_text = input(str("input your text for tokenisation: "))
print(sentence_to_chunks(input_text))
print(chunk_to_tokens(sentence_to_chunks(input_text)))
print(token_to_chunk(chunk_to_tokens(sentence_to_chunks(input_text))))
print(chunk_to_sentence(token_to_chunk(chunk_to_tokens(sentence_to_chunks(input_text)))))