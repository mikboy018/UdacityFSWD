import urllib

def read_text():
    reader = open("C:\Users\mike6\Google Drive\FullStack\UdacityFSWD\prof_check\message_string3.txt")
    contents_of_file = reader.read()
    print(contents_of_file)
    reader.close()
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity alert")
    elif "false" in output:
        print("No profanity")
    else:
        print("Something is wrong...")
    connection.close()
read_text()
