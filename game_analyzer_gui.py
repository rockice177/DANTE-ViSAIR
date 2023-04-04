import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QPlainTextEdit, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Analyzer")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Header
        header = QLabel("Game Analyzer")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(header)

        # Tabs
        tab_widget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab_widget.addTab(tab1, "Dashboard")
        tab_widget.addTab(tab2, "Settings")
        tab_widget.addTab(tab3, "About")
        main_layout.addWidget(tab_widget)

        # Dashboard Tab
        vbox1 = QVBoxLayout()
        start_button = QPushButton("Start")
        vbox1.addWidget(start_button)
        pause_button = QPushButton("Pause")
        vbox1.addWidget(pause_button)
        stop_button = QPushButton("Stop")
        vbox1.addWidget(stop_button)
        debug_button = QPushButton("Toggle Debug")
        vbox1.addWidget(debug_button)
        tab1.setLayout(vbox1)

        # Settings Tab
        vbox2 = QVBoxLayout()
        settings_label = QLabel("Settings")
        vbox2.addWidget(settings_label)
        settings_area = QPlainTextEdit()
        vbox2.addWidget(settings_area)
        tab2.setLayout(vbox2)

        # About Tab
        vbox3 = QVBoxLayout()
        about_label = QLabel("About Game Analyzer")
        vbox3.addWidget(about_label)
        tab3.setLayout(vbox3)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open('adrenalin_style.css', 'r') as file:
        css = file.read()
        app.setStyleSheet(css)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

