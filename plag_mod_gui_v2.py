import tkinter
import tkinter.messagebox
import customtkinter

from tkinter import filedialog
import plag
MAXSIM = 50

file_loc1 =""
file_loc2 = ""

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CheaterCatcher")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CheaterCatcher",
                                              text_font=("Roboto Medium", -16))  
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Check Plagiarism",
                                                command=self.plag_per)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="CTkButton",
        #                                         command=self.button_event)
        # self.button_2.grid(row=3, column=0, pady=10, padx=20)



        self.button_11 = customtkinter.CTkButton(master=self.frame_right,
                                                text="File 1",
                                                command= lambda:self.browseFiles(1))
        self.button_11.grid(row=5, column=0, pady=10, padx=20)

        self.button_22 = customtkinter.CTkButton(master=self.frame_right,
                                                text="File 2",
                                                command= lambda:self.browseFiles(2))
        self.button_22.grid(row=5, column=1, pady=10, padx=20)

        self.button_33 = customtkinter.CTkButton(master=self.frame_right,
                                                text="exit",
                                                command=exit)
        self.button_33.grid(row=8, column=1, pady=10, padx=20)



        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")


        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

  
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Enter your files here \n"  , text_font = ("Roberto", 22, 'bold'),
                                                   height=100,
                                                   corner_radius=6,  
                                                   fg_color=("white", "gray38"),  
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        self.label_info_11 = customtkinter.CTkLabel(master=self.frame_info, anchor = 'center', 
                                                   text="Enter File 1 \n"  , text_font = ("Roberto", 14, 'bold'),
                                                   height=30,
                                                   corner_radius=6, 
                                                   fg_color=("white", "gray38"), 
                                                   justify=tkinter.LEFT)
        self.label_info_11.grid(column=0, row=1, sticky="nwe", padx=15, pady=5)

        self.label_info_22 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Enter File 2 \n"  , text_font = ("Roberto", 14, 'bold'),
                                                   height=30,
                                                   corner_radius=6,  
                                                   fg_color=("white", "gray38"),  
                                                   justify=tkinter.LEFT)
        self.label_info_22.grid(column=0, row=2, sticky="nwe", padx=15, pady=5)


        self.progress = customtkinter.CTkLabel(master=self.frame_info , text = "allowed percent of plagiarism ?: 50" )

        self.progress.grid(row=6, column=0, pady=5, padx=20, sticky="we") #, sticky="we"
        
        self.slider_2 = customtkinter.CTkSlider(master=self.frame_info,
                                                from_ = 0 , to = 100  ,number_of_steps=100,
                                                orient='horizontal',
                                                command = lambda x:self.per2(x))
        self.slider_2.set(50)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.enter_button = customtkinter.CTkButton(master=self.frame_info, text = "enter" ,command=self.per)
        # self.enter_button.grid(row=7, column=0, pady=5, padx=20 )


    def button_event(self,x):
        print("Button pressed")

    def per2(self,x):
        global MAXSIM
        MAXSIM = x
        self.progress.configure(text = "allowed percent of plagarism ?: %d"%x )


    def browseFiles(self,n):
        initial = "C:/Users/rudra/Desktop/engineering/sem5/software engineering/project1/plag"
        filename = filedialog.askopenfilename(initialdir = initial,title = "Select a File",filetypes = (("Text files","*.txt*"),))
        global file_loc1
        global file_loc2
        if n==1:
            self.label_info_11.configure(text="File Opened: "+filename[filename.rindex('/'):])
            file_loc1 = filename
        elif n==2:
            self.label_info_22.configure(text="File Opened: "+filename[filename.rindex('/'):])
            file_loc2 = filename

    def plag_per(self):
        #if file_loc1 == "" or file_loc2 == "":
        global MAXSIM
        plags = 100 * plag.plag_rate(file_loc1,file_loc2)
        if plags != -100:
            self.label_info_1.configure(text = "Plagiarism Percentage is %.2f" %  plags ,fg_color=("white", "gray38"))
            print(MAXSIM,plags)
            if plags >= MAXSIM:
                self.label_info_1.configure(text = "Plagiarism Percentage is %.2f \nDocument is Plagiarised" %  plags ,fg_color=("salmon"))
        else: 
            self.label_info_1.configure(text = "File size too large or 0",fg='red')

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()