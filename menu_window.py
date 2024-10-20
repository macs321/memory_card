from PyQt6.QtWidgets import (QWidget, QLabel,
                             QRadioButton,QPushButton,
                             QGroupBox,QButtonGroup,
                              QVBoxLayout, QHBoxLayout,
                              QLineEdit )

menu_window = QWidget()


menu_v_line = QVBoxLayout()

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_question_text_lb = QLabel("ВВедіть текст питання:")
menu_question_text_input = QLineEdit()

menu_h_line_1.addWidget(menu_question_text_lb)
menu_h_line_1.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_1)

menu_answer_text_lb = QLabel("Введіть текст відповіді")
menu_answer_text_input = QLineEdit()
menu_h_line_2.addWidget(menu_answer_text_lb)
menu_h_line_2.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_2)
menu_wrong_1_lb = QLabel("Введіть текст неправильного варіанту")
menu_wrong_1_input = QLineEdit()
menu_h_line_3.addWidget(menu_wrong_1_lb)
menu_h_line_3.addWidget(menu_wrong_1_input)
menu_v_line.addLayout(menu_h_line_3)

menu_wrong_2_lb = QLabel("Введіть текст неправильного варіанту")
menu_wrong_2_input = QLineEdit()
menu_h_line_4.addWidget(menu_wrong_2_lb)
menu_h_line_4.addWidget(menu_wrong_2_input)
menu_v_line.addLayout(menu_h_line_4)

menu_wrong_3_lb = QLabel("Введіть текст неправильного варіанту")
menu_wrong_3_input = QLineEdit()
menu_h_line_5.addWidget(menu_wrong_3_lb)
menu_h_line_5.addWidget(menu_wrong_3_input)
menu_v_line.addLayout(menu_h_line_5)
menu_btn_add = QPushButton("Додати питання")
menu_btn_clear = QPushButton("Очистити")
menu_h_line_6.addWidget(menu_btn_add)
menu_h_line_6.addWidget(menu_btn_clear)
menu_v_line.addLayout(menu_h_line_6)


menu_back_btn = QPushButton("Назад")
menu_v_line.addWidget(menu_back_btn)



menu_window.setLayout(menu_v_line)