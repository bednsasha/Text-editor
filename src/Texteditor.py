from tkinter import *


def change_theme(theme):
    text_fild["bg"] = theme_colors[theme]["text_bg"]
    text_fild["fg"] = theme_colors[theme]["text_fg"]
    text_fild["insertbackground"] = theme_colors[theme]["cursor"]
    text_fild["selectbackground"] = theme_colors[theme]["select_bg"]


def change_fonts(ch_font):
    text_fild["font"] = font_list[ch_font]["font"]


root = Tk()
# создаем объект на основе класса Tk
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
root.config(menu=file_menu)
# Создаем выпадающий список "Файл", в котором будут находиться команды Открыть и Сохранить

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label="Тёмная", command=lambda: change_theme("dark"))
view_menu_sub.add_command(label="Светлая", command=lambda: change_theme("light"))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)
font_menu_sub.add_command(label="Arial", command=lambda: change_fonts("Arial"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: change_fonts("CSMS"))
font_menu_sub.add_command(label="Times New Roman", command=lambda: change_fonts("TNR"))
view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub)
root.config(menu=view_menu)


# Добавляем выпадающий список в меню
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Вид", menu=view_menu)


""""----------------------------------------------------------------------"""
root.config(menu=main_menu)
# к опции menu  присваиваем экземпляр Menu через переменную
root.title("Текстовый редактор")
root.geometry("900x600")
root.iconbitmap()
# создаем окно и настраиваем его параметры: имя, размер, иконку (по умолчанию)
f_text = Frame(root, bg="#2d2d2d")
f_text.pack(fill=BOTH, expand=1)
"""создаем фрейм на основе нашего объекта, задаем параметр fill - тем самым устанавливаем
то, что при увеличении размера окна, наш фрэйм также будет расстягивать и по x  и по y
устанавливаем expand - в значении True, при наличии свободного места, фрейм перемещается
в центр окна"""

theme_colors = {
    "dark": {
        "text_bg": "#606060",
        "text_fg": "white",
        "cursor": "#e1bee7",
        "select_bg": "#7b1fa2",
    },
    "light": {
        "text_bg": "white",
        "text_fg": "black",
        "cursor": "#7b1fa2",
        "select_bg": "#9c27b0",
    },
}

font_list = {
    "Arial": {"font": "Arial 14"},
    "CSMS": {"font": ("Comic Sans MS", 14)},
    "TNR": {"font": ("Times New Roman", 14)},
}

text_fild = Text(
    f_text,
    bg="white",
    fg="black",
    bd=1,
    wrap=WORD,
    insertbackground="#7b1fa2",
    selectbackground="#9c27b0",
    spacing3=10,
    width=30,
    font="Arial 12",
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
# Создаем скролл


root.mainloop()
