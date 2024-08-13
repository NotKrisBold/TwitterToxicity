import tkinter as tk
from CsvViewer.csv_viewer import CSVViewer

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewer(root)
    root.mainloop()

