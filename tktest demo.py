#percentage calculator
#import the tkinter functions
from tkinter import*

#create a GUI
percent_gui=Tk()

#backend function to calculate a percentage
def compute():
    #get numerator and denominator
    num=int(numerator.get())
    den=int(denominator.get())
    answer=(num*100)/den
    result['text']=str(answer)+'%'
    

#put a title on our new window
percent_gui.title('percentage calculator')

#entry box for the numerator
numerator=Entry(percent_gui,font=('Arial',32),width=5)
numerator.pack()

#entry box for the denominator
denominator=Entry(percent_gui,font=('Arial',32),width=5)
denominator.pack()

#widget for showing the result
result = Label(percent_gui,text='???',font=('Arial',32),bg='red')
result.pack()

#create a push button
start=Button(percent_gui, text = ' Calculate ',font=('Arial',32),activeforeground='red', command=compute)
start.pack()

#start the event loop
percent_gui.mainloop()
