from PyQt5.QtWidgets import QAction, QMenu
from functools import partial


class QAMenuHosts(QMenu):

    def __init__(self, hosts, parent):
        super().__init__("hosts", parent)

        self.hosts = hosts
        self.parent = parent

        for t, (k, v) in enumerate(self.hosts.items()):
            action = QAction(v["alias"], self, triggered=partial(
                self.change_host_and_update_ticks, k, v, t))
            action.setCheckable(True)
            self.addAction(action)
            if t == 0:
                self.change_host_and_update_ticks(k, v, t)

    def change_host_and_update_ticks(self, new_host, configs, idx):
        self.parent.change_host(new_host, configs)
        for act in self.actions():
            act.setChecked(False)
        self.actions()[idx].setChecked(True)
