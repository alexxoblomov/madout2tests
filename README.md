Фреймворк для облегчения тяжелой жизни QA в MadoutGames. Продуктового кода нет, поэтому репос открыт.

По структуре проекта:

- templates - общее хранилище шаблонов элементов интерфейса для библиотеки OpenCV
- clans - хранилище шаблонов конкретно по кланам
- templates.py - класс с хранящимися ссылками в переменных
- madout_apk - хранилище apk и конфига для них apk_path.py
***
- device_config.py - конфиг, где задаются параметры устройства для appium сервера
- basic.py - базовые функции, в данном случае проверки на наличие элемента на экране
- buttons.py - разбитые по классам элементы интерфейса и их координаты для разных девайсов
- conftest.py - фикстуры, стандартные для библиотеки pyTest
- test_madout.py - тестовая функция, где сами тесты
***
- utils.py - вспомогательные функции, функция-скриншот и функция-сравнение скриншота и шаблона
- screenshots - хранилище скриншотов, которые делают функции из utils.py


