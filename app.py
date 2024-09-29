from PyQt6.QtWidgets import QApplication



app = QApplication([])


from main_window import *


def chandge_box():
    if button_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        button_next.setText("Наступне питання")
    elif button_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        button_next.setText("Відповісти")


button_next.clicked.connect(chandge_box)

window.show()
app.exec()

