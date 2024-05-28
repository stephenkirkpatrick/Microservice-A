import webbrowser
import time

changed = ""
while True:
    time.sleep(10)
    with open('webpage.txt', 'r', encoding="utf-8") as f:
        fdata = f.read()
    if (fdata == "Success" or fdata == changed):
        pass
    else:
        changed = fdata
        try:
            webbrowser.open(fdata)
        except:
            with open('webpage.txt', 'w', encoding="utf-8") as f:
                f.write("Error")
        else:
            with open('webpage.txt', 'w', encoding="utf-8") as f:
                f.write("Success")

