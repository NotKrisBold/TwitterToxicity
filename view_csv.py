import tkinter as tk
from csv_viewer import CSVViewer

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewer(root)
    root.mainloop()
