from collections import OrderedDict
import pickle


class history_state:
    def __init__(self, state_path=None):
        self.out_dir = None
        self.state_path = state_path

    def update_history_state(self):
        with open(self.state_path, 'rb') as handle:
            loaded_state = pickle.load(handle)

        print(loaded_state)
        sorted_keys, max_experiment = self.sort_history(loaded_state)

        cleaned_keys: OrderedDict[str, int] = OrderedDict()
        for k in sorted_keys:
            pth = self.directory + "/" + self.project_name + "/" + k
            if os.path.exists(pth):
                if os.path.exists(pth + "/snapshot.pse"):
                    cleaned_keys[k] = 1
                else:
                    cleaned_keys[k] = 0

        print(cleaned_keys)

    def sort_history(self, in_dict):
        d = list(in_dict.keys())
        d = sorted([int(x) for x in d])
        if len(d) > 0:
            max_experiment = d[-1]
        else:
            max_experiment = 0

        d = [str(x) for x in d]
        return d, max_experiment


if __name__ == "__main__":
    print("HISTORYME")
    c = history_state("C:/Users/patc/Documents/Project1111/restore.pickle")
    c.update_history_state()
