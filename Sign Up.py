import customtkinter

root = customtkinter.CTk()
root.geometry("1200x600")
root.resizable(0,0)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def login():
    print("ReelTracker")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="ReelTracker", font=("Arial", 12))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Confirm password", show="*")
entry4.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Sign Up", command=login)
button.pack(pady=12, padx=10)

text_label = customtkinter.CTkLabel(master=frame, text="Already Have an account?", font=("Arial", 12))
text_label.pack()

#checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
#checkbox.pack(pady=12, padx=10)
   
root.mainloop()