#this file is for byte pair encoding.
#byte pair encoding is a way of forming 
# a llms vocabulary by iteratively replacing 
# the most frequent pair of bytes in a sequence 
# with a single byte by merging the most frequent 
# letter combinations into one. This process is 
# repeated until a desired vocabulary size is 
# reached. The resulting vocabulary can be used 
# for tokenization in natural language processing tasks.
import os
from csv_handling import csv_to_list, save_wordlist_to_csv

wrdlst_filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")
training_folder = os.path.join(os.path.dirname(__file__), "training_data")
wordlist = csv_to_list(wrdlst_filename)

def load_text_as_tokens(folder):
    corpus_tokens = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt") and filename != "README.txt":
            file_path = os.path.join(folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                # split the file into one-character tokens so we can count pair frequencies
                file_tokens = list(file.read())
                corpus_tokens.append(file_tokens)
    return corpus_tokens



def count_byte_pairs(all_files_tokens):
    word_pairs = {}

    # go through every text file and count the frequency of adjacent character pairs
    for file_tokens in all_files_tokens:
        for i in range(len(file_tokens) - 1):
            # ignore whitespace pairs so space characters do not get merged into words
            if not file_tokens[i].isspace() and not file_tokens[i + 1].isspace():
                # pair the current character with the next one, like ('a', 'b')
                pair = (file_tokens[i], file_tokens[i + 1])

                if pair in word_pairs:
                    word_pairs[pair] += 1
                else:
                    word_pairs[pair] = 1
    return word_pairs


def add_most_frequent_pair_to_vocab(word_pairs):
    BASE_VOCAB_SIZE = 99
    highest_pair = max(word_pairs, key=word_pairs.get)
    if max(word_pairs.values()) < 100:
        return False  # stop once the most common pair is not frequent enough
    # add the best pair as a new learned token in the vocabulary
    wordlist.insert(BASE_VOCAB_SIZE, highest_pair)
    save_wordlist_to_csv(wordlist, wrdlst_filename)
    return True


def merge_most_frequent_pair_in_tokens(all_files_tokens):
    for i in range(len(all_files_tokens)):
        if i == len(all_files_tokens) - 1:
            break
        for j in range(len(wordlist), 0, -1):
            if all_files_tokens[i] + all_files_tokens[i + 1] == wordlist[j]:
                # merge the matching pair into a single token in the current text stream
                all_files_tokens[i] = all_files_tokens[i] + all_files_tokens[i + 1]
                del all_files_tokens[i + 1]


def main():
    all_files_tokens = load_text_as_tokens(training_folder)

    while True:
        # count pairs again after each merge so the next best pair can be learned
        pair_counts = count_byte_pairs(all_files_tokens)

        if not pair_counts:
            break

        most_frequent_pair = max(pair_counts, key=pair_counts.get)
        frequency = pair_counts[most_frequent_pair]
        merged_token = "".join(most_frequent_pair)

        if frequency < 100:
            break

        if merged_token in wordlist:
            break

        # add this merged token to the vocabulary so it can be recognized later
        wordlist.append(merged_token)
        save_wordlist_to_csv(wordlist, wrdlst_filename)

        for file_tokens in all_files_tokens:
            index = 0

            while index < len(file_tokens) - 1:
                current_pair = (file_tokens[index], file_tokens[index + 1])

                if current_pair == most_frequent_pair:
                    # replace the pair with the merged token everywhere it appears
                    file_tokens[index:index + 2] = [merged_token]
                    index += 1
                else:
                    index += 1


if __name__ == "__main__":
    main()