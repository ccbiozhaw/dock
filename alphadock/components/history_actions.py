from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from alphadock.styles import *
from alphadock.helper import *

DEBUG = False


class QAMenu(QMenu):

    def __init__(self, parent=None, actions={}):
        super().__init__(parent)
        self.parent = parent
        self.actions = [str(x) for x in actions.keys()]
        self.snapshots_dict = actions
        self.setContentsMargins(0, 0, 0, 0)

        self.maximum_menu_width = 100
        self.expanded_menu_width = 230

        self.setMaximumWidth(self.maximum_menu_width)
        self.setAcceptDrops(True)
        self.parent.centralwidget.setAcceptDrops(True)

    def update_actions_(self, actions={}):
        self.actions = [str(x) for x in actions.keys()]
        self.snapshots_dict = actions

    def restore_up_(self, his, snap):
        self.parent.restore_(his, snap)

    def log_file_editor_(self, edit_id, edit_desc):
        import re
        try:
            self.log_file_ = self.parent.state.project_path / "experiment_log.txt"
            log_file = open(self.log_file_, "r").read()
            str_id = f"experimentNr: {edit_id}[^\d]"
            str_id = re.findall(str_id, log_file)

            if len(str_id) > 1:
                print("multiple entries found: ")
                for s in str_id:
                    print(s)
                print("aborting")
                return
            else:
                str_id = str_id[0]

            begin = log_file.index(str_id)
            end = begin + log_file[begin:].index("\n")
            new_file_ = log_file[:begin] + \
                str_id.strip() + " " + edit_desc + log_file[end:]

            with open(self.log_file_, "w") as log_file:
                log_file.write(new_file_)

        except:
            dumpException()

    def log_file_labels(self):
        from collections import defaultdict
        import re

        self.log_file_ = self.parent.state.project_path / "experiment_log.txt"
        log_file_ = open(self.log_file_, "r").readlines()

        self.exp_desc_dict = defaultdict(lambda: "no description found")

        for f in log_file_:
            str_id = "experimentNr: "
            exp_begin = f.index(str_id) + len(str_id)
            exp_num = re.findall("\d+", f[exp_begin:])[0]
            exp_desc = exp_begin + len(exp_num)
            self.exp_desc_dict[exp_num] = f[exp_desc:].split("\n")[0].strip()

    def update_history_entries(self):
        self.clear()
        if self.width() > self.maximum_menu_width:
            self.adjust_menu_size_()
        else:
            self.setMaximumWidth(self.maximum_menu_width)

        if DEBUG:
            print(self.actions)
        if DEBUG:
            print(self.log_file_labels())

        self.log_file_labels()
        for act in self.actions:
            desc = self.exp_desc_dict[act]
            self.addAction(QDWidgetAction(self, act, desc))

    def remove_history_directory_(self, his):
        del_dir_ = self.parent.state.project_path / str(his)
        if not DEBUG:
            import shutil
            if DEBUG:
                print(del_dir_ + ":  debug_remove_his_folder")
            shutil.rmtree(del_dir_, ignore_errors=True)
        print(f"folder {del_dir_} - removed")

    def move_history_directory_(self, src, dst):
        import shutil
        src_dir_ = self.parent.state.project_path / + \
            str(src) / "snapshot.pse"
        dst_dir_ = self.parent.state.project_path / \
            str(dst) / "snapshot.pse"

        if DEBUG:
            print(f"{src_dir_}, scr_dir")
        if DEBUG:
            print(f"{dst_dir_}, dst_dir_")
        shutil.move(src_dir_, dst_dir_)

    def remove_history_snapshot(self, src):
        import os
        src_dir_ = self.parent.state.project_path / \
            str(src) / "snapshot.pse"
        if DEBUG:
            print(f"{src_dir_}, deleting snapshot")
        if not DEBUG:
            os.remove(src_dir_)
        self.snapshots_dict[src] = 0

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            p = QPoint(event.pos().x(), event.pos().y())
            menu_event = self.actionAt(p)
            if hasattr(menu_event, "change_right_frame_"):
                menu_event.change_right_frame_()
            return

        if event.button() == Qt.MiddleButton:
            p = QPoint(event.pos().x(), event.pos().y())
            menu_event = self.actionAt(p)
            if hasattr(menu_event, "change_middle_frame_"):
                self.adjust_menu_size_()
            return

        if event.button() == Qt.LeftButton:
            p = QPoint(event.pos().x(), event.pos().y())
            menu_event = self.actionAt(p)
            if hasattr(menu_event, "middle_line_edit") and not menu_event.middle_line_edit.isEnabled():
                menu_event.middle_line_edit.setDisabled(False)

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            for act in self.children():
                if hasattr(act, "change_middle_frame_"):
                    act.left_btn_.clearFocus()
                    act.right_btn_.clearFocus()

        super().mouseReleaseEvent(event)

    def adjust_menu_size_(self):
        current_parent_width = self.width()
        try:
            if self.width() == self.maximum_menu_width:
                self.setMinimumWidth(self.expanded_menu_width)
                self.setMaximumWidth(self.expanded_menu_width)

                for act in self.children():
                    if hasattr(act, "change_middle_frame_"):
                        act.left_frame.setMaximumWidth(
                            act.right_frame_maximum_width)
                        act.left_frame.setMinimumWidth(
                            act.right_frame_maximum_width)
                        act.middle_frame.setMinimumWidth(self.expanded_menu_width -
                                                         act.right_frame_maximum_width -
                                                         act.right_frame.width())

            else:
                for act in self.children():
                    if hasattr(act, "change_middle_frame_"):
                        act.left_frame.setMaximumWidth(self.maximum_menu_width)
                        act.left_frame.setMinimumWidth(self.maximum_menu_width -
                                                       act.right_frame.width())
                        act.middle_frame.setMaximumWidth(0)
                        act.middle_frame.setMinimumWidth(0)

                self.setMinimumWidth(self.maximum_menu_width)
                self.setMaximumWidth(self.maximum_menu_width)

        except:
            dumpException()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            return
        elif event.key() == 16777249:
            self.highlight_snapshots_()
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == 16777249:
            self.highlight_snapshots_(False)
        else:
            super().keyReleaseEvent(event)

    def highlight_snapshots_(self, highlighting=True):
        for act in self.children():
            if hasattr(act, "change_middle_frame_"):
                try:
                    is_snapshot_ = self.snapshots_dict[act.left_btn_.lbl]
                    if is_snapshot_ and highlighting:
                        act.left_btn_.setStyleSheet(QPush_action_style_snapped)
                        act.right_btn_.setStyleSheet(
                            QPush_action_style_snapped)
                        act.is_highlighted = True
                    else:
                        act.left_btn_.setStyleSheet(QPush_action_style)
                        act.right_btn_.setStyleSheet(QPush_action_style)
                        act.is_highlighted = False
                except:
                    dumpException()

    def dragEnterEvent(self, e):
        origin_ = e.mimeData().text()
        is_snapshot = self.snapshots_dict[origin_]
        if is_snapshot:
            e.accept()
        else:
            return

    def dropEvent(self, e):
        position = e.pos()
        origin_ = e.mimeData().text()

        e.setDropAction(Qt.MoveAction)
        e.accept()

        p = QPoint(e.pos().x(), e.pos().y())
        menu_event = self.actionAt(p)
        drop_location_ = menu_event.lbl
        try:
            if DEBUG:
                print(f"from: {origin_} to: {drop_location_}")
            if not self.snapshots_dict[origin_]:
                return
            if origin_ == drop_location_:
                return
            else:
                if self.snapshots_dict[drop_location_] == 1:
                    reply = QMessageBox.question(self.parent, 'overwrite',
                                                 f'replace snapshot item: {drop_location_} with: {origin_}?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                    overwrite = True if reply == QMessageBox.Yes else False
                    if not overwrite:
                        self.highlight_snapshots_(False)
                        return

                self.snapshots_dict[origin_] = 0
                self.snapshots_dict[drop_location_] = 1

            self.highlight_snapshots_(False)
            self.highlight_snapshots_(True)

            self.move_history_directory_(origin_, drop_location_)
            if DEBUG:
                print(self.snapshots_dict)

        except:
            dumpException()


class QAPushButton(QPushButton):
    def __init__(self, lbl, parent=None):
        super().__init__(lbl)
        self.lbl = lbl

    def mouseMoveEvent(self, e):
        if not (e.button() == Qt.LeftButton or e.modifiers() & Qt.ControlModifier):
            return

        mimeData = QMimeData()
        mimeData.setText(self.lbl)
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)


class QDWidgetAction(QWidgetAction):
    def __init__(self, parent=None, lbl="test", desc="not found"):
        super().__init__(parent)
        self.parent = parent
        self.lbl = lbl
        self.desc = desc
        self.is_highlighted = False
        self.action_maximum_height = 30
        self.right_frame_maximum_width = 30
        self.extension_middle = 300
        self.initUi()

    def initUi(self):
        import functools

        self.main_frame = QFrame()
        self.main_frame.setFrameStyle(QFrame.NoFrame)
        self.main_frame.setMinimumWidth(self.parent.maximum_menu_width)
        self.main_frame.setMinimumHeight(self.action_maximum_height)

        self.main_frame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # left_frame
        self.left_frame = QFrame()
        self.left_frame.setFrameStyle(QFrame.NoFrame)
        left_layout = QHBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        self.left_btn_ = QAPushButton(self.lbl)
        self.left_btn_.clicked.connect(self.restore_to_menu_)
        self.left_btn_.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_btn_.setStyleSheet(QPush_action_style)
        left_layout.addWidget(self.left_btn_)
        self.left_frame.setLayout(left_layout)

        # middle_frame
        self.middle_frame = QFrame()
        self.middle_frame.setFrameStyle(QFrame.NoFrame)
        middle_layout = QHBoxLayout()
        middle_layout.setContentsMargins(0, 0, 0, 0)
        middle_layout.setSpacing(0)

        self.middle_frame.setMaximumWidth(0)

        self.middle_line_edit = QLineEdit(self.desc)
        self.middle_line_edit.setDisabled(True)
        self.middle_line_edit.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.middle_line_edit.setStyleSheet(line_edit_style)
        self.middle_line_edit.returnPressed.connect(
            self.change_experiment_log_up_)
        middle_layout.addWidget(self.middle_line_edit)
        self.middle_frame.setLayout(middle_layout)

        # right_frame
        self.right_frame = QFrame()
        self.right_frame.setFrameStyle(QFrame.NoFrame)
        right_layout = QHBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        self.right_btn_ = QPushButton("X")
        self.right_btn_.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_btn_.setStyleSheet(QPush_action_style)
        self.right_btn_.clicked.connect(self.delete_history_item_permanently_)
        right_layout.addWidget(self.right_btn_)
        self.right_frame.setLayout(right_layout)
        self.right_frame.setMaximumWidth(0)

        main_layout.addWidget(self.left_frame)
        main_layout.addWidget(self.middle_frame)
        main_layout.addWidget(self.right_frame)

        self.main_frame.setLayout(main_layout)
        self.setDefaultWidget(self.main_frame)

    def restore_to_menu_(self):
        self.parent.restore_up_(self.left_btn_.text(), self.is_highlighted)
        self.parent.highlight_snapshots_(False)

    def change_experiment_log_up_(self):
        self.middle_line_edit.clearFocus()
        self.middle_line_edit.setDisabled(True)

        self.parent.log_file_editor_(
            self.left_btn_.text().strip(), self.middle_line_edit.text())

    def change_right_frame_(self):

        current_middle_frame_width = self.middle_frame.width()

        if self.right_frame.width() == 0:
            self.right_frame.setMinimumWidth(self.right_frame_maximum_width)
            self.right_frame.setMaximumWidth(self.right_frame_maximum_width)

            if current_middle_frame_width > 0:
                self.middle_frame.setMinimumWidth(
                    self.middle_frame.width() - self.right_frame.width())
                self.middle_frame.setMaximumWidth(
                    self.middle_frame.width() - self.right_frame.width())

        else:
            self.right_frame.setMinimumWidth(0)
            self.right_frame.setMaximumWidth(0)

            if current_middle_frame_width > 0:
                self.middle_frame.setMinimumWidth(
                    self.middle_frame.width() + self.right_frame_maximum_width)
                self.middle_frame.setMaximumWidth(
                    self.middle_frame.width() + self.right_frame_maximum_width)

    def change_middle_frame_(self):

        current_width = self.middle_frame.width()
        current_parent_width = self.parent.width()

        try:
            if self.parent.width() == self.parent.maximum_menu_width:
                self.parent.setMinimumWidth(self.extension_middle)
                self.parent.setMaximumWidth(self.extension_middle)
                self.middle_frame.setMaximumWidth(300)
            else:
                self.parent.setMinimumWidth(self.parent.maximum_menu_width)
                self.parent.setMaximumWidth(self.parent.maximum_menu_width)

        except:
            dumpException()

    def delete_history_item_permanently_(self):

        if DEBUG:
            print("delete button highlighted: ", self.is_highlighted)

        if not self.is_highlighted:
            reply = QMessageBox.question(self.parent, 'Delete', f'delete history item {self.lbl} permanently?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            delete_history_item = True if reply == QMessageBox.Yes else False

            if not delete_history_item:
                self.change_right_frame_()
            else:
                self.parent.actions.remove(self.left_btn_.text())
                self.parent.remove_history_directory_(self.left_btn_.text())
                self.parent.update_history_entries()

        else:
            reply = QMessageBox.question(self.parent, 'Delete', f'delete snapshot item {self.lbl} permanently?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            delete_history_item = True if reply == QMessageBox.Yes else False

            if delete_history_item:
                self.parent.remove_history_snapshot(self.left_btn_.text())

            self.change_right_frame_()
            self.parent.highlight_snapshots_(False)
