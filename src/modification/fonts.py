import flet as ft
#Список шрифтов
fonts_list = [
        'Arial',
        'Arial Black',
        'Calibri',
        'Comic Sans MS',
        'Cooper',
        'Georgia',
        'Tahoma',
        'Times New Roman',
        'Verdana',
        
       
    ]

def get_options():
        options = []
        for font in fonts_list:
            options.append(
                ft.DropdownOption(
                    key=font,
                    content=ft.Text(
                        value=font,
                    
                       
                    ),
                )
            )
        return options


