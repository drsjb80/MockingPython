import tkinter
import unittest
import unittest.mock
from  unittest.mock import call

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()

class Testtkinter(unittest.TestCase):
    def test_create_widgets(self):
        root = tkinter.Tk()
        tkinter.Button = unittest.mock.PropertyMock()
        app = Application(master=root)
        app.create_widgets()
        # print(tkinter.Button.mock_calls)
        tkinter.Button.assert_has_calls([ \
            call().__setitem__('text', 'Hello World\n(click me)'), \
            call().pack(side='top') \
        ], any_order=True)
