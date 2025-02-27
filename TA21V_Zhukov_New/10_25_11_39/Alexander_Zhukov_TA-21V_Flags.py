from tkinter import *
root =Tk()
canvas = Canvas(root, width=600, height=600)



def fun1(bukva):
    bukva = bukva.lower()
    if bukva == "c":
        canvas.create_rectangle(20 , 8, 125, 80, outline="black", fill="#003EF0")
        canvas.create_rectangle(20, 18, 125, 70, fill='white')
        canvas.create_rectangle(20 ,35, 125, 55, fill='red')
    
    elif bukva == "d":
        canvas.create_rectangle(135, 8, 240, 80, fill='yellow')
        canvas.create_rectangle(135, 18, 240, 70, fill='#0056F0')
    
    elif bukva =="e":
        canvas.create_rectangle(250, 8, 355, 80)
        canvas.create_rectangle(250, 8, 355, 45, fill='#003EF0')
        canvas.create_rectangle(250, 45, 355, 80, fill='red')
    
    elif bukva =='j':
        canvas.create_rectangle(365, 8, 470, 80, fill='#003EF0')
        canvas.create_rectangle(365, 30, 470, 60, fill='white')
        
    elif bukva =='q':
        canvas.create_rectangle(480, 8, 585, 80, fill='yellow')
    return bukva

def fun2(bukva):
    bukva = bukva.lower()
    
    if bukva == 'g':
        canvas.create_rectangle(20, 90 , 125, 162, fill='yellow')
        canvas.create_rectangle(40, 90, 55, 162, fill='#003EF0')
        canvas.create_rectangle(75, 90, 90, 162, fill='#003EF0')
        canvas.create_rectangle(110, 90, 125, 162, fill='#003EF0')
    
    if bukva == 'h':
        canvas.create_rectangle(135, 90, 240, 162, fill='red')
        canvas.create_rectangle(135, 90, 187, 162, fill='white')
    
    if bukva =='k':
        canvas.create_rectangle(250, 90, 355, 162, fill='#003EF0')
        canvas.create_rectangle(250, 90, 300, 162, fill='yellow')
        
    if bukva =='t':
        canvas.create_rectangle(365, 90, 470, 162, fill='red')
        canvas.create_rectangle(400, 90, 435, 162, fill='white')
        canvas.create_rectangle(435, 90, 470, 162, fill='#003EF0')
        
    if bukva =='q':
        canvas.create_rectangle(480, 90, 585, 162, fill='yellow')

def fun3(bukva):
    bukva = bukva.lower()
    
    if bukva =='l':
        canvas.create_rectangle(20, 172, 125, 244, fill='yellow')
        canvas.create_rectangle(20, 172, 72, 208, fill='black')
        canvas.create_rectangle(72, 208, 125, 244, fill='black')
        
    if bukva =='n':
        canvas.create_rectangle(135, 172, 240, 244)
        canvas.create_rectangle(135, 172, 160, 190, fill='blue')
        canvas.create_rectangle(160, 190, 185, 208, fill='blue')
        canvas.create_rectangle(160, 208, 135, 225, fill='blue')
        canvas.create_rectangle(160, 225, 185, 244, fill='blue')
        canvas.create_rectangle(185, 190, 210, 172, fill='blue')
        canvas.create_rectangle(210, 190, 240, 210, fill='blue')
        canvas.create_rectangle(185, 208, 210, 226, fill='blue')
        canvas.create_rectangle(210, 226, 240, 244, fill='blue')



    if bukva =='u':
        canvas.create_rectangle(250, 172, 355, 244)
        canvas.create_rectangle(250, 172, 302, 208, fill='red')
        canvas.create_rectangle(302, 208, 355, 244, fill='red')
        
fun1('c')
fun1("D")
fun1('e')
fun1('j')
fun1('q')
fun2('g')
fun2('h')
fun2('k')
fun2('t')
fun2('q')
fun3('l')
fun3('n')
fun3('u')

canvas.pack()
root.mainloop()