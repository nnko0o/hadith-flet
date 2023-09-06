from flet import *
import asyncio
import sys
sys.setrecursionlimit(1000000)
print("Start..")


class P(UserControl):
    def __init__(
          self,
          content:Control                = None,
          padding: PaddingValue          = 0   ,
          margin : int | float | Margin  = 0   ,
          valigmint: MainAxisAlignment   = None,
          haligmint: CrossAxisAlignment  = None,
        ):
        super().__init__()
        self.content = content
        self.padding = padding
        self.margin  = margin
        self.v = valigmint
        self.h = haligmint

    def build(self):
        return Container(
            content=self.content,
            margin =self.margin ,
            padding=self.padding,
        )

class Diivider(UserControl):
    def __init__(self, height:int|float = 1, width:int|float = 0, color:str=colors.LIGHT_BLUE_700):
        super().__init__()
        self.w = width
        self.h = height
        self.c = color

    def build(self):
        return Container(
            width=self.w,
            height=self.h,
            bgcolor=self.c,
            padding=1
        )

class Hadith(UserControl):
    def __init__(
        self,
        page: Page,
        title: str,
        content: str,
        grading:bool,
    ):
        super().__init__()
        self.p = page
        self.title = title
        self.content = content
        self.grading = grading
    
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
                                        color=colors.LIGHT_BLUE_700
                                    ),
                                ]
                            ),
                            P( 
                                Diivider(
                                    height=0.8,
                                    width=240,
                                    color=colors.LIGHT_BLUE_700,
                                ),
                                2,
                                1
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.START
                    ),

                    self._build_grading()
                ]
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
                                        color=colors.GREEN_700 if self.grading else colors.RED_ACCENT_200,
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
                        padding.only(bottom=2),
                        margin.only(bottom=12) if not show_text else None
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
                        width=420,
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
        return self._c

class App(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.p = page
    
    def build(self):
        self.hadith_list = [
            Hadith(
                self.p,
                "عن ولادة رسول الله ص",
                "الْحُسَيْنُ بْنُ مُحَمَّدٍ الاشْعَرِيُّ عَنْ مُعَلَّى بْنِ مُحَمَّدٍ عَنْ أَبِي الْفَضْلِ عَبْدِ الله بْنِ إِدْرِيسَ عَنْ مُحَمَّدِ بْنِ سِنَانٍ قَالَ كُنْتُ عِنْدَ أَبِي جَعْفَرٍ الثَّانِي (a.s) فَأَجْرَيْتُ اخْتِلافَ الشِّيعَةِ فَقَالَ يَا مُحَمَّدُ إِنَّ الله تَبَارَكَ وَتَعَالَى لَمْ يَزَلْ مُتَفَرِّداً بِوَحْدَانِيَّتِهِ ثُمَّ خَلَقَ مُحَمَّداً وَعَلِيّاً وَفَاطِمَةَ فَمَكَثُوا أَلْفَ دَهْرٍ ثُمَّ خَلَقَ جَمِيعَ الاشْيَاءِ فَأَشْهَدَهُمْ خَلْقَهَا وَأَجْرَى طَاعَتَهُمْ عَلَيْهَا وَفَوَّضَ أُمُورَهَا إِلَيْهِمْ فَهُمْ يُحِلُّونَ مَا يَشَاءُونَ وَيُحَرِّمُونَ مَا يَشَاءُونَ وَلَنْ يَشَاءُوا إِلا أَنْ يَشَاءَ الله تَبَارَكَ وَتَعَالَى ثُمَّ قَالَ يَا مُحَمَّدُ هَذِهِ الدِّيَانَةُ الَّتِي مَنْ تَقَدَّمَهَا مَرَقَ وَمَنْ تَخَلَّفَ عَنْهَا مَحَقَ وَمَنْ لَزِمَهَا لَحِقَ خُذْهَا إِلَيْكَ يَا مُحَمَّدُ.",
                False
            )
            ,
            Hadith(self.p, "كلام غريب",  " قال رسول الله ص: كذات وكذا عن فللن هكذا", True),
            Hadith(self.p, "المنبه", "قال وهب بن منبه: ابي يصحيكم للدوام", False),
        ]
        self._c = Container(
            content=Column(
                controls=self.hadith_list,
                spacing=10,
                scroll=ScrollMode.AUTO,
                auto_scroll=False

            ),
            
        )
        return P(self._c)

async def main(p: Page):
    p.fonts = {
        'Iran Sans':'fonts/iran-sans-m.ttf'
    }
    p.bgcolor = colors.BLACK54
    p.theme = Theme(
        font_family='Iran Sans'
    )

    app = App(p)
    await p.add_async(
        P(app, 10,8)
    )

if __name__=='__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        app_async(
            target=main,
            host="0.0.0.0",
            port=8007,
            assets_dir='assets'
        )
    )

