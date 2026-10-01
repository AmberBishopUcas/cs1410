#this file is used to store the functions that are used to train the model back propogation has 
# already been created in back_propogation.py, this file will combine those functions to create a 
# training function that will be used to train the model

#how will i do training? (idea refinment)
#for training i will first make training "pairs" by creating a list of input and output pairs. 
# i will do this by going into the concise_llm_prompt_response.txt file and then taking each prompt, 
# and pairing it with its respective output. this will be stored in a dictionary. the prompt will be 
# the key, and the response will be the value. the response will be a the list of (expected output) 
# that we will use to train the network. first the input will be tokenised and put into the inputs of 
# the network. then the networks output will be calculated. it will be calculated token by token. 
# after the first token is calculated, the error will be calculated and the weights will be adjusted.
#  then the next token will be calculated, and the error will be calculated and the weights will be 
# adjusted. this will continue until all tokens have been calculated. then the next prompt will be 
# used to train the network. this will continue until all prompts have been used to train the network.

#for the shakespear file there will be a different approach: the shakespear file is individual 
# stories of shakespear, seperated by <start> <end> rather than <prompt> <response> we will put the 
# first 500 tokens from each story as the input, an then continusly calcualte the output, with rolling
#  tokens rather than the prompt and response format. this means that there are not dedicated prompt 
# token slots when training non <prompt> <response> files (pr files from here on out). this will be 
# done for all files, and if they do not contain se tags, the s and e tag will be placed at the start
#  and end of the file automatically. this will only be used to train the relationship of words with 
# eachother, not training responses. the response training is from the 
# "concise_llm_prompt_response.txt" file. the shakespear file will be used to train the relationship 
# of words with eachother, and the "concise_llm_prompt_response.txt" file will be used to train the 
# relationship of prompts with responses.

import os
from csv_handling import csv_to_list, save_wordlist_to_csv

wrdlst_filename = os.path.join(os.path.dirname(__file__), "wordlist.csv")
training_folder = os.path.join(os.path.dirname(__file__), "training_data")
wordlist = csv_to_list(wrdlst_filename)

def classify_file_type(text):
    """Determine the type of training data based on its content."""
    if "<prompt>" in text and "<response>" in text:
        return "pr"
    elif "<start>" in text and "<end>" in text:
        return "se"
    else:
        return "se"

def get_training_data(folder):
    training_data = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt") and filename != "README.txt":
            file_train = os.path.join(folder, filename)
            if classify_file_type(open(file_train, "r", encoding="utf-8").read()) == "pr":
                pass
            #had to pause coding to pack up at end of class. if its pr seperate prompt as key and 
            #response as value in dictionary. if its se, then just put the whole text as the value, 
            #and the key can be the filename. this will be used to train the model on the relationship 
            #of words with eachother.
