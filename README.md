# hangman_game_example_rus
 
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
