import flat as ft

class JanelaPrincipal:
  def __init__(self, page: ft.Page):
    self.page = page
    self.page.bgcolor = ft.colors.WHITE
    self.page.window_width = 350
    
    