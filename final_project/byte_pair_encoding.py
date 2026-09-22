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
            if not file_tokens[i].isspace() and not file_tokens[i + 1].isspace():
                # Create a tuple pair like ('a', 'b') or ('ab', 'c')
                pair = (file_tokens[i], file_tokens[i+1])
                
                if pair in word_pairs:
                    word_pairs[pair] += 1
                else:
                    word_pairs[pair] = 1
    return word_pairs

def add_most_frequent_pair_to_vocab(word_pairs):
    BASE_VOCAB_SIZE = 99
    highest_pair = max(word_pairs, key=word_pairs.get)
    if max(word_pairs.values()) < 100:
        return False  # Stop if the most frequent pair occurs less than 100 times
    wordlist.insert(BASE_VOCAB_SIZE, highest_pair)  # Insert the most frequent pair at the end
    save_wordlist_to_csv(wordlist, wrdlst_filename)
    return True  # Continue if the most frequent pair occurs 100 or more times

def merge_most_frequent_pair_in_tokens(all_files_tokens):
    for i in range(len(all_files_tokens)):
        if i == len(all_files_tokens) - 1:
            break  # Avoid index out of range error
        for j in range(len(wordlist), 0, -1):
            if all_files_tokens[i] + all_files_tokens[i+1] == wordlist[j]:
                all_files_tokens[i] = all_files_tokens[i] + all_files_tokens[i+1]
                del all_files_tokens[i+1]

def main():
    all_files_tokens = load_text_as_tokens(training_folder)

    while True:
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

        wordlist.append(merged_token)
        save_wordlist_to_csv(wordlist, wrdlst_filename)

        for file_tokens in all_files_tokens:
            index = 0

            while index < len(file_tokens) - 1:
                current_pair = (file_tokens[index], file_tokens[index + 1])

                if current_pair == most_frequent_pair:
                    file_tokens[index:index + 2] = [merged_token]
                    index += 1
                else:
                    index += 1
                    
if __name__ == "__main__":
    main()