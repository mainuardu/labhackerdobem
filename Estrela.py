from turtle import *

#uma função desenhar estrela #'def' significa 'definir'
def drawStar():
    pendown()
    begin_fill()
    for side in range(20):
        left(144)
        forward(50)
    end_fill()
    penup()


#isso vaisesenhar uma estrela cinza clara em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")

    #use a função para desenhar!

drawStar()
forwart(100)
drawStar()
left(120)
forwerd(150)
drawStar()
 
hideturtle()
done()
