import math
import turtle


# --- Mathematical Formula for Heart Shape ---
def xt(t):
    return 16 * math.sin(t) ** 3


def yt(t):
    return (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )


# --- Screen Setup ---
screen = turtle.Screen()
screen.title("Glowing Heart")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# --- Turtle Setup ---
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# --- Draw Animated Heart ---
screen.tracer(0)  # Smooth high-speed rendering

for i in range(160, 0, -2):
    t.color("#ff2e63")  # Crimson/Pink color gradient
    t.penup()

    for angle in range(0, 628, 2):
        rad = angle / 100.0
        x = xt(rad) * (i / 10)
        y = yt(rad) * (i / 10)

        if angle == 0:
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
        else:
            t.goto(x, y)

    t.end_fill()

screen.update()  # Render the final image

# --- Add Text (Fixed Typo) ---
t.penup()
t.goto(0, -15)  # Positions text near the middle
t.color("white")
# Note: align="center" with an 'e' avoids the KeyError!
t.write("I Love You", align="center", font=("Arial", 22, "bold"))

# Keep window open until you click on it
screen.exitonclick()