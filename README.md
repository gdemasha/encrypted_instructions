# Шифрованные инструкции
Алгоритм для решения поставленной задачи. 

## Описание задачи 
Марсоход получает с Земли сокращённые инструкции с заданиями. Из-за ограничений канала связи инструкции отправляются в сжатом виде. Например, если марсоходу нужно сделать 10 снимков подряд, инструкция будет выглядеть как 10[с].
Число перед квадратными скобками обозначает, сколько раз надо повторить последовательность внутри скобок. Скобки могут быть и вложенными: 2[ш3[с]]10[с].
Таким образом, командный центр на Земле может отправить марсоходу сжатую строку инструкций, а марсоход получит и расшифрует её в полную последовательность команд.
Команды могут обозначаться символами латиницы или кириллицы.
Задача: написать программу, которая расшифровывает сжатые сообщения и возвращает строку с командами.
