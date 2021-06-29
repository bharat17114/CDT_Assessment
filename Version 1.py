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
        img1 = tk.PhotoImage(file= "Start_image.png")
        img1= img1.subsample(2)
        tk.Frame.__init__(self, master)
        start_image = tk.Label(self, image= img1)
        start_image.place(relx =0.5, rely = 0.5, anchor= "center")
        start_image.image = img1
        tk.Button(self, text="Open Question 1 ",
                  command=lambda: master.switch_frame(PageOne)).pack()



class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

        tk.Button(self, text="Go to page 2 ",command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text = "wrong answer" , command = lambda:self.wrong_answer()).pack()

        self.testwrong = tk.Label(self, text = "try again")
  
    def wrong_answer(self):
        self.testwrong.pack()



class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()



class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page three").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('500x500')
    app.mainloop()
