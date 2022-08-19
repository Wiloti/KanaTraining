#!/usr/bin/python3

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer, Qt
import sys
import random

# create a dictionary of hiragana and katakana
kana_dict = {'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o', 'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko', 'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so', 'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to', 'な': 'na', 'に': 'ni', 'ぬ': 'nu',
             'ね': 'ne', 'の': 'no', 'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho', 'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo', 'や': 'ya', 'ゆ': 'yu', 'よ': 'yo', 'ら': 'ra', 'り': 'ri', '' 'る': 'ru', 'れ': 're', 'ろ': 'ro', 'わ': 'wa', 'を': 'wo', 'ん': 'n', 'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go', 'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo', 'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do', 'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo', 'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po', 'ア': 'A', 'イ': 'I', 'ウ': 'U', 'エ': 'E', 'オ': 'O', 'カ': 'KA', 'キ': 'KI', 'ク': 'KU', 'ケ': 'KE', 'コ': 'KO', 'サ': 'SA', 'シ': 'SHI', 'ス': 'SU', 'セ': 'SE', 'ソ': 'SO', 'タ': 'TA', 'チ': 'CHI', 'ツ': 'TSU', 'テ': 'TE', 'ト': 'TO', 'ナ': 'NA', 'ニ': 'NI', 'ヌ': 'NU', 'ネ': 'NE', 'ノ': 'NO', 'ハ': 'HA', 'ヒ': 'HI', 'フ': 'FU', 'ヘ': 'he', 'ホ': 'HO', 'マ': 'MA', 'ミ': 'MI', 'ム': 'MU', 'メ': 'ME', 'モ': 'MO',
             'ヤ': 'YA', 'ユ': 'YU', 'ヨ': 'YO', 'ラ': 'RA', 'リ': 'RI', 'ル': 'RU', 'レ': 'RE', 'ロ': 'RO', 'ワ': 'WA', 'ヲ': 'WO', 'ン': 'N', 'ガ': 'GA', 'ギ': 'GI', 'グ': 'GU', 'ゲ': 'GE', 'ゴ': 'GO', 'ザ': 'ZA', 'ジ': 'JI', 'ズ': 'ZU', 'ゼ': 'ZE', 'ゾ': 'ZO', 'ダ': 'DA', 'ヂ': 'JI', 'ヅ': 'ZU', 'デ': 'DE', 'ド': 'DO', 'バ': 'BA', 'ビ': 'BI', 'ブ': 'BU', 'ベ': 'be', 'ボ': 'BO', 'パ': 'PA', 'ピ': 'PI', 'プ': 'PU', 'ペ': 'PE', 'ポ': 'PO'}


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Correct = 0
        self.Wrong = 0
        # create our window
        self.setWindowTitle("Kana Training")
        self.setFixedSize(400, 800)
        self.setStyleSheet("background-color: #373748;")
        self.setWindowOpacity(0.9)
        # create a label which print kana
        self.kana = QLabel(self)
        self.kana.setFont(QFont("Arial", 150, QFont.Bold))
        self.kana.setStyleSheet("color: #ece8db;")
        self.kana.setGeometry(100, 150, 200, 250)
        self.kana.setText(random.choice(list(kana_dict.keys())))
        # create a label which print the score
        self.score = QLabel(self)
        self.score.setFont(QFont("Oswald", 25, QFont.Bold))
        self.score.setStyleSheet("color: #ece8db;")
        self.score.setGeometry(310, 10, 100, 50)
        self.score.setText("0/10")
        # create a qtlineedit which is the answer
        self.answer = QLineEdit(self)
        self.answer.setFont(QFont("Oswald", 25, QFont.Bold))
        self.answer.setStyleSheet("color: #ece8db;")
        self.answer.setGeometry(165, 500, 80, 60)
        self.answer.setAlignment(Qt.AlignCenter)
        # create a button which submit the text in answer
        self.submit = QPushButton(self)
        self.submit.setFont(QFont("Oswald", 25, QFont.Bold))
        self.submit.setStyleSheet("color: #ece8db;")
        self.submit.setGeometry(103, 600, 200, 50)
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.game)
        # create a label which print the correct answer
        self.correct = QLabel(self)
        self.correct.setFont(QFont("Oswald", 14, QFont.Bold))
        self.correct.setStyleSheet("color: #ece8db;")
        self.correct.setGeometry(125, 650, 200, 50)

    def win(self):
        popup = QMessageBox()
        popup.setWindowTitle("Congratulations")
        popup.setFont(QFont("Oswald", 12))
        popup.setFixedSize(300, 400)
        popup.setText(
            f"You win!\n{self.Correct} correct answers.\n{self.Wrong} wrong answers.")
        popup.setStyleSheet("color: #ece8db;" "background-color: #373748;")

        x = popup.exec()
        self.Correct = 0
        self.Wrong = 0
        self.score.setText(f"{self.Correct}/10")

    def game(self):
        # compare value of answer and kana
        if self.answer.text() == kana_dict[self.kana.text()]:
            if self.score.text() == "9/10":
                self.Correct += 1
                self.score.setText(
                    str(int(self.score.text().split("/")[0]) + 1) + "/10")
                self.win()
            else:
                # if score is not 5 / 5, then update the score and kana
                self.score.setText(
                    str(int(self.score.text().split("/")[0]) + 1) + "/10")
                self.Correct += 1
        else:
            # if the score is 0 / 5, stay at 0 / 5
            if self.score.text() != "0/10":
                self.score.setText(
                    str(int(self.score.text().split("/")[0]) - 1) + "/10")
                self.Wrong += 1
            # if answer is not correct, then update the score and kana
            else:
                self.Wrong += 1
        self.correct.setText("Correct Answer : " +
                             kana_dict.get(self.kana.text()))
        random_kana = random.choice(list(kana_dict.keys()))
        self.kana.setText(random_kana)
        self.answer.setMaxLength(len(kana_dict[self.kana.text()]))
        self.answer.setText("")
        self.answer.setFocus()


# run the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
