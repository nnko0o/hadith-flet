from flet import (
    UserControl,
    Control,
    CrossAxisAlignment,
    MainAxisAlignment,
    Container,
    PaddingValue,
    Margin,
    alignment
)

class P(UserControl):
    def __init__(
          self,
          content:Control                = None,
          padding: PaddingValue          = 0   ,
          margin : int | float | Margin  = 0   ,
        ):
        super().__init__()
        self.content = content
        self.padding = padding
        self.margin  = margin

    def build(self):
        return Container(
            content=self.content,
            margin =self.margin ,
            padding=self.padding,
        )

class Center(UserControl):
    def __init__(self, content: Control):
        super().__init__()
        self._content = content
    
    def build(self):
        self._result = Container(
            expand=True,
            alignment=alignment.center,
            content=self._content
        )
        return self._result


