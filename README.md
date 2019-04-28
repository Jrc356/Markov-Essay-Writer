# Markov-Essay-Writer
A Markov model generating essays based on scraped essays from the web

## Setup
Install the python requirements using requirements.txt  
`pip install -f requirements.txt`

## Usage
This tool runs in the command line and has the following arguments:
- 'data_folder' - [REQUIRED] the folder containing the data to load into the markov model
- '--state_size' - [OPTIONAL] the state size of the markov model. In other words, how many words to break the data up into. DEFAULT 2
- '--num_stories' - [OPTIONAL] how many stories to generate with the model. DEFAULT 5
- '--init_state' -[OPTIONAL] A string to start the stories off with. DEFAULT "". The length of this string must be as long as the state size. Entering an init_state does not guarantee that a story can be generated as it is based on the input data.

## Example Usage
`python main.py --state_size 1 --num_stories 1 --init_state "I"`  
Result:  
```
I have to become a contribution to overcome the time I am blessed that my two mosaic footprints. I recognized this. The memory of basic necessities in order in the same straw-thatched, mud-brick homes that I really am, yet were not able to write about.

So, I spend more than work a solution to students. I will be a process of Malawi for a barely livable temperature, a husband and our hands equally well. When I am not for strawberry plants experience the right fit for example, I start.

The world with the inevitable questions as one they won’t have to find a close the sandy floor of environmental engineering. I’ve always doing yardwork to protecting our home.

I also engaging in spring 2003 when she answered, “A hate symbol of leverage to help students have already see them.

I spent two Venus flytrap. Consequently, the achievement in a fire within people have set of a family of success. For me, ambidexterity as a construction site of Lodi High School, asked him a problem until this is effortless to speak that I received a tray inside of drip into a try. I ever read just as I read their voice on a system worked. Therefore, the 21st century.
---------------------------------------------------------
```

## Adding Data
If you add an essay to the Data folder you can use the rename.sh file to rename the files in there so that it looks nicer on the eyes. Do this by:  
`./rename Data`

#NOTE  
This is not intended to actually write useable essays; it is only for fun. If you, for any reason, use this to write your essays, I am not responsible for the F you will inevitably receive :) 
