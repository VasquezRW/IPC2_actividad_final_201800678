from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Totito | Wilmer Estuardo Vasquez Raxon - 201800678")
window.geometry("600x600")


def reiniciar():
    global turno
    turno = 1
    global espOcupados
    espOcupados = 0
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "


lbl = Label(window, text="TOTITO")
lbl.grid(row=0, column=0)
lbl = Label(window, text="Jugador 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Jugador 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)
btnRestart = Button(window, text="Reiniciar juego", command=reiniciar)
btnRestart.grid(row=3, column=0)

turno = 1

# para metodos clicked se asigna el simbolo correcto y se cambia de turno

def clicked1():
    global turno
    if btn1["text"] == " ":
        if turno == 1:
            turno = 2
            btn1["text"] = "X"
        elif turno == 2:
            turno = 1
            btn1["text"] = "O"
        verificar()


def clicked2():
    global turno
    if btn2["text"] == " ":
        if turno == 1:
            turno = 2
            btn2["text"] = "X"
        elif turno == 2:
            turno = 1
            btn2["text"] = "O"
        verificar()


def clicked3():
    global turno
    if btn3["text"] == " ":
        if turno == 1:
            turno = 2
            btn3["text"] = "X"
        elif turno == 2:
            turno = 1
            btn3["text"] = "O"
        verificar()


def clicked4():
    global turno
    if btn4["text"] == " ":
        if turno == 1:
            turno = 2
            btn4["text"] = "X"
        elif turno == 2:
            turno = 1
            btn4["text"] = "O"
        verificar()


def clicked5():
    global turno
    if btn5["text"] == " ":
        if turno == 1:
            turno = 2
            btn5["text"] = "X"
        elif turno == 2:
            turno = 1
            btn5["text"] = "O"
        verificar()


def clicked6():
    global turno
    if btn6["text"] == " ":
        if turno == 1:
            turno = 2
            btn6["text"] = "X"
        elif turno == 2:
            turno = 1
            btn6["text"] = "O"
        verificar()


def clicked7():
    global turno
    if btn7["text"] == " ":
        if turno == 1:
            turno = 2
            btn7["text"] = "X"
        elif turno == 2:
            turno = 1
            btn7["text"] = "O"
        verificar()


def clicked8():
    global turno
    if btn8["text"] == " ":
        if turno == 1:
            turno = 2
            btn8["text"] = "X"
        elif turno == 2:
            turno = 1
            btn8["text"] = "O"
        verificar()


def clicked9():
    global turno
    if btn9["text"] == " ":
        if turno == 1:
            turno = 2
            btn9["text"] = "X"
        elif turno == 2:
            turno = 1
            btn9["text"] = "O"
        verificar()


espOcupados = 1


def verificar():
    global espOcupados
    b_1_1 = btn1["text"]
    b_1_2 = btn2["text"]
    b_1_3 = btn3["text"]
    b_2_1 = btn4["text"]
    b_2_2 = btn5["text"]
    b_2_3 = btn6["text"]
    b_3_1 = btn7["text"]
    b_3_2 = btn8["text"]
    b_3_3 = btn9["text"]
    espOcupados = espOcupados + 1
    # se valida la primera fila, se manda resultado por el tipo de texto de la fila
    if b_1_1 == b_1_2 and b_1_1 == b_1_3 and b_1_1 == "O" or b_1_1 == b_1_2 and b_1_1 == b_1_3 and b_1_1 == "X":
        win(btn1["text"])
    # se valida la segunda fila, se manda resultado por el tipo de texto de la fila
    if b_2_1 == b_2_2 and b_2_1 == b_2_3 and b_2_1 == "O" or b_2_1 == b_2_2 and b_2_1 == b_2_3 and b_2_1 == "X":
        win(btn4["text"])
    # se valida la tercera fila fila, se manda resultado por el tipo de texto de la fila
    if b_3_1 == b_3_2 and b_3_1 == b_3_3 and b_3_1 == "O" or b_3_1 == b_3_2 and b_3_1 == b_3_3 and b_3_1 == "X":
        win(btn7["text"])
    # se valida la primera columna, se manda resultado por el tipo de texto de la columna
    if b_1_1 == b_2_1 and b_1_1 == b_3_1 and b_1_1 == "O" or b_1_1 == b_2_1 and b_1_1 == b_3_1 and b_1_1 == "X":
        win(btn1["text"])
    # se valida la segunda columna, se manda resultado por el tipo de texto de la columna
    if b_1_2 == b_2_2 and b_1_2 == b_3_2 and b_1_2 == "O" or b_1_2 == b_2_2 and b_1_2 == b_3_2 and b_1_2 == "X":
        win(btn2["text"])
    # se valida la tercera columna, se manda resultado por el tipo de texto de la columna
    if b_1_3 == b_2_3 and b_1_3 == b_3_3 and b_1_3 == "O" or b_1_3 == b_2_3 and b_1_3 == b_3_3 and b_1_3 == "X":
        win(btn3["text"])
    # se valida la diagonal principal, se manda resultado por el tipo de texto de la diagonal
    if b_1_1 == b_2_2 and b_1_1 == b_3_3 and b_1_1 == "O" or b_1_1 == b_2_2 and b_1_1 == b_3_3 and b_1_1 == "X":
        win(btn1["text"])
    # se valida la segunda diagonal, se manda resultado por el tipo de texto de la diagonal
    if b_3_1 == b_2_2 and b_3_1 == b_1_3 and b_3_1 == "O" or b_3_1 == b_2_2 and b_3_1 == b_1_3 and b_3_1 == "X":
        win(btn7["text"])
    # se valida la que todos los espacios esten ocupados
    if espOcupados == 10:
        messagebox.showinfo("Empate", "Empate, intente de nuevo :)")


def win(jugador):
    resultado = ""
    if jugador == "X":
        resultado = "Juego terminado, gana jugador 1 ! "
    elif jugador == "O":
        resultado = "Juego terminado, gana jugador 2 ! "
    messagebox.showinfo("Felicitaciones", resultado)
    window.destroy()


btn1 = Button(window, text=" ", width=3, height=1, command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", width=3, height=1, command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", width=3, height=1, command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", width=3, height=1, command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", width=3, height=1, command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", width=3, height=1, command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", width=3, height=1, command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", width=3, height=1, command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", width=3, height=1, command=clicked9)
btn9.grid(column=3, row=3)
window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
