
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.label import  Label

class PagesDirect():
    def get(self, array_objects_Direct):
        root = BoxLayout()
        list_direct = ScrollView()
        list_direct_box =   GridLayout()
        
        list_direct_box.cols = 3
        list_direct_box.size_hint_y= None
        list_direct_box.spacing = 1
        list_direct_box.bind(minimum_height=list_direct_box.setter('height'))
        list_direct_box.row_default_height = 30

        for tl in array_objects_Direct:
            
            sender = TextInput(text = str(tl.sender))
            msg_text = TextInput(text = str(tl.message_text))
            msg_date = TextInput(text = str(tl.message_date))

            list_direct_box.add_widget(sender)
            list_direct_box.add_widget(msg_text)
            list_direct_box.add_widget(msg_date)
            
        
        list_direct.add_widget(list_direct_box)
        root.add_widget(list_direct)
        return root
            
    def get_pretty_mode(self, array_objects_direct):
        root = BoxLayout(orientation="vertical")
        list_direct = ScrollView()
        
        list_direct_box =   BoxLayout(orientation="vertical")
        
        list_direct_box.size_hint_y= None
        list_direct_box.bind(minimum_height=list_direct_box.setter('height'))
        

        for tl in array_objects_direct:
            sender = Label(text = str(tl.sender), height=35, size_hint=(1, None),color="red")  
            msg_text = TextInput(text = str(tl.message_text), multiline=True, height=25*(2+str(tl.message_text).count("\n")), size_hint=(1, None))
            msg_date = Label(text = str(tl.message_date), height=35, size_hint=(1, None))
            
            list_direct_box.add_widget(sender)
            list_direct_box.add_widget(msg_text)
            list_direct_box.add_widget(msg_date)
            
        
        list_direct.add_widget(list_direct_box)
        root.add_widget(list_direct)
        return root