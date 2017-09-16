#Chick profanity program
#program to detects curse words in the text to avoid embarrassing messages
#--------------------------------------------------------------------
#-Algorithm idea
#1) make a list with the most common curse words
#2) compare every word in the input to the list
#3) show the result according to finding a bad word or not
#--------------------------------------------------------------------

import urllib

def read_text():
    quotes = open("C:\Profanity text\movie_quotes.txt")
    #open function allowed us to work with file on computer and this take the path of file then the file name
    #I attached Profanity text file and you can add the file as you want
    
    contents_of_file = quotes.read()
    
    print(contents_of_file)

    quotes.close()
    
    check_profanity(contents_of_file)
    
#function
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)

    output = connection.read()
    print (output)
    connection.close()
    if "true" in output:
        print("Profanit Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    

read_text()
