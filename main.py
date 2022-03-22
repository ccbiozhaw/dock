'''
PyMOL Plugin

'''
import os
import sys

sys.path.insert(1, os.path.dirname(__file__))

from alphadock.alphadock_main_wndw import dock_gui
from PyQt5.QtWidgets import QApplication



def __init_plugin__(app=None):
    '''
    Add an entry to the PyMOL "Plugin" menu
    '''
    from pymol.plugins import addmenuitemqt

    addmenuitemqt('AlphaDock', run_plugin_gui)


dialog = None


def run_plugin_gui():
    '''
    Open our custom dialog
    '''
    global dialog

    if dialog is None:
        dialog = dock_gui()

    dialog.show()


if __name__ == "__main__":
    print("MAIN")
    app = QApplication(sys.argv)

    wnd = dock_gui()
    wnd.show()

    sys.exit(app.exec_())
