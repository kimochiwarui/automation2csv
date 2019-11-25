import os
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tksheet import Sheet

app = tk.Tk()


def createList():
  frame = tk.Frame(app, height=400)
  for c, entry in enumerate(data):
    model = tk.Label(frame, text=entry['Model'], padx='12', pady='6')
    model.grid(row=c, column=0)
  frame.grid(row=1, column=0)


# os.path.expanduser('~/Documents/My Games/Automation/Sandbox_openbeta.db')
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

    c.execute("SELECT FUID,Name as Variant FROM Variants WHERE UID=?", (d['VUID'],))
    variant = c.fetchone()
    for key in variant:
      d[key] = variant[key]

    c.execute('SELECT Name as Family FROM Families WHERE UID=?', (d['FUID'],))
    family = c.fetchone()
    for key in family:
      d[key] = family[key]


readDatabase()
createList()
app.mainloop()