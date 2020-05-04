Практическая работа №6
=========
Реализовать код программы
---------
Задание 1: задача стабилизации перевёрнутого маятника.
---------
Для решения это задачи был взят код из официальной страницы open ai gym открытый код который изначально был запущен с начальными параметрами рандомного движеяния платформы при наклоне маятника.
Перевёрнутый маятник является классической проблемой динамики и теории управления и широко используется в качестве эталона для тестирования алгоритмов управления (ПИД-регуляторов, нейронных сетей, нечёткого управления и т. д.).
Проблема обратного маятника связана с наведением ракет, так как двигатель ракеты расположен ниже центра тяжести, вызывая нестабильность. Эта же проблема решена, например, в сегвее, самобалансирующемся транспортном устройстве.
Другим способом стабилизации обратного маятника является быстрое колебание основания в вертикальной плоскости. В этом случае можно обойтись без обратной связи. Если колебания достаточно сильные (в смысле величины ускорения и амплитуды), то обратный маятник может стабилизироваться. Если движущаяся точка колеблется в соответствии с простыми гармоническими колебаниями, то движение маятника описывается функцией Матьё.
---------
![alt text](https://raw.githubusercontent.com/AisvaldZeld/6/master/1-6.jpg)
---------
В итоге проведенной лабораторной работы было создано 1 программа, которая работает по заданному условию.
