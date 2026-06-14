from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class ContactApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Contact Maker'))
        btn = Button(text='Create VCF File')
        btn.bind(on_press=self.create_vcf)
        layout.add_widget(btn)
        return layout

    def create_vcf(self, instance):
        with open("contacts.vcf", "w") as f:
            f.write("BEGIN:VCARD\nVERSION:3.0\nFN:Test\nTEL:09121234567\nEND:VCARD")
        print("Done!")

if __name__ == "__main__":
    ContactApp().run()
