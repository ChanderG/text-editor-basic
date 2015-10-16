# Simple text editor using tkinter

import Tkinter as tk 

class Editor(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("text-editor-basic")
        self.pack(fill=tk.BOTH, expand=1)

def main():
    root = tk.Tk()
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
