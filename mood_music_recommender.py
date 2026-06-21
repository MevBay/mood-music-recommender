import random
import webbrowser
import tkinter as tk

print("Welcome to Mood Music Recommender :)")

happy_songs = [
    ("Uptown Funk (by Bruno Mars)", "https://open.spotify.com/search/uptownfunk"),
    ("Honey See you (by ISTERIF)", "https://open.spotify.com/search/honeyseeyou"),
    ("Billy Jean (by Michael Jackson)", "https://open.spotify.com/search/billyjean")
]

chill_songs = [
    ("WAIT FOR U (by Drake & Tems)", "https://open.spotify.com/search/waitforu"),
    ("One Dance (by Drake, Wizkid, Kyla)", "https://open.spotify.com/search/onedance"),
    ("Sure Thing (by Miguel)", "https://open.spotify.com/search/surething")
]

sad_songs = [
    ("Lonely (by Akon)", "https://open.spotify.com/search/lonely"),
    ("Let Me Down Slowly (by Alec Benjamin)", "https://open.spotify.com/search/letmedownslowly"),
    ("Someone You Loved (by Lewis Capaldi)", "https://open.spotify.com/search/someoneyouloved")
]

current_link = ""

window = tk.Tk()
window.title("Music Mood Recommender")

mood_var = tk.StringVar()
mood_var.set("happy")

mood_menu = tk.OptionMenu(window, mood_var, "happy", "sad", "chill")
mood_menu.pack()

def recommend_song():
    global current_link

    mood = mood_var.get()

    if mood == "happy":
        song, current_link = random.choice(happy_songs)

    elif mood == "sad":
        song, current_link = random.choice(sad_songs)

    elif mood == "chill":
        song, current_link = random.choice(chill_songs)

    else:
        song = "Sorry! I don't know that mood :("

    print("Try:", song)

    result_label.config(text=f"Try: {song}")


def play_song():
    webbrowser.open(current_link)


#my buttons
button1 = tk.Button(
    window,
    text="Recommend Song",
    command=recommend_song
)
button1.pack()

button2 = tk.Button(
    window,
    text="Play Song",
    command=play_song
)
button2.pack()

result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()