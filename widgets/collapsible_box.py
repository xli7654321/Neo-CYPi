from PySide6.QtCore import QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation, Qt, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QScrollArea, QSizePolicy, QToolButton, QVBoxLayout, QWidget  


class CollapsibleBox(QWidget):
    def __init__(self):
        super().__init__()

        font = QFont("Segoe UI", 12)

        # toggle_btn
        self.toggle_btn = QToolButton()
        self.toggle_btn.setObjectName("toolbtn")
        self.toggle_btn.setFont(font)
        self.toggle_btn.setText('Select Prediction Models')
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.setChecked(False)
        self.toggle_btn.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.toggle_btn.setArrowType(Qt.ArrowType.RightArrow)
        self.toggle_btn.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.toggle_btn.toggled.connect(self.on_toggle_btn_toggled)

        # toggle_btn_content
        self.toggle_btn_content = QScrollArea()
        self.toggle_btn_content.setObjectName("toolbtn_content")
        self.toggle_btn_content.setFont(font)
        self.toggle_btn_content.setMinimumHeight(0)
        self.toggle_btn_content.setMaximumHeight(0)
        self.toggle_btn_content.setWidgetResizable(True)
        self.toggle_btn_content.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.toggle_btn_content.setFrameShape(QFrame.Shape.NoFrame)

        # 给 toggle_btn 和 toggle_btn_content 增加垂直布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.toggle_btn)
        layout.addWidget(self.toggle_btn_content)
        # layout.addStretch()
        self.setLayout(layout)

        # 定义动画
        self.toggle_animation = QParallelAnimationGroup(self)
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self.toggle_btn_content, b"maximumHeight")
        )

    @Slot(bool)
    def on_toggle_btn_toggled(self, checked):
        self.toggle_btn.setArrowType(
            Qt.ArrowType.DownArrow if checked else Qt.ArrowType.RightArrow
        )

        self.toggle_animation.setDirection(
            QAbstractAnimation.Direction.Forward if checked else QAbstractAnimation.Direction.Backward
        )
        self.toggle_animation.start()
        

    def set_content_layout(self, layout):
        self.toggle_btn_content.setLayout(layout)
        self.toggle_btn_content.adjustSize()

        collapsed_height = (
            self.sizeHint().height() - self.toggle_btn_content.maximumHeight()
        )
        content_height = layout.count() * layout.spacing() + self.toggle_btn_content.sizeHint().height()

        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)  # animation 是一个 QPropertyAnimation 对象
            animation.setDuration(200)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(200)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)
