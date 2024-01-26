from PySide6.QtCore import Qt

from observerwidget import ObserverQWidget, Observer, QWidget
from PySide6.QtWidgets import QLabel, QSlider
from temperature import Temperature


class SliderViewer(ObserverQWidget):
    def __init__(self, t: Temperature, parent: QWidget):
        Observer.__init__(self)
        QWidget.__init__(self, parent=parent)
        self.__temperature: Temperature = t
        self.__temperature.add_observer(self)
        self.__slider: QSlider = QSlider(Qt.Horizontal, self)
        self.__slider.setRange(0, 100)
        self.__slider.valueChanged.connect(self.change_value)

    def change_value(self):
        self.__temperature.set_value(self.__slider.value())
        self.__temperature.notify_observers()

    def update(self):
        self.__slider.setValue(self.__temperature.get_value())
