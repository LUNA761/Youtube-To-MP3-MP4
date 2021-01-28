import time, os, youtube_dl, urllib.request, json, urllib, ffmpeg, ctypes
from bs4 import BeautifulSoup
from tkinter import *

failed = []
urls = []
url_list = "Add A Video!"
first = True

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def getsong(url, format):
    global urls, url_list, List_Of_Urls
    urlss = []
    urlss.append(url)
    try:
        if format == "mp3":
               urls = []
               url_list = "Add A Video!"
               List_Of_Urls["text"] = ""
               Mbox('Download', 'Please note it is normal for the window to go non responsive when downloading please just wait it out!', 0 )
               ydl_opts = {
                   'format': 'bestaudio/best',
                   'postprocessors': [{
                       'key': 'FFmpegExtractAudio',
                       'preferredcodec': 'mp3',
                       'preferredquality': '192',
                   }],
               }
               with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                   ydl.download(urlss)
                   return True
        elif format == "mkv":
              urls = []
              url_list = "Add A Video!"
              List_Of_Urls["text"] = ""
              Mbox('Download', 'Please note it is normal for the window to go non responsive when downloading please just wait it out!', 0 )
              with youtube_dl.YoutubeDL({'format': 'bestvideo+bestaudio/best',}) as ydl:
                  ydl.download(urlss)
                  return True
        else:
               return False
               print("Format")
    except Exception as E:
        print(E)
        return False

def Add_Url_Or_Search():
    global Url_Entry_Text, Url_Entry
    data = str(Url_Entry_Text.get())
    Url_Entry.delete(0, 'end')
    urls.append(data)

def Update_List_Of_Urls():
    global root, url_list, first
    url_list = ""
    for url in urls:
        url_list = url_list + "\n" + url
    List_Of_Urls["text"] = url_list
    root.after(50, Update_List_Of_Urls)

def start():
    global mkvmp3
    choice = str(mkvmp3.get())
    if choice == "Please Select:":
        Mbox('Error', 'Please select a format!', 0 )
    elif choice == "mp3":
        for url in urls:
            e = getsong(url, "mp3")
            if e == False:
                print(f"{url} has errored")
            elif e == True:
                print(f"{url} has been downloaded")
    elif choice == "mkv":
        for url in urls:
            e = getsong(url, "mkv")
            if e == False:
                print(f"{url} has errored")
            elif e == True:
                print(f"{url} has been downloaded")

#########################
root = Tk()
root.title("Youtube to mp3/mkv")
root.configure(bg = "#3d4b52")
w, h = 400, 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
##########
Url_Entry_Text = StringVar()
Url_Entry = Entry(root, textvariable = Url_Entry_Text)
Url_Entry.pack()
Button(root, text="Add", command=Add_Url_Or_Search).pack()
List_Of_Urls = Label(root, text="Loading!")
List_Of_Urls.pack()
List_Of_Urls.configure(bg = "#47565e", fg = "#ffffff", font=("Courier", 10))
mkvmp3 = StringVar()
mkvmp3.set("Please Select:") # default value
w = OptionMenu(root, mkvmp3, "Please Select:", "mp3", "mkv")
w.pack()
Button(root, text="Convert!", command=start).pack()
##########
root.after(1, Update_List_Of_Urls)
root.mainloop()
