import inspect
import colorama

colorama.init()

print("Назва модуля -->", colorama.__name__)
print("Чи є colorama модулем:", inspect.ismodule(colorama))

print("\n--- Перевірка наявності атрибутів (hasattr) ---")
print("Має Fore:", hasattr(colorama, 'Fore'))
print("Має Back:", hasattr(colorama, 'Back'))
print("Має Style:", hasattr(colorama, 'Style'))
print("Має init:", hasattr(colorama, 'init'))

print("\n--- Отримання атрибутів (getattr) ---")
print("Атрибут Fore:", getattr(colorama, 'Fore'))
print("Атрибут Style:", getattr(colorama, 'Style'))

print("\n--- Перевірка callable та inspect ---")
print("Чи можна викликати init():", callable(colorama.init))
print("Чи є Fore класом:", inspect.isclass(colorama.Fore))
print("Чи є init функцією:", inspect.isfunction(colorama.init))

print("\n--- Усі елементи colorama (через dir) ---")
for i in dir(colorama):
    print(i)