from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def calculate():
	if patname_entry.get()=="" or patage_entry.get()=="" or gen_entry.get()=="" or patweight_entry.get()=="" or patheight_entry.get()=="":
		messagebox.showerror("INVALID ENTRY"," PLEASE ENTER ALL FIELDS")


	else:
		kg = float(patweight_entry.get())
		mt = float( patheight_entry.get())
		result = kg/mt**2	
		listbox.insert(END,(patname_entry.get(),"-",patage_entry.get(),"-",gen_entry.get(),"-BMI->",(str(result)+' kg/m2')))	
	

def clear():
	patname_entry.delete(0,END)
	patweight_entry.delete(0,END)
	patheight_entry.delete(0,END)
	patage_entry.delete(0,END)
	gen_entry.delete(0,END)

def delete():
	listbox.delete(ANCHOR)


root = Tk()
root.geometry('700x500')
root.title('BMI CALCULATOR')
root.resizable(False,False)
root.configure(bg='#F0E100')


#patient name
patname_label = Label(root, 
	text = 'NAME',
	bg='#F0E100',
	font=("Times",12),
	fg="#000000")
patname_label.grid(row = 0, column = 0, pady = 20,padx = 15)
patname = StringVar()
patname_entry = Entry(root,
	 width=20,
	 textvariable= patname,
	 bd=2)
patname_entry.grid(row=0, column =1)

#patient age
patage_label = Label(root, 
	text = 'Age',
	bg='#F0E100',
	font=("Times",12),
	fg="#000000")
patage_label.grid(row = 1, column = 0, pady = 15,padx = 15)
patage = IntVar()
patage_entry = Entry(root, 
	width=20, 
	textvariable= patage,
	bd=2)
patage_entry.grid(row=1, column =1)

#patient height
patheight_label = Label(root, 
	text = 'HEIGHT(in mts)',
	bg='#F0E100',
	font=("Times",12),
	fg="#000000")
patheight_label.grid(row = 2, column = 0, pady = 15,padx = 15)
patheight = DoubleVar()
patheight_entry = Entry(root, 
	width=20, 
	textvariable= patheight,
	bd=2)
patheight_entry.grid(row=2, column =1)

#patient weight
patweight_label = Label(root, 
	text = 'WEIGHT(in kgs)',
	bg='#F0E100',
	font=("Times",12),
	fg="#000000")
patweight_label.grid(row = 3, column = 0, pady = 15,padx = 15)
patweight = DoubleVar()
patweight_entry = Entry(root, 
	width=20, 
	textvariable= patweight,
	bd=2)
patweight_entry.grid(row=3, column =1)

# gender
gen_label = Label(root,text='Gender',bg='#F0E100',font=("Times",12),fg="#000000")
gen_label.grid(row=4, column=0, pady = 15,padx = 15)
gender = StringVar()
gen_entry = Entry(root, 
	textvariable = gender,
	width = 20,
	bd=2)
gen_entry.grid(row=4, column=1)
 

#buttons
cal_bmi = Button(root, text= 'CALCULATE', command = calculate,relief=GROOVE)
cal_bmi.grid(row = 5, column = 0,pady=17)
del_bmi = Button(root, text= 'CLEAR INPUT', command = clear,relief=GROOVE)
del_bmi.grid(row = 5, column =1)
clear_inp = Button(root, text= 'DELETE BMI', command = delete,relief=GROOVE)
clear_inp.grid(row = 6, column =2)

#listbox 
listbox = Listbox(root, width = 50, height = 8)
listbox.grid(row = 6, column= 1)


#bmi label
label_bmi=Label(root, text='BMI CHART',bg='#F0E100',font=("Times",12),fg="#000000")
label_bmi.grid(row=0, column=2)
under_bmi=Label(root, text='<19-----UNDERWEIGHT',bg='#F0E100',font=("Times",12),fg="#000000")
under_bmi.grid(row=1, column=2)
norm_bmi=Label(root, text='19-24-----NORMAL',bg='#F0E100',font=("Times",12),fg="#000000")
norm_bmi.grid(row=2, column=2)
over_bmi=Label(root, text='25-29-----OVERWEIGTH',bg='#F0E100',font=("Times",12),fg="#000000")
over_bmi.grid(row=3, column=2)
obese_bmi=Label(root, text='30-39-----OBESE',bg='#F0E100',font=("Times",12),fg="#000000")
obese_bmi.grid(row=4, column=2)
extrm_bmi=Label(root, text='>40-----EXTREMELY OBESE',bg='#F0E100',font=("Times",12),fg="#000000")
extrm_bmi.grid(row=5, column=2)

root.mainloop()
