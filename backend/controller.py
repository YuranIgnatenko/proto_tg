from telethon.sync import TelegramClient
from backend.config import *
import os

class TimeLinePost():
    def __init__(self, sender, msg_text, msg_date):
        self.sender  = sender
        self.message_text = msg_text
        self.message_date = msg_date
        
class TimeLineFullPost():
    def __init__(self, sender, msg_text, msg_date, msg_views,msg_url_prev,msg_edit_date, msg_geo,msg_ar_photos):
        self.sender  = sender
        self.message_text = msg_text
        self.message_date = msg_date
        self.message_views = msg_views
        self.message_url_prev = msg_url_prev
        self.message_edit_date = msg_edit_date
        self.sender_geo = msg_geo
        self.images_path_files = msg_ar_photos
        
        
class DirectPost():
    def __init__(self, sender, msg_text, msg_date):
        self.sender  = sender
        self.message_text = msg_text
        self.message_date = msg_date
        

class Tg():
    def __init__(self):       
        self.client = TelegramClient(phone, api_id, api_hash)
        self.client.start()
        print(self.client)

    def get_groups(self):
        groups = ["test channel and groups"]
        for dialog in self.client.iter_dialogs():
            if  dialog.is_group or dialog.is_channel:
                groups.append(dialog.name)
        return groups
    
    def get_direct(self):
        direct = []
        max_length_sym_in_line = 30
        for dialog in self.client.iter_dialogs():
            if not dialog.is_group and not dialog.is_channel:
                if str(dialog.message.message).strip() == "":
                    continue
                if str(dialog.name).strip() == "":
                    continue
                new_message_text = self.convert_small_string(dialog.message.message)
                direct.append(DirectPost(dialog.name, new_message_text, dialog.message.date))
        return direct
    
    def get_allmsg(self):
        groups = ["test all chats"]   
        for dialog in self.client.iter_dialogs():
                groups.append(dialog.name)
        return groups

    def convert_small_string(self, line):
        max_length_sym_in_line = 60
        new_message_text = ""
        csym = 0
        try:
            for s in line:
                if csym >= max_length_sym_in_line:
                    csym = 0
                    new_message_text += "\n"
                new_message_text += s
                csym += 1
        except:
            new_message_text = str(line)
        return new_message_text

    def get_timeline(self):
        timelineposts = [] # objects TimeLinePost 
        c = 0
        max_v = 40
        max_length_sym_in_line = 40
        for dialog in self.client.iter_dialogs():
            if c > max_v:return timelineposts
            c+=1

            if  dialog.is_group or dialog.is_channel:
                # long string -> convert smail little partions
                new_message_text = self.convert_small_string(dialog.message.message)
                
                timelineposts.append(TimeLinePost(dialog.name, new_message_text, dialog.message.date))
                # groups.append(f"{dialog.name}:{dialog.message}")
                print(dir(dialog.message), "\n\n\n", dialog.message.media, "\n", dialog.message.date, "\n", dialog.message.file)
                # return
        return timelineposts

    def get_timeline_full(self):
        timelinefullposts = [] # objects TimeLineFullPost 
        c = 0
        imc = 0
        max_v = 50
        max_length_sym_in_line = 40
        path_photo = "not_found_photo"
        for dialog in self.client.iter_dialogs():
            # timed finish
            if c > max_v:return timelinefullposts
            c+=1

            if  not dialog.is_user:
                
                new_message_text = self.convert_small_string(dialog.message.message)
                
                if str(type(dialog.message.media)).find("MessageMediaPhoto") != -1: 
                    path_photo = PREFIX_PATH_PHOTO + str(imc) + ".jpg"
                    if not os.path.isfile(path_photo):
                        dialog.message.download_media(path_photo)
                    imc += 1

                
                tlf_post = TimeLineFullPost(
                        dialog.name, 
                        new_message_text, 
                        dialog.message.date,
                        dialog.message.views,
                        "not_found_url", # dialog.message.web_preview.url,
                        dialog.message.edit_date,
                        dialog.message.geo,
                        path_photo
                        )
                # print(f"{tlf_post.images_path_files}")
                timelinefullposts.append(tlf_post)
                
                # RESET NAMES
                path_photo = "not_found_photo"
                
                
        return timelinefullposts



class Profile():
    def __init__(self):
        self.tg = Tg()
        
    def get_direct(self):
        self.direct = self.tg.get_direct()
        return self.direct
    
    def get_groups(self):
        self.groups = self.tg.get_groups()
        return self.groups
    
    def get_timeline(self):
        self.timeline = self.tg.get_timeline()
        return self.timeline
    
    def get_timeline_full(self):
        self.timeline_full = self.tg.get_timeline_full()
        return self.timeline_full
    
    def get_allmsg(self):
        self.allmsg = self.tg.get_allmsg()
        return self.allmsg
        
