from PySide6.QtWidgets import QWidget
from observer import Observer


class ObserverQWidget(type(Observer), type(QWidget)):
    pass
