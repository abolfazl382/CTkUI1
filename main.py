import customtkinter
from sidebar import Sidebar
from tabview import MyTab
from radiobtn import RadioFrame
from segmented import SegmentedFrame
from checkbox import CheckboxFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1100x500')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)

        self.grid_rowconfigure((0, 1, 2), weight=1)

        ######### sidebar
        self.sidebar = Sidebar(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky='nsew')

        ######## text box
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=1, sticky='nsew', padx=15, pady=20)

        ####### tab view
        self.tabview = MyTab(self)
        self.tabview.grid(row=0, column=2, sticky='nsew', padx=(0, 15), pady=15)

        ###### radio button
        self.radio = RadioFrame(self)
        self.radio.grid(row=0, column=3, sticky='nsew', padx=(0, 15), pady=15)

        ###### segmented
        self.segmentedFrame = SegmentedFrame(self)
        self.segmentedFrame.grid(column=1, row=1, columnspan=2, sticky='nsew', padx=15)

        ####### check box
        self.checkboxFrame = CheckboxFrame(self)
        self.checkboxFrame.grid(column=3, row=1, sticky='nsew', padx=(0, 15))


if __name__ == '__main__':
    app = App()
    app.mainloop()