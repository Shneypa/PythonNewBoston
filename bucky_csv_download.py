from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=9&e=2&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"


# Function downloads a CSV file (table).
# First, as a string, then breaks down in lines and writes to a local file line by line.

def download_csv_data(csv_url):

    # setup connection to the url
    connection_object = request.urlopen(csv_url)

    # store all data from CSV file into a variable
    our_data = connection_object.read()

    # transform data into string format
    string_data = str(our_data)                     # now the table is a looooooong string

    string_by_lines = string_data.split("\\n")      # split long string by line breaks



    # create new file

    file = open("google_prices.csv", "w")

    for line in string_by_lines:                    # writes each line into a file
        file.write(line + "\n")

    file.close()




download_csv_data(goog_url)



