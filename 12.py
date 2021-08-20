import tkinter as tk
from tkinter import messagebox
import csv
from tkinter.ttk import *
import time
import tkinter


#Importing
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    #Switches the frame to StartPage

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True)
    #This section of the simply destroys the current frame and replaces the frame with a new one.
        
class StartPage(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)

######################################################################### Buttons & Labels #########################################################################

        self.img1 = tk.PhotoImage(file= "Start_image.png") 
        self.img1 = self.img1.subsample(2) # changes the size of the image


        self.start_image = tk.Label(self, image= self.img1)
        self.start_image.place(relx =0.5, rely = 0.5, anchor= "center")   
        self.start_image.image = self.img1

        self.img2 = tk.PhotoImage(file= "Next.png")
        self.img2 = self.img2.subsample(9)

        self.Next_image = tk.Button(self, image = self.img2, command=lambda: master.switch_frame(PageOne)) #Changes the 
        self.Next_image.place(relx =0.5, rely = 0.825, anchor= "center")
        self.Next_image.image = self.img2

#This class is simply instantiating all the various images / labels that are required for the inital start page.

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        
######################################################################### Buttons & Labels #########################################################################


        img3 = tk.PhotoImage(file= "Intro_1.png")
        img3 = img3.subsample(2)

        Intro_page = tk.Label(self, image = img3)
        Intro_page.place(relx =0.5, rely = 0.50, anchor= "center")
        Intro_page.image = img3

        img2 = tk.PhotoImage(file= "Next.png")
        img2 = img2.subsample(12)

        Next_image = tk.Button(self, image = img2, command=lambda: master.switch_frame(PageTwo))
        Next_image.place(relx =0.5, rely = 0.875, anchor= "center")
        Next_image.image = img2


#This class is simply instantiating all the various images / labels that are required for the instructions page.


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        img4 = tk.PhotoImage(file= "Intro_2.png")
        img4 = img4.subsample(2)

        Intro_page2 = tk.Label(self, image = img4)
        Intro_page2.place(relx =0.5, rely = 0.5, anchor= "center")
        Intro_page2.image = img4


        img2 = tk.PhotoImage(file= "Next.png")
        img2 = img2.subsample(15)
        
        Next_image = tk.Button(self, image = img2, command=lambda: master.switch_frame(PageThree))
        Next_image.place(relx =0.25, rely = 0.915, anchor= "center")
        Next_image.image = img2

#This class is simply instantiating all the various images / labels that are required for the instructions (countinued) page.


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
######################################################################### Buttons & Labels P3 #########################################################################


        img5 = tk.PhotoImage(file= "Intro_3.png")
        img5 = img5.subsample(2)

        
        Intro_page3 = tk.Label(self, image = img5)
        Intro_page3.place(relx =0.5, rely = 0.5, anchor= "center")
        Intro_page3.image = img5


        img2 = tk.PhotoImage(file= "Next.png")
        img2 = img2.subsample(15)

        Next_image = tk.Button(self, image = img2, command=lambda: master.switch_frame(PageFour))
        Next_image.place(relx =0.25, rely = 0.915, anchor= "center")
        Next_image.image = img2

#This class is simply instantiating all the various images / labels that are required for the instructions (countinued) page.

######################################################################### Buttons & Labels End P3 #########################################################################



class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

######################################################################### Buttons & Labels P4#########################################################################

        img6 = tk.PhotoImage(file= "Intro_4.png")
        img6 = img6.subsample(2)

        
        Intro_page4 = tk.Label(self, image = img6)
        Intro_page4.place(relx =0.5, rely = 0.5, anchor= "center")
        Intro_page4.image = img6


        img2 = tk.PhotoImage(file= "Next.png")
        img2 = img2.subsample(15)


        Next_image = tk.Button(self, image = img2, command=lambda: master.switch_frame(Question1))
        Next_image.place(relx =0.25, rely = 0.915, anchor= "center")
        Next_image.image = img2
        
#This class is simply instantiating all the various images / labels that are required for the instructions (countinued) page.

######################################################################### Buttons & Labels End P4 #########################################################################

        
class Question1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.time = 50
        
        def correct_ans(): #Function that runs allowing the user to proceed to next level
            tk.messagebox.showinfo(title="Congrats", message="Good Job - you have passed this stage. The next question is coming up!")
            master.switch_frame(Question2)

        def wrong_ans():
            tk.messagebox.showerror(title="wrong", message="This answer is wrong, please try again")




######################################################################### Buttons & Labels Q1#########################################################################


        img7 = tk.PhotoImage(file= "Question_1.png")
        img7 = img7.subsample(2)

      
        Question_3 = tk.Label(self, image = img7)
        Question_3.place(relx =0.5, rely = 0.5, anchor= "center")
        Question_3.image = img7

        
        img8 = tk.PhotoImage(file= "Option1.png")
        img8 = img8.subsample(14)

        answer_1 = tk.Button(self, image = img8, command = lambda: correct_ans())
        answer_1.place(relx =0.35, rely = 0.92, anchor= "center")
        answer_1.image = img8


        img9 = tk.PhotoImage(file= "Option2.png")
        img9 = img9.subsample(17)

        answer_2 = tk.Button(self, image = img9, command = lambda:wrong_ans())
        answer_2.place(relx =0.5, rely = 0.92, anchor= "center")
        answer_2.image = img9


        img10 = tk.PhotoImage(file= "Option3.png")
        img10= img10.subsample(17)

        answer_3 = tk.Button(self, image = img10, command = lambda:wrong_ans())
        answer_3.place(relx =0.65, rely = 0.92, anchor= "center")
        answer_3.image = img10

        self.progress = Progressbar(self, orient='horizontal',length=500,mode='determinate')
        self.progress['value']=100
        self.progress.place(relx =0.5, rely = 0.175, anchor= "center")
        self.Timer(master)

        #This section of the code simply instantiates the labels, images and buttons that are required for the game.

    def Timer(self,master):
        
        if self.time > 0:
            self.time -= 1
            self.progress['value'] = (self.time/50) * 100
            
            master.after(100,lambda:self.Timer(master))
            
        else:
            self.progress.destroy() #Destroys the progres bar after it has finished 

            tk.messagebox.showerror("Out of time", "You have run out of time!")

######################################################################### Buttons & Labels End Q1 #########################################################################


class Question2(tk.Frame):
      
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ######################################################################### Buttons & Labels Q2 #########################################################################
        self.time = 50
        img11 = tk.PhotoImage(file= "Question_2.png")
        img11= img11.subsample(2)


        imgQ2 = tk.Label(self, image = img11)
        imgQ2.place(relx =0.5, rely = 0.5, anchor= "center")
        imgQ2.image = img11

        self.Entry_1 = tk.Entry(self, font=('Arial', 14))  
        self.Entry_1.place(relx = 0.275, rely = 0.55)

        self.Entry_2 = tk.Entry(self, font=('Arial', 14))  
        self.Entry_2.place(relx = 0.275, rely = 0.75)

        self.Entry_3 = tk.Entry(self, font=('Arial', 14))
        self.Entry_3.place(relx = 0.375, rely = 0.9)

        self.check = tk.Button(self, text="Check",command = lambda: self.append2_list()) #Check buttons runs the above code
        self.check.place(relx =0.8, rely = 0.5725, anchor= "center")

        self.progress = Progressbar(self, orient='horizontal',length=500,mode='determinate')
        self.progress['value']=100
        self.progress.pack()
        self.Timer(master)

        #This section of the code simply instantiates the labels, images and buttons that are required for the game.

    def Timer(self,master):
        
        if self.time > 0:
            self.time -= 1
            self.progress['value'] = (self.time/50) * 100
            
            master.after(100,lambda:self.Timer(master))
            
        else:
            self.progress.destroy() #Destroys the progres bar after it has finished 

            tk.messagebox.showerror("Out of time", "You have run out of time!")

  # This section of the code simply instantiates the labels and images that are required for the game. #### FIXIXIXIXIIX

        
    def append2_list(self):
        Question2.student_ans = [self.Entry_1.get(),self.Entry_2.get(),self.Entry_3.get() ]# a varibale called answer_list stores the value from the entry box

        check = all(item.isdigit() for item in Question2.student_ans) 

        if(bool(check)) == True:
            print("This code is executing")
            two(self.master)
        else:

            invalid = ([x for x in Question2.student_ans if not str(x).isdigit()])
            print(invalid)
            tk.messagebox.showerror("Invalid Entry",  "The entry(s) you have made are invalid. \nConsider changing the following entries : " + str(invalid))



    #This section of the code simply retrieves the entries from the user and stores them into a variable (Question3.student_ansQ3)
    #A variable 'check' which returns a boolean value finds if all the entries are digits and if this is the case ;
    #The class three(self.master) is run, which finds out if all the values the digits the user has entered match the correct answers, otherwise -
    #invalidQ3 stores all the values 'x' in the list 'Question3.student_ansQ3' that arnt digits and display them on a tkinter error box.




class Question3(tk.Frame):
      
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.time = 50 #seconds
        
        self.master = master


        img12 = tk.PhotoImage(file= "Question3.png")
        img12= img12.subsample(2)


        Question3 = tk.Label(self, image = img12)
        Question3.place(relx =0.5, rely = 0.5, anchor= "center")
        Question3.image = img12

        self.Entry_4 = tk.Entry(self, font=('Arial', 14))  
        self.Entry_4.place(relx = 0.375, rely = 0.315)

        self.Entry_5 = tk.Entry(self, font=('Arial', 14))  
        self.Entry_5.place(relx = 0.375, rely = 0.54)

        self.Entry_6 = tk.Entry(self, font=('Arial', 14))
        self.Entry_6.place(relx = 0.375, rely = 0.725)

        self.Entry_7 = tk.Entry(self, font=('Arial', 14))
        self.Entry_7.place(relx = 0.375, rely = 0.905)

        self.checkQ3 = tk.Button(self, text="Check",command = lambda: self.append_listQ3()) #Check buttons runs the above code
        self.checkQ3.place(relx =0.8, rely = 0.5725, anchor= "center")
        
        self.progress = Progressbar(self, orient='horizontal',length=500,mode='determinate')
        self.progress['value']=100
        self.progress.pack()
        self.Timer(master)

        #This section of the code simply instantiates the labels, images and buttons that are required for the game.

    def Timer(self,master):
        
        if self.time > 0:
            self.time -= 1
            self.progress['value'] = (self.time/50) * 100
            
            master.after(100,lambda:self.Timer(master))
            
        else:
            self.progress.destroy() #Destroys the progres bar after it has finished 

            tk.messagebox.showerror("Out of time", "You have run out of time!")

            
    def append_listQ3(self):
        
                Question3.student_ansQ3 = [self.Entry_4.get(),self.Entry_5.get(),self.Entry_6.get(), self.Entry_7.get()]
                check = all(item.isdigit() for item in Question3.student_ansQ3) # Checks if all the values enters CAN be represented as intergers (whole numbers)

                if(bool(check)) == True:
                    three(self.master)
                    
                else:
                    invalidQ3 = ([x for x in Question3.student_ansQ3 if not str(x).isdigit()])
                    print(invalidQ3)
                    
                    tk.messagebox.showerror("Invalid Entry",  "The entry(s) you have made are invalid. \nConsider changing the following entries : " + str(invalidQ3))
    #This section of the code simply retrieves the entries from the user and stores them into a variable (Question3.student_ansQ3)
    #A variable 'check' which returns a boolean value finds if all the entries are digits and if this is the case ;
    #The class three(self.master) is run, which finds out if all the values the digits the user has entered match the correct answers, otherwise -
    #invalidQ3 stores all the values 'x' in the list 'Question3.student_ansQ3' that arnt digits and display them on a tkinter error box.
                    
    
class wrong_entry:

  which_answrong = []
   
  def readcsv():
    answer_list = [] 
    
    f = open('values.csv','r') # opens the csv file
    num_lines = sum(1 for line in open('values.csv','r'))
    for i in range(0,num_lines):
      line = f.readline()
      line = line.rstrip()
      questions = line.split(",")
      correct_ans = [string for string in questions if string != ""]
      answer_list.append(correct_ans)

    f.close() 
    return answer_list

    # The block of code above, opens the csv file 'values.csv'
    # The number of lines in the csv are counted
    # From 0 lines to the number of lines present in the csv - 
    # Each line is read and any trialing characters are removed
    # The split function, seperates each line into its own list
    # correct_ans stores each value in questions if cell is not empty
    # This is appended

  def findincorrectQ2(answer_list,master):
    if answer_list[0] == Question2.student_ans:
        master.switch_frame(Question3)
        tk.messagebox.showinfo(title="Nice work!!!", message="congratulations - you have once again passed this stage. The last question is coming up!")


    else:
        for i in range(len(Question2.student_ans)):
          if Question2.student_ans[i] == answer_list[0][i]: 
            
            print("CORRECT")
            
          else:
            print("INCORRECT")
            wrong_entry.which_answrong.append(Question2.student_ans[i])
            print(wrong_entry.which_answrong)
            wrong_entry.which_answrong.clear()
            
    # This function above reads the first line of the csv file (answer_list[0]) and if all values match the student's answers
    # The info box alerting the user that all the entries are correct is displayed and the frame is switched to Q3.
    # Otherwise, each entry that the student enters is checked against the csv file within the first line & ans every cell value ; i
    # If this specific entry matches the cell value - then 'correct is printed'
    # Otherwise, Incorrect is printed, and the value is appended to the empty which_answrong list, which is printed
    # THis is subsequently cleared, so that each time the user makes another entry the list is empty and doesnt store the previous answers.


  def findincorrectQ3(answer_list,master):
    if answer_list[1] == Question3.student_ansQ3:
        master.switch_frame(Question2)

    else:
        for i in range(len(Question3.student_ansQ3)):
          if Question3.student_ansQ3[i] == answer_list[1][i]: # within answer list (the first line,) each if each student ans matches the csv
            print("CORRECT")

          else:
            print("INCORRECT")

            wrong_entry.which_answrong.append(Question3.student_ansQ3[i])
            print(wrong_entry.which_answrong)
            wrong_entry.which_answrong.clear()

    # This code simply has the same intended function as desribed above, only difference being that this runs for Question 3.
    
class two:
    def __init__(self,master):
      self.master = master
      classwrong_entry = wrong_entry
      answer_list = wrong_entry.readcsv()
      wrong_entry.findincorrectQ2(answer_list,master)

#This section of the code does the following:
#Initalize's master (so that when this is called in the wrong entry class - the frame is switched)
#Creates a variable "answer_list" and calls the function readcsv (in the wrong_entry class)
#Runs the answer_list function inaddition to the findincorrectQ2 function and then run the function to detect if all entries in the -
#Question 2 class are the same as the values in the csv file.
      


class three:
    def __init__(self,master):
      self.master = master
      classwrong_entry = wrong_entry
      answer_list = wrong_entry.readcsv()
      wrong_entry.findincorrectQ3(answer_list,self.master)
      
#This section of the code does the following:
#Initalize's master (so that when this is called in the wrong entry class - the frame is switched)
#Creates a variable "answer_list" and calls the function readcsv (in the wrong_entry class)
#Runs the answer_list function inaddition to the findincorrectQ3 function to read the csv file and then run the function to detect if all entries in the -
#Question 3 class are the same as the values in the csv file.

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('530x540')
    app.maxsize(530, 540)
    app.minsize(530, 540)
    app.mainloop()

#This section of code prevents select code (from imported modules) to be run.
#Sets the geometry of the game and fixes the max min size of the game.








#Switching frames from Q3 class    
