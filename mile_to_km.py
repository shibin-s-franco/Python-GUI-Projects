import tkinter

def calculate():
    mile=input.get()
    kms=round(float(mile)*1.609)
    # print(kms)
    output.config(text=kms)

window=tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=100,width=100)
window.config(padx=10,pady=10)

# label
miles=tkinter.Label(text="Miles")
miles.grid(row=0,column=2)

is_equal_to=tkinter.Label(text="is equal to")
is_equal_to.grid(row=1,column=0)

km=tkinter.Label(text="Km")
km.grid(row=1,column=2)

output=tkinter.Label(text="0")
output.grid(column=1,row=1)

# entry
input=tkinter.Entry()
input.focus()
input.grid(column=1,row=0)

# text


# button
button=tkinter.Button(text="calculate",command=calculate)
button.grid(row=2,column=1)


window.mainloop()