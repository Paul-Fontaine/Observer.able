import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from temperature import Temperature
from sliderview import SliderViewer
from labelviewer import LabelViewer


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        vlayout: QVBoxLayout = QVBoxLayout

        self.__temperature: Temperature = Temperature(50)
        self.__label_viewer: LabelViewer = LabelViewer(self.__temperature, parent=self)
        self.__slider_viewer: SliderViewer = SliderViewer(self.__temperature, parent=self)

        vlayout.addWidget(self.__label_viewer)
        vlayout.addWidget(self.__slider_viewer)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
