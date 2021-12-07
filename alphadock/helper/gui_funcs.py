from PyQt5 import QtWidgets, QtCore, QtGui


# https://stackoverflow.com/questions/64202927/how-to-save-and-restore-widget-properties-that-is-unique-for-each-instance-of-th
def settings_get_all_widgets(parent):
    # Possible fix to the issue: 
    # https://stackoverflow.com/questions/64202927/how-to-save-and-restore-widget-properties-that-is-unique-for-each-instance-of-th 

    if parent:
        # Find all children inside the given parent that is of type QWidget 
        all_widgets = parent.findChildren(QtWidgets.QWidget)
        if parent.isWidgetType():
            # If parent is of type QWidget, add the parent itself to the list 
            all_widgets.append(parent)
    else:
        # If no parent is given then get all the widgets from all the PyQt applications 
        all_widgets = QtWidgets.qApp.allWidgets()

    return all_widgets


def settings_value_is_valid(val):
    # Originally adapted from:
    # https://stackoverflow.com/a/60028282/4988010
    # https://github.com/eyllanesc/stackoverflow/issues/26#issuecomment-703184281
    if isinstance(val, QtGui.QPixmap):
        return not val.isNull()
    return True


def settings_restore(settings, parent=None):
    # Originally adapted from:
    # https://stackoverflow.com/a/60028282/4988010
    # https://github.com/eyllanesc/stackoverflow/issues/26#issuecomment-703184281

    if not settings:
        return

    all_widgets = settings_get_all_widgets(parent)

    finfo = QtCore.QFileInfo(settings.fileName())
    if finfo.exists() and finfo.isFile():
        for w in all_widgets:
            if w.objectName() and not w.objectName().startswith("qt_"):
                # if w.objectName():
                mo = w.metaObject()
                for i in range(mo.propertyCount()):
                    prop = mo.property(i)
                    name = prop.name()
                    last_value = w.property(name)
                    key = "{}/{}".format(w.objectName(), name)
                    if not settings.contains(key):
                        continue
                    val = settings.value(key, type=type(last_value), )
                    if (
                            val != last_value
                            and settings_value_is_valid(val)
                            and prop.isValid()
                            and prop.isWritable()
                    ):
                        w.setProperty(name, val)


def settings_save(settings, parent=None):
    # Originally adapted from:
    # https://stackoverflow.com/a/60028282/4988010
    # https://github.com/eyllanesc/stackoverflow/issues/26#issuecomment-703184281

    if not settings:
        return
    all_widgets = settings_get_all_widgets(parent)

    for w in all_widgets:
        if w.objectName() and not w.objectName().startswith("qt_"):
            mo = w.metaObject()
            for i in range(mo.propertyCount()):
                prop = mo.property(i)
                name = prop.name()
                key = "{}/{}".format(w.objectName(), name)
                val = w.property(name)
                if settings_value_is_valid(val) and prop.isValid() and prop.isWritable():
                    settings.setValue(key, w.property(name))



def sort_history(in_dict):
    d = list(in_dict.keys())
    is_save = "temp" in d
    d = [x for x in d if x not in ["temp"]]

    d = sorted([int(x) for x in d])
    try:
        max_experiment = d[-1]
    except:
        max_experiment = 0
    d = [str(x) for x in d]

    # ".ini" in os.listdir(in_dict)

    # if is_save:
    #     d += ["temp"]
    return d, max_experiment
