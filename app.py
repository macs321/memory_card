from random import choice, shuffle
from PyQt6.QtWidgets import QApplication



app = QApplication([])


from main_window import *

class Question():
    def __init__(self, question_text, answer_text, wrong:tuple) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong_answer = wrong
        
    def got_right(self):
        ...
    def got_wrong(self):
        ...

q1 = Question("Ярік", "jarik", ("appolon 11", "cigan", "lochara"))
q2 = Question("Сердючка", "man",("women", "fig zna", "dima"))
q3 = Question("коли діма піде на тренування", "when  will he wont to go",("never", "after 15 years" ,"I dont know"))
q4 = Question("коли я получу 12", "коли нормалбно вивчу тему",("коли будуть нормальні вчителі", "коли діма підe на тренування", "коли перестану тупити і втикати в дошку"))

question_list = [q1, q2, q3, q4]
radio_button_list = [rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4]


def new_question():
    random_question =choice(question_list)


    shuffle(radio_button_list)

    question_lb.setText(random_question.question_text)

    radio_button_list[0].setText(random_question.answer_text)
    for i in  range(3):
      radio_button_list[i + 1].setText(random_question.wrong_answer[i])

 

new_question()


def chandge_box():
    if button_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        button_next.setText("Наступне питання")
    elif button_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        button_next.setText("Відповісти")

        new_question()


button_next.clicked.connect(chandge_box)

window.show()
app.exec()

