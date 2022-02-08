from tkinter import *
import tkinter as tk
import sys
from constants import *
from Easy import *
from Medium import *
from Hard import *
from Database import *
from tkinter.messagebox import askyesno



### main_frame , start_frame, setting_frame, about_frame


class main_frame(tk.Frame):

    def __init__(self, parent, root):
        super().__init__(parent)
        top_label = tk.Label(self, text="PC Shooting Practice Game", font=("Arial", 40), bg="blue", fg="white")
        top_label.pack(ipadx=70, ipady=10)

        start = tk.Button(self, text="Start", font=("Arial", 20), command=lambda: root.show_frame(start_frame))
        start.pack(ipadx=20, pady=50)

        settings = tk.Button(self, text="Settings", font=("Arial", 20), command=lambda: root.show_frame(setting))
        settings.pack()

        about = tk.Button(self, text="About", font=("Arial", 20), command=lambda: root.show_frame(about_frame))
        about.pack(ipadx=15, pady=50)

        exit = tk.Button(self, text="Exit", font=("Arial", 20), command=lambda:Exit_func())
        exit.pack(ipadx=30)

        def Exit_func():
            con.click_sound.play()
            sys.exit()


class start_frame(tk.Frame):
    def __init__(self, parent, root):
        self.root = root
        super().__init__(parent)

        easy = tk.Button(self, text="Easy", font=("Arial", 20), command=lambda: self.button_pressed(1))
        easy.pack(ipadx=30, ipady=10, pady=65)

        medium = tk.Button(self, text="Medium", font=("Arial", 20),command=lambda: self.button_pressed(2))
        medium.pack(ipadx=20, ipady=10)

        hard = tk.Button(self, text="Hard", font=("Arial", 20),command=lambda: self.button_pressed(2))
        hard.pack(ipadx=40, ipady=10, pady=65)

        back = tk.Button(self, text="Back", font=("Arial", 20), command=lambda: root.show_frame(main_frame))
        back.pack(ipadx=40, ipady=10)

    def button_pressed(self, game_type):
        con.click_sound.play()
        self.root.show_frame(chooseCrosshair_frame)
        con.game_type = game_type


class about_frame(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        a = "This game is to enhance the PC gamer Rection Time"
        b = "All the components are free to use and can  "
        c = "be used in any non commercial projects.            "
        d = "It is based on Python(Tkinter,pygame)                "

        f = "YoutubeLink:                                                        "
        g = "Thankyou"
        h = "Tarun"

        label = tk.Label(self, text=a + "\n" + b + "\n" + c + "\n" + d + "\n"  + "\n" + f + "\n\n\n" + g + "\n" + h,
                         font=("Arial", 20))
        label.pack(pady=20)

        back = tk.Button(self, text="Back", font=("Arial", 20), command=lambda: root.show_frame(main_frame))
        back.pack(ipadx=65)

class setting(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)

        label = Label(self, text = "No of max Targets  : "+str(con.no_of_targets), font=("Arial", 20))
        label.grid(row=0,column=0,pady = 30)

        input = tk.Text(self, height=2, width=25, font=("Arial", 20))
        input.grid(row=1,column=0)

        help = tk.Button(self, text="?", font=("Arial", 20), command=lambda: help())
        help.grid(row=1, column=1)


        ok = tk.Button(self, text="Ok", font=("Arial", 20), command=lambda: change_value())
        ok.grid(row=1,column=2,padx = 30,pady = 40)

        back = tk.Button(self, text="Back", font=("Arial", 20), command=lambda: root.show_frame(main_frame))
        back.grid(row=2,column=1,pady = 40)

        reset = tk.Button(self, text="Reset", font=("Arial", 20), command=lambda: reset())
        reset.grid(row = 3,column = 2)

        def change_value():
            con.click_sound.play()
            value = input.get("1.0","end-1c")
            try:
                 int(value)
            except:
                tk.messagebox.showwarning("Warning!!!","Please fill a correct integer value")
                pass


            if value :
                con.no_of_targets = value
                max_noOfshot(value)
                label.configure(text = "No of max Targets  : "+str(value))
                tk.messagebox.showinfo(message="you successfully updated data")

        def reset():
            con.click_sound.play()
            answer = askyesno(message="Do you want to reset the data ???")
            if answer:
                reset_data()
                tk.messagebox.showinfo(message="your saved data is reseted")
            pass

        def help():
            con.click_sound.play()
            tk.messagebox.showinfo(message="Fill the maximum number of target you want in one turn\n"
                                           "But do remember the delay will decrease beween two targets\n"
                                           "every time you shoot.")




class chooseCrosshair_frame(tk.Frame):
    def __init__(self, parent, root):
        self.root = root
        super().__init__(parent)

        ### create cursor image matrix
        self.cursor_matrix = []
        self.row = 0
        for i in range(0, 3):
            self.cursor_column = []
            for j in range(0, 4):
                self.cursor_column.append(PhotoImage(file=con.img_path[self.row]))
                self.row += 1
            self.cursor_matrix.append(self.cursor_column)

        ### creatre btn matrix
        self.btn_matrix = []
        for i in range(0, 3):
            self.columns = []
            for j in range(0, 4):
                self.columns.append(tk.Button(self, image=self.cursor_matrix[i][j],
                                              command=lambda i=i,j=j: self.btn_function(i,j)))

                self.columns[j].grid(row=i, column=j, padx=25, pady=30, ipadx=40, ipady=30, sticky=E + W + N + S)
            self.btn_matrix.append(self.columns)

        back = tk.Button(self, text="Back", font=("Arial", 20), command=lambda: root.show_frame(main_frame))
        back.grid(row=3, column=3, padx=30, pady=10)



    ### fun defines what happens if we choose a crosshair type

    def btn_function(self, a, b):

        con.click_sound.play()

        ### make all button raised except the one we pressed
        for i in range(0, 3):
            for j in range(0, 4):
                self.btn_matrix[i][j].configure(state=NORMAL, relief=RAISED)

        con.crosshair_type = 4 * a + b

        ### choose gametype
        if con.game_type == 1:
            self.root.show_frame(start_frame)
            game_obj = Easy(con.crosshair_type)


            pass
        elif con.game_type == 2:
            self.root.show_frame(start_frame)
            game_obj = medium(con.crosshair_type)
            pass
        elif con.game_type == 3:
            self.root.show_frame(start_frame)
            game_obj = hard(con.crosshair_type)
            pass

        pass


######################### Creating the main Window Class ########################

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600+300+50")
        self.resizable(False, False)
        self.title("Shooting Game PC")
        icon = PhotoImage(file="Files/Images/icon.png")
        self.iconphoto(False, icon)

        ########### create root Frame
        root_F = tk.Frame(self)
        root_F.pack()

        ### create a list of frames

        self.Frames = {}
        for F in (main_frame, start_frame, about_frame, chooseCrosshair_frame,setting):
            frame = F(root_F, self)
            self.Frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  ##### important line
        self.show_frame(main_frame)

    def show_frame(self, f_name):
        con.click_sound.play()
        frame = self.Frames[f_name]
        frame.tkraise()

if __name__ == '__main__':
   win = window()

   win.mainloop()
