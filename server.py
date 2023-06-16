import socket

# Класс s - место для обмена данными. IP-протокол 6 версии. Протокол TCP
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 8888))   # Резерв порта и всех адресов на локальном компьютере
s.listen(5)     # 'Очередь' для подключенных клиентов (макс - 5)

# Прием подключения и данные
client, addr = s.accept()