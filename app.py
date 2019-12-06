import os
import fnmatch
import tkinter as tk
from functools import partial
from readDatabase import readDatabase
from replaceValues import replaceValues


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        # place canvas on self
        self.canvas = tk.Canvas(self, borderwidth=0,
                                background="#ffffff", height='500')
        # place a frame on the canvas, this frame will hold the child widgets
        self.viewPort = tk.Frame(self.canvas, pady='6', background="#ffffff")
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
        filteredData = filterData(data)
        for c, entry in enumerate(filteredData):
            model = tk.Label(self.scrollFrame.viewPort,
                             text=entry['Model'] + ' - ' + entry['Trim'],
                             background="#ffffff",
                             padx='12', pady='6')
                            #  Fix bug of wrongly chosen car when filtered
            button = tk.Button(self.scrollFrame.viewPort,
                            padx='12', pady='6',
                            text='Export ', 
                            command=partial(exportCar, filteredData[c]['UID']))
            model.grid(pady='6', row=c, column=0)
            button.grid(row=c, column=1)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)

class controls(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.controls = tk.Frame(self)
        filterLabel = tk.Button(
            self.controls, text='Filter name to:', command=cars.refresh)
        filterLabel.grid(row=1, column=1)
        filterInput = tk.Entry(self.controls, textvariable=filterInputData)
        filterInput.grid(padx='12', pady='12', row=1, column=2)

        presetLabel = tk.Label(self.controls, text='Choose export preset')
        presetLabel.grid(row=3, column=1)
        presetMenu = tk.OptionMenu(self.controls, presetChose, *presetChoices)
        presetMenu.grid(pady='12', row=3, column=2)

        exportAllBtn = tk.Button(self.controls, text='Export Filtered', command=exportFiltered)
        exportAllBtn.grid(pady='12', row=6, column=1)
        self.controls.pack()


def filterData(data):
    filteredData = []
    for item in data:
        if filterInputData.get():
            if filterInputData.get().lower() in item['Model'].lower():
                filteredData.append(item)
            elif filterInputData.get().lower() in item['Trim'].lower():
                filteredData.append(item)
        else:
            filteredData.append(item)
    return filteredData


def createCSV(item):
    choice = presetChose.get()
    csv = ''
    if choice == 'Full':
        for entry in item:
            csv += entry + ', '
        csv += '\n'
        for entry in item:
            csv += str(replaceValues(entry, item[entry])) + ', '
        return csv
    else:
        content = open(choice + '.txt').readline()
        settingsList = content.split(',')
        for line in settingsList:
            for word in line.split('*'):
                if word.startswith('+'):
                    if word.replace('+', '') in item:
                        csv += str(replaceValues(word.replace('+', ''), item[word.replace('+', '')]))
                    else: 
                        csv += 'ND'
                else:
                    csv += word
            csv += ','
        return csv


def saveCSV(string, filename):
    f = open(filename + '.csv', 'w+')
    f.write(string)
    f.close()


def exportCar(uid):
    for item in data:
        if item['UID'] == uid:
            car = item
    try:
        assert(car)
        csv = createCSV(car)
        saveCSV(csv, car['Model'] + ' ' + car['Trim'])
    except:
        print('Error, no car found')
        pass


def exportFiltered():
    filteredData = filterData(data)
    csv = ''
    for item in filteredData:
        csv += createCSV(item)
        csv += '\n'
    saveCSV(csv, 'Collection of ' + str(len(filteredData)) + ' by ' + filterInputData.get())


class renderCars(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self._frame = carList(self)
        self._frame.pack()

    def refresh(self):
        self._frame.destroy()
        self._frame = carList(self)
        self._frame.pack()


if __name__ == "__main__":
    app = tk.Tk()
    app.minsize(500, 500)
    app.title('Automation2CSV')
    icon = tk.PhotoImage(file='icon2.png')
    app.iconphoto(False, icon)
    databasePointer = os.path.expanduser('~/Documents/My Games/Automation/Sandbox_openbeta.db')
    data = []
    filterInputData = tk.StringVar(app)
    presetChose = tk.StringVar(app)
    presetChoices = {'Full'}
    presetChose.set('Full')
    # Threats all .txt files as presets
    for f in os.listdir('.'):
        if fnmatch.fnmatch(f, '*.txt'):
            presetChoices.add(f.split('.')[0])
    data = readDatabase(databasePointer)
    cars = renderCars(app)
    cars.pack(side='left')
    controls(app).pack(side='right')
    app.mainloop()
