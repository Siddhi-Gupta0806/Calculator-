# Calculator Expression Evaluation 
e = input("Expr: ")
n, o, x = [], [], ""
for i in e:
    if i in "+-*/":
        n.append(float(x))
        o.append(i)
        x = ""
    else:
        x += i
n.append(float(x))

i = 0
while i < len(o):
    if o[i] == '*':
        n[i] = n[i] * n[i + 1]
        n.pop(i + 1)
        o.pop(i)
    elif o[i] == '/':
        n[i] = n[i] / n[i + 1]
        n.pop(i + 1)
        o.pop(i)
    else:
        i += 1

i = 0
while i < len(o):
    if o[i] == '+':
        n[i] = n[i] + n[i + 1]
        n.pop(i + 1)
        o.pop(i)
    elif o[i] == '-':
        n[i] = n[i] - n[i + 1]
        n.pop(i + 1)
        o.pop(i)

print("Result:", n[0])
