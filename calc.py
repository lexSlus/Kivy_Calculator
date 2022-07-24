from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 350)


class CalculatorApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_operations(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
            self.update_label()

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))

    def result_clear(self, instance):
        self.lbl.text = '0'
        self.formula = '0'

    def build(self):
        self.formula = '0'

        self.lbl = Label(text='0', font_size=40, halign='right', valign='center', size_hint=(.8, .6),
                         text_size=(400 - 50, 500 * .40 - 50))

        b1 = BoxLayout(orientation='vertical', padding=25)

        g1 = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        g1.add_widget(Button(text='7', on_press=self.add_number))
        g1.add_widget(Button(text='8', on_press=self.add_number))
        g1.add_widget(Button(text='9', on_press=self.add_number))
        g1.add_widget(Button(text='x', on_press=self.add_operations))

        g1.add_widget(Button(text='4', on_press=self.add_number))
        g1.add_widget(Button(text='5', on_press=self.add_number))
        g1.add_widget(Button(text='6', on_press=self.add_number))
        g1.add_widget(Button(text='-', on_press=self.add_operations))

        g1.add_widget(Button(text='1', on_press=self.add_number))
        g1.add_widget(Button(text='2', on_press=self.add_number))
        g1.add_widget(Button(text='3', on_press=self.add_number))
        g1.add_widget(Button(text='+', on_press=self.add_operations))

        g1.add_widget(Button(text='C', on_press=self.result_clear))
        g1.add_widget(Button(text='0', on_press=self.add_number))
        g1.add_widget(Button(text='.', on_press=self.add_number))
        g1.add_widget(Button(text='=', on_press=self.calc_result))

        b1.add_widget(self.lbl)
        b1.add_widget(g1)

        return b1


if __name__ == '__main__':
    CalculatorApp().run()
