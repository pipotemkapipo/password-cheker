import tkinter as tk 
import customtkinter 

root1 = tk.Tk()
root1.geometry("400x240")
root1.title("CustomTkinter")
root1.configure(background='black')

def btw1():
	def btw2():
		if entry.get()== entry1.get():
			label["text"] = "password correct"
		else:	
			label["text"] = "password is not correct"

	entry = customtkinter.CTkEntry(master=root1)
	entry.pack(padx=5, pady=5)


	btw = customtkinter.CTkButton(master=root1, text="Check password", command=btw2)
	btw.pack(padx=5, pady=5)	

	label = tk.Label(master=root1,font=('TkDefaultFont', 13), background='#000000', fg='#ffffff')
	label.pack(padx=6, pady=6)




entry1 = customtkinter.CTkEntry(master=root1)
entry1.pack(padx=6, pady=6)

password = entry1.get()

btw1 = customtkinter.CTkButton(master=root1, text="Create password", command=btw1)
btw1.pack(padx=6, pady=6)


root1.mainloop()