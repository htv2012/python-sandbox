import flet as ft


def main(page: ft.Page):
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def set_number(delta: int):
        value = int(txt_number.value) + delta
        txt_number.value = str(value)
        page.update()

    def minus_click(_):
        set_number(-1)

    def plus_click(_):
        set_number(1)

    page.add(
        ft.Row(
            [
                txt_number,
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)

# As web browser app
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
