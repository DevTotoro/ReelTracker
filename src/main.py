from services.theme import AppearanceMode, ColorTheme, Theme

import tkinter as tk
import customtkinter as ctk

if __name__ == '__main__':
    theme = Theme(appearance_mode=AppearanceMode.SYSTEM, color_theme=ColorTheme.DARK_BLUE)

    root = ctk.CTk()

    root.title('Hello, World!')
    root.geometry('300x300')

    button = ctk.CTkButton(master=root, text='Hello, World!', command=lambda: print('Hello, World!'))
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()
