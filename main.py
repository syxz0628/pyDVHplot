import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from PyQt5.QtGui import QStandardItem

from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex

from PlotUtil import get_plot

from UI.Ui_MainWindow import Ui_MainWindow

from colorDialog import ColorDialog

import matplotlib.pyplot as plt

from QtModelUtil import get_row_model, set_tableview, clear_model

import os


class VOI:
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        self.dic1 = {}  # gd1文件的字典
        self.dic2 = {}  # gd2文件的字典
        self.newDic1 = {}  # 数据处理之后的gd1
        self.newDic2 = {}  # 数据处理之后的gd2
        self.fileName = None
        self.gd1 = None  # gd1打开的文件名称
        self.gd2 = []  # gd2打开的多个文件名称集合
        self.s1 = 1.0
        self.color_map = plt.get_cmap("Pastel1")

        self.plot1, layout1 = get_plot(1, 1)
        self.plot2, layput2 = get_plot(1, 1)

        self.UI.frame.setLayout(layout1)
        self.UI.frame_2.setLayout(layput2)

        self.__init_listView()

    def __init_listView(self):
        model1 = get_row_model(["文件名称"])
        model2 = get_row_model(["文件名称"])

        self.UI.listView_1.setModel(model1)
        self.UI.listView_2.setModel(model2)

        set_tableview(self.UI.listView_1)
        set_tableview(self.UI.listView_2)

    @pyqtSlot(bool)
    def on_rab_proton_toggled(self, state):
        if state: self.s1 = 1.0
        self.preprocess_data()

    @pyqtSlot(bool)
    def on_rab_proton_toggled(self, state):
        if state: self.s1 = 1.1
        self.preprocess_data()

    @pyqtSlot()
    def on_btn_clear1_clicked(self):
        self.clear_common()
        self.clear1()

    @pyqtSlot()
    def on_btn_clear2_clicked(self):
        self.clear_common()
        self.clear2()

    @pyqtSlot()
    def on_btn_opengd1_clicked(self):
        filename, flt = QFileDialog.getOpenFileName(self, "打开文件", "", filter=("*.gd"))
        if filename:
            self.__add_gd1_text(filename)
            self.read_gd_file(filename, 1)
            self.append_list1_model()

    @pyqtSlot()
    def on_btn_opengd2_clicked(self):
        filenames, flt = QFileDialog.getOpenFileNames(self, "打开文件", "", filter=("*.gd"))
        if filenames:
            self.__add_gd2_text(filenames)
            for i in self.gd2:
                self.read_gd_file(i, 2)
            self.preprocess_data()

    # 导出txt数据槽函数
    # todo：导出txt
    @pyqtSlot()
    def on_btn_1_clicked(self):
        saveFilename, flt = QFileDialog.getSaveFileName(self, f"选择保存文件", "", filter=("*.txt"))
        if saveFilename:
            saveVoiNames, _ = self.__get_plot_data()
            with open(saveFilename, 'w') as writeFile:
                writeFile.write(f"{self.fileName}")
                for voiName in saveVoiNames:
                    writeFile.write(f"VOI:{voiName}\n")
                    res = self.find_all_VOI(voiName)
                    N = len(res) - 1
                    gd1 = res[0]
                    gd2 = res[1:]
                    writeFile.write("X\t")
                    for i in range(N):
                        writeFile.write(f"Y{i + 1}\t")

                    writeFile.write("\n")

                    for i, v in enumerate(gd1.data):
                        writeFile.write(f"{v[0]}\t")
                        for j in gd2:
                            writeFile.write(f"{j.data[i][1]}\t")

                        writeFile.write("\n")

    # 导出图像槽函数
    @pyqtSlot()
    def on_btn_3_clicked(self):
        for i in [1, 2]:
            self.__save_plot(i)

    # L1->L2槽函数
    @pyqtSlot(QModelIndex)
    def on_listView_1_doubleClicked(self, index):
        old_model = self.UI.listView_1.model()
        row = index.row()
        old_data_item = old_model.item(row)
        old_data_text = old_data_item.text()
        tar_model = self.UI.listView_2.model()
        tar_model.appendRow(QStandardItem(old_data_text))
        old_model.removeRow(row)

    @pyqtSlot(QModelIndex)
    def on_listView_2_doubleClicked(self, index):
        old_model = self.UI.listView_2.model()
        tar_model = self.UI.listView_1.model()
        row = index.row()
        old_data_item = old_model.item(row)
        old_data_text = old_data_item.text()

        tar_model.appendRow(QStandardItem(old_data_text))
        old_model.removeRow(row)

    # 画图槽函数
    @pyqtSlot()
    def on_btn_plot_clicked(self):
        self.clear_plot()
        plot_data, colors = self.__get_plot_data()
        self.plot_data(plot_data, colors, 2)
        self.plot_data(plot_data, colors, 1)

    # 选择颜色槽函数
    @pyqtSlot()
    def on_btn_2_clicked(self):
        window = ColorDialog(self)
        window.color_sig.connect(self.do_receive_cmap)
        window.show()

    # 接受选择槽函数
    @pyqtSlot(str)
    def do_receive_cmap(self, cmap):
        self.color_map = cmap

    # 获取画图数据和颜色
    def __get_plot_data(self):
        color_map = plt.get_cmap(self.color_map)
        model = self.UI.listView_2.model()
        N = model.rowCount()
        plot_list = []
        for i in range(N):
            item_name = model.item(i).text()
            plot_list.append(item_name)
        colors = self.cmap2RGb(color_map, N)

        return plot_list, colors

    # 导出图像实质函数
    def __save_plot(self, num):
        filename, flt = QFileDialog.getSaveFileName(self, f"plot{num}选择保存文件", "", filter=("*.png"))
        if num == 1:
            self.plot1.fig.savefig(filename)
        else:
            self.plot2.fig.savefig(filename)

    # 添加文件
    def append_model_data(self, data, model):
        if not isinstance(data, list):
            data = [data]
        for i in data:
            if i: model.appendRow(QStandardItem(str(i)))

    # 读取gd文件
    def read_gd_file(self, file_name, type):
        if type == 1:
            self.read_single_file(file_name, self.dic1)
        else:
            self.read_single_file(file_name, self.dic2)

    def read_single_file(self, file_name, ret_dic: dict):
        temp_dic = {}
        if file_name is not None:
            with open(file_name, 'r') as file:
                current_data = []
                current_name = None
                for line in file:
                    if self.fileName is None and line.startswith("'MI"):
                        self.fileName = line
                    if not line and line.startswith("H:"):
                        continue
                    split_line = line.split()
                    if line.startswith('c:'):
                        if split_line[1] != 'VOI':
                            current_name = split_line[1]
                        elif current_name is not None:
                            obj = VOI(current_name, [i for i in current_data])
                            temp_dic[current_name] = obj
                            current_name = None
                            current_data.clear()
                    elif len(split_line) == 3:
                        current_data.append([float(split_line[0]), float(split_line[1])])
            ret_dic[file_name] = temp_dic

    @pyqtSlot(int)
    def on_spinBox_1_valueChanged(self, v):
        self.preprocess_data()
        self.on_btn_plot_clicked()

    @pyqtSlot(int)
    def on_spinBox_2_valueChanged(self, v):
        self.preprocess_data()
        self.on_btn_plot_clicked()

    @pyqtSlot(int)
    def on_spinBox_3_valueChanged(self, v):
        self.preprocess_data()
        self.on_btn_plot_clicked()

    @pyqtSlot(int)
    def on_spinBox_4_valueChanged(self, v):
        self.preprocess_data()
        self.on_btn_plot_clicked()

    # 画图
    def plot_data(self, plot_data, colors, type):

        for name, color in zip(plot_data, colors):
            if type == 2:

                self.plot_p2(name, color)
            else:

                self.plot_p1(name, color)

    def plot_p1(self, voiName, color):

        fileName = self.UI.lineEdit_gd1.text()
        x = [i[0] for i in self.newDic1[fileName][voiName].data]
        y1 = [i[1] for i in self.dic1[fileName][voiName].data]

        maxv = [i[0] for i in self.newDic2[voiName]]
        minv = [i[1] for i in self.newDic2[voiName]]
        self.plot1.axes_list.fill_between(x, y1, maxv, alpha=self.UI.doubleSpinBox.value())
        self.plot1.axes_list.fill_between(x, minv, y1, alpha=self.UI.doubleSpinBox.value())
        # self.plot1.axes_list.scatter(x, y1)
        self.plot1.axes_list.plot(x, y1, color=color)

        for fileName in self.newDic2:
            pass

        self.plot1.axes_list.set_ylabel("Volume(%)", fontsize=15)
        self.plot1.axes_list.set_xlabel(f"Dose(%)", fontsize=15)
        self.plot1.axes_list.grid(True)
        self.plot1.draw()

    def plot_p2(self, voiName, color):

        fileName = self.UI.lineEdit_gd1.text()
        x = [i[0] for i in self.newDic1[fileName][voiName].data]
        y1 = [i[1] for i in self.dic1[fileName][voiName].data]
        # self.plot2.axes_list.scatter(x, y1)
        self.plot2.axes_list.plot(x, y1, linestyle='dashed', color=color, alpha=self.UI.doubleSpinBox.value())

        res = self.find_all_VOI(voiName)[1:]
        for voiObj in res:
            y = [i[1] for i in voiObj.data]
            self.plot2.axes_list.plot(x, y, linestyle='dashed', alpha=self.UI.doubleSpinBox.value())

        # todo:设置标签、标题
        self.plot2.axes_list.set_ylabel("Volume(&)", fontsize=15)
        self.plot2.axes_list.set_xlabel(f"Dose()", fontsize=15)
        # self.plot2.axes_list.set_title(f"{voiName}", fontsize=25)
        self.plot2.axes_list.grid(True)
        self.plot2.draw()

    # 预处理数据

    def preprocess_data(self):
        if self.dic1 and self.dic2:
            self.preprocess_min_length()

            for fileName in self.dic1:
                tmpData = self.dic1[fileName]
                self.newDic1[fileName] = {}
                for voiName in tmpData:
                    curVoiData = tmpData[voiName].data
                    T3 = self.UI.spinBox_1.value()
                    T4 = self.UI.spinBox_2.value()
                    T5 = self.UI.spinBox_3.value()
                    T6 = self.UI.spinBox_4.value()
                    new_data = [[i[0] * self.s1 * (T3 / T4) / (T5 / T6), i[1]] for i in curVoiData]

                    self.newDic1[fileName][voiName] = VOI(voiName, new_data)

            self.newDic2 = {}
            for fileName in self.dic1:
                for voiName in self.dic1[fileName]:
                    target_voi = self.dic1[fileName][voiName]
                    compare_voi_list = self.find_all_VOI(voiName)
                    res = []
                    for index, target in enumerate(target_voi.data):
                        tmpY = [i.data[index][1] for i in compare_voi_list]
                        minV = min(tmpY)
                        maxV = max(tmpY)
                        avgV = np.mean(tmpY)
                        medianV = np.median(tmpY)
                        res.append([maxV, minV, medianV, avgV])

                    self.newDic2[voiName] = res

            # for fileName in self.dic2:
            #     self.newDic2[fileName] = {}
            #     tmpData = self.dic2[fileName]
            #     for voiName in tmpData:
            #         voiData = tmpData[voiName].data
            #         tmpY = [i[1] for i in voiData]
            #         minV = min(tmpY)
            #         maxV = max(tmpY)
            #         avgV = np.mean(tmpY)
            #         medianV = np.median(tmpY)
            #
            #         self.newDic2[fileName][voiName] = [maxV, minV, medianV, avgV]

    # cmap转换函数
    def cmap2RGb(self, color_map, N):
        res = []
        for i in range(N):
            colo = color_map(i)
            R = int(colo[0] * 255)
            G = int(colo[1] * 255)
            B = int(colo[2] * 255)

            r16 = str(hex(int(R)))[2:]
            g16 = str(hex(int(G)))[2:]
            b16 = str(hex(int(B)))[2:]

            if len(r16) == 1: r16 = "0" + r16
            if len(g16) == 1: g16 = "0" + g16
            if len(b16) == 1: b16 = "0" + b16
            color16 = f"#{r16}{g16}{b16}"

            res.append(color16)
            res.append(color16)

        return res

    def append_list1_model(self):
        model = self.UI.listView_1.model()
        for fileName in self.dic1:
            data = self.dic1[fileName]
            keys = list(data.keys())
            self.append_model_data(keys, model)

    def preprocess_min_length(self):
        for fileName in self.dic1:
            tmpVoiDatas = self.dic1[fileName]
            for voiName in tmpVoiDatas:
                res = self.find_all_VOI(voiName)
                minLength = None
                for voiObj in res:
                    if minLength is None:
                        minLength = len(voiObj.data)
                    else:
                        minLength = min(minLength, len(voiObj.data))

                self.set_min_length(minLength, res)

    def set_min_length(self, minLength, voiList):
        for voiObj in voiList:
            voiObj.data = voiObj.data[:minLength]

    def clear_common(self):
        self.plot1.axes_list.cla()
        self.plot2.axes_list.cla()
        self.plot1.draw()
        self.plot2.draw()

    def clear1(self):
        self.UI.lineEdit_gd1.clear()
        self.gd1 = None
        model1 = self.UI.listView_1.model()
        model2 = self.UI.listView_2.model()
        clear_model(model1)
        clear_model(model2)

        self.dic1.clear()
        self.newDic1.clear()

    def clear2(self):
        self.UI.lineEdit_gd2.clear()
        self.gd2 = []
        self.dic2.clear()
        self.newDic2.clear()

    def __add_gd1_text(self, filename):
        self.gd1 = filename
        self.UI.lineEdit_gd1.setText(filename)

    def __add_gd2_text(self, filenames):
        self.gd2.clear()
        self.gd2 = self.gd2 + filenames
        text = ";".join(filenames)
        self.UI.lineEdit_gd2.setText(text)

    def find_all_VOI(self, voiName):
        res = []
        flg = False
        for i in self.dic1:
            data = self.dic1[i]
            tmpVoiData = data.get(voiName, None)
            if tmpVoiData is not None:
                flg = True
                res.append(tmpVoiData)
        for gdFile in self.dic2:
            data = self.dic2[gdFile]
            tmpVoiData = data.get(voiName, None)
            if tmpVoiData is not None:
                res.append(tmpVoiData)

        return res if flg else None

    def clear_plot(self):
        self.plot2.axes_list.cla()
        self.plot1.axes_list.cla()
        self.plot2.draw()
        self.plot1.draw()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
