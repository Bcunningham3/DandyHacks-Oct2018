from tkinter import *
import turtle

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.main_window()

    #Creation of main_window
    def main_window(self):

        # changing the title of our master widget
        self.master.title("Shopping List")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        QuitButton = Button(self, text="Quit", bg="orange", command=self.quit_gui)
        ShoppingListButton = Button(self, text="Enter Items", bg="orange", command=self.enteritem_window)
        ItemButton = Button(self, text="Items", bg="orange", command=self.item_button)
        QuitButton.config(height=1, width=15)
        ShoppingListButton.config(height=10, width=15)
        ItemButton.config(height=1, width=15)

        # placing the button on my window
        ShoppingListButton.place(x=140, y=80)
        QuitButton.place(x=140, y=250)
        ItemButton.place(x=140, y=40)

    def quit_gui(self):
        exit()

    def enteritem_window(self):
        pass
        #Function for Enter Items Button

    def item_button(self):
        pass
        #Function for Item Button

root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()