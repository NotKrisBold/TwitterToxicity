import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

class CSVViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("800x600")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.button = tk.Button(self.frame, text="Open CSV File", command=self.load_csv)
        self.button.pack(pady=10)

        self.tree_frame = tk.Frame(self.frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=1)

        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.hsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path, low_memory=False)
                self.show_data(df)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while reading the file: {e}")

    def show_data(self, df):
        self.tree.delete(*self.tree.get_children())
        self.tree["column"] = list(df.columns)
        self.tree["show"] = "headings"

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))
