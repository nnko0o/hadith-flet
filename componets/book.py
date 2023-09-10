from flet import *
from componets.utils import P, Center

from pages.book import Book as BookView

class Book(UserControl):
    def __init__(
        self,
        page: Page,
        name:str,
        subtext:str,
        cover:str, # URL or Path in `assets` dir
        hadith:list,
    ):
        super().__init__()
        self.page = page
        self.name = name
        self.subtext = subtext
        self.cover = cover
        self._hdata = hadith

    async def on_click_book(self, e: ControlEvent):
        page_t = BookView(
            self.name,
            self.cover,
            self.page,
            self._hdata,
        )
        self.page.views.append(
            View(
                '/',
                controls=[
                    page_t,
                ],
                appbar=page_t._build_app_bar(),
                scroll=ScrollMode.ALWAYS
            )
        )
        await self.page.update_async()

    def build(self):
        self._content = Container(
            content=Row(
                controls=[
                    Container(
                        image_src='images/Al-Kafi.jpg',
                        height=185,
                        width=128 ,
                        #padding=padding.only(right=19),
                        margin=0  ,
                        border_radius=BorderRadius(5, 1, 5, 5),
                        border=border.all(0.9, colors.with_opacity(0.7, colors.LIGHT_BLUE_700))
                    ),
                    P(
                        Column(
                            controls=[

                                Text(
                                    value=self.name,
                                    size=24,
                                    weight=FontWeight.W_700,
                                ),
                                Center(
                                    Text(
                                        value=self.subtext,
                                        size=12,
                                    )
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.START,
                            run_spacing=9,
                        ),
                        padding.only(left=30, )
                    )
                ],
                alignment=MainAxisAlignment.START
            ),
            bgcolor=colors.with_opacity(0.1, colors.WHITE10),
            padding=10,
            margin=10,
            border=border.all(1, colors.GREY_800,),
            border_radius=10,
            on_click=self.on_click_book,
            ink=True
        )

        return self._content
