from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton

class Example(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            column_data=[
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),

            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                ("1", "2"),
                ("1", "2"),
                ("1", "2"),
            ],
        )

    def on_start(self):
        self.data_tables.open()


Example().run()