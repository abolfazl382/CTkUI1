import customtkinter

class SegmentedFrame(customtkinter.CTkFrame):
    color = 'transparent'
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color=self.color)

        self.grid_columnconfigure(0, weight=1)

        segmented_controller = customtkinter.StringVar(value='Value2')
        self.segmented = customtkinter.CTkSegmentedButton(self,
                                                          values=['Value1', 'Value2', 'Value3'],
                                                          variable=segmented_controller
                                                          )
        self.segmented.grid(row=0, column=0, sticky='ew', padx=15, pady=(15, 0))

        self.progress1 = customtkinter.CTkProgressBar(self)
        self.progress1.grid(row=1, column=0, sticky='ew', padx=15, pady=(15, 0))

        self.progress2 = customtkinter.CTkProgressBar(self)
        self.progress2.grid(row=2, column=0, sticky='ew', padx=15, pady=(15, 0))

        self.slider1 = customtkinter.CTkSlider(self, )
        self.slider1.grid(row=3, column=0, sticky='ew', padx=15, pady=(15, 0))

        self.slider2 = customtkinter.CTkSlider(self, orientation='vertical')
        self.slider2.grid(row=0, column=1, rowspan=8, sticky='ew', padx=15, pady=(15, 0))

        self.progress3 = customtkinter.CTkProgressBar(self, orientation='vertical')
        self.progress3.grid(row=0, column=2, rowspan=8 ,sticky='ew', padx=15, pady=(15, 0))