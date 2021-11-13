def sales_reports(log_file, day_of_week):       # defines a function named sales_reports that takes in 2 params, log_file, day_of_week
    for line in log_file:                       # starts a for loop for each line in the log_file
        line = line.rstrip()                    # strips all white space from the right side of the line
        day = line[0:3]                         # sets a variable that is the first three letters of the line
        if day == day_of_week:                  # starts an if block if day = day_of_week
            print(line)                         # prints all lines that start with day_of_week

def qty_reports(log_file, qty):                 # defines a function named qty_reports that takes in 2 params, log_file, qty
    for line in log_file:                       # starts a for loop for each line in the log_file
        line = line.rstrip()                    # strips all white space from the right side of the line
        data = line.split(' ')                  # splits the line string into a list, making the qty easier to find
        if int(data[2]) > qty:                  # converts (casts) the data at index 2 into an int and checks if it is > the requested qty
            print(line)                         # prints all lines where qty > requested qty

log_file = open("um-server-01.txt")             # sets a variable referencing the .txt file
sales_reports(log_file, "Mon")                  # runs the defined function
print('--------------------------------------') # visually separate the reports
log_file = open("um-server-01.txt")             # reopens the file to allow another report to run
qty_reports(log_file, 10)                       # runs the newly defined function