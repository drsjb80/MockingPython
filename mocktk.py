import tkinter
from unittest import TestCase
from unittest.mock import call, PropertyMock, patch

# https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
# with some cleanup.
class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        hi_there = tkinter.Button(self)
        hi_there["text"] = "Hello World\n(click me)"
        hi_there["command"] = self.say_hi
        hi_there.pack(side="top")

        quit = tkinter.Button(self, text="QUIT", fg="red", \
            command=self.master.destroy)
        quit.pack(side="bottom")

    def say_hi():
        print("hi there, everyone!")

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()

class Testtkinter(TestCase):
    # there are two buttons created in create_widgets; it would probably be
    # better to break into two methods to more closely track the calls to
    # the PropertyMock as seen with the two calls to pack.
    def test_create_widgets(self):
        with patch("tkinter.Button", new_callable=PropertyMock) as mock_button:
            root = tkinter.Tk()
            app = Application(master=root)
            app.create_widgets()
            # print(tkinter.Button.mock_calls)
            mock_button.assert_has_calls([ \
                call().__setitem__('text', 'Hello World\n(click me)'), \
                call().pack(side='top'), \
                call().pack(side='bottom') \
            ], any_order=True)
