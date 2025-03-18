import customtkinter

class RadioFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.radio1 = customtkinter.CTkLabel(self, text='Radio buttons', font=customtkinter.CTkFont(size=16))
        self.radio1.grid(row=0, column=0, sticky='ew', padx=55, pady=(15, 0))

        radio_controller = customtkinter.IntVar(value=1)

        self.radio1 = customtkinter.CTkRadioButton(self, text='Radio1', value=1, variable=radio_controller)
        self.radio1.grid(row=1, column=0, sticky='ew', padx=55, pady=(15, 0))

        self.radio2 = customtkinter.CTkRadioButton(self, text='Radio2', value=2, variable=radio_controller)
        self.radio2.grid(row=2, column=0, sticky='ew', padx=55, pady=(15, 0))

        self.radio3 = customtkinter.CTkRadioButton(self, text='Radio3', state='disabled', value=3, variable=radio_controller)
        self.radio3.grid(row=3, column=0, sticky='ew', padx=55, pady=(15, 0))