from tkinter import *

root = Tk()
# создаем объект на основе класса Tk
root.title("Текстовый редактор")
root.geometry("700x700")
root.iconbitmap()
# создаем окно и настраиваем его параметры: имя, размер, иконку (по умолчанию)
f_text = Frame(root, bg="#2d2d2d")
f_text.pack(fill=BOTH, expand=1)
"""создаем фрейм на основе нашего объекта, задаем параметр fill - тем самым устанавливаем
то, что при увеличении размера окна, наш фрэйм также будет расстягивать и по x  и по y
устанавливаем expand - в значении True, при наличии свободного места, фрейм перемещается
в центр окна"""
text_fild = Text(
    f_text,
    bg="white",
    fg="black",
    bd=1,
    wrap=WORD,
    insertbackground="#7b1fa2",
    selectbackground="#e1bee7",
    spacing3=10,
    width=30,
)
"""wrap - грамотный перенос слов, 
insertbackground - цвет курсора 
selectbackground - цвет выделения
spacing3 - отступ между абзацами ; width - ширина текста 
"""
text_fild.pack(expand=1, fill=BOTH, side=LEFT, padx=20, pady=20)
# задаем текстовое поле
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)
root.mainloop()
