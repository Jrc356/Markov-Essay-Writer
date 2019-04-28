# Markov-Essay-Writer
A Markov model generating essays based on scraped essays from the web

# Setup
Install the python requirements using requirements.txt
`pip install -f requirements.txt`

# Usage
This tool runs in the command line and has the following arguments:
- 'data_folder' - [REQUIRED] the folder containing the data to load into the markov model
- '--state_size' - [OPTIONAL] the state size of the markov model. In other words, how many words to break the data up into. DEFAULT 2
- '--num_stories' - [OPTIONAL] how many stories to generate with the model. DEFAULT 5
- '--init_state' -[OPTIONAL] A string to start the stories off with. DEFAULT "". The length of this string must be as long as the state size. Entering an init_state does not guarantee that a story can be generated as it is based on the input data.


*NOTE: This is not intended to actually write useable essays; it is only for fun. If you, for any reason, use this to write your essays, I am not responsible for the F you will inevitably receive :) 
