import discord

BATTERYFILENAME = "data/frift/batterytable.jpg"

def batterytable(message):
    file = discord.File(BATTERYFILENAME,filename=BATTERYFILENAME)
    msg = "> source: `https://mhwiki.hitgrab.com/wiki/index.php/Furoma_Rift#Batteries`"
    
    return message.channel.send(msg, file=file)