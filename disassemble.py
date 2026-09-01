import sys
import dis
import os

def show_bytecode(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"❌ File '{filepath}' not found.")
        return
    except Exception as e:
        print(f"❌ Read error: {e}")
        return

    if not source.strip():
        print(f"⚠️ File '{filepath}' is empty or contains only whitespace. No bytecode.")
        return

    try:
        code_obj = compile(source, filepath, 'exec')
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        return
    except Exception as e:
        print(f"❌ Compilation error: {e}")
        return

    print(f"\n===== Bytecode for {filepath} (Python {sys.version.split()[0]}) =====")
    dis.dis(code_obj)
    print("===== End of bytecode =====\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        show_bytecode(sys.argv[1])
    else:
        print("Current directory:", os.getcwd())
        print("Enter .py filenames to show bytecode (empty line to exit).")
        while True:
            filename = input("Enter .py filename: ").strip()
            if not filename:
                print("Exiting.")
                break
            show_bytecode(filename)