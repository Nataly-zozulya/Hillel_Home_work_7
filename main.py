
# створити список з 12 елементів
lst = [10,20,30,40,50,60,70,80,90,100,110,120]

# добавити в середину списку новий елемент зі значенням 56,середина має обчислюватися автоматично
lst.insert(6,56)

# обновити 2й елемент до 25
lst[1] = 25

# додати в кінець списку 88
lst.append(88)

# видалити перший елемент списку
del lst[0]

# видалити остатній елемент списку і вивести в консоль його значення (для будь якої довжини списка)
print(lst.pop(12))

# знайти довжину кола і його площу якщо у вас відомий радіус кола. с = 2 * pi * r, s = pi * r ^ 2. Радіус задаєте в коді r = <something>, r - це змінна.
r = 20
import math
c = 2*r*math.pi
print(c)
s = math.pi*(r)**2
print(s)