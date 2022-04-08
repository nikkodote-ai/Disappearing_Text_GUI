import tkinter as tk
import tkinter.ttk as ttk

MINI_LIMIT = 5
#TODO 1: wireframe tkinter design based on squibler.io
#TODO 2: selection (can be a dropdown box, radio button if minutes or words) - no need to be fancy, goal, set difficulty
#TODO 3: when start writing is pressed, 2 timers will start
#       1 for the 'session length' the other for while FIXED,,
#       2. set to 5 seconds  or else DELETE EVERYTHING

global timer_switch, continue_timer
timer_switch = False

class MainApplication(tk.Frame):
    def __init__(self, parent):
        # TODO 1: wireframe tkinter design based on squibler.io; prototype
        # TODO 2: selection (can be a dropdown box, radio button if minutes or words) - no need to be fancy, goal, set difficulty
        # TODO 3: when start writing is pressed, 2 timers will start
        #       1 for the 'session length' the other for while FIXED,,
        #       2. set to 5 seconds  or else DELETE EVERYTHING
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=800, height = 600)
        self.canvas.grid(row= 0, column=0)

        title = tk.Label(self.canvas, text = 'The Most Dangerous Random Prompt Generator')
        title.grid(row = 0, column=0, columnspan = 3)

        #TEXTBOX
        self.entry = tk.Text(self.canvas)
        self.entry.grid(row = 1, column =0, columnspan = 2)

        #TODO bind key release function to start mini-timer
        self.mini_timer = 5

        self.entry.bind('<KeyPress>',lambda event, time_limit = MINI_LIMIT:self.start_type_timer(time_limit, event))

        # after 5 seconds, check if timer is ok

        #TODO bind space release, count words

        #make radiobutton to choose if words or minutes
        self.r = tk.BooleanVar()
        self.r.set(True)
        self.clicked(self.r)
        minute_radio = tk.Radiobutton(self.canvas, text = 'Set Difficulty by MINUTES', variable = self.r, value = True, command = lambda: self.clicked(self.r.get()))
        minute_radio.grid(row = 2, column = 0)
        words_radio = tk.Radiobutton(self.canvas, text = 'Set Difficulty by WORDS', variable = self.r, value = False, command = lambda: self.clicked(self.r.get()))
        words_radio.grid(row = 2, column = 1)


        #BUTTONS
        generate_button = tk.Button(text='Generate New Prompt', command=self.generate_prompt)
        generate_button.grid(row=4, column=0,)

        start_button = tk.Button(text='Start Writing', command=self.start_writing)
        start_button.grid(row=4, column=1,)

        #if initialize timer
        self.timer = None


    ##create dropdown menu
    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label.config(text = self.timer)
            self.after(1000, self.update_timer)

        else:
            self.entry.delete(1.0, tk.END)
            popup = tk.Toplevel()
            tk.Label(popup, text = "TIME'S UP").grid(column=0, row=0)


    def start_type_timer(self, reset_time, event):
        """ when key is pressed, start the timer, then check every 0.50."""
        self.canvas.after_cancel(self.canvas)
        if event != None:
            self.mini_timer = 5
            # return self.mini_timer
            print(f'KEY PRESSED, {self.mini_timer}')

            self.canvas.after(1000, lambda x=MINI_LIMIT: self.start_type_timer(x, None))
            return self.mini_timer

        elif event == None:
            self.mini_timer -= 1
            print(f'no key pressed, {self.mini_timer}')
            self.canvas.after(1000, lambda x=self.mini_timer: self.start_type_timer(x, None))
            return self.mini_timer

            if self.mini_timer < 0:
                print(reset_time)
                self.entry.delete(1.0, tk.END)






    def clicked(self, value):
        # make a dropbox for the difficulty
        ##initial value:
        difficulty = tk.StringVar()

        if value:
            options = ['0', '3', '5', '10', '15', '20', '30', '60']
            difficulty.set(options[0])
            self.dropdown = ttk.Combobox(self.canvas, values=options, state = 'readonly') #convert to int later, else prompt select minute

        else:
            options = ['75', '150', '250', '500', '1700']
            difficulty.set(options[0])
            self.dropdown = ttk.Combobox(self.canvas, values=options, state = 'readonly') #convert to int later, else prompt select minute
        self.dropdown.grid(row = 3, column = 0, columnspan = 3)


    def generate_prompt(self):
        pass

    def start_writing(self):
        if self.r.get():
            # countdowntimer
            self.timer =int(self.dropdown.get()) * 60
            print(f'{self.timer} seconds')
            self.timer_label = tk.Label(text=self.timer)
            self.timer_label.grid(row=1, column=1)
            self.update_timer()
            #TODO: function to start timer

            global timer_switch
            timer_switch = True

        else:
            self.word_count = len(self.entry.get())


            #TODO:function check word count
            #recursive counter like timer



if __name__ =='__main__':
    root = tk.Tk()
    MainApplication(root).grid()
    root.mainloop()
