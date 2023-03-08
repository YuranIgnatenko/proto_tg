from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.screenmanager import ScreenManager, Screen

from frontend_kivy.pagetimeline import PagesTimeline
from frontend_kivy.pagedirect import PagesDirect
# from frontend_kivy.pagesettings import PagesSettings

import frontend_kivy.const as const

WIN_W = const.WIN_W
WIN_H = const.WIN_H
NAME_START_PAGE = const.NAME_START_PAGE
BTN_H = const.BTN_H
COUNT_BTN = const.COUNT_BTN

class MyApp(App):
    def set_user_tg(self, user_tg):
        self.user_tg = user_tg
        
    def theme_app_pages(self):
        data_timeline = [x for x in self.user_tg.get_timeline()]
        data_direct = [x for x in self.user_tg.get_direct()]
        
        page_direct = PagesDirect().get(data_direct)
        page_timeline = PagesTimeline().get(data_timeline)
        # page_settings = PagesSettings().get()
        
        box = PageLayout()
        box.add_widget(page_timeline)
        box.add_widget(page_direct)
        # box.add_widget(page_settings)
        return box
    
    def theme_app_tabs(self):
        root = BoxLayout()
        panel = TabbedPanel()
        tabs1 = TabbedPanelHeader(text='Tab1')
        tabs2 = TabbedPanelHeader(text='Tab2')
        tabs3 = TabbedPanelHeader(text='Tab3')
        panel.add_widget(tabs1)
        panel.add_widget(tabs2)
        panel.add_widget(tabs3)
        root.add_widget(panel)
        return root
    
    def theme_app_screens_table(self):
        root = FloatLayout()
        sm = ScreenManager(pos=(0, BTN_H))

        scr_login = Screen(name='login',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_bio = Screen(name='bio',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_direct = Screen(name='direct',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_timeline = Screen(name='timeline',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_groups = Screen(name='groups',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_settings = Screen(name='settings',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))


        data_timeline = [x for x in self.user_tg.get_timeline()]
        data_direct = [x for x in self.user_tg.get_direct()]

        page_direct = PagesDirect().get(data_direct)
        page_timeline = PagesTimeline().get(data_timeline)
        # page_settings = PagesSettings().get()
        
        scr_direct.add_widget(page_direct)
        # scr_settings.add_widget(page_settings)
        scr_timeline.add_widget(page_timeline)

        sm.add_widget(scr_direct)
        sm.add_widget(scr_timeline)
        sm.add_widget(scr_settings)
        
            
        def open_direct():
            sm.current = "direct"
            sm.transition.direction = "right"
            
        def open_timeline():
            sm.current = "timeline"
            sm.transition.direction = "right"
            
        def open_settings():
            sm.current = "settings"
            sm.transition.direction = "right"
        
        bt_direct = Button(text="Direct",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))
        bt_timeline = Button(text="Timeline",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))
        bt_settings = Button(text="Settings",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))

        bt_direct.on_press = open_direct
        bt_timeline.on_press = open_timeline
        bt_settings.on_press = open_settings
        
        box_btn = BoxLayout()
        
        box_btn.add_widget(bt_direct)
        box_btn.add_widget(bt_timeline)
        box_btn.add_widget(bt_settings)
                
        root.add_widget(sm)
        root.add_widget(box_btn)
        
        sm.current = NAME_START_PAGE
                
        return root
     
    def theme_app_screens_table_add_image(self):
        root = FloatLayout()
        sm = ScreenManager(pos=(0, BTN_H))

        scr_direct = Screen(name='direct',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_timeline = Screen(name='timeline',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        # scr_settings = Screen(name='settings',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
        #                     pos = (0,0))


        data_timeline = [x for x in self.user_tg.get_timeline_full()]
        data_direct = [x for x in self.user_tg.get_direct()]


        page_direct = PagesDirect().get_pretty_mode(data_direct)
        page_timeline = PagesTimeline().get_pretty_mode(data_timeline)
        # page_settings = PagesSettings().get()
        

        scr_direct.add_widget(page_direct)
        # scr_settings.add_widget(page_settings)
        scr_timeline.add_widget(page_timeline)
        
        sm.add_widget(scr_direct)
        sm.add_widget(scr_timeline)
        # sm.add_widget(scr_settings)

            
        def open_direct():
            sm.current = "direct"
            sm.transition.direction = "right"
            
        def open_timeline():
            sm.current = "timeline"
            sm.transition.direction = "right"
            
        # def open_settings():
        #     sm.current = "settings"
        #     sm.transition.direction = "right"

        bt_direct = Button(text="Direct",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))
        bt_timeline = Button(text="Timeline",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))
        # bt_settings = Button(text="Settings",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))

        bt_direct.on_press = open_direct
        bt_timeline.on_press = open_timeline
        # bt_settings.on_press = open_settings
        
        box_btn = BoxLayout()
        
        box_btn.add_widget(bt_direct)
        box_btn.add_widget(bt_timeline)
        # box_btn.add_widget(bt_settings)
                
        root.add_widget(sm)
        root.add_widget(box_btn)
        
        sm.current = NAME_START_PAGE
                
        return root
    
    
     
    def theme_app_only_timeline(self):
        root = FloatLayout()
        sm = ScreenManager(pos=(0, BTN_H))

        scr_login = Screen(name='login',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))
        scr_timeline = Screen(name='timeline',size=(WIN_W,WIN_H-BTN_H), size_hint=(None, None),
                            pos = (0,0))


        data_timeline = [x for x in self.user_tg.get_timeline()]

        page_timeline = PagesTimeline().get(data_timeline)
        
        scr_timeline.add_widget(page_timeline)
        
        # sm.add_widget(scr_login
        sm.add_widget(scr_timeline)
        
        def open_login():
            # print(sm.current_screen)
            sm.current = "login"
            sm.transition.direction = "right"
       
        def open_timeline():
            sm.current = "timeline"
            sm.transition.direction = "right"
     
        # bt_bio = Button(text="Bio",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))        
        bt_timeline = Button(text="Timeline",size=(WIN_W/COUNT_BTN,BTN_H), size_hint=(None, None))

        bt_timeline.on_press = open_timeline
        
        box_btn = BoxLayout()
        
        box_btn.add_widget(bt_timeline)
                
        root.add_widget(sm)
        root.add_widget(box_btn)
        
        sm.current = NAME_START_PAGE
                
        return root
    
    
    def build(self):
        from kivy.core.window import Window
        Window.size = (WIN_W, WIN_H)

        return self.theme_app_screens_table_add_image()


