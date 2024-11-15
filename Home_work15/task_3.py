class Tv:
    channel = ['BBC', 'Discovery', 'FOX', 'World of CINEMA', 'HBO'] # Создаем список,атрибут класса
    current_index = 0 # Устанавливаем текущий канал как первый (индекс 0).

    def first_channel (self):
       self.current_index = 0   # Метод Переключаем текущий канал на первый (индекс 0).
       return self.channel [self.current_index]

    def last_channel (self):
        self.current_index = len(self.channel) -1  # Метод.Последний канал то есть равен длинне списка - с конца
        return self.channel [self.current_index]

    def turn_channel(self, n):
        if n >= 1:
            if n<= len(self.channel):  # Переключение каналов и проверка есть канал или нет.
                self.current_index = n - 1
                return self.channel[self.current_index]
            else:
                return 'There is no such channel!'
        else:
            return 'There is no such channel!'

    def next_channel (self):
        self.current_index = (self.current_index + 1) % len(self.channel) # Переключаем на следующий канал. Если последний, то возвращаемся на первый
        return self.channel[self.current_index]

    def previous_channel (self):
        self.current_index = (self.current_index - 1) % len(self.channel) #Переключаем на предыдущий канал. Если первый, то переключаем на последний.
        return self.channel [self.current_index]

    def current_channel (self):
        return self.channel [self.current_index] # Текущий канал.Выводит его название и номер.

    def exists(self , n_or_name):
        if isinstance(n_or_name , int):   # Проверяет, является ли n_or_name числом
            if n_or_name >=1 and n_or_name <= len(self.channel): # Проверяет, находится ли число в диапазоне от 1 до длины списка каналов
                return  'Yes'
            else:
                return 'No'
        elif isinstance(n_or_name , str):  # Проверяет, является ли n_or_name строкой
            if n_or_name in self.channel:  # Проверяет, есть ли строка (название канала) в списке каналов
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'



# Создаем объект класса Tv
tv = Tv()

# Проверяем метод first_channel() и т.д.
print(tv.first_channel()) 


"""
Разбор оператора %. -  self.current_index = (self.current_index + 1) % len(self.channel) 

Оператор % используется для деления по остатку. В контексте он помогает нам "зациклить" индекс, 
чтобы при достижении конца списка мы снова начинали с начала.

Представь себе список каналов длиной 5:

channels = ['BBC', 'Discovery', 'CNN', 'MTV', 'HBO']
И текущий индекс, который указывает на канал, который сейчас включен.

Теперь представим, что текущий индекс находится на последнем канале (индекс 4 для 'HBO') 
и мы хотим переключиться на следующий канал:

current_index = 4  # 'HBO'
current_index = (current_index + 1) % len(channels)
Что здесь происходит:

current_index + 1 увеличивает текущий индекс до 5.

len(channels) возвращает 5, так как длина списка каналов - 5.

(current_index + 1) % len(channels) делит 5 на 5 и возвращает остаток, который равен 0.

Таким образом, при достижении конца списка, current_index "зацикливается" обратно на 0, 
что соответствует первому каналу 'BBC'.

Если бы текущий индекс был, скажем, 2:

current_index = 2  # 'CNN'
current_index = (current_index + 1) % len(channels)  # это будет 3
Тогда следующий канал будет с индексом 3 ('MTV').
"""