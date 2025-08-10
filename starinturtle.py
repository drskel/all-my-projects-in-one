from turtle import * 
def star():
    while True:
        speed(5)
        color('purple')
        bgcolor('black')
        b = 220
        while b > 0:
            left(b)
            forward(b * 3)
            b = b - 1.5

if __name__ == '__main__':
    star()
