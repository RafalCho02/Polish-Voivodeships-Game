import turtle, pandas

screen = turtle.Screen()
screen.title("Polish Voivodeships Game")
image = "blank_voivodeships.gif"
screen.addshape(image)
screen.setup(width=730,height=495)
turtle.shape(image)


data = pandas.read_csv("16_voivodeships.csv")
all_voivodeships = data.voivodeship.to_list()
guessed_voivodships = []



game_is_on = True
while game_is_on:
    answer_voivodeship = screen.textinput(title=f"{len(guessed_voivodships)}/16 Voivodships Correct", prompt="What's another voivodeship's name?\n "
                                                                                             "If you want left print Left").title()

    if answer_voivodeship == 'Left':
        missing_voivodeships = [voivodeship for voivodeship in all_voivodeships if voivodeship not in guessed_voivodships]
        new_data = pandas.DataFrame(missing_voivodeships)
        new_data.to_csv("Voivodeships_to_learn.csv")
        break
    if len(guessed_voivodships) >= 16:
        game_is_on = False
        screen.textinput(title='Congratulations',prompt='🎂🎂🎂🎂🎂🎂🎂🎂🎂 \nCongratulations you have guessed\nall 16 polish Voivodeships!\n 🎂🎂🎂🎂🎂🎂🎂🎂🎂')
    elif answer_voivodeship in all_voivodeships:
        guessed_voivodships.append(answer_voivodeship)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.voivodeship == answer_voivodeship]
        t.goto(int(voivodeship_data.x), int(voivodeship_data.y))
        t.write(answer_voivodeship)



screen.exitonclick()