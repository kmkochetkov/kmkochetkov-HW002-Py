# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
#
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

indexes = [2, 2, 3, 1, 8]
numbers = []
number = int(input("Введите число\n"))

#Заполнение списка из  из (2*N+1) элементов
for num in range((-1*number),(number+1)):
    numbers.append(num)
# Проверка вхождение индекса из списка индексов в диапазон из индексов (2*N+1) начальных элементов
for i in range(len(indexes)):
    if (indexes[i]) > (number*2+1):
        print('Координаты в списке индексов больше введённого диапазона')
        break
mult = 1
for i in range(len(indexes)):
    mult  = mult*numbers[indexes[i]]
print ('Произведение элементов из указанного списка индексов:',mult)