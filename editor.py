# Simple text editor using tkinter

import Tkinter as tk 
import tkFont
import tkMessageBox
import tkFileDialog

class Editor(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("text-editor-basic")

        self.textWindow = tk.Text(font="18")
        # name of file bein edited
        self.currFileName = None
        self.textWindow.pack(fill=tk.BOTH, expand=tk.YES)

        # operations label -> echoes last operation done
        self.opsLabel = tk.Label(text = 'editor ready')
        self.opsLabel.pack(anchor='e')

        menubar = tk.Menu(self)

        # file menu 
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label='New', command = self.newFile)
        filemenu.add_command(label='Open', command = self.openFile)
        filemenu.add_command(label='Save', command = self.saveFile)
        filemenu.add_command(label='Save As', command = self.saveAsFile)
        menubar.add_cascade(label = 'File', menu=filemenu)

        formatmenu = tk.Menu(menubar)
        formatmenu.add_command(label='Increase font size', command = self.incFontSize)
        formatmenu.add_command(label='Decrease font size', command = self.decFontSize)
        formatmenu.add_command(label='Reverse colors', command = self.reverseColor)
        menubar.add_cascade(label = 'Format', menu = formatmenu)

        # help menus
        helpmenu = tk.Menu(menubar)
        helpmenu.add_command(label="About", command = self.displayAbout)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        self.parent.config(menu = menubar)

    def newFile(self):
        """ Edit a new file. """
        if tkMessageBox.askyesno('Unsaved changes', 'Are you sure? You will lose unsaved changes!'):
            self.textWindow.delete("1.0", tk.END)
            self.currFileName = None
            self.opsLabel.config(text = 'Opened new buffer for editing')

    def openFile(self):
        """ Open a new file for editing."""
        self.newFile()

        openedfilename = tkFileDialog.askopenfilename()
        # save file name
        self.currFileName = openedfilename

        openedfile = open(openedfilename, 'w')
        text = openedfile.read()
        self.textWindow.insert(tk.END, text)
        openedfile.close()

        self.opsLabel.config(text = 'Opened file "{0}" for editing'.format(self.currFileName))

    def saveFile(self):
        """ Overwrite the file being currently edited. """

        if self.currFileName == None:
            # no file being edited
            tkMessageBox.showerror('No file being edited', "Currently not editing an existing file. Use Save As to save this buffer to a filename of your choice.")
        else:
            # save the current file
            savefile = open(self.currFileName, 'w')
            text = self.textWindow.get("1.0", tk.END)
            savefile.write(text)
            savefile.close()
            self.opsLabel.config(text = 'Saved file "{0}"'.format(self.currFileName))


    def saveAsFile(self):
        """ Save contents to a file.
        
        Simple brute force overwriting.
        """
        savefilename = tkFileDialog.asksaveasfilename()

        # note down file name
        self.currFileName = savefilename

        savefile = open(savefilename, 'w')
        text = self.textWindow.get("1.0", tk.END)
        savefile.write(text)
        savefile.close()
        self.opsLabel.config(text = 'Saved buffer as "{0}"'.format(self.currFileName))

    def incFontSize(self):
        """ Increase editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']+1)))
        self.textWindow.config(font=font)

    def decFontSize(self):
        """ Decrease editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']-1)))
        self.textWindow.config(font=font)

    def reverseColor(self):
        """ Reverse color scheme. """
        fg_color = self.textWindow['foreground']
        bg_color = self.textWindow['background']

        # shows all config variables
        #print self.textWindow.config()
        # TODO -- take care of all variables, like highlight color, cursor color etc

        if fg_color == "#ffffff":
            self.textWindow.config(foreground="#000000")
        else:
            self.textWindow.config(foreground="#ffffff")

        if bg_color == "#ffffff":
            self.textWindow.config(background="#000000")
        else:
            self.textWindow.config(background="#ffffff")

    def displayAbout(self):
        """ Display an About message."""
        tkMessageBox.showinfo('About', "This is a basic text editor written for fun.")

def main():
    root = tk.Tk()
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
