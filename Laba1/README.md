# Звіт до першої лабораторної
## Тема: перша програма на мові *Python*

### Виконання роботи
- Результати виконання завдання:
    1. Виконали першу програму, результат виконання: ![alt](img1.png);
    1. Модифікували програму та використали [Python Notebook для її виконання](lab1.ipynb);
    
    
    
    1. Програма вивела значення
    1. Отримано наступні результати: 
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
Андрій почав програмувати 08.12.2024 12:47:30.
Львів — чудове місто для роботи та натхнення!
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*

    5. Навчились прості програми на мові Python



___


```Python
from datetime import datetime

# Змінні з інформацією
name = "Андрій"
location = "Львів"
activity = "програмувати"

# Отримуємо поточний час у форматі "день.місяць.рік години:хвилини"
current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# Вивід інформації
print(f"""{">*<"*20}
{name} почав {activity} {current_time}. 
{location} — чудове місто для роботи та натхнення!
{"<*>"*20}""")



```