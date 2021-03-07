import time, calendar
from statistics import stdev, mean, median_grouped

times = []

print("Generic Puzzle Timer by Ethan")
print("Distributed under the Unlicense License.")
print()
print("Keyboard interrupt (Ctrl + C) to quit.")
print("Type '/s' to see your statistics.")
print()

def calculate_stats(times):
    try:
        min_time = str(min(times))
        max_time = str(max(times))
        mean_time = str(mean(times))
        median_time = str(median_grouped(times))
        stddev_time = str(round(stdev(times), 1))

        print()
        print("Lowest time: " + min_time)
        print("Highest time: " + max_time)
        print("Average time: " + mean_time)
        print("Median time: " + median_time)
        print("Standard deviation: " + stddev_time)
        print()
    except ValueError:
        print("Insufficient data to show statistics.")

while True:
    try:
        cont = input("Press enter to start the timer. ")
        if cont == "/s":
            print()
            print("Session statistics: ")
            calculate_stats(times)
        else:
            start_epoch = calendar.timegm(time.gmtime())
            cont = input("Press enter to end the timer. ")
            end_epoch = calendar.timegm(time.gmtime())
            total_time = end_epoch - start_epoch
            sec_time = str(total_time % 60)
            min_time = str(total_time // 60)
            times.append(total_time)
            print("You solved your puzzle in " + min_time + " min and " + sec_time + " sec.")
    
    except KeyboardInterrupt:
        print()
        print("Session summary: ")
        calculate_stats(times)
        break
        
        
    
