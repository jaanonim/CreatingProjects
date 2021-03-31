import os


def loadTemplates():
    f = open("templates/index.html", "r")
    html = f.read()
    f.close()

    f = open("templates/main.css", "r")
    css = f.read()
    f.close()

    return html, css


def createWeb(path, name):
    _dir = path + "/" + name

    try:
        html, css = loadTemplates()

        os.mkdir(_dir)
        os.chdir(_dir)
        os.mkdir("img")
        os.mkdir("css")

        html = html.replace("##name##", name)

        f = open("index.html", "w")
        f.write(html)
        f.close()

        f = open("css/main.css", "w")
        f.write(css)
        f.close()

        print(f"{name} created.")
        os.system("code .")

    except:
        print(f"Cannot create project {name}.")
