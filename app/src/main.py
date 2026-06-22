import asyncio
import flet as ft
from flet import Colors, View, CrossAxisAlignment, ListView, Card, Container, Text
from rotas import rastrear_encomenda
from datetime import datetime


def main(page: ft.Page):
    page.title = "App FlashLog"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    page.window.width = 373
    page.window.height = 695

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def definir_icones(status):
        if status == "POSTADO":
            return ft.Icons.OUTBOX_OUTLINED
        elif status == "TRANSITO":
            return ft.Icons.LOCAL_SHIPPING_OUTLINED
        elif status == "CAMINHO":
            return ft.Icons.ROUTE
        elif status == "ENTREGUE":
            return ft.Icons.CHECK_CIRCLE_OUTLINE

    def definir_data(status,data):
        data_ = datetime.strptime(data, "%a, %d %b %Y %H:%M:%S GMT")

        result_data = data_.strftime("%d/%m/%Y - %H:%M")

        if status == "POSTADO":
            return result_data
        elif status == "TRANSITO":
            return result_data
        elif status == "CAMINHO":
            return result_data
        elif status == "ENTREGUE":
            return result_data

    def definir_msg(status):
        if status == "POSTADO":
            return f"Encomenda Postada"
        elif status == "TRANSITO":
            return f"Encomenda em Transito"
        elif status == "CAMINHO":
            return f"Encomenda a Caminho da sua Casa"
        elif status == "ENTREGUE":
            return f"Encomenda Entregue"

    def definir_msg2(status, galpao):
        if status == "ENTRADA":
            return f"Encomenda chegou em {galpao}"
        elif status == "SAIDA":
            return f"Encomenda saiu de {galpao}"

    def montar_lista_encomenda():
        list_view.controls.clear()

        codigo = rastrear_encomenda(input_code.value)

        if len(codigo) == 0:
            return list_view.controls.append(
                ft.Card(
                    bgcolor="#FD8065",
                    content=ft.Container(
                        ft.Row(
                            margin=ft.Margin.all(8),
                            spacing=12,
                            controls=[
                                ft.Container(
                                    width=35,
                                    height=35,
                                    bgcolor="#FF4F28",
                                    border_radius=25,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Icon(ft.Icons.CLOSE)
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            'Nenhuma Encomenda Encontrada'

                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                )
            )

        if input_code.value == "" or input_code.value == None:
            return list_view.controls.append(
                ft.Card(
                    bgcolor="#FD8065",
                    content=ft.Container(
                        ft.Row(
                            margin=ft.Margin.all(8),
                            spacing=12,
                            controls=[
                                ft.Container(
                                    width=35,
                                    height=35,
                                    bgcolor="#FF4F28",
                                    border_radius=25,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Icon(ft.Icons.CLOSE)
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            'Nenhuma Encomenda Encontrada'

                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                )
            )

        for i in codigo:
            list_view.controls.append(
                ft.Card(
                    bgcolor="#FD8065",
                    content=ft.Container(
                        ft.Row(
                            margin=ft.Margin.all(8),
                            spacing=12,
                            controls=[
                                ft.Container(
                                    width=35,
                                    height=35,
                                    bgcolor="#FF4F28",
                                    border_radius=25,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Icon(definir_icones(i['encomenda']['status_encomenda']))
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            definir_data(i['encomenda']['status_encomenda'],i['movimentacao']['data_atual']),
                                        ),
                                        ft.Text(
                                            definir_msg(i['encomenda']['status_encomenda']),
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            definir_msg2(i['movimentacao']['status_movimentacao'],
                                                         f"{i['galpao']['cidade']}/{i['galpao']['estado']}"),
                                            size=10,
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                )
            )

            page.update()


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
                                            on_click=lambda _: navegar("/tela_pesquisa"),
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

        elif page.route == "/tela_pesquisa":
            page.views.append(
                View(
                    route="/tela_pesquisa",
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


    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    input_code = ft.TextField(
        label=Text("Digite o Codigo de Rastreio", color=Colors.WHITE),
        prefix_icon=ft.Icon(ft.Icons.SEARCH, color=Colors.WHITE),
        color=Colors.WHITE,
        on_submit=lambda _: montar_lista_encomenda(),
    )

    list_view = ListView(width=373, height=450)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.update()
    route_change()

ft.run(main)
