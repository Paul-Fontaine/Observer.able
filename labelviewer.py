from observerwidget import ObserverQWidget, Observer, QWidget
from PySide6.QtWidgets import QLabel
from temperature import Temperature


class LabelViewer(Observer, QWidget, metaclass=ObserverQWidget):
    def __init__(self, t: Temperature, parent: QWidget):
        Observer.__init__(self)
        QWidget.__init__(self, parent=parent)
        self.__temperature: Temperature = t
        self.__temperature.add_observer(self)
        self.__label: QLabel = QLabel(str(t.get_value()), self)

    def update(self):
        self.__label.setText(str(self.__temperature.get_value()))
