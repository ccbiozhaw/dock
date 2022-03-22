from collections import OrderedDict
import pickle
import os
from pathlib import Path

DEBUG = True


class history_state:
    def __init__(self):
        self.state_path = None
        self.experiment_nr = 1
        self.directory = Path(os.getcwd())
        self.project_name = 'Project'

    def check_outdir(self, parent):

        self.project_name = parent.form.lineEdit.text().strip()

        os.makedirs(self.project_path, exist_ok=True)
        self.state_path = self.project_path / "restore.pickle"
        self.update_history(parent)

        if parent.debug:
            self.outdir = self.project_path / "tempfiles"
            os.makedirs(self.outdir, exist_ok=True)
        else:
            self.outdir = self.project_path / str(self.experiment_nr)
            os.makedirs(self.outdir, exist_ok=True)

        print(self.outdir)

    def update_history_state(self):

        if os.path.exists(self.state_path):
            with open(self.state_path, 'rb') as handle:
                self.loaded_restore = pickle.load(handle)
        else:
            self.loaded_restore = {}

        sorted_keys, max_experiment = self.sort_history(self.loaded_restore)
        self.experiment_nr = max_experiment
        return self.get_cleaned_keys(sorted_keys)

    def update_history(self, parent):

        cleaned_keys = self.update_history_state()

        parent.form.lcdNumber.display(self.experiment_nr)
        parent.form.menuhistory.update_actions_(cleaned_keys)

        if len(cleaned_keys) >= 1:
            parent.form.menuhistory.update_history_entries()
        else:
            parent.form.menuhistory.clear()



    def get_cleaned_keys(self, sorted_keys):
        cleaned_keys: OrderedDict[str, int] = OrderedDict()
        for k in sorted_keys:
            pth = self.directory / self.project_name / k
            if os.path.exists(pth):
                if os.path.exists(pth / "snapshot.pse"):
                    cleaned_keys[k] = 1
                else:
                    cleaned_keys[k] = 0
        return cleaned_keys

    def sort_history(self, in_dict):
        d = list(in_dict.keys())
        d = sorted([int(x) for x in d if x not in ["temp"]])
        if len(d) > 0:
            max_experiment = d[-1] + 1
        else:
            max_experiment = 1

        d = [str(x) for x in d]
        return d, max_experiment

    @property
    def project_path(self):
        newpath = self.directory / self.project_name
        return newpath


class tempParent:
    debug = False


if __name__ == "__main__":
    print("HISTORYME")
    c = history_state()
    c.check_outdir(tempParent)
