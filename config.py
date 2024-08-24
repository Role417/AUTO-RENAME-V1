import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "12618934")
    API_HASH  = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Leachv3")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Leachv3:Leachv3@cluster0.rasbnes.mongodb.net/")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/2a18be2ff945f5feef130.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1297128957').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002116152617"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.
    
<b>Bot Is Made By @OTT_ARAKAL_THERAVAD_MOVIESS</b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Madflix_Bots </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 𝑴𝒚 𝑵𝒂𝒎𝒆 : <a href=https://t.me/{}>{}</a>
                                                        
📝 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : <a href='https://t.me/+Ou3rqTttBbJmOTA1'>𝑷𝒚𝒕𝒉𝒐𝒏</a>
                                                         
📚 𝑭𝒓𝒂𝒎𝒆𝒘𝒐𝒓𝒌 : <a href='https://t.me/+UtYVAU57YVIxNThl'>𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎</a>

📡 𝑯𝒐𝒔𝒕𝒆𝒅 𝑶𝒏 : <a href='https://t.me/+1YiWOavPrhc0NmI1'>𝑯𝒆𝒓𝒌𝒖𝒐</a>

👨‍💻 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 : <a href='https://t.me/ARAKAL_THERAVAD_MOVIES_02_bot'>𝑵𝒂𝒛𝒓𝒊𝒚𝒂</a>

👥 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 : <a href='https://t.me/+FAa3tYIjXYcyZDY1'>𝑨𝑻𝑴</a>

📢 𝑼𝒑𝒅𝒂𝒕𝒆 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href='https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS'>𝑨𝑻𝑴 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍</a></b>"""
        
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>8921579529@naviaxis</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""




