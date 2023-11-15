def unique_values_copy(input_channel, output_channel):
    unique_values = set()

    while True:
        message = input("Введите значения или :reset для сброса: ")
        split_values = message.split()
        for value in split_values:
            if value.lower() == ":reset":
                unique_values.clear()
            else:
                if value not in unique_values:
                    unique_values.add(value)
                    output_channel.append(value)
                
        print("Выходной канал с уникальными значениями:", output_channel)

# Пример использования:
input_channel = []
output_channel = []

unique_values_copy(input_channel, output_channel)