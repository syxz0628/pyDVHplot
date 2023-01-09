__all__ = ["get_plot"]

from typing import NoReturn

from PyQt5.QtWidgets import QSizePolicy, QGridLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt


# 画图类
class MyPlot(FigureCanvas):

    def __init__(
            self,
            norow: int,
            nocol: int,
            parent=None,
            width: int = 15,
            height: int = 10,
            dpi: int = 100,
            bg_color: str = "white") -> NoReturn:
        """
        初始化画图对象

        :param norow: 指定行数
        :param nocol: 指定列数
        :param parent: 指定父控件
        :param width: 指定图框宽度
        :param height: 指定图框高度
        :param dpi: 指定分辨率
        :param bg_color: 指定背景颜色
        """

        # 设置支持中文
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 设置-号
        plt.rcParams['axes.unicode_minus'] = False

        # 创建一个新的图框
        self.fig, self.axes_list = plt.subplots(norow, nocol, figsize=(width, height), dpi=dpi)
        # 设置背景颜色
        rect = self.fig.patch
        rect.set_facecolor(bg_color)

        # 激活图框，必须要有这句话！！
        FigureCanvas.__init__(self, self.fig)
        # 设定父类，！注：暂不指定父类，用来以后修改继承从而增加新的功能
        self.setParent(parent)

        # 调整各个轴之间的间距
        self.fig.subplots_adjust(hspace=0.3, wspace=0.3)

        # 设置画布的尺寸策略
        FigureCanvas.setSizePolicy(self, QSizePolicy.Ignored, QSizePolicy.Ignored)

    def clear_data(self,
                   row: int,
                   col: int,
                   all_clear: bool = False) -> NoReturn:
        """
        清除画图的数据

        :param row: 要清除的子图行索引
        :param col: 邀清除的子图列索引
        :param all_clear: 是否清除全部
        :return: None
        """
        if all:
            row = self.axes_list.shape[0]
            col = self.axes_list.shape[1]
            for i in range(row):
                for j in range(col):
                    self.axes_list[i][j].cla()
        else:
            self.axes_list[row][col].cla()
        self.draw()


def get_plot(row: int, col: int, layout=None):
    """
    获取画图对象

    :param row:指定子图行数
    :param col:指定子图列数
    :param layout:指定画图对象所属的布局
    :return:画图对象，布局对象
    """
    if layout is None:
        layout = QGridLayout()

    plot = MyPlot(row, col)
    layout.addWidget(plot)

    return plot, layout
