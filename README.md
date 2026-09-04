## 🔍 disassemble-Py

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

1. Запустите
2. Напишите названия `.py`
3. Готовый байт-код

## Требования
- **Python 3.6** и выше

## Прммер кода (исходник + байт-код)
``` python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```
----

```
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
```

## 🔍 disassemble-Py

A simple console tool for viewing Python bytecode.

It compiles a specified .py file and shows what Python turns your code into before execution.

---

## 📦 What is it?

disassemble-py is a lightweight wrapper around the built-in dis module. It helps you:

- understand how the CPython interpreter works;

- find "hot spots" in your code;

- debug unexpected behavior;

- study bytecode for self‑education.

---

## 🚀 Installation

Copy the script to any folder:

1. Run it.
2. Enter the name of the .py file.
3. Get the resulting bytecode.

## Requirements

- ***Python 3.6*** and above

## Example code (source + bytecode)
``` python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```
---

```
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
```
