# # Snowflake

# import turtle


# # ha.forward(100)
# # #ha.backwars()
# # ha.left(90)
# # #ha.right()
# # ha.forward(100) 

# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length*n)
#     t.lt(angle)
#     draw(t, length, n-1) # function call 1
#     t.rt(2*angle)   
#     draw(t, length, n-1) #function call 2
#     t.lt(angle)
#     t.bk(length*n)
    
# ha = turtle.Turtle()
# ha.color('red')
# ha.pensize(5)
# ha.shape('arrow')
  
# draw(ha, 20, 10)


#Koch curve
import turtle

def draw_koch(t,length):
    if length < 20:
        t.fd(length)
        return
    draw_koch(t,length/3)
    t.lt(60)
    draw_koch(t,length/3)
    t.rt(120)
    draw_koch(t,length/3)
    t.lt(60)
    draw_koch(t,length/3)



#Snowflake

def snowflake(t,length,n):
    for i in range(n):
        draw_koch(t,length)
        t.rt(360/n)

ha = turtle.Turtle()   
ha.color('red') 
snowflake(ha,100,6)