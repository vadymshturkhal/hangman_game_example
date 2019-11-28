"""
Завести класс, отвечающий за логику игры, который:
+ позволяет настраивать кол-во позволенных ошибок (API принимает соответствующий параметр)
+ позволяет клиентскому коду запрашивать генерацию слова
+ позволяет клиентскому коду передавать в логику догадку игрока (передача буквы)

позволяет клиентскому коду запрашивать:
+ кол-во оставшихся попыток
+ строку показывающую какие буквы открыты, а какие скрыты (если буква скрыта вместо неё ставим подчёркивание или дефис),
    т.е., по сути, текущее состояние игры
+ отсортированные буквы, которые игрок уже называл (вводил)

+ Уведомляет о поражении
+ Уведомляет о победе
"""

import random


class PartsOfHangman:
    def __init__(self, file):
        self.file = file

    def count_words_in_file(self):
        with open(self.file, 'r') as file:
            return sum(1 for line in file)

    @staticmethod
    def chose_word(all_words: int) -> int:
        return random.randint(1, all_words)

    def guess_word(self, choice):
        with open(self.file, 'r') as file:
            for i in range(choice):
                guess_word = file.readline().split()[0]
            return guess_word

    @staticmethod
    def implicit_word(word: str) -> str:
        symbol_for_use = '-'
        tmp = ''
        for _ in word:
            tmp += symbol_for_use
        return tmp


class LogicHangman:
    def __init__(self, mistakes, guess_word, tries):
        self.__mistakes = mistakes
        self.__guess_word = guess_word
        self.__tries = tries
        self.__entered_chars = list()

    @property
    def show_mistakes(self):
        return self.__mistakes

    @property
    def progress(self) -> str:
        return self.__tries

    @staticmethod
    def check(another_try: str, guess_word: str, impl: str) -> str:
        tmp = ''
        for i in range(len(guess_word)):
            if another_try == guess_word[i]:
                tmp += another_try
            else:
                tmp += impl[i]
        return tmp

    def main_circle(self):
        word = '\tWhat would you like to do now?:'
        a = '1 - show mistakes;'
        b = '2 - check status of a game;'
        c = '3 - show entered chars;'
        d = '4 - enter char;'
        e = '5 - exit.'
        while True:
            print(word, a, b, c, d, e, sep='\n')
            result = input()
            if result.isdigit():
                result = int(result)
                if result == 1:
                    print(f'You have {self.show_mistakes} mistakes.')
                elif result == 2:
                    print(f'You have {self.progress} word')
                elif result == 3:
                    print(f'You entered {self.__entered_chars} char(\'s)')
                elif result == 4:
                    another_try = input('OK. Now, please enter the char: ')
                    if len(another_try) != 1:
                        print('Oops, your char is too long')
                    else:
                        self.__entered_chars.append(another_try)
                        tmp = self.__tries
                        self.__tries = self.check(another_try, self.__guess_word, self.__tries)
                        if self.__tries == tmp:
                            if self.__mistakes == 0:
                                print('\n\t\t\tGame over. Sorry, you lose!')
                                print(f'The word was {self.__guess_word}')
                                break
                            else:
                                self.__mistakes -= 1
                                print('Ops, mistake :)')
                        elif self.__tries == self.__guess_word:
                            print(f'Congratulations. You win. The word was {self.__guess_word}')
                            break
                        else:
                            print('OK. Saved it.')
                elif result == 5:
                    print('OK. Thanks for the game. Hope to see you later. Bye.')
                    break

            else:
                print(f'You have {self.progress} word')
            print()


def push_hangman():
    # Block for initialize class Hangman
    path = r'/home/vshturkhal/PycharmProjects/eco/WordsStockRus.txt'
    miss = mistakes_for_hangman()
    example_hangman = PartsOfHangman(path)

    # Block for guess word
    count_of_words = example_hangman.count_words_in_file()
    target_word_or_line = example_hangman.chose_word(count_of_words)
    guess = example_hangman.guess_word(target_word_or_line)
    implicit_guess = example_hangman.implicit_word(guess)

    logic_hangman = LogicHangman(mistakes=miss, guess_word=guess, tries=implicit_guess)
    logic_hangman.main_circle()


def mistakes_for_hangman() -> int:
    misses = input('Please enter count of mistakes or nothing (default = 5): ')
    misses = int(misses) if misses.isdigit() else 5
    return misses


if __name__ == '__main__':
    push_hangman()
