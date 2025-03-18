import customtkinter

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.check1 = customtkinter.CTkCheckBox(self)
        self.check2 = customtkinter.CTkCheckBox(self)
        self.switch1 = customtkinter.CTkSwitch(self)
        self.switch2 = customtkinter.CTkSwitch(self)

        self.check1.grid(row=0, column=0, sticky='ew', padx=15, pady=(15, 0))
        self.check2.grid(row=1, column=0, sticky='ew', padx=15, pady=(15, 0))
        self.switch1.grid(row=2, column=0, sticky='ew', padx=15, pady=(15, 0))
        self.switch2.grid(row=3, column=0, sticky='ew', padx=15, pady=(15, 0))
