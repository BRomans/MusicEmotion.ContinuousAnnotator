import json
import time


class ExperimentTracker:

    def __init__(self):
        self.trial_data = {}

    def add_entry(self, key, entry):
        self.trial_data[key] = {}
        self.trial_data[key]['val'] = entry
        self.trial_data[key]['timestamp'] = time.time()  #in seconds

    def add_entry_trial(self, trial_name, key, entry):
        self.trial_data[trial_name] = {}
        self.trial_data[trial_name][key] = {}
        self.trial_data[trial_name][key]['val'] = entry
        self.trial_data[trial_name][key]['timestamp'] = time.time()

    def write_trial(self, trial_name, folder=''):
        with open(folder + trial_name + '.json', 'w+') as f:
            json.dump(self.trial_data, f, indent=4)
