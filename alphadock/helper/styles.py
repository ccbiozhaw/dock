

menu_style = """
        
QMenu {
    background-color: rgb(37, 41, 48);
    color: rgb(255, 255, 255);
	font: 75 10pt "MS Shell Dlg 2";
    border: 0px;
        }
QMenu::item {
    /* sets background of menu item. set this to something non-transparent
        if you want menu color and menu item color to be different */
    background-color: transparent;
    padding: 5px 40px;
    border - 0px;

}

QMenu::item:selected { /* when user selects item using mouse or keyboard */
	background-color: rgb(57, 65, 80);
	border: 2px solid rgb(61, 70, 86);
}

QMenu::item:hover { /* when user selects item using mouse or keyboard */
	background-color: rgb(57, 65, 80);
	border: 2px solid rgb(61, 70, 86);
}
QMenu::indicator {
    width: 0px;
    height: 0px;
}
QMenu::icon:checked { /* when user selects item using mouse or keyboard */
	background-color: rgb(57, 65, 80);
	border: 3px solid rgb(61, 70, 86);

}

QMenu::item:checked { /* when user selects item using mouse or keyboard */

	background-color: rgb(57, 65, 80);
	border: 2px solid rgb(61, 70, 86);
    background-image: url(potatofix/images/icons/cil-check-alt.png);
    background-repeat: no-reperat;
    background-position: center left;
    
    
}
          
"""

line_edit_style = """
QLineEdit {
	background-color: rgb(33, 37, 43);
	border-radius: 5px;
	border: 2px solid rgb(33, 37, 43);
	padding-left: 10px;
	selection-color: rgb(255, 255, 255);
	selection-background-color:rgb(0, 172, 255);
	color: rgb(255, 255, 255);
	padding:2px;
	font: 75 10pt "MS Shell Dlg 2";
	padding-left: 10px;
}
QLineEdit:hover {
	border: 2px solid rgb(64, 71, 88);
	padding-left: 10px;
}
QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124);
	padding-left: 10px;
}
"""


fix_combo_style = """
            QComboBox{
                background-color: rgb(27, 29, 35);
                border-radius: 5px;
                border: 2px solid rgb(33, 37, 43);
                padding: 2px;
                padding-left: 10px;
                color: rgb(255, 255, 255);
                font: 75 10pt "MS Shell Dlg 2";
            }
            QComboBox:hover{
                border: 2px solid rgb(64, 71, 88);
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px; 
                border-left-width: 3px;
                border-left-color: rgba(39, 44, 54, 150);
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;	
                background-position: center;
                background-image: url(potatofix/images/icons/cil-arrow-bottom.png);
                background-repeat: no-reperat;
             }
            QComboBox QAbstractItemView {
                color: rgb(112, 255, 16);
                background-color: rgb(33, 37, 43);
                padding: 10px;
                selection-background-color: rgb(39, 44, 54);
            }
        """

QPush_action_style = """
QPushButton {
	border: 2px solid rgb(37, 41, 48);
	border-radius: 2px;	
	background-color: rgb(37, 41, 48);
    color: rgb(255, 255, 255);
	font: 75 10pt "MS Shell Dlg 2";
}
 QPushButton:hover {
	background-color: rgb(57, 65, 80);
	border: 2px solid rgb(61, 70, 86);
}
 QPushButton:pressed {	
	background-color: rgb(35, 40, 49);
	border: 2px solid rgb(43, 50, 61);
}"""

QPush_action_style_snapped = """
QPushButton {
	border: 2px solid rgb(61, 70, 86);
	border-radius: 2px;	
	background-color: rgb(61, 70, 86);
    color: rgb(255, 255, 255);
	font: 75 10pt "MS Shell Dlg 2";
}
 QPushButton:hover {
	background-color: rgb(57, 65, 80);
	border: 2px solid rgb(61, 70, 86);
}
 QPushButton:pressed {	
	background-color: rgb(35, 40, 49);
	border: 2px solid rgb(43, 50, 61);
}"""

