from pyrogram import Client, filters    
from pyrogram.types import Message
from datetime import datetime
import pytz , schedule ,re,api_key




bot = Client("SoccerBot" ,bot_token=api_key.SoccerBot_token, api_id=api_key.api_id, api_hash=api_key.api_hash)

# Class

class PlaySchedule:
    Inst = []
    def __init__(self,date,time):
        self.Date = date
        self.Time = time
        PlaySchedule.Inst.append(self)

# Data Def 

FGroup = api_key.FGroup
Ec = api_key.Ec
Enc = api_key.Enc

text = """
|2024-03-09 | 04PM - 06PM | 
|2024-03-15 | 04PM - 06PM | 
|2024-03-22 | 04PM - 06PM | 
|2024-03-29 | 04PM - 06PM |  

|2024-04-06 | 10AM - 12PM |    
|2024-04-13 | 04PM - 06PM |   
|2024-04-21 | 10AM - 12PM |  
|2024-04-26 | 04PM - 06PM | 

|2024-05-03 | 10AM - 12PM |   
|2024-05-11 | 06PM - 08PM |   
|2024-05-16 | 09AM - 11AM |   
|2024-05-24 | 04PM - 06PM |   
|2024-05-31 | 04PM - 06PM |   

|2024-06-07 | 04PM - 06PM |   
|2024-06-14 | 04PM - 06PM |   
|2024-06-19 | 04PM - 06PM |   
|2024-06-28 | 04PM - 06PM |
"""
date_strings = re.findall(r"2024-\d{2}-\d{2}", text)
play_times = re.findall(r"\b\d{2}(?:AM|PM) - \d{2}(?:AM|PM)\b", text)

# Objects 

for items in range (len(date_strings)):
    PlaySchedule(date_strings[items],play_times[items]) 

# Methods 

def method1():

    current_date = datetime.now().date()
    current_month = current_date.month
    # print(current_month)

    filtered_dates = [
        datetime.strptime(date_str, "%Y-%m-%d").date()
        for date_str in date_strings
        if datetime.strptime(date_str, "%Y-%m-%d").date().month == current_month
    ]
    for date in filtered_dates:
        if current_date == date:
            print('ok')
            for obj in PlaySchedule.Inst:
                if str(obj.Date) == str(current_date):
                    ms = bot.send_poll(Enc,f"Are you guys comming for tomorrow's {obj.Time} game?",["Yes I'm Comming","No I Can't"],is_anonymous=False)
                    bot.pin_chat_message(Enc,ms.id,disable_notification=True,both_sides=True)


# scheduler                                                 
# schedule.every().day.at('04:00',tz=pytz.utc).do(method1)
schedule.every().day.at('14:54',tz=pytz.utc).do(method1)


# pyrotriggers 

@bot.on_message(filters.command('sendpoll'))
def polltry(bot,message):
    ms = bot.send_poll(message.chat.id,"Poll Question",['Choice 1','Choice 2'],is_anonymous=False )
    bot.pin_chat_message(message.chat.id,ms.id,disable_notification=True,both_sides=True)

@bot.on_message(filters.command('ScheduleRun'))
def ScheduleRun(bot,message):
    message.reply("👍")
    while True:
        schedule.run_pending()
    message.reply("👎")

    
print("Bot is working")
bot.run()