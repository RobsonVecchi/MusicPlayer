import tkinter
from PIL import ImageTk, Image
import os
from pygame import mixer

#real_bg = #25272C
WHITE = "#ffffff"
PURPLE = "#3C1DC6"
BLACK= "#333333"
LIGHT_PURPLE = "#CFC7F8"

window = tkinter.Tk()
window.title("Music Player")
window.geometry("352x230")
window.configure(background=WHITE)
window.resizable(width=False, height=False)


#events
def play_music():
    running = listbox.get(tkinter.ACTIVE)
    running_song["text"] = running
    mixer.music.load(running)
    mixer.music.play()
    
def pause_music():
    mixer.music.pause()
    
def unpause_music():
    mixer.music.unpause()        

def stop_music():
    mixer.music.stop()
    
def next_music():
    playing = running_song["text"]
    index = songs.index(playing)
    new_index = index+1
    playing = songs[new_index] 
    mixer.music.load(playing)
    mixer.music.play()   
    listbox.delete(0, tkinter.END)
    show()
    listbox.select_set(new_index)
    running_song["text"] = playing
    
def previous_music():
    playing = running_song["text"]
    index = songs.index(playing)
    new_index = index-1
    playing = songs[new_index] 
    mixer.music.load(playing)
    mixer.music.play()   
    listbox.delete(0, tkinter.END)
    show()
    listbox.select_set(new_index)
    running_song["text"] = playing    
    
#frames
left_frame = tkinter.Frame(window, width=150, height=150, bg=BLACK)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = tkinter.Frame(window, width=250, height=150, bg=BLACK)
right_frame.grid(row=0, column=1, padx=0)

down_frame = tkinter.Frame(window, width=400, height=100, bg=LIGHT_PURPLE)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)
          
#List of songs
listbox = tkinter.Listbox(right_frame, selectmode=tkinter.SINGLE, font=("Arial 9 bold"), width=22, bg=PURPLE, fg=WHITE)
listbox.grid(row=0, column=0)



scroll_bar = tkinter.Scrollbar(right_frame, bg=WHITE)
scroll_bar.grid(row=0, column=1)

listbox.config(yscrollcommand=scroll_bar.set, bg=BLACK)
scroll_bar.config(command = listbox.yview)
                
#images
logo_img = Image.open("imgs/logo.png")
logo_img = ImageTk.PhotoImage(logo_img)
app_image = tkinter.Label(left_frame, height=150, image=logo_img, padx=10, bg=BLACK)
app_image.place(x=10, y=10)

previous_img = Image.open("imgs/previous.png")
previous_img = ImageTk.PhotoImage(previous_img)
previous_bt = tkinter.Button(down_frame, height=40, image=previous_img, bg=BLACK, command=previous_music)
previous_bt.place(x=40, y=20)

play_img = Image.open("imgs/play.png")
play_img = ImageTk.PhotoImage(play_img)
play_bt = tkinter.Button(down_frame, height=40, image=play_img, bg=BLACK, command=play_music)
play_bt.place(x=85, y=20)


next_img = Image.open("imgs/next.png")
next_img = ImageTk.PhotoImage(next_img)
next_bt = tkinter.Button(down_frame, height=40, image=next_img, bg=BLACK, command=next_music)
next_bt.place(x=130, y=20)

pause_img = Image.open("imgs/pause.png")
pause_img = ImageTk.PhotoImage(pause_img)
pause_bt = tkinter.Button(down_frame, height=40, image=pause_img, bg=BLACK, command=pause_music)
pause_bt.place(x=175, y=20)

continue_img = Image.open("imgs/continue.png")
continue_img = ImageTk.PhotoImage(continue_img)
continue_bt = tkinter.Button(down_frame, height=40, image=continue_img, bg=BLACK, command=unpause_music)
continue_bt.place(x=220, y=20)

stop_img = Image.open("imgs/stop.png")
stop_img = ImageTk.PhotoImage(stop_img)
stop_bt = tkinter.Button(down_frame, height=40, image=stop_img, bg=BLACK, command=stop_music)
stop_bt.place(x=265, y=20)


#Choose
running_song = tkinter.Label(down_frame, text = "Choose a song", font=("Ivy 10"), width=44, height=1, padx=10, bg=BLACK, fg=WHITE)
running_song.place(x=0, y=1)


os.chdir(r"C:\Users\Dell\Desktop\Learn To Code\Portfolio\5.MusicPlayer\songs")
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(tkinter.END, i)

show()

mixer.init()
music_state = tkinter.StringVar()
music_state.set("Choose one!")

window.mainloop()