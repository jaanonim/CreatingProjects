import os


def createPython(path, name):
    _dir = path + "/" + name
    python_path = _dir + "/env/Scripts/python.exe"

    try:
        os.mkdir(_dir)
        os.chdir(_dir)
        os.mkdir(".vscode")
        os.system("git init")
        os.system("py -m venv env")
        os.system(f'"{python_path}" -m pip install black')
        os.system("type NUL > requirements.txt")
        os.system("type NUL > main.py")
        os.system(f"echo # {name} > README.md")

        f = open(".vscode/settings.json", "w")
        f.write(
            '{ "python.pythonPath": '
            + python_path
            + '", "python.formatting.provider": "black"} '
        )
        f.close()

        f = open(".gitignore", "w")
        f.write("env\n.vscode")
        f.close()

        print(f"{name} created.")
        os.system("code .")

    except Exception as e:
        print(f"Cannot create project {name}.")
        print(e)
