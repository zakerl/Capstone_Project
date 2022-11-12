import tkinter as tk
from tkinter.filedialog import asksaveasfile

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, HostSfwr, Records, Configuration, DataView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        btnNamesList = ["HostSfwr", "Connect",
                        "Configuration", "Records", "DataView"]
        greeting = tk.Label(master=self, text="Main Menu")
        greeting.pack(fill=tk.X)
        frame_a = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_a.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_a, text="HostSfwr", width=50, command=lambda: controller.show_frame("HostSfwr"))
        btnHandle.pack(fill=tk.BOTH, expand=True)

        frame_b = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_b.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_b, text="Connect", width=50, command=lambda: controller.show_frame("Connect"))
        btnHandle.pack(fill=tk.BOTH, expand=True)

        frame_c = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_c.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_c, text="Configuration", width=50, command=lambda: controller.show_frame("Configuration"))
        btnHandle.pack(fill=tk.BOTH, expand=True)

        frame_d = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_d.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_d, text="Records", width=50, command=lambda: controller.show_frame("Records"))
        btnHandle.pack(fill=tk.BOTH, expand=True)

        frame_e = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_e.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_e, text="DataView", width=50, command=lambda: controller.show_frame("DataView"))
        btnHandle.pack(fill=tk.BOTH, expand=True)


class HostSfwr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        btnNamesList = ["Main Menu", "Connect",
                        "Configuration", "Records", "Data View"]
        greeting = tk.Label(master=self, text="Host Software")
        greeting.pack(fill=tk.X)
        for i in range(len(btnNamesList)):
            frame = tk.Frame(master=self, height=200,
                             padx=100, pady=50,  bg='grey')
            frame.pack(expand=True, fill=tk.BOTH)
            btnHandle = tk.Button(
                master=frame, text=btnNamesList[i], width=50)
            btnHandle.pack(fill=tk.BOTH, expand=True)
        # For going back to main menu
        frame_m = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_m.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_m, text="Back to Main Menu", width=50, command=lambda: controller.show_frame("MainMenu"))
        btnHandle.pack(fill=tk.BOTH, expand=False)


class Records(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        greeting = tk.Label(master=self, text="Records")
        greeting.pack(fill=tk.X)
        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Name", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Age", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Participant ID", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Monitoring Period", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        # For going back to main menu
        frame_m = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_m.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_m, text="Back to Main Menu", width=50, command=lambda: controller.show_frame("MainMenu"))
        btnHandle.pack(fill=tk.BOTH, expand=False)

class Configuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        greeting = tk.Label(master=self, text="Configuration")
        greeting.pack(fill=tk.X)
        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Number of activities", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Type of activity", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Threshold setting", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        frame_a = tk.Frame(master=self, height=200,
                           bg="grey")
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Setting 2", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        # For going back to main menu
        frame_m = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_m.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_m, text="Back to Main Menu", width=50, command=lambda: controller.show_frame("MainMenu"))
        btnHandle.pack(fill=tk.BOTH, expand=False)


class DataView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        greeting = tk.Label(master=self, text="Data View")
        greeting.pack(fill=tk.X)

        frame_a = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_a.pack(expand=True, fill=tk.BOTH)

        tk.Button(frame_a, text= "Load Data",height=2, width=15).pack()


        # Entry 1 
        frame_a = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Entry 1", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        # Entry 2
        frame_a = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_a.pack(expand=True, fill=tk.BOTH)
        label_a = tk.Label(master=frame_a, text="Entry 2", bg="grey")
        label_a.pack(side=tk.LEFT, padx=((30, 0)))
        entry_a = tk.Entry(master=frame_a, width=40)
        entry_a.pack(fill=tk.X, expand=True, padx=30)

        # Saving to CSV
        frame_a = tk.Frame(master=self, height=200,
                           padx=100, pady=50,  bg='grey')
        frame_a.pack(expand=True, fill=tk.BOTH)
        tk.Button(frame_a, text= "Save as DataView.csv",height=2, width=25, command= lambda:self.save_file()).pack()

        # For going back to main menu
        frame_m = tk.Frame(master=self, height=200,
                           padx=250, pady=50,  bg='grey')
        frame_m.pack(expand=True, fill=tk.BOTH)
        btnHandle = tk.Button(
            master=frame_m, text="Back to Main Menu", width=20, command=lambda: controller.show_frame("MainMenu"))
        btnHandle.pack(fill=tk.BOTH, expand=False)

    def save_file(self):
        f = asksaveasfile(initialfile = 'DataView.csv', defaultextension=".csv",filetypes=[("Csv files","*.csv")])
       


app = SampleApp()
app.mainloop()
