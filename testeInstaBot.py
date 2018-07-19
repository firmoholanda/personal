import os
import time

from instaBot.src import InstaBot

bot = InstaBot('firmoholanda', 'hollanda003#')
bot.get_media_id_by_tag('recife')
#bot.get_media_id_by_tag('smartmentorbr.t3')
#bot.get_media_id_by_tag('firmo')
bot.like_all_exist_media(1)
