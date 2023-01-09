# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_opengd2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opengd2.setObjectName("btn_opengd2")
        self.gridLayout.addWidget(self.btn_opengd2, 1, 0, 1, 1)
        self.btn_clear2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear2.setObjectName("btn_clear2")
        self.gridLayout.addWidget(self.btn_clear2, 1, 2, 1, 1)
        self.lineEdit_gd2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gd2.setReadOnly(True)
        self.lineEdit_gd2.setObjectName("lineEdit_gd2")
        #self.lineEdit_gd2.setText('/run/user/1000/doc/e4e06acb/total.bio_hd.dvh.gd;/run/user/1000/doc/140c79d3/total.bio_hd_nx.dvh.gd;/run/user/1000/doc/1119903a/total.bio_hd_ny.dvh.gd;/run/user/1000/doc/1712f7d1/total.bio_hd_nz.dvh.gd;/run/user/1000/doc/1b906512/total.bio_hd_px.dvh.gd;/run/user/1000/doc/fb633117/total.bio_hd_py.dvh.gd;/run/user/1000/doc/4d294222/total.bio_hd_pz.dvh.gd;/run/user/1000/doc/ba890fb0/total.bio_ld.dvh.gd;/run/user/1000/doc/68eacb74/total.bio_ld_nx.dvh.gd;/run/user/1000/doc/dc487c21/total.bio_ld_ny.dvh.gd;/run/user/1000/doc/2c96c6a9/total.bio_ld_nz.dvh.gd;/run/user/1000/doc/4f8132e9/total.bio_ld_px.dvh.gd;/run/user/1000/doc/4289b42d/total.bio_ld_py.dvh.gd;/run/user/1000/doc/459804b9/total.bio_ld_pz.dvh.gd;/run/user/1000/doc/f713f0e9/total.bio_nx.dvh.gd;/run/user/1000/doc/107dc23a/total.bio_ny.dvh.gd;/run/user/1000/doc/bb990b37/total.bio_nz.dvh.gd;/run/user/1000/doc/a6c3fe7a/total.bio_px.dvh.gd;/run/user/1000/doc/58ec1931/total.bio_py.dvh.gd;/run/user/1000/doc/b735653a/total.bio_pz.dvh.gd;/run/user/1000/doc/257a2e5d/total.bio_voxelwiseMax.dvh.gd;/run/user/1000/doc/e042219f/total.bio_voxelwiseMin.dvh.gd')
        self.gridLayout.addWidget(self.lineEdit_gd2, 1, 1, 1, 1)
        self.btn_opengd1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opengd1.setObjectName("btn_opengd1")
        self.gridLayout.addWidget(self.btn_opengd1, 0, 0, 1, 1)
        self.lineEdit_gd1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gd1.setReadOnly(True)
        self.lineEdit_gd1.setObjectName("lineEdit_gd1")
        #self.lineEdit_gd1.setText('/home/yurii/Sheng/Pythoncode/pyDVHplot/gd-files/total.bio_nom.dvh.gd')
        self.gridLayout.addWidget(self.lineEdit_gd1, 0, 1, 1, 1)
        self.btn_clear1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear1.setObjectName("btn_clear1")
        self.gridLayout.addWidget(self.btn_clear1, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rab_proton = QtWidgets.QRadioButton(self.centralwidget)
        self.rab_proton.setObjectName("rab_proton")
        self.horizontalLayout_3.addWidget(self.rab_proton)
        self.rab_carbon = QtWidgets.QRadioButton(self.centralwidget)
        self.rab_carbon.setChecked(True)
        self.rab_carbon.setObjectName("rab_carbon")
        self.horizontalLayout_3.addWidget(self.rab_carbon)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 0, 3, 1, 1)
        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setMinimum(1)
        self.spinBox_1.setProperty("value", 3)
        self.spinBox_1.setObjectName("spinBox_1")
        self.gridLayout_2.addWidget(self.spinBox_1, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setProperty("value", 70)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_2.addWidget(self.spinBox_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setProperty("value", 20)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_2.addWidget(self.spinBox_4, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.listView_1 = QtWidgets.QListView(self.centralwidget)
        self.listView_1.setObjectName("listView_1")
        self.gridLayout_3.addWidget(self.listView_1, 1, 0, 1, 1)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_3.addWidget(self.listView_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_4.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_4.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_4.addWidget(self.btn_3)
        self.btn_plot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plot.setObjectName("btn_plot")
        self.horizontalLayout_4.addWidget(self.btn_plot)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.05)
        self.doubleSpinBox.setProperty("value", 0.6)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_opengd2.setText(_translate("MainWindow", "Open Compare gd"))
        self.btn_clear2.setText(_translate("MainWindow", "clear"))
        self.btn_opengd1.setText(_translate("MainWindow", "Open Ref gd"))
        self.btn_clear1.setText(_translate("MainWindow", "clear"))
        self.rab_proton.setText(_translate("MainWindow", "Proton"))
        self.rab_carbon.setText(_translate("MainWindow", "Carbon"))
        self.label.setText(_translate("MainWindow", "planned dose in gd"))
        self.label_2.setText(_translate("MainWindow", "Real prescirbed dose"))
        self.label_4.setText(_translate("MainWindow", "Real prescirbed fx"))
        self.label_3.setText(_translate("MainWindow", "planned fix in gd"))
        self.label_5.setText(_translate("MainWindow", "vols in gd"))
        self.label_6.setText(_translate("MainWindow", "vols to plot"))
        self.btn_1.setText(_translate("MainWindow", "Export ribbon plot data"))
        self.btn_2.setText(_translate("MainWindow", "set plot colors"))
        self.btn_3.setText(_translate("MainWindow", "exports plot"))
        self.btn_plot.setText(_translate("MainWindow", "plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ribbon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "AllDHV"))