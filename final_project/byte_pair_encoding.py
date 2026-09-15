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
folder = "training_data"

def byte_pair_vocab_maker():
    wordlst = []
    with open(wrdlst_filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])
    for filename in os.listdir(folder):
        if filename.endswith(".txt") and filename != "README.txt":
            file_path = os.path.join(folder, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                print(f"Processing file: {filename}")

byte_pair_vocab_maker()