# CSV helper functions for the language model project.
# These utilities handle reading and writing the vocabulary file that stores token IDs
# and their matching word strings.
import csv
import os

# The project stores its vocabulary in a CSV file beside this module.
filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")


def csv_to_list(filename):
    """Read the vocabulary CSV and return a list of word tokens in order."""
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row: id,word
        for row in reader:
            wordlst.append(row[1])
    return wordlst


def save_wordlist_to_csv(wordlist, filename):
    """Write the vocabulary back to CSV using the same id/word format."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "word"])
        for i, item in enumerate(wordlist, start=1):
            writer.writerow([i, item])