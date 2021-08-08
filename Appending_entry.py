
import tkinter as tk
from tkinter import messagebox
import csv
from tkinter import *
from tkinter.ttk import *
import time



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Question2)
        #### might need to delete this above

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True) # 


class Question2(tk.Frame):
    
  student_ans = []
  
  def __init__(self, master):
      tk.Frame.__init__(self, master)
      empty = []
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
      
      def append2_list(self):
            # prints out the lis
            Question2.student_ans = [self.Entry_1.get(),self.Entry_2.get(),self.Entry_3.get() ]# a varibale called answer_list stores the value from the entry box

            check = all(item.isdigit() for item in Question2.student_ans) # Checks if all the values enters CAN be represented as intergers (whole numbers)
            
            if(bool(check)) == True:
                print("This code is executing")
                two()


            else:

                invalid = ([x for x in Question2.student_ans if not str(x).isdigit()])
                print(invalid)
                tk.messagebox.showerror("Invalid Entry",  "The entry(s) you have made are invalid. \nConsider changing the following entries : " + str(invalid)) 


class wrong_entry:
  which_answrong = []
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

    #print(answer_list)
    f.close() # close the file

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
            
          

class two:

    def __init__(self):
      classwrong_entry = wrong_entry
      answer_list = wrong_entry.readcsv()
      wrong_entry.findincorrectQ1(answer_list)
      

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('530x540')
    app.maxsize(530, 540)
    app.minsize(530, 540)


    app.mainloop()

