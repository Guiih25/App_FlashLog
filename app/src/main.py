import flet as ft
from flet import Colors


def main(page: ft.Page):
    page.title = "App FlashLog"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    # Configuração do tamanho da janela
    page.window.width = 373
    page.window.height = 695

    # Conteúdo principal da página
    content_column = ft.Column(
        [
            ft.Image(
                src="../src/assets/img.png",
                width=150,
                margin=ft.Margin.only(bottom=100)
            ),
            ft.Image(
                src="../src/assets/van.png",
                border_radius=ft.BorderRadius.all(50),
                width=250,
                margin=ft.Margin.only(bottom=20)

            ),


            ft.Text(
                "Bem-vindo",
                size=40,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            ft.Text(
                "Uma interface moderna e fluida construída inteiramente com Flet.",
                size=16,
                color=ft.Colors.WHITE70,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),  # Espaçador
            ft.Button(
                "Começar Agora",
                on_click=lambda _: print("Botão clicado!"),
                style=ft.ButtonStyle(
                    color=ft.Colors.BLUE_800,
                    bgcolor=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=20,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    # Corrigido: Uso do ft.DecorationImage para carregar o fundo
    main_layout = ft.Container(
        content=ft.Container(
            content=content_column,
            alignment=ft.Alignment(0, 0),
            padding=20,
        ),
        image=ft.DecorationImage(
            src="../src/assets/tela4.png",

        ),
        expand=True,
    )

    page.add(main_layout)


# Corrigido: Atualizado de ft.app para ft.run() para remover o aviso do terminal
ft.run(main)
