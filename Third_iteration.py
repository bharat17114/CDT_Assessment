import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True) # 

class StartPage(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)


        img1 = tk.PhotoImage(file= "Start_image.png")
        img1= img1.subsample(2) # changes the size of the image


        start_image = tk.Label(self, image= img1)
        start_image.place(relx =0.5, rely = 0.5, anchor= "center")
        start_image.image = img1

        
        img2 = tk.PhotoImage(file= "Next_icon.png")
        img2 = img2.subsample(8)

        Next_image = tk.Button(self, image = img2, command=lambda: master.switch_frame(PageOne))
        Next_image.place(relx =0.5, rely = 0.825, anchor= "center")
        Next_image.image = img2




class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)

 
        tk.Button(self, text="Go to page 2 ",command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text = "wrong answer" , command = lambda:self.wrong_answer()).pack()

        self.testwrong = tk.Label(self, text = "try again")

        img3 = tk.PhotoImage(file= "Intro_1.png")
        img3 = img3.subsample(2)

        Intro_page = tk.Label(self, image = img3)
        Intro_page.place(relx =0.5, rely = 0.50, anchor= "center")
        Intro_page.image = img3

        #tk.Button(self, text="Return to start page",
         #         command=lambda: master.switch_frame(StartPage)).pack()
 
        Page_1_next = tk.Button(self, text="Go to page 2 ",command=lambda: master.switch_frame(PageTwo))
        Page_1_next.place(relx =0.5, rely = 0.9, anchor= "center")

        #tk.Button(self, text = "wrong answer" , command = lambda:self.wrong_answer()).pack()

        self.testwrong = tk.Label(self, text = "try again")
    
        
  
    def wrong_answer(self):
        self.testwrong.pack()



class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
      #  tk.Button(self, text="Return to start page",
                 # command=lambda: master.switch_frame(StartPage)).pack()


        img4 = tk.PhotoImage(file= "Intro_2.png")
        img4 = img4.subsample(2)

        Intro_page2 = tk.Label(self, image = img4)
        Intro_page2.place(relx =0.5, rely = 0.5, anchor= "center")
        Intro_page2.image = img4


        Page_2_next = tk.Button(self, text="Go to page 2 ",command=lambda: master.switch_frame(PageThree))
        Page_2_next.place(relx =0.5, rely = 0.9, anchor= "center")


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        img5 = tk.PhotoImage(file= "Intro_3.png")
        img5 = img5.subsample(2)

        
        Intro_page3 = tk.Label(self, image = img5)
        Intro_page3.place(relx =0.5, rely = 0.5, anchor= "center")
        Intro_page3.image = img5

        Page_3_next = tk.Button(self, text="Go to page 2 ",command=lambda: master.switch_frame(Question1))
        Page_3_next.place(relx =0.5, rely = 0.9, anchor= "center")

        
class Question1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


        img6 = tk.PhotoImage(file= "Question_1.png")
        img6 = img6.subsample(2)

      
        Question_3 = tk.Label(self, image = img6)
        Question_3.place(relx =0.5, rely = 0.5, anchor= "center")
        Question_3.image = img6

        
        img7 = tk.PhotoImage(file= "Option1.png")
        img7 = img7.subsample(14)

        answer_1 = tk.Button(self, image = img7)
        answer_1.place(relx =0.35, rely = 0.92, anchor= "center")
        answer_1.image = img7


        img8 = tk.PhotoImage(file= "Option2.png")
        img8 = img8.subsample(17)

        answer_2 = tk.Button(self, image = img8)
        answer_2.place(relx =0.5, rely = 0.92, anchor= "center")
        answer_2.image = img8


        img9 = tk.PhotoImage(file= "Option3.png")
        img9 = img9.subsample(17)

        answer_3 = tk.Button(self, image = img9)
        answer_3.place(relx =0.65, rely = 0.92, anchor= "center")
        answer_3.image = img9

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('530x540')
    app.mainloop()
