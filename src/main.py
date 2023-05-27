import tkinter as tk
import customtkinter as ctk

if __name__ == '__main__':
    ctk.set_appearance_mode('system')
    ctk.set_default_color_theme('dark-blue')

    root = ctk.CTk()

    root.title('Hello, World!')
    root.geometry('300x300')

    button = ctk.CTkButton(master=root, text='Hello, World!', command=lambda: print('Hello, World!'))
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()
