import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction

from alphadock.components import *
from alphadock.styles import *


class UIFunctions(QtWidgets.QMainWindow):

    def update_style_(self):
        script_dir = os.path.dirname(os.path.dirname(__file__))
        script_dir = script_dir.replace("\\", "/")
        self.comboBox_1.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))
        self.comboBox_2.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))
        self.comboBox_3.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))
        self.comboBox_4.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))
        self.comboBox_5.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))
        self.comboBox_7.setStyleSheet(
            fix_combo_style.replace("potatofix", script_dir))

    def inputs_(self, help_path):
        import functools
        import webbrowser

        # disable drops
        self.form.lineEdit.setAcceptDrops(False)
        self.form.lineEdit_1.setAcceptDrops(False)
        self.form.lineEdit_2.setAcceptDrops(False)
        self.form.lineEdit_3.setAcceptDrops(False)
        self.form.lineEdit_4.setAcceptDrops(False)
        self.form.lineEdit_5.setAcceptDrops(False)
        self.form.lineEdit_6.setAcceptDrops(False)
        self.form.lineEdit_7.setAcceptDrops(False)
        self.form.lineEdit_8.setAcceptDrops(False)
        self.form.lineEdit_10.setAcceptDrops(False)

        # help -wiki
        self.form.open_wiki_button.clicked.connect(
            lambda: webbrowser.open(help_path))

        # receptor_side
        self.form.comboBox_1.highlighted.connect(self.update_combo)
        self.form.comboBox_1.activated.connect(self.update_combo)
        self.form.comboBox_1.addItems(self.selections)

        self.form.comboBox_2.highlighted.connect(self.update_combo)
        self.form.comboBox_2.activated.connect(self.update_combo)
        self.form.comboBox_2.addItems(self.selections)

        self.form.pushButton_1.clicked.connect(self.process_receptor)
        self.form.pushButton_2.clicked.connect(
            functools.partial(self.help_receptor, "receptor_help.ui"))

        self.form.pushButton_3.clicked.connect(self.flexible_receptor)
        self.form.pushButton_4.clicked.connect(
            functools.partial(self.help_receptor, "flexreceptor_help.ui"))

        self.form.lineEdit_1.setText("-A hydrogens -v -U nphs_lps_waters")
        self.form.lineEdit_2.setText("-v")

        # ligand_side
        self.form.comboBox_3.highlighted.connect(self.update_combo)
        self.form.comboBox_3.activated.connect(self.update_combo)
        self.form.comboBox_3.addItems(self.selections)

        self.form.pushButton_5.clicked.connect(self.process_ligand)
        self.form.lineEdit_3.setText("--add_hydrogen --pH 7.4")
        self.form.lineEdit_3.textChanged.connect(self.hydrated_force_field)

        self.form.pushButton_6.clicked.connect(
            functools.partial(self.help_receptor, "ligand_help.ui"))

        # cofactor side
        self.form.comboBox_7.highlighted.connect(self.update_combo)
        self.form.comboBox_7.activated.connect(self.update_combo)
        self.form.comboBox_7.addItems(self.selections)

        self.form.pushButton_12.clicked.connect(
            functools.partial(self.process_ligand, 1))
        self.form.lineEdit_10.setText("--add_hydrogen --pH 7.4")
        self.form.pushButton_13.clicked.connect(
            functools.partial(self.help_receptor, "ligand_help.ui"))

        # BOX
        self.form.comboBox_4.highlighted.connect(self.update_combo)
        self.form.comboBox_4.activated.connect(self.update_combo)
        self.form.comboBox_4.addItems(self.selections)

        self.form.comboBox_4.activated.connect(functools.partial(self.box_me))

        self.form.lineEdit_4.setText("10")
        self.x = 10.
        self.form.lineEdit_5.setText("10")
        self.y = 10.
        self.form.lineEdit_6.setText("10")
        self.z = 10.

        self.form.lineEdit_4.textChanged.connect(self.update_box)
        self.form.lineEdit_5.textChanged.connect(self.update_box)
        self.form.lineEdit_6.textChanged.connect(self.update_box)

        # Force Fields
        self.form.comboBox_5.addItems(["vina", "ad4"])
        self.form.pushButton_8.clicked.connect(
            functools.partial(self.help_receptor, "ad4_or_vina.ui"))

        # Docking
        self.form.pushButton_10.clicked.connect(
            functools.partial(self.help_receptor, "docking_help.ui"))
        self.form.lineEdit_8.setText(f"--seed 42 --exhaustiveness 8")

        self.form.pushButton.clicked.connect(self.docking)

        # outputs
        self.form.pushButton_7.clicked.connect(self.get_out_dir_)

        # settings
        self.form.actionclean_up.triggered.connect(self.clean_up)
        self.form.actionnew.triggered.connect(self.new_)
        self.form.actionsave.triggered.connect(
            functools.partial(self.save_snap_))
        self.form.actionload.triggered.connect(self.load_)
        self.form.actionplayground.triggered.connect(self.update_debug_)

    def definitions_(self):
        self.form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.form.pushButton_close.clicked.connect(lambda: self.close())
        self.form.pushButton_minimze.clicked.connect(
            lambda: self.showMinimized())
        # weird way to block. idc ill take it
        self.form.frame_5.mouseMoveEvent = self.mousePressEvent2

        self.comboboxes_all_ = [self.form.comboBox_1, self.form.comboBox_2, self.form.comboBox_3,
                                self.form.comboBox_4, self.form.comboBox_7]

        self.comboboxes_FF_ = [self.form.comboBox_5]

        self.line_edits_all_ = [self.form.lineEdit, self.form.lineEdit_1, self.form.lineEdit_2,
                                self.form.lineEdit_3, self.form.lineEdit_4, self.form.lineEdit_5,
                                self.form.lineEdit_6, self.form.lineEdit_7, self.form.lineEdit_8,
                                self.form.lineEdit_10]

    def update_menus_(self, hosts):
        script_dir = os.path.dirname(os.path.dirname(__file__))
        script_dir = script_dir.replace("\\", "/")

        self.actionnew = QAction("new", self)
        self.actionload = QAction("load", self)
        self.actionsave = QAction("save", self)

        self.actionclean_up = QAction("clean_up", self)

        self.actionplayground = QAction("history", self)
        self.actionplayground.setCheckable(True)
        self.actionplayground.setChecked(True)

        self.actionall = QAction("all", self)
        self.actionall.setCheckable(True)
        self.actionall.setChecked(True)

        self.actionscores = QAction("scores", self)
        self.actionscores.setCheckable(True)
        self.actionscores.setChecked(False)

        file_menu = QtWidgets.QMenu(self)
        file_menu.setStyleSheet(menu_style.replace("potatofix", script_dir))
        self.pushButton_file.setMenu(file_menu)

        file_menu.addAction(self.actionnew)
        file_menu.addAction(self.actionload)
        file_menu.addAction(self.actionsave)

        settings_menu = QtWidgets.QMenu(self)
        settings_menu.setStyleSheet(
            menu_style.replace("potatofix", script_dir))
        self.pushButton_settings.setMenu(settings_menu)

        settings_menu.addAction(self.actionclean_up)
        settings_menu.addAction(self.actionplayground)

        settings_menu.setStyleSheet(
            menu_style.replace("potatofix", script_dir))

        sub_menu = QAMenuHosts(hosts, self)

        settings_menu.addMenu(sub_menu)
        sub_menu.setStyleSheet(menu_style.replace("potatofix", script_dir))

        sub_menu = QtWidgets.QMenu("verbosity", self)
        settings_menu.addMenu(sub_menu)
        sub_menu.setStyleSheet(menu_style.replace("potatofix", script_dir))
        sub_menu.addAction(self.actionall)
        sub_menu.addAction(self.actionscores)
        sub_menu.triggered.connect(self.set_verbosity)

        self.menuhistory = QAMenu(self)
        self.menuhistory.setStyleSheet(
            menu_style.replace("potatofix", script_dir))
        self.pushButton_history.setMenu(self.menuhistory)
