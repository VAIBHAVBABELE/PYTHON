import tkinter
import random
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black','Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 15
def startGame(event):
    if timeleft == 15:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0 :
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 5
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))
    
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        timeLabel.config(text="TIME : "+ str(timeleft))
        timeLabel.after(1000, countdown)


def resetGame():
    global timeleft, score
    timeleft = 15
    score = 0
    scoreLabel.config(text = "PRESS ENTER")
    label.config(text = '')
    timeLabel.config(text="TIME : "+ str(timeleft))
    e.delete(0, tkinter.END)


root = tkinter.Tk()
root.title("COLORGAME")
root.minsize(300,200)
root.maxsize(600,400)
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",font=('Arial Black', 12),fg='red')
instructions.pack()
scoreLabel = tkinter.Label(root, text="PRESS ENTER ",font=('Arial Black', 12),fg='green')
scoreLabel.pack()
time = tkinter.Label(root, text="TIME ", font=('Arial Black', 12),fg='blue')
timeLabel = tkinter.Label(root, text="Time left: " +str(timeleft), font=('Arial Black', 12),fg='blue')
timeLabel.pack()
label = tkinter.Label(root, font=('Arial Black', 60) )
label.pack()
btn_frame = tkinter.Frame(root, width= 80, height = 40, bg= 'red')
btn_frame.pack(side = tkinter.BOTTOM)

reset_button = tkinter.Button(btn_frame, text = "RESTART",font=('Arial Black', 10), width = 20, fg = "black", bg = "light blue", bd = 5,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)
e = tkinter.Entry(root,font=('Arial Black', 15),bg='yellow',fg='brown',bd=4)

root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()