import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class ClientGUI(QWidget):

    def __init__(self):
        super(ClientGUI, self).__init__()
        self.init_ui()

    def init_ui(self):
        connect_button = QPushButton('Connect', self)
        run_button = QPushButton('Run', self)
        status_label = QLabel('Status:')
        status_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(connect_button)
        layout.addWidget(run_button)
        layout.addWidget(status_label)
        self.setLayout(layout)
        self.resize(400, 300)
        self.setWindowTitle('Client')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cg = ClientGUI()
    sys.exit(app.exec_())
