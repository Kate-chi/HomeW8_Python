# Вычислить значение выражения

# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4

# Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3

# Уровень 4 * (дополнительная задача, сдавать не обязательно)
# Действия разделяются скобками
# (12 - 4) * 2

def calc(a, b, ch):
    match ch:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b

problem = input('Введите выражение, разделяя каждый элемент пробелом: ')

separate_problem = problem.split()

first_prioriti = '/*'
second_prioriti = '+-'

correct_que = []
stack = [problem[1]]

for i in range(len(separate_problem)):
    if separate_problem[i].isdigit():
        correct_que.append(separate_problem[i])

    elif separate_problem[i] in second_prioriti: 
        while stack[-1] in second_prioriti or stack[-1] in first_prioriti:
            correct_que.append(stack[-1])
            stack.pop()    
        stack.append(separate_problem[i])

    elif separate_problem[i] in first_prioriti:
        if stack[-1] in first_prioriti:
            correct_que.append(stack[-1])
            stack.pop()
        stack.append(separate_problem[i])

    elif separate_problem[i] == '(':
        stack.append(separate_problem[i])

    elif separate_problem[i] == ')':
        correct_que.append(stack[-1])
        while stack[-1] != '(':
            stack.pop()
        stack.pop()       
        
stack.reverse()
stack.pop()

correct_que += stack
result_list = []

for i in range(len(correct_que)):
    
    if correct_que[i] in '+-*/':
        if (float(result_list[-1])) == 0:
            result_list[0] = 1
            break
        else:
            b = float(result_list.pop())
            a = float(result_list.pop())
            result_list.append(calc(a, b, correct_que[i]))
    else:
        result_list.append(correct_que[i])
   
if type (result_list[0]) == float:
    print(f'Ответ = {result_list[0]} ^_^')
else:
    print('На ноль делить нельзя! >_<')

