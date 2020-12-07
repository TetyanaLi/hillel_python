katet_a = float(input('Введите длину:'))
katet_b = float(input('Введите ширину:'))
if katet_a != katet_b:
     s = katet_a * katet_b * 0.5
elif katet_a == katet_b:
     s = katet_a ** 2
print((s))
#вопрос - как ограничить знаки после запятой в вещественном числе?