from queue import Queue
import threading

def unique_values_copy(input_queue, output_queue):
    unique_values = set()

    while True:
        message = input_queue.get()  # Получаем значение из входной очереди

        if message.lower() == ":reset":
            unique_values.clear()
        else:
            if message not in unique_values:
                unique_values.add(message)
                output_queue.put(message)  # Добавляем уникальное значение в выходную очередь
                
        print("Уникальные значения:", unique_values)

# Пример использования с использованием потоков
input_queue = Queue()
output_queue = Queue()

# Запускаем функцию unique_values_copy в отдельном потоке
thread = threading.Thread(target=unique_values_copy, args=(input_queue, output_queue))
thread.start()

# Ввод данных с клавиатуры и добавление во входную очередь
while True:
    user_input = input("Введите значение или :reset для сброса: ")
    input_queue.put(user_input)