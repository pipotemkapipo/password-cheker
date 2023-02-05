import tkinter as tk 
import customtkinter 
a = "1"

while a == "1":

	root1 = tk.Tk()
	root1.geometry("400x200")
	root1.title("CustomTkinter")
	root1.configure(background='black')

	entry1 = customtkinter.CTkEntry(master=root1)
	entry1.pack(padx=6, pady=6)		
	
	def btw1():
		password = entry1.get()
		def btw2():
			if entry.get()== password:
				label["text"] = "password correct"
			else:	
				label["text"] = "password is not correct"
		def btw3():
			root11.destroy()

		def btw4():
			if a == "1":
				exit(0) 

				
		root11 = tk.Tk()
		root11.geometry("400x200")
		root11.title("CustomTkinter")
		root11.configure(background='black')

		entry = customtkinter.CTkEntry(root11)
		entry.pack(padx=5, pady=5)


		btw = customtkinter.CTkButton(root11,text="Check password", command=btw2)
		btw.pack(padx=5, pady=5)	

		label = tk.Label(root11,font=('TkDefaultFont', 13), background='#000000', fg='#ffffff')
		label.pack(padx=6, pady=6)

		btw = customtkinter.CTkButton(root11,text="Restart", command=btw3)
		btw.pack(padx=5, pady=5)

		btw = customtkinter.CTkButton(root11,text="Quit", command=btw4)
		btw.pack(padx=5, pady=5)

		root1.destroy()	

	#win one





	btw1 = customtkinter.CTkButton(master=root1, text="Create password", command=btw1)
	btw1.pack(padx=6, pady=6)














	root1.mainloop()