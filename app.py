import os
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tksheet import Sheet


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        # place canvas on self
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        # place a frame on the canvas, this frame will hold the child widgets
        self.viewPort = tk.Frame(self.canvas, background="#ffffff")
        # place a scrollbar on self
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        # attach scrollbar action to scroll of canvas
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # pack scrollbar to right of self
        self.vsb.pack(side="right", fill="y")
        # pack canvas to left of self and expand to fil
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",  # add view port frame to canvas
                                                       tags="self.viewPort")

        # bind an event whenever the size of the viewPort frame changes.
        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        # bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
        self.onFrameConfigure(None)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))  # whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)


class carList(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)  # add a new scrollable frame.

        # Now add some controls to the scrollframe.
        # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
        for c, entry in enumerate(data):
            model = tk.Label(self.scrollFrame.viewPort,
                             text=entry['Model'] + ' - ' + entry['Trim'], padx='12', pady='6')
            model.grid(row=c, column=0)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def printMsg(self, msg):
        print(msg)


class controls(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.controls = tk.Frame(self)
        filterLabel = tk.Label(self.controls, text='Filter to:')
        filterLabel.grid(row=1, column=1)
        filterInput = tk.Entry(self.controls)
        filterInput.grid(row=1, column=2)
        cleanLabel = tk.Label(self.controls, text='Remove text')
        cleanLabel.grid(row=2, column=1)
        cleanInput = tk.Entry(self.controls)
        cleanInput.grid(row=2, column=2)

        presetLabel = tk.Label(self.controls, text='Choose export preset')
        presetLabel.grid(row=3, column=1)
        choices = {'Full', 'Basic', 'CSR'}
        tkvar = tk.StringVar(app)
        tkvar.set('Basic')
        presetMenu = tk.OptionMenu(self.controls, tkvar, *choices)
        presetMenu.grid(row=4, column=1)

        exportBtn = tk.Button(self.controls, text='Export Selected')
        exportBtn.grid(row=5, column=1)
        exportAllBtn = tk.Button(self.controls, text='Export All')
        exportAllBtn.grid(row=6, column=1)
        self.controls.grid()


database = 'database/Sandbox_openbeta.db'
data = []


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def readDatabase():
    conn = sqlite3.connect('database/Sandbox_openbeta.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("""SELECT 
    UID,
    MUID,
    VUID,
    Name as Trim
    FROM Trims""")
    rows = c.fetchall()
    for d in rows:
        data.append(d)
    for d in data:
        c.execute("SELECT Name as Model FROM Models WHERE UID=?", (d["MUID"],))
        model = c.fetchone()
        for key in model:
            d[key] = model[key]

        c.execute(
            "SELECT FUID,Name as Variant FROM Variants WHERE UID=?", (d['VUID'],))
        variant = c.fetchone()
        for key in variant:
            d[key] = variant[key]

        c.execute('SELECT Name as Family FROM Families WHERE UID=?',
                  (d['FUID'],))
        family = c.fetchone()
        for key in family:
            d[key] = family[key]


readDatabase()


if __name__ == "__main__":
    app = tk.Tk()
    readDatabase()
    carList(app).grid(row=1, column=1)
    controls(app).grid(row=1, column=2)
    app.mainloop()
