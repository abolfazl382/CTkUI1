import customtkinter
from sidebar import Sidebar
from tabview import MyTab
from radiobtn import RadioFrame
from segmented import SegmentedFrame
from checkbox import CheckboxFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1100x550')
        self.title('My First CTk UI')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)

        self.grid_rowconfigure((0, 1, 2), weight=1)

        ######### sidebar
        self.sidebar = Sidebar(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky='nsew')

        ######## text box
        self.textbox = customtkinter.CTkTextbox(self, wrap='word', font=customtkinter.CTkFont(size=16), padx=5, pady=5)
        self.textbox.grid(row=0, column=1, sticky='nsew', padx=15, pady=20)

        self.file1 = open("MyFile1.txt", "r+")
        self.text = self.file1.readlines()[0]
        self.textbox.insert('end', self.text)
        self.file1.close()

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

        ###### entry
        self.myEntry = customtkinter.CTkEntry(self, placeholder_text='Entry ...')
        self.myEntry.grid(column=1, row=2, columnspan=2, sticky='ew', padx=15, pady=15)

        ####### btn
        self.btn = customtkinter.CTkButton(self, text='Button1')
        self.btn.grid(column=3, row=2, sticky='ew', padx=(0, 15), pady=15)


if __name__ == '__main__':
    app = App()
    app.mainloop()