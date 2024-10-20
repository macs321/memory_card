from random import choice, shuffle
from PyQt6.QtWidgets import QApplication



app = QApplication([])


from main_window import *
from menu_window import *
class Question():
    def __init__(self, question_text, answer_text, wrong:tuple) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong_answer = wrong
        
    def got_right(self):
        ...
    def got_wrong(self):
        ...

q1 = Question("Ярік", "jarik", ("appolon 11", "cigan", "rak"))
q2 = Question("Сердючка", "man",("women", "fig zna", "dima"))
q3 = Question("коли діма піде на тренування", "when  will he wont to go",("never", "after 15 years" ,"I dont know"))
q4 = Question("коли я получу 12", "коли нормалбно вивчу тему",("коли будуть нормальні вчителі", "коли діма підe на тренування", "коли перестану тупити і втикати в дошку"))

question_list = [q1, q2, q3, q4]
radio_button_list = [rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4]


def new_question():
    global random_question
    random_question =choice(question_list)


    shuffle(radio_button_list)

    question_lb.setText(random_question.question_text)

    radio_button_list[0].setText(random_question.answer_text)
    for i in  range(3):
      radio_button_list[i + 1].setText(random_question.wrong_answer[i])

 

new_question()

def check_result():

    correct_unswer_lb.setText(random_question.answer_text)
    radio_button_group.setExclusive(False)


    for btn in radio_button_list:
        if btn.isChecked():
            btn.setChecked(False)
            if btn.text() == random_question.answer_text:
                resoult_lb.setText("Правильно Молодець")
                break
    else:
        resoult_lb.setText("Не правильно, не ростраюйся")

    radio_button_group.setExclusive(True)


def chandge_box():
    if button_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        button_next.setText("Наступне питання")
        check_result()
    elif button_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        button_next.setText("Відповісти")

        new_question()


def open_menu():
    window.hide()
    menu_window.show()
def close_menu():
    window.show()
    menu_window.hide()

menu_btn.clicked.connect(open_menu)
menu_back_btn.clicked.connect(close_menu)



button_next.clicked.connect(chandge_box)

def clear_menu():
    menu_answer_text_input.clear()
    menu_question_text_input.clear()
    menu_wrong_1_input.clear()
    menu_wrong_2_input.clear()
    menu_wrong_3_input.clear()
    
menu_btn_clear.clicked.connect(clear_menu)

def add_question():
    new_q = Question(
        menu_question_text_input.text(),
        menu_answer_text_input.text(),
        (
            menu_wrong_1_input.text(),
            menu_wrong_2_input.text(),
            menu_wrong_3_input.text(),
            

        )
    )
    question_list.append(new_q)
    close_menu()
    clear_menu()

menu_btn_add.clicked.connect(add_question)



window.show()
app.exec()



