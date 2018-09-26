import sys

from PySide2 import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
# Main widget
w = QtWidgets.QWidget()

# Main Layout
mainHbox = QtWidgets.QHBoxLayout(w)
leftVbox = QtWidgets.QVBoxLayout()
rightVbox = QtWidgets.QVBoxLayout()
mainHbox.addLayout(leftVbox)
mainHbox.addLayout(rightVbox)

# Contains dropdowns, labels and buttons
projectCategoryVbox = QtWidgets.QVBoxLayout()
leftVbox.addLayout(projectCategoryVbox)
# Projects Hbox
projectsHbox = QtWidgets.QHBoxLayout()
projectCategoryVbox.addLayout(projectsHbox)

projectLabel = QtWidgets.QLabel("Project:")
projectLabel.setFixedWidth(80)
projectsHbox.addWidget(projectLabel)
projectComboBox = QtWidgets.QComboBox()
projectComboBox.addItem("")
for i in range(1,11):
    projectComboBox.addItem("Project "+`i`)

projectsHbox.addWidget(projectComboBox)

projectPlusButton = QtWidgets.QPushButton("+")
projectPlusButton.setFixedSize(25,25)
projectsHbox.addWidget(projectPlusButton)

# Category hbox
categoryHbox = QtWidgets.QHBoxLayout()
projectCategoryVbox.addLayout(categoryHbox)

categroyLabel = QtWidgets.QLabel("Category:")
categroyLabel.setFixedWidth(80)
categoryHbox.addWidget(categroyLabel)
categoryComboBox = QtWidgets.QComboBox()
categoryComboBox.addItem("")
for i in range(1,6):
    categoryComboBox.addItem("Category "+`i`)
categoryHbox.addWidget(categoryComboBox)

categoryPlusButton = QtWidgets.QPushButton("+")
categoryPlusButton.setFixedSize(25,25)
categoryHbox.addWidget(categoryPlusButton)

categoryList = QtWidgets.QListWidget()
categoryList.addItem("Item")

# Left Vbox components
taskList = QtWidgets.QListWidget()
for i in range(1,20):
    taskList.addItem("task_"+`i`)

leftVbox.addWidget(taskList)
leftVbox.addWidget(QtWidgets.QPushButton("New task"))

#Right vbox 
fileList = QtWidgets.QListWidget()
for i in range(1,12):
    fileList.addItem("file1_"+'{0:03}'.format(i)+".ma")
publishButton = QtWidgets.QPushButton("Publish file")
rightVbox.addWidget(fileList)
rightVbox.addWidget(publishButton)

w.resize(800,600)
w.setWindowTitle("Maya AssetManager")
w.show()
sys.exit(app.exec_())