#!/usr/bin/python3

import markovify
import os

def getFileNames(folder):
    *_, walk = os.walk(folder)
    files = walk[2]
    return files

def loadData(folder, files):
    text = []
    for file in files:
        with open(folder + "/" + file, "r", encoding='cp1252') as f:
            text.append(f.readlines())
    return text

def splitText(text):
    split_text = []
    for t in text:
        split_text.append("".join(t).split(" "))
    return split_text


if __name__ == "__main__":
    STATE_SIZE = 2
    NUM_STORIES = 5
    INIT_STATE = ("I", "am")
    
    DATA_FOLDER = "Data"
    
    fileNames = getFileNames(DATA_FOLDER)
    text = splitText(loadData(DATA_FOLDER, fileNames))

    # Create a list of markov chains for combination
    chains = [markovify.Chain(text, state_size=STATE_SIZE) for t in text]

    # Combine all chains
    chain = markovify.combine(chains)

    # Generate stories
    stories = []
    for i in range(NUM_STORIES):
        if INIT_STATE:
            gen = [i for i in chain.gen(init_state=INIT_STATE)]
        else:
            gen = [i for i in chain.gen()]
            
        stories.append(" ".join(gen))

    # Enjoy the masterpieces
    for story in stories:
        print(" ".join(INIT_STATE), story)
        print("---------------------------------------------------------\n")