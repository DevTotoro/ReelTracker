import customtkinter
from authentication import Authentication

root = customtkinter.CTk()
root.geometry("1200x600")
root.resizable(0,0)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def login(username,password):
   object = Authentication()
   login = object.login(username,password)
   if login == 1:
      print("Login Successful")
   else:
      print("Login Failed")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="ReelTracker", font=("Arial", 12))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=lambda username='test', password='test':  login(username,password))
button.pack(pady=12, padx=10)

text_label = customtkinter.CTkLabel(master=frame, text="New here?", font=("Arial", 12))
text_label.pack()

#checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
#checkbox.pack(pady=12, padx=10)
   
root.mainloop()
