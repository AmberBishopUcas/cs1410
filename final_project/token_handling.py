# Token and chunk utilities for the language model pipeline.
# These functions convert between text, vocabulary tokens, and embedded matrix values.
import os
from csv_handling import csv_to_list
from matrix_handling import create_matrix, randomise_matrix, save_matrix, load_matrix, hadamard_product

wrdlst_filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")
wordlist_matrix = os.path.join(os.path.dirname(__file__), "wordlist_matrix.txt")


def sentence_to_chunks(sentence):
    """Merge common adjacent characters into larger vocabulary chunks when possible."""
    wordlist = csv_to_list(wrdlst_filename)
    tokens = [char for char in sentence if char != "\n"]
    while True:
        merged = False
        for i in range(len(tokens) - 1):
            # if two adjacent chunks form a known token, merge them into one larger chunk
            if tokens[i] + tokens[i + 1] in wordlist:
                tokens[i] = tokens[i] + tokens[i + 1]
                del tokens[i + 1]
                merged = True
                break
        if not merged:
            break
    return tokens


def chunk_to_tokens(chunk):
    """Translate a chunk or character sequence into numeric token IDs from the vocabulary."""
    wordlist = csv_to_list(wrdlst_filename)
    tokens = []
    for token in chunk:
        if token.isspace():
            token = "<SPACE>"
        # map each known token to its ID, otherwise fall back to the unknown token
        if token in wordlist:
            tokens.append(wordlist.index(token) + 1)
        else:
            tokens.append(wordlist.index("<UNK>") + 1)
    return tokens


def tokens_to_matrix(tokens):
    """Map a sequence of token IDs into their corresponding embedding rows."""
    matrix = load_matrix(wordlist_matrix)
    matrix_tokens = []
    for token in tokens:
        # each token ID points to one row in the embedding matrix
        matrix_tokens.append(matrix[token - 1])
    return matrix_tokens


def token_to_chunk(tokens):
    """Convert numeric token IDs back into readable text fragments for decoding."""
    wordlist = csv_to_list(wrdlst_filename)
    chunks = []
    for token in tokens:
        token = wordlist[token - 1]
        if token == "<SPACE>":
            token = " "
        chunks.append(token)
    return chunks


def chunk_to_sentence(chunks):
    """Join chunk strings back into a single sentence string."""
    return "".join(chunks)
