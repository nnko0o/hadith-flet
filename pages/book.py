from flet import *

from componets.hadith import Hadith
from componets.utils import P , Center
from componets.divider import Diivider

class Book(UserControl):
    def __init__(self, title:str, cover:str, page: Page, hadith_data: list):
        super().__init__()
        self.hadith_data = hadith_data
        self.title = title
        self.cover = cover
        self.page = page
        self.app_bar = self._build_app_bar()

        self.hadiths = []
    
    def _build_app_bar(self) -> AppBar:
        self._app_bar = AppBar(
            title=Container(
                content=Row(
                    controls=[
                            Text('الباقيات الصالحات', size=30, color=colors.LIGHT_BLUE_700),
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                padding=4,
                margin=4,
                alignment=alignment.center
            ),
            actions=[
                IconButton(
                    icon=icons.BOOK_SHARP,
                    icon_color=colors.LIGHT_BLUE_700,
                    url='https://t.me/nnk0o',
                    url_target='blank'
                    # on_click=lambda e: self.page.launch_url('https://t.me/nnk0o', web_popup_window=True),
                ),
            ]
        )
        return self._app_bar
    
    def _build_hadiths(self):
        for hadith in self.hadith_data: # ['content', True]
            print(hadith)
            self.hadiths.append(
                Hadith(self.page, 'Hadith', hadith[0], hadith[1], self.width)
            )
        
        return self.hadiths

    def build(self):
        self._build_hadiths()

        self._content = Container(
            content=Column(
                controls=[
                    Center(
                        Row(
                            controls=[
                                Container(
                                    image_src=self.cover,
                                    height=185,
                                    width=128 ,
                                    #padding=padding.only(right=19),
                                    margin=0  ,
                                    border_radius=BorderRadius(5, 1, 5, 5),
                                    border=border.all(0.9, colors.with_opacity(0.7, colors.LIGHT_BLUE_700))
                                ),
                                P(
                                    Text(
                                        value=self.title + '  ',
                                        size=34,
                                        weight=FontWeight.W_700
                                    ),
                                    margin=padding.only(35, 0, 0, 0),

                                )
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ),
                    Diivider(
                        height=1,
                        width=self.width,
                    ),
                    ListView(
                        controls=self.hadiths,
                        padding=15,
                        spacing=15,
                        auto_scroll=True
                    ),
                ],
            ),
            
        )
        return self._content