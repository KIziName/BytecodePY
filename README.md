# 🔍 disassemble-Py

Простой консольный инструмент для просмотра байт-кода Python.  

Он компилирует указанный `.py`-файл и показывает, во что Python превращает ваш код перед выполнением.

---

## 📦 Что это?

`disassemble-py` – это лёгкая обёртка над встроенным модулем `dis`. Она помогает:
- понять, как работает интерпретатор CPython;
- находить «горячие» места в коде;
- отлаживать неочевидное поведение;
- изучать байт-код для самообразования.

---

## 🚀 Установка

Перенесите скрипт в любую папку:

1-запустите

2-напишите названия `.py`

3-готовый байт-код

## Требования
- Python 3.6 и выше

## Прммер кода (исходник + байт-код)
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))


  1           0 LOAD_CONST               0 (<code object greet at 0x...>)
              2 LOAD_CONST               1 ('greet')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (greet)

  4           8 LOAD_NAME                1 (print)
             10 LOAD_NAME                0 (greet)
             12 LOAD_CONST               2 ('World')
             14 CALL_FUNCTION            1
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               3 (None)
             22 RETURN_VALUE
===== End of bytecode =====

