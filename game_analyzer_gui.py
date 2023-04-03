from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        top_layout = QVBoxLayout()
        status_label = QLabel('Status: Idle')
        top_layout.addWidget(status_label)

        bottom_layout = QHBoxLayout()
        start_button = QPushButton('Start')
        start_button.clicked.connect(self.start_clicked)
        bottom_layout.addWidget(start_button)

        stop_button = QPushButton('Stop')
        stop_button.clicked.connect(self.stop_clicked)
        bottom_layout.addWidget(stop_button)

        pause_button = QPushButton('Pause')
        pause_button.clicked.connect(self.pause_clicked)
        bottom_layout.addWidget(pause_button)

        debug_button = QPushButton('Debug')
        debug_button.clicked.connect(self.debug_clicked)
        bottom_layout.addWidget(debug_button)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def start_clicked(self):
        print("Start button clicked")

    def stop_clicked(self):
        print("Stop button clicked")

    def pause_clicked(self):
        print("Pause button clicked")

    def debug_clicked(self):
        print("Debug button clicked")

if __name__ == '__main__':
    app = QApplication([])
    main_win = MainWindow()
    main_win.show()
    app.exec_()
