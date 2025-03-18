import customtkinter

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(4, weight=1)

        self.myLabel = customtkinter.CTkLabel(self,
                                              text='Abolfazl',
                                              font=customtkinter.CTkFont(size=20, weight='bold')
                                              )
        self.myLabel.grid(column=0, row=0, padx=10, pady=(15, 0))

        self.btn1 = customtkinter.CTkButton(self,text='Button 1')
        self.btn1.grid(column=0, row=1, padx=10, pady=(15, 0))

        self.btn2 = customtkinter.CTkButton(self,text='Button 2')
        self.btn2.grid(column=0, row=2, padx=10, pady=(15, 0))

        self.btn3 = customtkinter.CTkButton(self,text='Button 3', state='disabled')
        self.btn3.grid(column=0, row=3, padx=10, pady=(15, 0))

        self.myOption1 = customtkinter.CTkOptionMenu(self, values=['dark', 'light', 'system'])
        self.myOption1.grid(column=0, row=5, padx=10, pady=(15, 0))

        self.myOption2 = customtkinter.CTkOptionMenu(self, values=['100%', '120%', '150%'])
        self.myOption2.grid(column=0, row=6, padx=10, pady=15)