import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("500x500")

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image=mo)
  elif person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image=katie)
  else:
    hello["text"] = "Unable to find this user"

hello = tk.Label(text="Gues who?")
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Click me!", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
charlotte = ImageTk.PhotoImage(Image.open("Day 67\Guess Who\charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("Day 67\Guess Who\gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("Day 67\Guess Who\katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("Day 67\Guess Who\mo.jpg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()