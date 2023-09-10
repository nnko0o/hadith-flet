from flet import (
    UserControl,
    Container,
    colors,
    BorderRadius
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
            padding=1     ,
            border_radius=BorderRadius(5, 5, 5, 5)
        )