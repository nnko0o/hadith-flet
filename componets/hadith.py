from flet import *
from .divider import Diivider
from .utils import P

class Hadith(UserControl):
    def __init__(
        self,
        page: Page,
        title: str,
        content: str,
        grading:bool,
        width
    ):
        super().__init__()
        self.p = page
        self.title = title
        self.content = content
        self.grading = grading
        self.width   = width

        self.divider_width = self.width
    
    def _build_title(self):
        self._title = Container(
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    Container(
                                        width=4,
                                        height=27,
                                        bgcolor=colors.LIGHT_BLUE_700,
                                        padding=5
                                    ),
                                    Text(
                                        value=f'{self.title}',
                                        size=17,
                                        color=colors.LIGHT_BLUE_700,
                                        weight=FontWeight.W_700
                                    ),
                                ]
                            ),
                            P( 
                                #Diivider(
                                #    height=0.8,
                                #    width=self.divider_width,
                                #    color=colors.LIGHT_BLUE_700,
                                #),
                                None,
                                1,
                                1
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.START
                    ),

                    self._build_grading()
                ],
                
            )
        )
        return self._title

    def _build_content(self):
        self._content = Container(
            content=Column(
                controls=[
                    Text(
                        value=self.content,
                        width=320,
                        text_align=TextAlign.JUSTIFY,
                        size=14,
                        selectable=True,
                        #font_family='org'
                    )
                ],

            )
        )
        return self._content

    def _build_grading(self, show_text:bool = False):
        if show_text:
            if self.grading:
                text = 'سنده صحيح'
            else:
                text= 'سنده ضعيف'
        else:
            text = None

        self._grading = Container(
            content=Column(
                controls=[
                    P(
                        Row(
                            controls=[
                                P(
                                    Icon(
                                        name=icons.CHECK_CIRCLE_SHARP if self.grading else icons.CANCEL_SHARP,
                                        color=colors.LIGHT_BLUE_700 if not show_text else (colors.GREEN_700 if self.grading else colors.RED_ACCENT_200),
                                        size= 28 if show_text else 20
                                    ), padding.only(left=4, top=4, ),
                                ),
                                Text(
                                    value=text,
                                    color=colors.GREEN_800 if self.grading else colors.RED_ACCENT_200,
                                    size=12
                                ) 
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        padding.only(bottom=2) if show_text     else None,
                        margin.only(bottom=17) if not show_text else None,
                    )
                ]
            ),
            alignment=alignment.center,
            #bgcolor=colors.with_opacity(0.2, colors.WHITE)
        )
        return self._grading

    def build(self):
        title   = self._build_title()
        content = self._build_content()
        grading = self._build_grading(True)
        self._c = Container(
            content=Column(
                controls=[
                    title,
                    P(margin=margin.only(bottom=5)),
                    content,
                    P(margin=margin.only(bottom=5, top=1)),
                    Diivider(
                        height=0.7,
                        width=self.divider_width,
                        color=colors.LIGHT_BLUE_500,
                    ),
                    grading
                    
                ]
            ),
            bgcolor=colors.with_opacity(0.1, colors.WHITE10),
            border=border.all(1, colors.GREY_800,),
            border_radius=10,
            padding=15,
            margin=margin.only(right=5, left=5, top=2)
        )
        self.divider_width = 9 # SET THE NEW WIDTH
        # self.update()
        return self._c