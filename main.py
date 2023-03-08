from frontend_kivy.front_kivy import MyApp
from backend.controller import Profile

user_tg = Profile()

app = MyApp()
app.title = "TG beta v1"
app.set_user_tg(user_tg)
app.run()

# user_tg.get_timeline_full()