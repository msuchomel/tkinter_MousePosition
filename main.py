import tkinter as tk

def left_click(event):
    coord_label['text'] = f'({event.x},{event.y})'

def right_click(event):
    coord_label['text'] = 'Right button clicked!'

my_window = tk.Tk()
canvas = tk.Canvas(my_window, width=400, height=400, background='white')
label_title = tk.Label(bd=0, text='Title text here', relief='solid', font='Arial 18', bg=None)
coord_label = tk.Label(bd=0, relief='solid', text='Click a point on the canvas', font='Times 14 bold', by=None)
canvas.bind('<Button-1>', left_click)       # left button click action
canvas.bind('<Button-3>', right_click)      # right button click action  <Button-2> responds to L & R buttons together

label_title.grid(row=0, column=0, sticky=tk.W+tk.E)
canvas.grid(row=1, column=0, sticky='nsew')
coord_label.grid(row=2, column=0, sticky=tk.W+tk.E)

my_window.rowconfigure(1, weight=1)
my_window.columnconfigure(0, weight=1)

my_window.mainloop()
