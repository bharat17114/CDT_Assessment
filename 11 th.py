
import tkinter as tk
from tkinter import messagebox
import csv
from tkinter.ttk import *
import time

#Importing
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Question3)
        #### might need to delete this above
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True) # 


class Question2(tk.Frame):
      
  def __init__(self, master):
      tk.Frame.__init__(self, master)
      
######################################################################### Buttons & Labels Q2 #########################################################################

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
    
      self.check = tk.Button(self, text="Check",command = lambda: append2_list(self)) #Check buttons runs the above code
      self.check.place(relx =0.8, rely = 0.5725, anchor= "center")


      # This section of the code simply instantiates the labels and images that are required for the game.
      
      def append2_list(self):
            Question2.student_ans = [self.Entry_1.get(),self.Entry_2.get(),self.Entry_3.get() ]# a varibale called answer_list stores the value from the entry box

            check = all(item.isdigit() for item in Question2.student_ans) 
            
            if(bool(check)) == True:
                print("This code is executing")
                two()


            else:

                invalid = ([x for x in Question2.student_ans if not str(x).isdigit()])
                print(invalid)
                tk.messagebox.showerror("Invalid Entry",  "The entry(s) you have made are invalid. \nConsider changing the following entries : " + str(invalid))


        # A varibale called student_ans stores the value from the entry box, (these are the various entries into the entry boxes)
        # A variable 'check' returns a True/False value if all the entries are digits

        # If all entries are digits then class two() is called
        # Otherwise, a list is created that finds all entries in Question2.student_ans that are not digits
        # A error box displays these entries

class Question3(tk.Frame):


    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.time = 50 #seconds



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
        
        self.progress = Progressbar(self,orient='horizontal',length=500,mode='determinate')
        self.progress['value']=100
        self.progress.pack()
        self.Timer(master)

        #This section of the code simply instantiates the labels, images and buttons that are required for the game.

    def Timer(self,master):
        if self.time > 0:
            self.time -= 1
            self.progress['value'] = (self.time/50) * 100
            
            master.after(1000,lambda:self.Timer(master))
            
        else:
            print("Loser")
            
    def append_listQ3(self):
        
                Question3.student_ansQ3 = [self.Entry_4.get(),self.Entry_5.get(),self.Entry_6.get(), self.Entry_7.get()]
                check = all(item.isdigit() for item in Question3.student_ansQ3) # Checks if all the values enters CAN be represented as intergers (whole numbers)

                if(bool(check)) == True:
                    three()
                    
                else:
                    
                    invalidQ3 = ([x for x in Question3.student_ansQ3 if not str(x).isdigit()])
                    print(invalidQ3)
                    
                    tk.messagebox.showerror("Invalid Entry",  "The entry(s) you have made are invalid. \nConsider changing the following entries : " + str(invalidQ3))
                
        # A varibale called student_ans stores the value from the entry box, (these are the various entries into the entry boxes)
        # A variable 'check' returns a True/False value if all the entries are digits

        # If all entries are digits then class two() is called
        # Otherwise, a list is created that finds all entries in Question2.student_ans that are not digits
        # A error box displays these entries


class wrong_entry:
  which_answrong = []

  currentscore = 0
  gainscore = 10
  def readcsv():
    answer_list = [] # Initialize  variable temp list

    
    f = open('values.csv','r') # opens the csv file
    num_lines = sum(1 for line in open('values.csv','r'))
    #print("This file has",num_lines,"lines")
    for i in range(0,num_lines): # for every line after that format and append to list
      line = f.readline()
      line = line.rstrip()       #removes trailing characters from line
      questions = line.split(",")
      correct_ans = [string for string in questions if string != ""]
      answer_list.append(correct_ans)

    f.close() # close the file

    # The block of code above, opens the csv file 'values.csv'
    # The number of lines in the csv are counted
    # From 0 lines to the number of lines present in the csv - 
    # Each line is read and any trialing characters are removed
    # The split function, seperates each line into its own list
    # correct_ans stores each value in questions if cell is not empty
    # This is appended
    

    return answer_list
  def findincorrectQ1(answer_list):
    if answer_list[0] == Question2.student_ans:
        print("All entries in Q1 are right")

    else:
        for i in range(len(Question2.student_ans)):
          if Question2.student_ans[i] == answer_list[0][i]: # within answer list (the first line,) each if each student ans matches the csv
            print("CORRECT")
            
          else:
            print("INCORRECT")
            wrong_entry.which_answrong.append(Question2.student_ans[i])
            print(wrong_entry.which_answrong)
            wrong_entry.which_answrong.clear()
    # This function above reads the first line of the csv file (answer_list[0]) and if all values match the student's answers
    # All entries correct is printed

    # Otherwise, each entry that the student enters is checked against the csv file within the first line & ans every cell value ; i
    # If this specific entry matches the cell value - then 'correct is printed'
    # Otherwise, Incorrect is printed, and the value is appended to the empty which_answrong list, which is printed
    # THis is subsequently cleared, so that each time the user makes another entry the list is empty and doesnt store the previous answers.

  def add_score():
    currentscore += gainscore
    print(currentscore)

        
  def findincorrectQ2(answer_list):
    if answer_list[1] == Question3.student_ansQ3:
        print("All entries in Q1 are right")

    else:
        for i in range(len(Question3.student_ansQ3)):
          if Question3.student_ansQ3[i] == answer_list[1][i]: # within answer list (the first line,) each if each student ans matches the csv
            print("CORRECT")

            add_score()

            
          else:
            print("INCORRECT")
            wrong_entry.which_answrong.append(Question3.student_ansQ3[i])
            print(wrong_entry.which_answrong)
            wrong_entry.which_answrong.clear()
            
    # This code simply has the ame intended function as desribed above, only difference being that this runs for Question 3
class two:

    def __init__(self):
      classwrong_entry = wrong_entry
      answer_list = wrong_entry.readcsv()
      wrong_entry.findincorrectQ1(answer_list)


class three:
    def __init__(self):
      classwrong_entry = wrong_entry
      answer_list = wrong_entry.readcsv()
      wrong_entry.findincorrectQ2(answer_list)


      



if __name__ == "__main__":
    app = SampleApp()
    app.geometry('530x540')
    app.maxsize(530, 540)
    app.minsize(530, 540)
    app.mainloop()

