import asyncio

import flet as ft
from flet import Colors, View, CrossAxisAlignment, ListView, Card, Container, Text
from rotas import rastrear_encomenda

def main(page: ft.Page):
    page.title = "App FlashLog"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    page.window.width = 373
    page.window.height = 695

    list_view = ListView(width=373, height=250)

    input_code = ft.TextField(
        label=Text("Digite o Codigo de Rastreio", color=Colors.WHITE),
        prefix_icon=ft.Icon(ft.Icons.SEARCH, color=Colors.WHITE),
        color=Colors.WHITE,
        on_submit=lambda _: pesquisar_encomenda(),
    )

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_encomenda():
        list_view.controls.clear()
        for i in rastrear_encomenda(input_code.value):
            list_view.controls.append(
                ft.Card(
                    bgcolor="#0A4682",
                    content = ft.Container(
                        ft.Row(
                            margin=ft.Margin.all(5),
                            spacing=12,
                            controls=[

                            ]
                        )
                    )

                )
            )


    def route_change(e=None):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    padding=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            image=ft.DecorationImage(src="../src/assets/tela4.png"),
                            content=ft.Container(
                                alignment=ft.Alignment(0, 0),
                                padding=20,
                                content=ft.Column(
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
                                        ),
                                        ft.Text(
                                            "Bem-vindo",
                                            size=35,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE_70
                                        ),
                                        ft.Text(
                                            disabled=False,
                                            text_align=ft.TextAlign.CENTER,
                                            spans=[
                                                ft.TextSpan(
                                                    "FLASHLOG\n",
                                                    style=ft.TextStyle(
                                                        size=22,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.Colors.WHITE
                                                    )
                                                ),
                                                ft.TextSpan(
                                                    "Envio sem ",
                                                    style=ft.TextStyle(
                                                        size=16,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.Colors.WHITE
                                                    )
                                                ),
                                                ft.TextSpan(
                                                    "interrupções\n",
                                                    style=ft.TextStyle(
                                                        size=16,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.Colors.ORANGE_900)),
                                                ft.TextSpan(
                                                    "Envie com ",
                                                    style=ft.TextStyle(
                                                        size=16,
                                                        weight=ft.FontWeight.W_100,
                                                        color=ft.Colors.WHITE)),
                                                ft.TextSpan(
                                                    "FLASHLOG",
                                                    style=ft.TextStyle(
                                                        size=17,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.Colors.WHITE
                                                    )
                                                ),
                                            ],
                                        ),
                                        ft.Container(height=20),
                                        ft.Button(
                                            ft.Text("ENTRAR", size=22, weight=ft.FontWeight.BOLD),
                                            on_click=lambda _: navegar("/segunda_tela"),
                                            margin=ft.Margin.only(bottom=180, left=9),
                                            bgcolor="#17385B",
                                            color=ft.Colors.WHITE,
                                            width=190,
                                            height=80,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=15,
                                )
                            )
                        )
                    ]
                )
            )

        elif page.route == "/segunda_tela":
            montar_lista_encomenda()
            page.views.append(
                View(
                    route="/segunda_tela",
                    padding=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            image=ft.DecorationImage(src="../src/assets/flamingo_2.png", ),
                            content=ft.Container(
                                alignment=ft.Alignment.CENTER,
                                padding=20,
                                content=ft.Column(
                                    spacing=5,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="../src/assets/img.png",
                                            width=150,
                                            # margin=ft.Margin.only(bottom=100)
                                        ),
                                        input_code,
                                        list_view
                                    ]
                                )
                            )
                        ),
                    ]
                )
            )

            page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.update()
    route_change()




ft.run(main)
