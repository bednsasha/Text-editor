from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

name = "Новый документ"


def file_name(Name):
    global name  # Объявление переменной name как глобальной
    name = Name
    update_file_menu()  # Обновляем отображение имени файла в меню


def update_file_menu():
    # Обновляем текст в пункте меню "Новый документ"
    main_menu.entryconfig(3, label=name)


def new_file():
    text_fild.delete("1.0", END)
    file_name("Новый документ")


def change_theme(theme):
    text_fild["bg"] = theme_colors[theme]["text_bg"]
    text_fild["fg"] = theme_colors[theme]["text_fg"]
    text_fild["insertbackground"] = theme_colors[theme]["cursor"]
    text_fild["selectbackground"] = theme_colors[theme]["select_bg"]


def change_fonts(ch_font):
    text_fild["font"] = font_list[ch_font]["font"]


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Выбор файла",
        filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")),
    )
    # открываем окно, с выбором файла с компьютера, askopenfilename(...) возвращает путь файла
    if file_path:
        text_fild.delete("1.0", END)
        # очищаем поле с первого символа

        text_fild.insert("1.0", open(file_path, encoding="utf-8").read())
        file_name(file_path[file_path.rindex("/") + 1 :])
        # считываем и записываем данный с файла


def save_file():
    global file_path  # Объявляем переменную file_path глобальной для использования
    if name == "Новый документ":  # Если файл еще не сохранен
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")),
        )

    # Сохраняем файл
    with open(file_path, "w", encoding="utf-8") as f:
        text = text_fild.get("1.0", END)
        f.write(text)


def close_file():
    # Определяем, есть ли что-то в текстовом поле
    current_text = text_fild.get("1.0", END).strip()

    # Проверяем, если текущий текст пуст и имя документа "Новый документ", ничего не сохраняем
    if current_text == "" and name == "Новый документ":
        root.destroy()  # Просто закрываем приложение

    # Проверяем, есть ли несохраненные изменения в тексте
    elif current_text != "" and name == "Новый документ":
        answer = messagebox.askokcancel(
            "Выход", "У вас есть несохраненные изменения. Вы точно хотите выйти?"
        )
        if answer:
            root.destroy()

    # Если документ был открыт и изменен
    elif name != "Новый документ":
        # Сравниваем текущее содержимое с тем, что было сохранено
        with open(file_path, "r", encoding="utf-8") as file:
            saved_text = file.read().strip()

        if current_text != saved_text:
            answer = messagebox.askokcancel(
                "Выход", "У вас есть несохраненные изменения. Вы точно хотите выйти?"
            )
            if answer:
                root.destroy()
        else:
            root.destroy()  # Закрываем приложение, если ничего не изменилось


root = Tk()
# создаем объект на основе класса Tk
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Создать", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Закрыть", command=close_file)
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
main_menu.add_command(label=name, command=lambda: file_name("Новый документ"))


""""----------------------------------------------------------------------"""
root.config(menu=main_menu)
# к опции menu  присваиваем экземпляр Menu через переменную
root.title("Textopia")
root.geometry("900x600")
icon = PhotoImage(file="C:\\Users\\Honor\\Desktop\\иконка textopia.png")
root.iconphoto(False, icon)


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
