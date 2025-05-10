import flet as ft

from fonts import *

def main(page: ft.Page):
    page.title='Textopia'
    page.theme_mode='light'
    icon_color = '#2d2d2d'
    #Устанавливаем начальную тему и цвет иконок начальной темы
    file_path=''
    content=''
    def change_theme(e):
        nonlocal icon_color  # Используем nonlocal для изменения переменной вне функции
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        # Меняем цвет темы в зависимости от текущей темы
        icon_color = '#ffffff' if page.theme_mode == 'dark' else '#2d2d2d'
        
        # Обновляем цвета иконок 
        theme_icon_button.icon_color = icon_color
        save_icon_button.icon_color = icon_color
        close_icon_button.icon_color = icon_color
        page.update()

    # Создаем IconButton для смены темы
    theme_icon_button = ft.IconButton(
        ft.Icons.SUNNY, 
        on_click=change_theme,  
        icon_color=icon_color, 
        hover_color='#e1bee7', 
        
    )
    
    #Функция для создания нового документа
    def new_doc_click(e):
        text_field.value=''
        file_name.value = 'Новый документ'
        page.update()
    
    # Функция для сохранения файла
    def save_doc_click(e):
        if file_name.value!='Новый документ':
            
                with open(file_path, 'w', encoding='utf-8') as f:
                    nonlocal content
                    content = text_field.value  # Получаем содержимое из текстового поля
                    f.write(content)  # Записываем содержимое в файл
                    page.open(
                    ft.SnackBar(content=ft.Text("Сохранено!"))) # Отображаем уведомление
            
        
        else:
           
            save_new_file = ft.FilePicker(on_result=save_file_picker_result)
            page.overlay.append( save_new_file)
            page.add(save_new_file)
            save_new_file.save_file()
            
        page.update()  
 
    def save_file_picker_result(event):
        if event.path: 
            with open(event.path, 'w', encoding='utf-8') as f:
                nonlocal file_path
                file_path=event.path
                file_name.value=event.path.split("\\")[-1]
                nonlocal content
                content = text_field.value  
                f.write(content)
                page.open(
                    ft.SnackBar(content=ft.Text("Сохранено!"), 
                                duration=ft.Duration(seconds=2),
                                )
        )
        page.update()
            
    # Функция для открытия документа        
    def open_doc_click(e):
        pick_files_dialog = ft.FilePicker(on_result=file_picker_result)
        page.overlay.append(pick_files_dialog)
        page.add(pick_files_dialog)
        pick_files_dialog.pick_files()

    def file_picker_result(event):
        try:
            if event.files:  # Проверяем, что файл был выбран
                nonlocal file_path
                file_path = event.files[0].path  # Получаем путь к файлу
            prev_file_name=file_name.value
            file_name.value=event.files[0].name
            with open(file_path, 'r', encoding='utf-8') as f:
                nonlocal content
                content = f.read()  
                text_field.value = content  
        except UnicodeDecodeError:
                file_name.value=prev_file_name
                page.open(ft.AlertDialog(
                    title=ft.Text("Ошибка"),
                    content=ft.Text("Пожалуйста откройте файл поддерживающий текстовый формат"),
                    alignment=ft.alignment.center,
                    on_dismiss=lambda e: print("Modal dialog dismissed!"),
                    title_padding=ft.padding.all(25)
                ))
        page.update() 
    banner=None

    def close_banner(e):
        # Скрываем баннер
        global banner
        page.close(banner)
        page.update()

    def close_doc_click(e):
        global banner  
        doc_text=text_field.value
        if file_path:  # Если существует путь к файлу
            
                with open(file_path, 'r', encoding='utf-8') as f:
                    doc_text = f.read()  
       
        if ((text_field.value == '') and (file_name.value == 'Новый документ')) or ((doc_text == text_field.value) and (file_name.value != 'Новый документ')):
            print(text_field.value, file_name)
            
            page.window.close()  # Закрыть приложение
        else:
            # Создаем баннер с предупреждением
            banner = ft.Banner(
                bgcolor=ft.Colors.AMBER_100,
                leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
                content=ft.Text(
                    value="У вас есть несохраненные изменения. Вы уверены, что хотите закрыть документ?",
                    color=ft.Colors.BLACK,
                ),
                actions=[
                    ft.TextButton(text="Все равно закрыть", on_click=lambda e:  page.window.close()),  # Закрывает приложение
                    ft.TextButton(text="Остаться", on_click=close_banner),  # Закрывает баннер
                ],
            )
            page.open(banner)  # Добавляем баннер на страницу
            page.update()

   
    
    file_name=ft.Text(value='Новый документ', expand=True)

    
    save_icon_button=ft.IconButton(
        ft.Icons.SAVE,
        icon_color=icon_color, 
        hover_color='#e1bee7', 
        on_click=save_doc_click)
    
    close_icon_button=ft.IconButton(
        ft.Icons.CLOSE,
        icon_color=icon_color,
        hover_color='#e1bee7',
        on_click=close_doc_click
        )
    
    page.appbar=ft.AppBar(
        leading=ft.Image(src='C:\\Users\\Honor\\Desktop\\иконка textopia.png',fit=ft.ImageFit.CONTAIN),
        title=ft.Image(src='C:\\Users\\Honor\\Desktop\\лого практика уменьш.png',fit=ft.ImageFit.CONTAIN),
        center_title=False,
        bgcolor=ft.Colors.ON_TERTIARY,
        actions=
            [
                
                
                theme_icon_button,
                file_name,
                save_icon_button,
                close_icon_button,
                
                
            ],
        toolbar_height=60,
    )
    page.add(page.appbar)
   
    

    txt_number = ft.TextField(value="12", text_align="center", width=100,text_vertical_align=-1, border_color=ft.Theme,bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        text_field.text_size=txt_number.value
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        text_field.text_size=txt_number.value
        page.update()


    current_text_style = ft.TextStyle()

    def italic_button(e):
        nonlocal current_text_style  
        current_text_style = ft.TextStyle(
            italic=not current_text_style.italic,
            weight=current_text_style.weight,
            font_family=current_text_style.font_family,
            decoration=current_text_style.decoration
            
        )
        text_field.text_style = current_text_style
        page.update()

    def bold_button(e):
        nonlocal current_text_style
        current_text_style = ft.TextStyle(
            italic=current_text_style.italic,
            weight= 'BOLD' if current_text_style.weight != 'BOLD' else 'NORMAL',
            font_family=current_text_style.font_family,
            decoration=current_text_style.decoration
        )
        text_field.text_style=current_text_style
        page.update()

    def underline_button(e):
        nonlocal current_text_style
        current_text_style = ft.TextStyle(
            italic=current_text_style.italic,
            weight= current_text_style.weight,
            font_family=current_text_style.font_family,
            decoration=ft.TextDecoration.UNDERLINE if current_text_style.decoration!=ft.TextDecoration.UNDERLINE else ft.TextDecoration.NONE
        )
        text_field.text_style=current_text_style
        page.update()

    def change_text_color_button(e):
        ch_col_text.icon_color=inp_col_text.value
        ch_col_text.focus_color=inp_col_text.value
        text_field.color=inp_col_text.value
        page.update()
    
    ch_col_text=ft.IconButton(ft.Icons.CIRCLE, icon_color=ft.Colors.BLACK,icon_size=30)  
    inp_col_text=ft.TextField( width=90,value='', hint_text='#000000',read_only=False, bgcolor=ft.Colors.WHITE, on_submit=change_text_color_button, color=ft.Colors.BLACK)
    sep=ft.TextField(border_color=ft.Colors.ON_TERTIARY)

    def dropdown_font_changed(e):
        e.control.font = e.control.value
        current_text_style.font_family=e.control.value
        text_field.text_style=current_text_style
        page.update()


    align_list = [
        {"По ширине": ft.TextAlign.JUSTIFY, "align_name": ft.Icons.FORMAT_ALIGN_JUSTIFY},
        {"По центру": ft.TextAlign.CENTER, "align_name": ft.Icons.ALIGN_HORIZONTAL_CENTER},
        {"По левому краю": ft.TextAlign.LEFT, "align_name": ft.Icons.ALIGN_HORIZONTAL_LEFT},
        {"По правому краю":ft.TextAlign.RIGHT, "align_name": ft.Icons.ALIGN_HORIZONTAL_RIGHT},
    ]
    

    def dropdown_align_changed(e):
        
        alignment_value = e.control.value
        for align in align_list:
               if alignment_value in align.keys():
                      text_field.text_align=align[alignment_value]
         
        page.update()  

    def get_align_options():
        options = []
        for align in align_list:
            k,*tail=align.keys()
            options.append(
                ft.dropdown.Option(key=k, leading_icon=align["align_name"])
            )
        return options

    menubar=ft.MenuBar(
        
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            padding=3,
            bgcolor=ft.Colors.TERTIARY_CONTAINER,
            
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text('Файл', text_align=ft.TextAlign.CENTER, weight=3),
                
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text('Создать'),
                        leading=ft.Icon(ft.Icons.CREATE_NEW_FOLDER),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED:ft.Colors.TERTIARY_CONTAINER}
                        ),
                        on_click=new_doc_click,
        
                    ),
                    ft.MenuItemButton(
                        content=ft.Text('Открыть'),
                        leading=ft.Icon(ft.Icons.FILE_OPEN),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.TERTIARY_CONTAINER}
                        ),
                         on_click=open_doc_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text('Сохранить'),
                        leading=ft.Icon(ft.Icons.SAVE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.TERTIARY_CONTAINER}
                        ),
                         on_click=save_doc_click,
                    ),
                    


                ]
            ),
            sep,
            
            ft.Dropdown(
                editable=True,
                hint_text='Шрифт',
                options=get_options(),
                on_change=dropdown_font_changed,
                border_width=0,
                enable_filter=True,
                label_content='',
                autofocus=True,
                menu_height=150
            ),

            sep,
            ft.Row(controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click,icon_color=ft.Colors.ON_TERTIARY_CONTAINER),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click,icon_color=ft.Colors.ON_TERTIARY_CONTAINER),
            ], width=200,
            ),
            sep,
            ft.Dropdown(
                editable=True,
                leading_icon=ft.Icons.FORMAT_ALIGN_JUSTIFY,
                hint_text="Выравнивание",
                options=get_align_options(),
                width=230,
                border_width=0,
                on_change=dropdown_align_changed,
                
            ),
            sep,
            ft.Row(controls=[
                ft.IconButton(ft.Icons.FORMAT_ITALIC, on_click=italic_button,icon_size=30,icon_color=ft.Colors.ON_TERTIARY_CONTAINER),
                
                
            ], width=45,
            ),
            sep,
            ft.Row(controls=[
    
                ft.IconButton(ft.Icons.FORMAT_BOLD, on_click=bold_button,icon_size=30,icon_color=ft.Colors.ON_TERTIARY_CONTAINER),
                
            ], width=45,
            ),

            sep,
            ft.Row(controls=[
    
                ft.IconButton(ft.Icons.FORMAT_UNDERLINE, on_click=underline_button,icon_size=30,icon_color=ft.Colors.ON_TERTIARY_CONTAINER),
                
            ], width=45,
            ),
            sep,
            ft.Row(controls=[
    
                ch_col_text,
                
                
            ], width=40,
            )
            


        ]
    )
    
   
        

    
    layout = ft.Row(controls=[menubar, inp_col_text], alignment=ft.MainAxisAlignment.START)

    
    page.add(layout)
    
    
    text_field = ft.TextField(
        expand=True, 
        content_padding=20,
        multiline=True,
        border_width=0,
        bgcolor=ft.Colors.SURFACE,
        focused_bgcolor=ft.Theme,
        selection_color='#e1bee7',
        text_size=int(txt_number.value),
        
    )
    text_field.hover_color=text_field.bgcolor

  
    page.add(ft.Divider(color=ft.Theme, thickness=3))
    page.add(text_field)
    page.add(ft.Divider(color=ft.Theme,thickness=3))


ft.app(target=main)
