import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()
style.theme_settings("default", {
                        "Custom.TEntry": {
                            "configure": {"padding": 5},
                            "map": {
                                "background": [("active", "green2"),
                                                ("!disabled", "green4")],
                                "fieldbackground": [("!disabled", "red")],
                                "foreground": [("focus", "OliveDrab1"),
                                                ("!disabled", "red")]
       }
   }
})



disabled_entry = ttk.Entry(root, style='Custom.TEntry', state='disabled')
disabled_entry.insert(0, 'Disabled Entry')
disabled_entry.pack()

root.mainloop()
