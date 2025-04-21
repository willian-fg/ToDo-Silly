import flet 
from flet import(
      Checkbox,
      Column,
      FloatingActionButton,
      IconButton,
      OutlinedButton,
      Page,
      Row,
      Tab,
      Tabs,
      Text,
      TextField,
      colors,
      icons,
)

#Classes

class Task():
      def __init__(self, task_name, task_status_change, task_delete):
            super().__init__()
            self.completed = False
            self.task_name = task_name
            self.task_status_change = task_delete
            
class Silly():
      def build(self):
            self.new_task = TextField(
                  hint_text = 'Escreva a Tarefa',
                  expand = True,
                  on_submit = self.add_clicked

            
            )
            self.task = Column()

            self.filter = Tabs(
                  selected_index = 0,
                  on_change = self.tabs_changes,
                  tabs = [Tab(text = 'Todas'), Tab(text = 'Ativas'), Tab(text = 'Completas')]
            )

            return Column(
                  width = 600,
                  controls = [
                        Row([Text(value='Tarefas',
                                  style='headlineMedium')], alignment = 'center'),
                        Row()

                  ]
                        
            )

      
      def add_clicked(self):
            pass
            


#Funçâo Principal
def main(page: Page):
      page.title = "Silly"
      page.horizontal_alignment = 'center'
      page.scroll = 'adaptative'
      page.update()

      app = Silly() #Instancia da classe principal

      page.add(app) #Adição da Calsse Primcipal



flet.app(target=main)