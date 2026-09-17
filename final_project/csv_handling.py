import csv
import os

filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")

def csv_to_list(filename):
    wordlst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            wordlst.append(row[1])
    return wordlst

def save_wordlist_to_csv(wordlist, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "word"])
        for i, item in enumerate(wordlist, start=1):
            writer.writerow([i, item])