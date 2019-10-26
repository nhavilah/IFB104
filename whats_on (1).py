
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****PUT YOUR STUDENT NUMBER HERE*****
#    Student name: *****PUT YOUR NAME HERE*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it as a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#
#create the main GUI in this function
def event_category_1_window():
    #define a function that adds all of the selected events to a list
    def save_user_choices():
        if var0.get()==1:
            for event in event_choices:
                if event in event_choices:
                    event_choices.append(museum_event_names[0].strip())
                    event_choices.append(mueseum_events_dates[0].strip())
                    print(event_choices)
            event_choices=list(set(event_choices))
        if var1.get()==1:
            event_choices.append(museum_event_names[1].strip())
            event_choices.append(mueseum_events_dates[1].strip())
        if var2.get()==1:
            event_choices.append(museum_event_names[2].strip())
            event_choices.append(mueseum_events_dates[2].strip())
        if var3.get()==1:
            event_choices.append(museum_event_names[3].strip())
        if var4.get()==1:
            event_choices.append(museum_event_names[4].strip())
            event_choices.append(mueseum_events_dates[4].strip())
        if var5.get()==1:
            event_choices.append(museum_event_names[5].strip())
            event_choices.append(mueseum_events_dates[5].strip())
        if var6.get()==1:
            event_choices.append(museum_event_names[6].strip())
            event_choices.append(mueseum_events_dates[6].strip())
        if var7.get()==1:
            event_choices.append(museum_event_names[7].strip())
            event_choices.append(mueseum_events_dates[7].strip())
        if var8.get()==1:
            event_choices.append(museum_event_names[8].strip())
            event_choices.append(mueseum_events_dates[8].strip())
        if var9.get()==1:
            event_choices.append(museum_event_names[9].strip())
            event_choices.append(mueseum_events_dates[9].strip())
        #print(event_choices)
        
    #create a new window to display the options and give it a title
    category_1_window=Toplevel()
    category_1_window.title('Category 1')
    #add some instructions to the window
    instructions=Label(category_1_window,text='Select The Events You Would Like To Attend',font=('Arial',20))
    instructions.grid(row=0,column=1)
    #decide whether to download the web page or work from an offline copy
    if offline==False:
        #current_url_code=open('download.html').read()
        print('offline')
    if offline==True:
        download('https://www.museumofbrisbane.com.au/whats-on/','mueseum_brisbane','html')
        current_url_code=open('mueseum_brisbane.html').read()
    #retrieve the event names
    museum_event_names=findall('<div class="tile-info-title">\s(.*)\s</div>',current_url_code)
    #retrieve the event dates
    mueseum_events_dates=findall('class="tile-info-date">\s(.*)\s</span>',current_url_code)
    #retrieve the image urls for each event
    mueseum_events_images=findall('<div class="tile-thumb" style="background-image:url\((.*)\)',current_url_code)
    
    #create a group of 10 checkboxes and put them on the screen
    #the names will change depending on which webpage is being used
    var0=IntVar()
    event_option_0=Checkbutton(category_1_window,text=museum_event_names[0].strip(),variable=var0,command=save_user_choices)
    event_option_0.grid(row=1,column=0)
    var1=IntVar()
    event_option_1=Checkbutton(category_1_window,text=museum_event_names[1].strip(),variable=var1,command=save_user_choices)
    event_option_1.grid(row=2,column=0)
    var2=IntVar()
    event_option_2=Checkbutton(category_1_window,text=museum_event_names[2].strip(),variable=var2,command=save_user_choices)
    event_option_2.grid(row=3,column=0)
    var3=IntVar()
    event_option_3=Checkbutton(category_1_window,text=museum_event_names[3].strip(),variable=var3,command=save_user_choices)
    event_option_3.grid(row=4,column=0)
    var4=IntVar()
    event_option_4=Checkbutton(category_1_window,text=museum_event_names[4].strip(),variable=var4,command=save_user_choices)
    event_option_4.grid(row=5,column=0)
    var5=IntVar()
    event_option_5=Checkbutton(category_1_window,text=museum_event_names[5].strip(),variable=var5,command=save_user_choices)
    event_option_5.grid(row=6,column=0)
    var6=IntVar()
    event_option_6=Checkbutton(category_1_window,text=museum_event_names[6].strip(),variable=var6,command=save_user_choices)
    event_option_6.grid(row=7,column=0)
    var7=IntVar()
    event_option_7=Checkbutton(category_1_window,text=museum_event_names[7].strip(),variable=var7,command=save_user_choices)
    event_option_7.grid(row=8,column=0)
    var8=IntVar()
    event_option_8=Checkbutton(category_1_window,text=museum_event_names[8].strip(),variable=var8,command=save_user_choices)
    event_option_8.grid(row=9,column=0)
    var9=IntVar()
    event_option_9=Checkbutton(category_1_window,text=museum_event_names[9].strip(),variable=var9,command=save_user_choices)
    event_option_9.grid(row=10,column=0)






























    
def event_category_2_window():
    print('hey')
def event_category_3_window():
    print('hello')
def printed_button():
    global event_choices
    for event in event_choices:
       # if event not in html_list:
            #event_choices.append(event)
        print(event)
    #print(html_list)

def main_window():
    #create a nested function to check the network state
    def working_offline():
        #create an if statement that checks if the offline checkbox is ticked and changes the state accordingly
        if var.get()==0:
            offline=False
        if var.get()==1:
            offline=True
    
    #create the main GUI
    the_GUI=Tk()
    the_GUI.title('The Entertainment Planner')
    
    GUI_title_box=Label(the_GUI,text='The Entertainment Guide', width=20,font=('Arial',32),borderwidth=10, relief='ridge')
    GUI_title_box.grid(pady=5,row=1,columnspan=3,column=1)

    event_categories_label=Label(the_GUI,text='Event Categories',width=15,font=('Arial',15),borderwidth=5,relief='ridge')
    event_categories_label.grid(pady=5,row=2,column=2)

    event_category_1_button=Button(the_GUI,text='Category 1',font=('Arial',13),activeforeground='red',activebackground='blue',command=(event_category_1_window))
    event_category_1_button.grid(padx=40,row=3,column=1)

    event_category_2_button=Button(the_GUI,text='Category 2',font=('Arial',13),activeforeground='red',activebackground='blue',command=(event_category_2_window))
    event_category_2_button.grid(padx=40,row=3,column=2)
    
    event_category_3_button=Button(the_GUI,text='Category 3',font=('Arial',13),activeforeground='red',activebackground='blue',command=event_category_3_window)
    event_category_3_button.grid(padx=40,row=3,column=3)

    #create the online/offline checkbox and define its features       
    var=IntVar()
    offline_checker=Checkbutton(the_GUI,text="Offline Mode",variable=var,command=working_offline)
    offline_checker.grid(row=4,column=1)
    #add a button that prints the planner
    printing_button=Button(the_GUI,text='Print Planner',font=('Arial',13),activeforeground='red',activebackground='blue',command=(printed_button))
    printing_button.grid(pady=10,row=4,column=2)


#write the code that will be executed at runtime without being called through other functions(define any variables here that will be used throughout the code)
#variable to check if working offline or online
offline=True
#create an empty list to store the chosen events(there will be duplicates in this list so the final list(which will be appended to through a function) that outputs to the html document will needto be a different list)
event_choices=[]
#create an empty list that will be appended with all the final choices for the user
html_list=[]
#call any functions down here
main_window()
# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'

