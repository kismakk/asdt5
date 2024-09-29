import os
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from pygame import mixer
import PIL
import random
import threading

# Constants
TK_MAIN_WINDOW_GEOMETRY = "1024x512+200+0"
MONKEY_NORTH_COORDS = (200, 50)
MONKEY_SOUTH_COORDS = (200, 300)

# Message to be sent
MESSAGE = "Ernesti ja Kernesti tässä terve! Olemme autiolla saarella, voisiko joku tulla sieltä sivistyneestä maailmasta hakemaan meidät pois! Kiitos!"

# Split message into words and initialize counters to keep track of words sent
message_words = MESSAGE.split()
word_counter_ernesti = 0
word_counter_kernesti = 0

# Initialize main window
window = tk.Tk()
window.configure(bg="cyan")
window.title("Ernesti ja Kernesti autiosaarella")
window.geometry(TK_MAIN_WINDOW_GEOMETRY)

# Sound initialization
mixer.init()
swim_audio = os.path.join("assets/sounds", "swim.wav")
victory_audio = os.path.join("assets/sounds", "victory.wav")

swim_sound = mixer.Sound(swim_audio)
swim_sound.set_volume(0.1)
victory_sound = mixer.Sound(victory_audio)
victory_sound.set_volume(0.2)

# Initialize images
IMG_SIZE = (512, 256)

island_jpeg = os.path.join("assets/pictures", "island.jpeg")
island_jpeg = PIL.Image.open(island_jpeg).resize(IMG_SIZE)
island_jpeg = island_jpeg.transpose(method=PIL.Image.Transpose.ROTATE_90)
island_image = PIL.ImageTk.PhotoImage(island_jpeg)

city_jpeg = os.path.join("assets/pictures", "city.jpeg")
city_jpeg = PIL.Image.open(city_jpeg).resize(IMG_SIZE)
city_jpeg = city_jpeg.transpose(method=PIL.Image.Transpose.ROTATE_270)
city_image = PIL.ImageTk.PhotoImage(city_jpeg)

# Label for island and city
island_label = tk.Label(window, image=island_image)

city_label = tk.Label(window, image=city_image)

# Common button styling
button_style = {
    "bg": "white",
    "font": ("Arial", 12),
    "width": 20,
    "height": 2,
    "relief": "raised",
    "borderwidth": 2,
}


def main():
    island_label.pack(side="left")
    city_label.pack(side="right")

    # Button for Ernesti to send a monkey
    ernesti_button = tk.Button(
        window,
        text="Ernesti lähettää apinan",
        command=ernesti_send_monkey,
        **button_style,
    )

    ernesti_button.pack(side="top")

    # Button for Kernesti to send a monkey
    kernesti_button = tk.Button(
        window,
        text="Kernesti lähettää apinan",
        command=kernesti_send_monkey,
        **button_style,
    )

    kernesti_button.pack(side="top")

    window.mainloop()


def get_message_word(sender):
    global word_counter_ernesti, word_counter_kernesti

    if sender == "Ernesti":
        if word_counter_ernesti == len(message_words):
            word_counter_ernesti = 0
        word = message_words[word_counter_ernesti]
        word_counter_ernesti += 1
    else:
        if word_counter_kernesti == len(message_words):
            word_counter_kernesti = 0
        word = message_words[word_counter_kernesti]
        word_counter_kernesti += 1

    return word


def move_monkey(sender, word):
    counter = 0
    beach_x = city_label.winfo_x()

    # Create a monkey
    monkey_label = tk.Label(text="🐵")
    (monkey_pos_x, monkey_pos_y) = (
        MONKEY_NORTH_COORDS if sender == "Ernesti" else MONKEY_SOUTH_COORDS
    )

    # Place monkey with a variance
    monkey_variance = random.randint(50, 100)
    monkey_label.place(x=monkey_pos_x, y=monkey_pos_y + monkey_variance)

    window.update_idletasks()

    # Calculate step size
    step_size = (beach_x - monkey_pos_x) // 100

    def move():
        nonlocal monkey_pos_x, beach_x, counter, sender, word

        swim_sound.play()

        # Update monkey position
        monkey_pos_x += step_size

        # Update label
        monkey_label.configure(text=f"🐵 {counter} km, sana: {word}")
        monkey_label.place(x=monkey_pos_x, y=monkey_pos_y + monkey_variance)

        # Check if monkey has reached the city
        if counter == 100:
            print(f"{sender}n apina ui perille seuraava sana mukanaan: {word}")
            victory_sound.play()
            monkey_label.after(50, monkey_label.destroy())
            return

        # Continue moving
        window.after(600, move)
        counter += 1

    move()


def ernesti_send_monkey():
    word_for_monkey = get_message_word("Ernesti")

    monkey_handler = threading.Thread(
        target=move_monkey, args=("Ernesti", word_for_monkey)
    )
    monkey_handler.start()


def kernesti_send_monkey():
    word_for_monkey = get_message_word("Kernesti")

    monkey_handler = threading.Thread(
        target=move_monkey, args=("Kernesti", word_for_monkey)
    )
    monkey_handler.start()


if __name__ == "__main__":
    main()
