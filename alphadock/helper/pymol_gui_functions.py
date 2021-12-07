from __future__ import absolute_import
from __future__ import print_function


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
        dialog = gui()

    dialog.show()
