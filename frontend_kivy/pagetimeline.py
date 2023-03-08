import cv2

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


import frontend_kivy.const as const

WIN_W = const.WIN_W
WIN_H = const.WIN_H

class PagesTimeline():
    def get(self, array_objects_Timeline):
        root = BoxLayout()
        list_direct = ScrollView()
        list_direct_box =   GridLayout()
        
        list_direct_box.cols = 3
        list_direct_box.size_hint_y= None
        list_direct_box.spacing = 1
        list_direct_box.bind(minimum_height=list_direct_box.setter('height'))
        list_direct_box.row_default_height = 30

        for tl in array_objects_Timeline:
            # boxtimeline = FloatLayout()
            
            sender = TextInput(text = str(tl.sender))
            msg_text = TextInput(text = str(tl.message_text))
            msg_date = TextInput(text = str(tl.message_date))

            list_direct_box.add_widget(sender)
            list_direct_box.add_widget(msg_text)
            list_direct_box.add_widget(msg_date)
            
            # list_direct_box.add_widget(boxtimeline)
        
        list_direct.add_widget(list_direct_box)
        root.add_widget(list_direct)
        return root
    
    def get_full_mode(self, array_objects_Timeline):
        root = BoxLayout()
        list_direct = ScrollView()
        list_direct_box =   GridLayout()
        
        list_direct_box.cols = 4
        list_direct_box.size_hint_y= None
        list_direct_box.spacing = 1
        list_direct_box.bind(minimum_height=list_direct_box.setter('height'))
        list_direct_box.row_default_height = 30

        for tl in array_objects_Timeline:
            boxtimeline = BoxLayout(orientation="vertical")
            
            sender = TextInput(text = str(tl.sender))
            msg_text = TextInput(text = str(tl.message_text))
            msg_date = TextInput(text = str(tl.message_date))
            try:
                msg_photo =  Image(source=tl.images_path_files)
            except:
                msg_photo = TextInput(text = "not_photo")
            
            list_direct_box.add_widget(sender)
            list_direct_box.add_widget(msg_text)
            list_direct_box.add_widget(msg_date)
            list_direct_box.add_widget(msg_photo)
            
            # list_direct_box.add_widget(boxtimeline)
        
        list_direct.add_widget(list_direct_box)
        root.add_widget(list_direct)
        return root
    
    def get_pretty_mode(self, array_objects_Timeline):
        root = BoxLayout(orientation="vertical")
        list_direct = ScrollView()
        
        list_direct_box =   BoxLayout(orientation="vertical")
        
        list_direct_box.size_hint_y= None
        list_direct_box.bind(minimum_height=list_direct_box.setter('height'))
        

        for tl in array_objects_Timeline:
            boxtimeline = BoxLayout(orientation="vertical")
            HT = 200
            sender = Label(text = str(tl.sender), height=35, size_hint=(1, None),color="red")
            msg_text = TextInput(text = str(tl.message_text),disabled=True, multiline=True, height=25*(2+str(tl.message_text).count("\n")), size_hint=(1, None))
            msg_views = Label(text = "Views: "+str(tl.message_views), height=35, size_hint=(1, None))
            msg_date = Label(text = str(tl.message_date), height=35, size_hint=(1, None))
            if tl.images_path_files != "not_found_photo":
                im = cv2.imread(tl.images_path_files)
                h,_,_ = im.shape
                output = cv2.resize(im, (WIN_W, h))
                cv2.imwrite(tl.images_path_files,output) 
                msg_photo =  Image(source=tl.images_path_files,width=WIN_W,height=h, size_hint=(None, None))
            else:
                msg_photo =  Image()
            
            list_direct_box.add_widget(sender)
            list_direct_box.add_widget(msg_photo)
            list_direct_box.add_widget(msg_text)
            list_direct_box.add_widget(msg_views)
            list_direct_box.add_widget(msg_date)
            
            
        
        list_direct.add_widget(list_direct_box)
        root.add_widget(list_direct)
        return root