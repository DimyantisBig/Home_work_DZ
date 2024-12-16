import socket

# Задаем адрес и порт сервера
SERVER_IP = "127.0.0.1"  # Локальный адрес (localhost)
SERVER_PORT = 8008       # Порт сервера

# Создаем UDP сокет
# socket.AF_INET: Используем IPv4
# socket.SOCK_DGRAM: Используем UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к адресу и порту
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Сервер UDP запущен на {SERVER_IP}:{SERVER_PORT}")
# Создаем бесконечный цикл
while True:
    # Получаем данные от клиента
    # Размер буфера 1024 bytes
    data, address = server_socket.recvfrom(1024)  # recvfrom() возвращает данные и адрес клиента

    # Декодируем полученные данные из байтов в строку
    message = data.decode()
    print(f"Получено сообщение '{message}' от {address}")

    # Отправляем ответ клиенту (эхо)
    server_socket.sendto(data, address) # sendto() отправляет данные по указанному адресу

"""
Не совсем ясно что и как.
Требуется повтор и разяснение!
"""
"""
Подробный разбор файла -> G:\Мой диск\Обучение\Beetroot Academy\Информация
"""