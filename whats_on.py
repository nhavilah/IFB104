
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10469231
#    Student name: NICHOLAS HAVILAH
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
def download(url = 'https://www.museumofbrisbane.com.au/whats-on/',
             target_filename = 'test_run',
             filename_extension = 'html'):

    # Import the function for opening online documents
    from urllib.request import urlopen

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
                        target_filename + "'")

    # Return the downloaded document to the caller
    return web_page_contents


#-----------------------------------------------------------
#
# A main program to call the function.  If you want to download a
# specific web document, add its URL as the function's argument.
#


#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

#develop the GUI
#create the window
the_GUI=Tk()
#give the window a name
the_GUI.title('The Entertainment Planner')
#create an empty list to save the events that the user wants to attend
saved_events=[]
#create a boolean variable to check if working online or offline
offline=0
#define functions to open the other windows
def event_category_1_window():
    event_category_1_window=Toplevel()
    event_category_1_window.title('Event Category 1')
    window_instructions=Label(event_category_1_window,text='Select The Event You Would Like To Attend',font=('Arial',20))
    window_instructions.pack(side=TOP,anchor=W)
    #download the required web page
    download('https://www.museumofbrisbane.com.au/whats-on/','mueseum_brisbane','html')
    #assign the downloaded web page to a variable and read the code
    current_url="mueseum_brisbane.html"
    current_url_code=open('mueseum_brisbane.html').read()
    #find the event names
    mueseum_events_names=findall('<div class="tile-info-title">\s(.*)\s</div>',current_url_code)
    for event_name in mueseum_events_names:
        #remove the leading and trailing spaces from the names and any special character formatting (replace with the Enlgish verisons that a user would see instead)
        modified_event_name=event_name.replace('&#8217;',"'")
        modified_event_name=modified_event_name.replace('&#8220;','"')
        modified_event_name=modified_event_name.replace('&#8221;','"')
        modified_event_name.lstrip()
        modified_event_name.rstrip()
        print(modified_event_name)
        checkbox=Checkbutton(event_category_1_window,text=modified_event_name)
        checkbox.pack(side=TOP,anchor=W)
    #find the event times/dates
    mueseum_events_dates=findall('class="tile-info-date">\s(.*)\s</span>',current_url_code)
    for event_date_or_time in mueseum_events_dates:
        #remove the leading and trailing spaces from the dates/times
        event_date_or_time.lstrip()
        event_date_or_time.rstrip()
        print(event_date_or_time)
    #find the event images(for the html document that is outputted from the "print planner" button
    mueseum_events_images=findall('<div class="tile-thumb" style="background-image:url\((.*)\)',current_url_code)
    for event_image_url in mueseum_events_images:
        #remove the leading and trailing spaces from the dates/times
        event_image_url.lstrip()
        event_image_url.rstrip()
        print(event_image_url)
    

def event_category_2_window():
    event_category_2_window=Toplevel()
    event_category_2_window.title('Event Category 2')
    window_instructions=Label(event_category_2_window,text='Select The Event You Would Like To Attend',font=('Arial',20))
    window_instructions.pack(side=TOP,anchor=W)
    #download the required web page
    download('http://thezoo.com.au/','mueseum_brisbane','html')
    #assign the downloaded web page to a variable and read the code
    current_url="the_zoo.html"
    current_url_code=open('the_zoo.html',encoding='UTF-8').read()
    #find the event names
    the_zoo_event_names_with_spaces=findall('href="http://.*>(.*)</a></h2>',current_url_code)
    for event_name in the_zoo_event_names_with_spaces:
        #remove the leading and trailing spaces from the dates/times and any html character formatting(replace it with the English version that a user would normally see instead)
        modified_event_name=event_name.replace('&#8217;',"'")
        modified_event_name=modified_event_name.replace('&#8211;','-')
        modified_event_name=modified_event_name.replace('&#8216;',"'")
        modified_event_name.lstrip()
        modified_event_name.rstrip()
        print(modified_event_name)
        checkbox=Checkbutton(event_category_2_window,text=modified_event_name)
        checkbox.pack(side=TOP,anchor=W)
    #find the event dates and times
    the_zoo_event_times=findall('<span class="like-nav custom-meta">\s*(.*)\s*</span>',current_url_code)
    for event_time in the_zoo_event_times:
        #remove the leading and trailing spaces from the dates and times
        event_time.lstrip()
        event_time.rstrip()
        print(event_time)
    the_zoo_image_urls=findall('srcset="(.*.jpg)\s530w',current_url_code)
    for event_image in the_zoo_image_urls:
        #remove the leading and trailing spaces from the image urls
        event_image.lstrip()
        event_image.rstrip()
        print(event_image)

def event_category_3_window():
    global offline
    potato=offline
    event_category_3_window=Toplevel()
    event_category_3_window.title('Event Category 3')
    window_instructions=Label(event_category_3_window,text='Select The Event You Would Like To Attend',font=('Arial',20))
    window_instructions.pack(side=TOP,anchor=W)
    #download the required web page
    download('https://concreteplayground.com/brisbane/events','concrete_playground','html')
    current_url=''
    if potato==1:
        #current_url="concrete_playground"
        current_url_code=open('concrete_playground.html').read()
        print(current_url_code)
    if potato==2:
        current_url_code=open('download2.html').read()
        print(current_url_code)
    #find the event names
    concrete_playground_event_names=findall('"name":"(.*)","description":',current_url_code)
    how_many_events=len(concrete_playground_event_names)
    for names in range(how_many_events):
        event_name=concrete_playground_event_names[names]
    #define an empty list to store the chosen events in(temporarily in case they change their mid about the events they want to attend)
    events_chosen=[]
    def display_choice():
        #check if any events have been selected from the list
        if choices.curselection() != ():
            #add the selected event to the list of chosen events
            events_list.insert(END, choices.get(choices.curselection()) + '\n')
            events_chosen.append(choices.curselection())
            #remove the option from the choices list to prevent double ups in the chosen events list
            choices.delete(choices.curselection())
    def restore_choices():
        for item in events_chosen:
            #convert each of the events in the index into strings(item returns a variable like (0,) so it needs to be converted and reformatted
            new_item=str(item)
            #remove the unneccessary parts of the string
            new_item=new_item.replace('(','')
            new_item=new_item.replace(')','')
            new_item=new_item.replace(',','')
            #convert the formatted item into an integer to use as an index
            new_item=int(new_item)
            #insert the removed item back into the choices list(use the sorted list to put it back in the same spot it was in before
            choices.insert(new_item,concrete_playground_event_names[new_item])
            #clear the listbox of all events currently in it
            events_list.delete(1.0,END)
            #wipe the list of selected events clear as well so it matches the listbox
            events_chosen.clear()
    def save_choices():
        for event in events_chosen:
            #convert each of the events in the index into strings(item returns a variable like (0,) so it needs to be converted and reformatted
            new_item=str(event)
            #remove the unneccessary parts of the string
            new_item=new_item.replace('(','')
            new_item=new_item.replace(')','')
            new_item=new_item.replace(',','')
            #convert the formatted item into an integer to use as an index
            new_item=int(new_item)
            #add the selected events to a list to store the user choices that can then be printed in a html document
            saved_events.append(concrete_playground_event_names[new_item])
            print(saved_events)
        #close the current_window
        event_category_3_window.destroy()
        
    #create the buttons that allow the user to add events, clear all selected events, or save events to be printed off later
    # provide a list of event options for the user
    events_list = Text(event_category_3_window, width = 30, height = 10,font = ('Arial', 10),borderwidth = 2, relief = 'groove')
    events_list.pack()
    
    choices = Listbox(event_category_3_window, font = ('Arial', 10), height = how_many_events)
    choices.pack()
    for item in concrete_playground_event_names:
        choices.insert(END, item)
    margin_size=5
    # Create a button to push when the user is happy with their choice
    add_to_list = Button(event_category_3_window, text = ' Add to list ',font = ('Arial', 10), command = display_choice)
    add_to_list.pack(pady = margin_size)

    remove_from_list=Button(event_category_3_window,text='Clear Selections',font=('Arial',10),command=restore_choices)
    remove_from_list.pack()

    save_event_choices=Button(event_category_3_window,text='Save Selection',font=('Arial',10),command=save_choices)
    save_event_choices.pack()

    #find the event dates
    concrete_playground_event_dates=findall('<div><p class="dates">(.*)</p><p class',current_url_code)
    for event_date in concrete_playground_event_dates:
        #remove the leading and trailing spaces fromt the event dates
        event_date.lstrip()
        event_date.rstrip()
        #print(event_date)
    #find the event image urls
    concrete_playground_image_urls=findall('data-srcset="(.*)\s325w',current_url_code)
    for event_image in concrete_playground_image_urls:
        #remove the leading and trailing spaces from the image urls
        event_image.lstrip()
        event_image.rstrip()
        #print(event_image)

def main_window():
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
    def working_offline():
        global offline
        if var.get()==0:
            offline=1    
        if var.get()==1:
            offline=2
        print(offline)
            
    var=IntVar()
    offline_checker=Checkbutton(the_GUI,text="Offline Mode",variable=var,command=working_offline)
    offline_checker.grid(row=4,column=1)
    def printed_button():
        if len(saved_events)>0:
            print(saved_events)
        else:
            no_events_chosen_text="No Events Selected!"
        printed_the_planner=Label(the_GUI,text=no_events_chosen_text,font=('Arial',13))
        printed_the_planner.grid(pady=5,row=5,column=2)

    printing_button=Button(the_GUI,text='Print Planner',font=('Arial',13),activeforeground='red',activebackground='blue',command=(printed_button))
    printing_button.grid(pady=10,row=4,column=2)
        
main_window()
#This function will switch between the online and offline modes

    

#for each website, find the event titles and append them to their corresponding list
#if url1.find('<div class="tile-info-title">\s(.*\b)\s')==0:
#    print('nothing found')
#print(url1_code)

# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'

