from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox


def show_input_warning_msgbox(parent, input_widget):
    """
    Show a warning message box when user input an invalid SMILES string
    
    Parameters
    ----------
    parent : QWidget
        Parent widget
    input_widget : QWidget
        Input widget
    """
    # 创建 QMessageBox
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText('Please input a valid SMILES string!')
    msg_box.setWindowTitle('Input Error')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setFont(QFont('Segoe UI', 11))
    
    # 显示 QMessageBox 并返回选中的按钮
    return_value = msg_box.exec()
    
    if return_value == QMessageBox.StandardButton.Ok:
        # 用户点击确定后，将焦点重新定位到输入框
        input_widget.setFocus()
        # return 用于在显示警告并处理用户的响应后结束此方法或函数的执行
        return


def show_select_warning_msgbox(parent, input_widget):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText('No Model Selected!')
    msg_box.setInformativeText('Please select at least one model to start prediction.')
    msg_box.setWindowTitle('Select Error')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setFont(QFont('Segoe UI', 11))
    
    return_value = msg_box.exec()
    
    if return_value == QMessageBox.StandardButton.Ok:
        input_widget.setFocus()
        return


def show_file_warning_msgbox(parent, input_widget):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText('Invalid File Type!')
    msg_box.setInformativeText('Please upload a valid txt or sdf format file for prediction.')
    msg_box.setWindowTitle('File Type Error')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setFont(QFont('Segoe UI', 11))
    
    return_value = msg_box.exec()
    
    if return_value == QMessageBox.StandardButton.Ok:
        input_widget.setFocus()
        return


def file_empty_warning_msgbox(parent, input_widget):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText('The Uploaded File is Empty!')
    msg_box.setInformativeText('Please check the contents of your file and upload again.')
    msg_box.setWindowTitle('File Content Error')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setFont(QFont('Segoe UI', 11))
    
    return_value = msg_box.exec()
    
    if return_value == QMessageBox.StandardButton.Ok:
        input_widget.setFocus()
        return


def no_file_chosen_msgbox(parent, input_widget):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setText('No File Chosen!')
    msg_box.setInformativeText('Please choose a file to upload before prediction.')
    msg_box.setWindowTitle('File Error')
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setFont(QFont('Segoe UI', 11))
    
    return_value = msg_box.exec()
    
    if return_value == QMessageBox.StandardButton.Ok:
        input_widget.setFocus()
        return
