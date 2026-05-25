import flet as ft

def main(page: ft.Page):
    # Configurações de alinhamento da página
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Elemento da imagem de fundo
    background_image = ft.Image(
        src="assets/Captura de tela 2026-05-19 084347.png", # URL ou caminho local
        fit=ft.ImageFit.COVER,
        expand=True,
    )

    # Conteúdo que vai ficar na frente do fundo
    content = ft.Container(
        content=ft.Column(
            [
                ft.Text("Olá, Mobile!", size=30, color="white", weight="bold"),
                ft.ElevatedButton("Clique Aqui"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

    # O Stack sobrepõe os elementos (fundo primeiro, conteúdo depois)
    page.add(
        ft.Stack(
            [
                background_image,
                content,
            ],
            expand=True,
        )
    )

ft.app(target=main)
