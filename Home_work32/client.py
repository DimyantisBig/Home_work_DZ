import socket

SERVER_IP = "127.0.0.1"  # IP-адрес сервера
SERVER_PORT = 8008       # Порт сервера

# Создаем UDP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Привет от клиента UDP!" # сообщение для отправки

# Кодируем сообщение в байты
message_bytes = message.encode()

# Отправляем сообщение серверу
client_socket.sendto(message_bytes, (SERVER_IP, SERVER_PORT))

# Получаем ответ от сервера
data, address = client_socket.recvfrom(1024)

# Декодируем полученные данные
received_message = data.decode()
print(f"Получен ответ от сервера: {received_message}")

client_socket.close() # закрытие сокета