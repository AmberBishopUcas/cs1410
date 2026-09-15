#this file is for byte pair encoding.
#byte pair encoding is a way of forming 
# a llms vocabulary by iteratively replacing 
# the most frequent pair of bytes in a sequence 
# with a single byte by merging the most frequent 
# letter combinations into one. This process is 
# repeated until a desired vocabulary size is 
# reached. The resulting vocabulary can be used 
# for tokenization in natural language processing tasks.
import csv
import os

wrdlst_filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")
folder = os.path.join(os.path.dirname(__file__), "training_data")

def load_text_as_tokens(folder):
    corpus_tokens = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt") and filename != "README.txt":
            file_path = os.path.join(folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                # Convert "hello" into ['h', 'e', 'l', 'l', 'o']
                file_tokens = list(file.read())
                corpus_tokens.append(file_tokens)
    return corpus_tokens



def count_byte_pairs(all_files_tokens):
    word_pairs = {}

    # Iterate through each file's token list
    for file_tokens in all_files_tokens:
        # Loop stops 1 item short so i+1 always exists
        for i in range(len(file_tokens) - 1):
            
            # Skip spaces so we don't pair words together
            if file_tokens[i] != " " and file_tokens[i+1] != " ":
                # Create a tuple pair like ('a', 'b') or ('ab', 'c')
                pair = (file_tokens[i], file_tokens[i+1])
                
                if pair in word_pairs:
                    word_pairs[pair] += 1
                else:
                    word_pairs[pair] = 1
    return word_pairs