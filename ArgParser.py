from argparse import ArgumentParser

class ArgParser(ArgumentParser):
    def __init__(self):
        # STATE_SIZE = 2
        # NUM_STORIES = 5
        # INIT_STATE = ("I", "am")
        # DATA_FOLDER = "Data"
        super().__init__(description="Generate essays using a markov model")
        self.add_argument('data_folder', type=str, help="Folder containing the essay data files")
        self.add_argument('--state_size', dest="state_size", type=int, help="State size to use for the markov chain. DEFAULT 2", default=2)
        self.add_argument('--num_stories', dest="num_stories", type=int, help="The number of stories to generate with the model. DEFAULT 5", default=5)
        self.add_argument('--init_state', dest="init_state", type=str, help="The initial words to use to generate the stories. Must be either empty or of the same length as state_size", default="")