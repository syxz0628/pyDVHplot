from typing import Optional, NoReturn, List, NewType, Sequence, Tuple, AnyStr, Any, Dict, Union

from PyQt5.QtGui import QStandardItem, QStandardItemModel

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QAbstractItemView, QTableView, QWidget, QListView, QTreeView




def _append_row_data(model: QStandardItemModel, row: List[Any]) -> bool:
    """
    添加一行

    :param model: 模型
    :param row: 一行数据
    :return: None
    """
    if isinstance(row, list):
        raise TypeError("错误的数据类型")

    col_cnt = model.columnCount()

    if len(row) > col_cnt:
        row = row[0: col_cnt]

    row_data = [QStandardItem(str(i)) for i in row]
    model.appendRow(row_data)

    return len(row) == col_cnt

def append_widget_data(widget: QWidget, data):
    if isinstance(widget, QListView): __append_list_data(widget, data)
    if isinstance(widget, QTableView): __append_table_data(data)
    if isinstance(widget, QTreeView): __append_tree_data(data)


def __append_list_data(widget, data):
    model = widget.model()
    if not isinstance(data, list):
        model.appendRow(QStandardItem(f"{data}"))
    else:
        for i in data:
            pass


def __append_tree_data():
    pass

def __append_table_data():
    pass

# 添加模型数据
def append_model_data(
        model: QStandardItemModel,
        append_data: Sequence[Sequence],
        is_clear: bool = False) -> bool:
    """
    给一个模型中添加数据

    :param model: 要添加的模型
    :param append_data: 要添加的数据
    :param is_clear: 指定是否清空原有数据
    :param header: 指定新的标题
    :return: None
    """
    clear_model(model) if is_clear else None

    if len(append_data) == 1:
        return _append_row_data(append_data)

    res = True

    for i, v in enumerate(append_data):
        res = res & _append_row_data(model, v)
        if not res:
            print(f"第{i}个数据出现问题，请检查", end='\t')

    return res


# 清除模型数据
def clear_model(
        model: QStandardItemModel,
        keep: bool = True) -> NoReturn:
    """
    清除给定模型的信息

    :param model: 要清除数据的模型
    :param keep: 指定是否保留原始标题
    :return: None
    """
    old_header = [model.horizontalHeaderItem(i).text() for i in range(model.columnCount())]

    model.clear()
    if keep: model.setHorizontalHeaderLabels(old_header)

    return None


# 获取模型数据
def get_model_data(
        model: QStandardItemModel,
        mask: Sequence[int] = None) -> List[Tuple[str]]:
    """
    获取StandardItemModel模型数据

    :param model: 要获取数据的模型
    :param mask: 要屏蔽的列号
    :return: 获取到的数据列表
    """

    # 获取行数
    row_count = model.rowCount()
    # 获取列数
    column_count = model.columnCount()
    res = []

    # 获取数据
    for i in range(row_count):
        row = []
        for j in range(column_count):
            item = model.item(i, j)
            if item is not None and j not in mask:
                row.append(item.text())
            else:
                row.append("")
        res.append(tuple(row))

    return res


# 获取初始TableModel模型
def get_row_model(header: List[AnyStr]) -> QStandardItemModel:
    """
    获取初始的StandardItemModel模型。

    :param header: 模型的标题
    :return: QStandardItemModel模型
    """
    col_cnt = len(header)

    # 创建表格模型
    model = QStandardItemModel(0, col_cnt)
    # 设置标题
    model.setHorizontalHeaderLabels(header)

    return model


# 初始化table_view函数

def set_tableview(
        widget: QTableView,
        hor_size: int = 100,
        ver_size: int = 75,
        is_alter_color: bool = True,
        is_edit: bool = False) -> NoReturn:
    """
    设置tableview控件

    :param widget: 要设置的TableView控件
    :param hor_size: 指定单元格水平长度
    :param ver_size: 指定单元格垂直长度
    :param is_alter_color: 指定是否使用交替颜色
    :param is_edit: 指定是否可编辑
    :return:
    """
    # 设置交错颜色
    widget.setAlternatingRowColors(is_alter_color)
    # 设置选择行为单位
    widget.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 设置只能单选
    widget.setSelectionMode(QAbstractItemView.SingleSelection)
    if isinstance(widget, QTableView):
        # 设置单元格大小
        widget.horizontalHeader().setDefaultSectionSize(hor_size)
        widget.verticalHeader().setDefaultSectionSize(ver_size)
    if not is_edit:
        # 设置不可编辑
        widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    return None


def find_item(
        model: QStandardItemModel,
        target_text: str,
        pattern: int = Qt.MatchContains) -> Dict[int, List[Union[QStandardItem, QStandardItem]]]:
    """
    查询模型中的item对象

    :param model: 进行查询的模型对象
    :param target_text: 指定查询的字符串
    :param pattern: 指定查询的模式，默认包含指定的字符串则视为搜索到
    :param col_no: 指定查询的列号
    :return: 查询到的列表
    """
    col_cnt = model.columnCount()
    ret_dict = {}
    for i in range(col_cnt):
        ret, res = _find_item_in_col(model, target_text, i, pattern)
        if res:
            ret_dict[i] = ret

    return ret_dict


def _find_item_in_col(
        model: QStandardItemModel,
        target_text: str,
        col_index: int,
        pattern: int) -> Tuple[List[QStandardItem], bool]:
    ret_list = model.findItems(target_text, pattern, col_index)

    return (ret_list, True) if ret_list else ([], False)
