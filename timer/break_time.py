import webbrowser as wb
import time as stopwatch

count = 0
total_breaks = 3
break_gap = 2*60*60

while count < total_breaks:
    stopwatch.sleep(break_gap)
    wb.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count+=1
print "Exiting!"
