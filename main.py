# 1.

def function_1(a: int, b: int, c: int):
    print(f"Сумма: {a + b + c}")
    print(f"Произведение: {a*b*c}")
    print(f"Наибольшее число: {max(a,b,c)}")
    print(f"Наибольшее число: {min(a,b,c)}")
function_1(1,2,3)

# 2.

def function_2(a: str):
    b = a.split(" ")
    print(f"Количество слов в строке: {len(b)}")
    p=[]
    for i in b:
        if len(i) > 2:
            p.append(i)
    print(f"Количество слов, в которых больше 2-ух символов: {len(p)}")
    print(f"нижний регистр: {a.lower()}")
    print(f"ВЕРХНИЙ РЕГИСТР: {a.upper()}")
function_2("В этой строке 5 слов.")

# 3.

list_numbers = [1,30,30,25,24,30,1,27,25,40]
unique = list(set(list_numbers))
print(unique)
list_numbers_2 = []
for num in unique:
    if num > 24:
        list_numbers_2.append(num)
print(list_numbers_2)
new_dict = dict()
h=[]
for k in list_numbers_2:
    if k % 2 == 0:
        h.append(k)
print(h)
for i in h:
        new_dict[i] = i
print(new_dict)

# 4.

def meters(cm: int):
    m = cm / 100
    print(m)
meters(300)

# 5.
def my_func(time: int):
    hour = int(time / 60)
    minute = int(((time / 60) - hour) * 60)
    print(f"{hour} час", f"{minute} минут")
my_func(90)

# 6.

def function_6(a: int):
    if a < 100:
        print("Введите трёхзначное число!")
    elif a < 0:
        print("Число должно быть положительным!")
    elif a > 999:
        print("Введите трёхзначное число!")
    else:
        b = list(str(a))
        print(int(b[0]) + int(b[1]) + int(b[2]))
        print(int(b[0]) * int(b[1]) * int(b[2]))
function_6(132)

# 7.

def inside_range(x: int, a: int, b: int):
    if x in range(a, b):
        print("Число x принадлежит промежутку от a до b")
    else:
        print("Число x НЕ принадлежит промежутку от a до b")
inside_range(10, 5, 11)
inside_range(1, 5, 11)

# 8.

# 9.
# name = input("Введите ФИО: ")
# age = input("Введите возраст: ")
# phone = input("Введите телефон: ")
# def function_9():
#     if age not in range(1, 150):
#         age = 0
#     if len(phone) not in range(4, 11):
#         phone =  8-000-000-00-00



# 10.

string_10 = "Python is the best programming language"
print(len(string_10))
print(string_10[0])
print(string_10[-1])
a = string_10.split(" ")
print(a[0])
print(a[-1])
print(a[4: 5: 1])

# 11.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(operation, a, b):
    print(operation(a,b))

calculator(add,56,2)
calculator(subtract, 40, 20)
calculator(multiply, 3, 5)
calculator(divide, 10, 5)
