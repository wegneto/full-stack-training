import time
import webbrowser

total_breaks = 3;
break_count = 0;

print("This program started on: " + time.ctime())
while total_breaks > break_count:
    time.sleep(10)
    webbrowser.open("http://www.uol.com.br")
    break_count = break_count + 1