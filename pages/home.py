from flet import *

from componets.book import Book
from componets.utils import P , Center

class Home(UserControl):
    def __init__(self, page: Page, data: dict):
        super().__init__()
        self.data = data
        self.page = page
        self.app_bar = self._build_app_bar()
        self.books = []
    
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
                    on_click=lambda e: self.page.launch_url('https://t.me/nnk0o', web_popup_window=True),
                ),
            ]
        )
        return self._app_bar

    def _build_books(self):
        #print(self.data.get('books'))
        if len(self.data.get('books'))==0:
            return 
        
        list_ = []
        for book in self.data.get('books'):
            list_.append(
                Book(
                    self.page,
                    book.get('title'),
                    book.get('subtext'),
                    book.get('cover'),
                    book.get('hadith'),
                )
            )
        return list_

    def build(self):
        books = self._build_books()
        #print(books)
        self.home_content = Container(
            content=Column(
                controls=books
            ),
            padding=1,
            margin =0.1,
        )

        return self.home_content
