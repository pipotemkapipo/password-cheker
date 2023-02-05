import tkinter as tk 

root1 = tk.Tk()
root1.geometry("400x240")
root1.title("CustomTkinter")


def btw1():
	def btw2():
		if entry.get()== entry1.get():
			label["text"] = "password correct"
		else:	
			label["text"] = "password is not correct"

	entry = tk.Entry()
	entry.pack(padx=5, pady=5)


	btw = tk.Button(text="check password", command=btw2)
	btw.pack(padx=5, pady=5)	

	label = tk.Label()
	label.pack(padx=6, pady=6)




entry1 = tk.Entry()
entry1.pack(padx=6, pady=6)

password = entry1.get()

btw1 = tk.Button(text="Create password", command=btw1)
btw1.pack(padx=6, pady=6)


root1.mainloop()