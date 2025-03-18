import customtkinter

class MyTab(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



        self.add('tab1')
        self.add('tab2')
        self.add('tab3')

        self.tab('tab1').grid_columnconfigure(0, weight=1)

        self.option = customtkinter.CTkOptionMenu(self.tab('tab1'), values=['a', 'b', 'c'])
        self.option.grid(row=0, column=0, sticky='ew', padx=55, pady=(15, 0))

        self.combo = customtkinter.CTkComboBox(self.tab('tab1'), values=['a', 'b', 'c'])
        self.combo.grid(row=1, column=0, sticky='ew', padx=55, pady=(15, 0))

        self.btn = customtkinter.CTkButton(self.tab('tab1'), text='OK')
        self.btn.grid(row=2, column=0, sticky='ew', padx=55, pady=(15, 0))