#
#  Project: MXCuBE
#  https://github.com/mxcube.
#
#  This file is part of MXCuBE software.
#
#  MXCuBE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MXCuBE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with MXCuBE.  If not, see <http://www.gnu.org/licenses/>.


import BlissFramework
if BlissFramework.get_gui_version() == "QT5":
    from PyQt5 import QtCore
    from PyQt5 import QtGui
else:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

from random import randint
import numpy as np

#Basic core colors
WHITE = QtGui.QColor( QtCore.Qt.white )
GRAY =  QtGui.QColor( QtCore.Qt.gray )
LIGHT_GRAY = QtGui.QColor( QtCore.Qt.lightGray )
DARK_GRAY = QtGui.QColor( QtCore.Qt.darkGray )
GREEN = QtGui.QColor( QtCore.Qt.green )
RED = QtGui.QColor( QtCore.Qt.red )

LIGHT_GREEN = QtGui.QColor(204,255,204)
LIGHT_RED = QtGui.QColor(255,204,204)
LIGHT_YELLOW = QtGui.QColor(254, 254, 121)
LIGHT_BLUE = QtGui.QColor(72, 191, 255)
LIGH_2_GRAY = QtGui.QColor(240, 240, 240)
SKY_BLUE = QtGui.QColor(190, 225 ,255)
PLUM = QtGui.QColor(142, 69, 133, 70)

LINE_EDIT_ORIGINAL = QtGui.QColor(0, 0, 12)
LINE_EDIT_ACTIVE = QtGui.QColor(204,255,204)
LINE_EDIT_CHANGED =  QtGui.QColor(255,165,0)
LINE_EDIT_ERROR = QtGui.QColor(255,204,204)

BUTTON_ORIGINAL = QtGui.QColor(242, 241, 240)
GROUP_BOX_GRAY = QtGui.QColor(230, 230, 230)
QUEUE_ENTRY_COLORS = [WHITE, LIGHT_GREEN, LIGHT_YELLOW, LIGHT_RED]

TREE_ITEM_SAMPLE = QtGui.QColor(240, 240, 240)
TREE_ITEM_COLLECTION = QtGui.QColor(255, 230, 210)

TASK_GROUP = [QtGui.QColor("#B0DBFF"), QtGui.QColor("#E57935"), QtGui.QColor("#B1FF52")]


def set_widget_color(widget, color, color_role=None):
    """
    Descript. :
    """
    if color_role is None:
        color_role = QtGui.QPalette.Window
    widget_palette = widget.palette()
    widget_palette.setColor(color_role, color)
    widget.setAutoFillBackground(True) 
    widget.setPalette(widget_palette)

def get_random_color(alpha=255):
    return QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255), alpha)

def get_random_rgb(alpha=255):
    return [randint(0, 255), randint(0, 255), randint(0, 255), alpha]

def get_random_hex(alpha=255):
    return "#{0:02x}{1:02x}{2:02x}".format(randint(0, 255), randint(0, 255), randint(0, 255))

def get_random_numpy_color(alpha=255):
    return np.random.rand(3,1)

def color_to_hexa(color):
    return "#%x%x%x" % (color.red(), color.green(), color.blue())

