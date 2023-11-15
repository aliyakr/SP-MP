def unique_values_copy(input_channel, output_channel):
    unique_values = set()

    for message in input_channel:
        if message == ":reset":
            unique_values.clear()
        else:
            if message not in unique_values:
                unique_values.add(message)
                output_channel.append(message)

# Пример использования:
input_channel = ["a", "b", "c", "a", "d", ":reset", "b", "e", "c"]
output_channel = []

unique_values_copy(input_channel, output_channel)

print("Входной канал:", input_channel)
print("Выходной канал с уникальными значениями:", output_channel)
