
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
    global offline
    global museum_event_names
    global mueseum_events_dates
    global mueseum_events_images
    #create a new window to display the options and give it a title
    category_1_window=Toplevel()
    category_1_window.title('Arts And Culture')
    category_1_window.configure(background='black')
    #add some instructions to the window
    instructions=Label(category_1_window,text='Select The Events You Would Like To Attend',font=('Arial',20),borderwidth=5,relief='ridge',bg='purple',fg='red',width=37)
    instructions.pack(side=TOP,anchor=W)
    #decide whether to download the web page or work from an offline copy
    if offline==1:
        current_url_code=open('download.html').read()
    if offline==0:
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
    event_option_0=Checkbutton(category_1_window,text=museum_event_names[0].strip(),variable=var0,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_1=Checkbutton(category_1_window,text=museum_event_names[1].strip(),variable=var1,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_2=Checkbutton(category_1_window,text=museum_event_names[2].strip(),variable=var2,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_3=Checkbutton(category_1_window,text=museum_event_names[3].strip(),variable=var3,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_4=Checkbutton(category_1_window,text=museum_event_names[4].strip(),variable=var4,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_5=Checkbutton(category_1_window,text=museum_event_names[5].strip(),variable=var5,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_6=Checkbutton(category_1_window,text=museum_event_names[6].strip(),variable=var6,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_7=Checkbutton(category_1_window,text=museum_event_names[7].strip(),variable=var7,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_8=Checkbutton(category_1_window,text=museum_event_names[8].strip(),variable=var8,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_9=Checkbutton(category_1_window,text=museum_event_names[9].strip(),variable=var9,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)

    #create a button that closes the window
    close_the_window=Button(category_1_window,text='Close',command=category_1_window.destroy,bg='light blue',fg='purple',relief='ridge',overrelief='flat').pack(side=TOP,anchor=W,pady=10)
    #create a label telling the user where the events are sourced from
    source_label=Label(category_1_window,text='Events Sourced From: https://www.museumofbrisbane.com.au/whats-on/',bg='purple',fg='red',relief='ridge').pack(side=TOP,anchor=W)
def event_category_2_window():
    global offline
    global the_zoo_events_names
    global the_zoo_events_dates
    global the_zoo_events_images
    #create a new window to display the options and give it a title
    category_2_window=Toplevel()
    category_2_window.title('Sports')
    category_2_window.configure(background='black')
    #add some instructions to the window
    instructions=Label(category_2_window,text='Select The Events You Would Like To Attend',font=('Arial',20),borderwidth=5,relief='ridge',bg='purple',fg='red',width=37)
    instructions.pack(side=TOP,anchor=W)
    #decide whether to download the web page or work from an offline copy
    if offline==1:
        current_url_code=open('download1.html').read()
    if offline==0:
        download('https://cbussuperstadium.com.au/what-s-on.aspx','cbus_super_stadium','html')
        current_url_code=open('cbus_super_stadium.html').read()
    #retrieve the event names
    the_zoo_events_names=findall('<h6 class="event-title">(.*)</h6>',current_url_code)
    #retrieve the event dates
    the_zoo_events_dates=findall('<h7 class="event-date text-uppercase">(.*)</h7>',current_url_code)
    #retrieve the image urls for each event
    the_zoo_events_images=findall('src="(.*)"\sclass=".*">\s*</div>',current_url_code)
    
    #create a group of 10 checkboxes and put them on the screen
    #the names will change depending on which webpage is being used(online or offline)
    #because this web page uses UTF-8 formatting, the special characters are presented incorrectly so these need to be replaced
    option_10_text=the_zoo_events_names[0].replace("&#8211;","-")
    modified_event_name=option_10_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_10=modified_event_name.strip()
    event_option_10=Checkbutton(category_2_window,text=modified_event_name_10,variable=var10,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_11_text=the_zoo_events_names[1].replace("&#8211;","-")
    modified_event_name=option_11_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_11=modified_event_name.strip()
    event_option_11=Checkbutton(category_2_window,text=modified_event_name_11,variable=var11,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_12_text=the_zoo_events_names[2].replace("&#8211;","-")
    modified_event_name=option_12_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_12=modified_event_name.strip()
    event_option_12=Checkbutton(category_2_window,text=modified_event_name_12,variable=var12,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_13_text=the_zoo_events_names[3].replace("&#8211;","-")
    modified_event_name=option_13_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_13=modified_event_name.strip()
    event_option_13=Checkbutton(category_2_window,text=modified_event_name_13,variable=var13,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_14_text=the_zoo_events_names[4].replace("&#8211;","-")
    modified_event_name=option_14_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_14=modified_event_name.strip()
    event_option_14=Checkbutton(category_2_window,text=modified_event_name_14,variable=var14,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_15_text=the_zoo_events_names[5].replace("&#8211;","-")
    modified_event_name=option_15_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_15=modified_event_name.strip()
    event_option_15=Checkbutton(category_2_window,text=modified_event_name_15,variable=var15,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    option_16_text=the_zoo_events_names[6].replace("&#8211;","-")
    modified_event_name=option_16_text.replace('&#8216;',"'")
    modified_event_name=modified_event_name.replace('&#8217;',"'")
    modified_event_name=modified_event_name.replace('&#038;',"&")
    modified_event_name_16=modified_event_name.strip()
    event_option_16=Checkbutton(category_2_window,text=modified_event_name_16,variable=var16,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    #create a button that closes the window
    close_the_window=Button(category_2_window,text='Close',command=category_2_window.destroy,bg='light blue',fg='purple',relief='ridge',overrelief='flat').pack(side=TOP,anchor=W,pady=10)
    #create a label telling the user where the events are sourced from
    source_label=Label(category_2_window,text='Events Sourced From: https://cbussuperstadium.com.au/what-s-on.aspx',bg='purple',fg='red',relief='ridge').pack(side=TOP,anchor=W)
def event_category_3_window():
    global offline
    global concrete_playground_event_names
    global concrete_playground_event_dates
    global concrete_playground_event_images
    #create a new window to display the options and give it a title
    category_3_window=Toplevel()
    category_3_window.title('Public Events')
    category_3_window.configure(background='black')
    #add some instructions to the window
    instructions=Label(category_3_window,text='Select The Events You Would Like To Attend',font=('Arial',20),borderwidth=5,relief='ridge',bg='purple',fg='red',width=37)
    instructions.pack(side=TOP,anchor=W)
    #decide whether to download the web page or work from an offline copy
    if offline==1:
        current_url_code=open('download2.html').read()
    if offline==0:
        download('https://concreteplayground.com/brisbane/events','concrete_playground','html')
        current_url_code=open('concrete_playground.html').read()
    #retrieve the event names
    concrete_playground_event_names=findall('"name":"(.*)","description":',current_url_code)
    #retrieve the event dates
    concrete_playground_event_dates=findall('<div><p class="dates">(.*)</p><p class',current_url_code)
    #retrieve the image urls for each event
    concrete_playground_event_images=findall('data-srcset="(.*)\s325w',current_url_code)
    
    #create a group of 10 checkboxes and put them on the screen
    #the names will change depending on which webpage is being used
    event_option_20=Checkbutton(category_3_window,text=concrete_playground_event_names[0].strip(),variable=var20,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_21=Checkbutton(category_3_window,text=concrete_playground_event_names[1].strip(),variable=var21,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_22=Checkbutton(category_3_window,text=concrete_playground_event_names[2].strip(),variable=var22,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_23=Checkbutton(category_3_window,text=concrete_playground_event_names[3].strip(),variable=var23,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_24=Checkbutton(category_3_window,text=concrete_playground_event_names[4].strip(),variable=var24,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_25=Checkbutton(category_3_window,text=concrete_playground_event_names[5].strip(),variable=var25,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_26=Checkbutton(category_3_window,text=concrete_playground_event_names[6].strip(),variable=var26,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_27=Checkbutton(category_3_window,text=concrete_playground_event_names[7].strip(),variable=var27,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_28=Checkbutton(category_3_window,text=concrete_playground_event_names[8].strip(),variable=var28,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)
    event_option_29=Checkbutton(category_3_window,text=concrete_playground_event_names[9].strip(),variable=var29,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=40,anchor=W).pack(side=TOP,anchor=W)

    #create a button that closes the window
    close_the_window=Button(category_3_window,text='Close',font=('Arial',10),command=category_3_window.destroy,bg='light blue',fg='purple',relief='ridge',overrelief='flat').pack(side=TOP,anchor=SW,pady=10)

    #create a label telling the user where the events are sourced from
    source_label=Label(category_3_window,text='Events Sourced From: https://concreteplayground.com/brisbane/events',bg='purple',fg='red',relief='ridge').pack(side=TOP,anchor=W)
def printed_button():
    global save_results_to_db
    events_not_selected_counter=0
    for variable in varlist:
        if variable.get()==0:
            events_not_selected_counter=events_not_selected_counter+1
        if events_not_selected_counter==30:
            html_page='</DOCTYPE html><html><style>h1{color:red;}body{background-color:#000000;}></style><title>The Entertainment Planner</title></head><h1>Your Entertainment Schedule:</h1>'
            body_content='<p><font color="red";font size="5">No Events Selected!</font></p>'
            html_page=html_page+body_content+"</body></html>"
            plan_page=open("planner.html","w")
            plan_page.write(html_page)
        if variable.get()==1:
            event_index=varlist.index(variable)
            if event_index>=0 and event_index<=9:
                if mueseum_events_images[event_index].strip() not in html_list:
                    html_list.append(mueseum_events_images[event_index].strip())
                if museum_event_names[event_index].strip() not in html_list:
                    html_list.append(museum_event_names[event_index].strip())
                if mueseum_events_dates[event_index].strip() not in html_list:
                    html_list.append(mueseum_events_dates[event_index].strip())
            elif event_index>=10 and event_index<=19:
                if the_zoo_events_images[event_index-10].strip() not in html_list:
                    html_list.append(the_zoo_events_images[event_index-10].strip())
                if the_zoo_events_names[event_index-10].strip() not in html_list:
                    html_list.append(the_zoo_events_names[event_index-10].strip())
                if the_zoo_events_dates[event_index-10].strip() not in html_list:
                    html_list.append(the_zoo_events_dates[event_index-10].strip())
            elif event_index>=20 and event_index<=29:
                if concrete_playground_event_images[event_index-20].strip() not in html_list:
                    html_list.append(concrete_playground_event_images[event_index-20].strip())
                if concrete_playground_event_names[event_index-20].strip() not in html_list:
                    html_list.append(concrete_playground_event_names[event_index-20].strip())
                if concrete_playground_event_dates[event_index-20].strip() not in html_list:
                    html_list.append(concrete_playground_event_dates[event_index-20].strip())
            html_page="</DOCTYPE html><html><style>h1{color:red;}body{background-color:#000000;}></style><title>The Entertainment Planner</title></head><h1>Your Entertainment Schedule:</h1>"
            for html_item in html_list:
                if 'http' in html_item:
                    body_content="<img src="+html_item+">"
                elif "/CMSPages" in html_item:
                    body_content="<img src="+"https://cbussuperstadium.com.au"+html_item+">"
                else:
                    body_content='<p style="border:3px; border-style:solid; border-color:purple; padding: 1em;">'+'<font color=#00ccff>'+html_item+'</font>'+'</p>'
                html_page='<p>'+html_page+body_content+'</p>'
            html_page=html_page+"<p1>Events Sourced From:<br>https://www.museumofbrisbane.com.au/whats-on/<br>https://cbussuperstadium.com.au/what-s-on.aspx<br>https://concreteplayground.com/brisbane/events</p1></body></html>"
            plan_page=open("planner.html","w")
            plan_page.write(html_page)
    import webbrowser, os.path
    plan=webbrowser.open('file:///'+os.path.abspath('planner.html'))
    if save_results_to_db==1:
        save_to_db()
    html_list.clear()
#create a function to save the events to a database
def save_to_db():
    #create the counters that track the positions of the event names and times in the list of selected events
    #this will have to be a list of all the possible event name positions to account for users picking any number of events
    event_name_position_counter=[1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,73,76]
    event_time_position_counter=[2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59,62,65,68,71,74,77]
    #create an empty list tht ONLY stores the event names and times(to append them to the database
    event_names=[]
    event_times=[]
    for html_item in html_list:
        current_index=html_list.index(html_item)
        if current_index in event_name_position_counter:
            event_names.append(html_item)
        elif current_index in event_time_position_counter:
            event_times.append(html_item)
        #format the event names to remove any html formatting
        html_item=html_item.replace("&#8211;","-")
        html_item=html_item.replace('&#8216;',"'")
        html_item=html_item.replace('&#8217;',"'")
        html_item=html_item.replace('&#038;',"&")
        html_item=html_item.strip()
    #clear the database of any previous entries
    connection=connect(database='entertainment_planner.db')
    entertainment_planner_db=connection.cursor()
    delete_from_db="DELETE FROM events"
    entertainment_planner_db.execute(delete_from_db)
    connection.commit()
    entertainment_planner_db.close()
    connection.close()
    #append each event to the database
    for database_item in range(len(event_names)):
        connection=connect(database='entertainment_planner.db')
        entertainment_planner_db=connection.cursor()
        insert_into_db="INSERT INTO events VALUES('"+event_names[database_item]+"','"+event_times[database_item]+"')"
        entertainment_planner_db.execute(insert_into_db)
        connection.commit()
        entertainment_planner_db.close()
        connection.close()
    #clear the event_names_and_times list for the next time the button is pressed
    event_names.clear()
    event_times.clear()

#create a function to check the network state
def working_offline():
    #create an if statement that checks if the offline checkbox is ticked and changes the state accordingly
    global offline
    if offline_var.get()==0:
        offline=0
    if offline_var.get()==1:
        offline=1
    return offline
#create a function that checks if the user wants to save their selection to a database
def save_to_db():
    global save_results_to_db
    if save_to_database_checkbutton.get()==0:
        save_results_to_db=0
    if save_to_database_checkbutton.get()==1:
        save_results_to_db=1
    return save_results_to_db
def close_current_window():
    Toplevel.destroy()
#create a list to store the states of each checkbutton
varlist=[]
#create an empty list to store the chosen events(there will be duplicates in this list so the final list(which will be appended to through a function) that outputs to the html document will needto be a different list)
event_choices=[]
#create an empty list that will be appended with all the final choices for the user
html_list=[]
#create the offline condition(1 means offline and 0 means online)
offline=0
#create the save to database condition
save_results_to_db=0
#empty lists that store the museum events, dates and images for each event type
museum_event_names=[]
mueseum_events_dates=[]
mueseum_events_images=[]
the_zoo_events_names=[]
the_zoo_events_dates=[]
the_zoo_events_images=[]
concrete_playground_event_names=[]
concrete_playground_event_dates=[]
concrete_playground_event_images=[]
#create the main GUI
the_GUI=Tk()
the_GUI.title('The Entertainment Planner')
the_GUI.configure(background='black')

logo=PhotoImage(file="logo.gif")
GUI_title_box=Label(the_GUI,image=logo)
GUI_title_box.grid(pady=5,row=1,columnspan=3,column=1)

event_categories_label=Label(the_GUI,text='Choose An Event Category',width=25,font=('Arial',15),borderwidth=5,relief='ridge',bg='purple',fg='red')
event_categories_label.grid(pady=5,row=2,column=2)

event_category_1_button=Button(the_GUI,text='Arts And Culture',font=('Arial',13),activeforeground='red',activebackground='blue',command=(event_category_1_window),bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=17)
event_category_1_button.grid(pady=10,row=3,column=1)

event_category_2_button=Button(the_GUI,text='Sports',font=('Arial',13),activeforeground='red',activebackground='blue',command=(event_category_2_window),bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=17)
event_category_2_button.grid(pady=10,row=3,column=2)

event_category_3_button=Button(the_GUI,text='Public Events',font=('Arial',13),activeforeground='red',activebackground='blue',command=event_category_3_window,bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=17)
event_category_3_button.grid(pady=10,row=3,column=3)

#create the online/offline checkbox and define its features
offline_var=IntVar()
offline_checker=Checkbutton(the_GUI,text="Offline Mode",variable=offline_var,command=working_offline,bg='light blue',fg='purple',relief='ridge',overrelief='flat',font=('Arial',13),width=15)
offline_checker.grid(pady=10,row=4,column=2)

#create the online/offline checkbox and define its features
save_to_database_checkbutton=IntVar()
save_to_db_checker=Checkbutton(the_GUI,text="Save To Database",variable=save_to_database_checkbutton,command=save_to_db,bg='light blue',fg='purple',relief='ridge',overrelief='flat',font=('Arial',13),width=15)
save_to_db_checker.grid(pady=10,row=5,column=2)

#add a button that prints the planner
printing_button=Button(the_GUI,text='Print Planner',font=('Arial',13),activeforeground='red',activebackground='blue',command=(printed_button),bg='light blue',fg='purple',relief='ridge',overrelief='flat',width=17)
printing_button.grid(pady=10,row=6,column=2)

#create all the checkbutton variables(leave them outside any functions so every function can read them)
var0=IntVar()
varlist.append(var0)
var1=IntVar()
varlist.append(var1)
var2=IntVar()
varlist.append(var2)
var3=IntVar()
varlist.append(var3)
var4=IntVar()
varlist.append(var4)
var5=IntVar()
varlist.append(var5)
var6=IntVar()
varlist.append(var6)
var7=IntVar()
varlist.append(var7)
var8=IntVar()
varlist.append(var8)
var9=IntVar()
varlist.append(var9)
var10=IntVar()
varlist.append(var10)
var11=IntVar()
varlist.append(var11)
var12=IntVar()
varlist.append(var12)
var13=IntVar()
varlist.append(var13)
var14=IntVar()
varlist.append(var14)
var15=IntVar()
varlist.append(var15)
var16=IntVar()
varlist.append(var16)
var17=IntVar()
varlist.append(var17)
var18=IntVar()
varlist.append(var18)
var19=IntVar()
varlist.append(var19)
var20=IntVar()
varlist.append(var20)
var21=IntVar()
varlist.append(var21)
var22=IntVar()
varlist.append(var22)
var23=IntVar()
varlist.append(var23)
var24=IntVar()
varlist.append(var24)
var25=IntVar()
varlist.append(var25)
var26=IntVar()
varlist.append(var26)
var27=IntVar()
varlist.append(var27)
var28=IntVar()
varlist.append(var28)
var29=IntVar()
varlist.append(var29)
# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'
