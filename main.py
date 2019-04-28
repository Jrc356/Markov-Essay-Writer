import markovify
import os
from ArgParser import ArgParser

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
    parser = ArgParser()
    args = parser.parse_args()
    
    fileNames = getFileNames(args.data_folder)
    text = splitText(loadData(args.data_folder, fileNames))

    # Create a list of markov chains for combination
    chains = [markovify.Chain(text, state_size=args.state_size) for t in text]

    # Combine all chains
    chain = markovify.combine(chains)

    # Generate stories
    stories = []
    init_state = tuple(args.init_state.split(" ")) if args.init_state else ()
    if args.init_state and len(init_state) != args.state_size:
        print("Length of init_state must be equal to state_size. Received length {} and state size {}".format(len(init_state), args.state_size))
        exit(1)
        
    for i in range(args.num_stories):
        if init_state:
            try:
                gen = [i for i in chain.gen(init_state=init_state)]
            except KeyError:
                print("Could not generate a story with the init_state {}".format(init_state))
                exit(1)
        else:
            gen = [i for i in chain.gen()]
            
        stories.append(" ".join(gen))

    # Enjoy the masterpieces
    for story in stories:
        print(" ".join(init_state), story)
        print("---------------------------------------------------------\n")