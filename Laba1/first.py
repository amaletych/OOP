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
