# -*- coding: utf-8 -*-

import random
import time
import discord
import pymysql.cursors
import datetime
from discord.ext import commands
from test.test_nntplib import bypass_context

TOKEN = ''

extensions = ['PullReddit','Fun','SQLData','Dicing','CMLData']
client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=".help for commands",type=1))
    print('Logged in as')
    print(client.user.name)
    print("User ID: " + client.user.id)
    for server in client.servers:
        print("Connected to server: {}".format(server))
    print('------')
    
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        print(error)
        
@client.command(pass_context=True)
async def clearhighscores(ctx, number):
    msgs = []
    number = int(number)
    channel = client.get_channel('571447326787502080')
    async for x in client.logs_from(channel, limit = number):
        msgs.append(x)
    await client.delete_messages(msgs)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed1 = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed2 = discord.Embed(
        colour = discord.Colour.orange()
    )
    
    embed.set_author(name='"Fun" Commands')
    embed.add_field(name='.ags', value='Returns ags spec', inline=False)
    embed.add_field(name='.barrows', value='Shows # of chests until you get an item', inline=False)
    embed.add_field(name='.dclaws', value='Returns Dragon Claw spec', inline=False)
    embed.add_field(name='.dds', value='Returns Dragon Dagger spec', inline=False)
    embed.add_field(name='.didpopgetmoleyet', value='Returns sadness', inline=False)
    embed.add_field(name='.flip', value='Returns a coin flip', inline=False)
    embed.add_field(name='.gmaul', value='Returns Gmaul spec', inline=False)
    embed.add_field(name='.pet [name]', value='Returns # of kills until you got a pet', inline=False)
    embed.add_field(name='.ping', value='Returns pong', inline=False)
    embed.add_field(name='.rangerboots', value='Returns # of Med Clues until Ranger Boots', inline=False)
    embed.add_field(name='.whichskillnext', value='Returns a random OSRS skill', inline=False)
    embed.add_field(name='.poordice', value='Rolls 1-6, if you get higher than Cubert you win 1gp', inline=False)
    embed.add_field(name='.lowdice', value='Rolls 1-6, if you get higher than Cubert you win 10gp', inline=False)
    embed.add_field(name='.dice', value='Rolls 1-6, if you get higher than Cubert you win 100gp', inline=False)
    embed.add_field(name='.highdice', value='Rolls 1-6, if you get higher than Cubert you win 1000gp', inline=False)
    
    embed1.set_author(name='Reddit Commands')
    embed1.add_field(name='.dadjoke', value='Returns dad joke', inline=False)
    embed1.add_field(name='.random60', value='Ask an Admin to join the NSFW CHANNEL', inline=False)
    embed1.add_field(name='.randomles', value='Ask an Admin to join the NSFW CHANNEL', inline=False)
    embed1.add_field(name='.randomporngif', value='Ask an Admin to join the NSFW CHANNEL', inline=False)
    embed1.add_field(name='.randomdankmeme', value='Returns "Dank Meme"', inline=False)
    embed1.add_field(name='.randommeme', value='Returns meme', inline=False)
    embed1.add_field(name='.randomhentai', value='Ask an Admin to join the NSFW CHANNEL', inline=False)
    
    embed2.set_author(name='Admin Commands')
    embed2.add_field(name='.msgall [message]', value='Sends message to everyone in the server', inline=False)
    embed2.add_field(name='.pickrandomsotw', value='Returns four random skills for SOTW', inline=False)
    embed2.add_field(name='.rankup', value='Prints the names of members who need a rankup', inline=False)
    embed2.add_field(name='.memberlist', value='Returns txt file of all current members', inline=False)
    embed2.add_field(name='.userdata ["member name"]', value='Returns all current data of a specific server member', inline=False)
    embed2.add_field(name='.updatehighscores', value='Returns high scores in the #high-scores channel', inline=False)
    embed2.add_field(name='.clearhighscores [number]', value='Clears the high scores in the #high-scores channel', inline=False)
    
    
    await client.send_message(author, embed=embed)
    await client.send_message(author, embed=embed1)
    await client.send_message(author, embed=embed2)
    await client.say("Just sent you a PM with a command list!")
    

@client.command(pass_context=True)
async def msgall(ctx,*,message):
    if ctx.message.author.server_permissions.administrator:
        for server in client.servers:
            for member in server.members:
                try:
                    await client.send_message(member, message)
                    print("Message Sent to " + str(member))
                except Exception:
                    pass
    else:
        await client.say("You do not have permission to run that command")
        
@client.command()
async def pickrandomsotw():
    skills = ['<:attack:498673023629393925>', '<:strength:498673024115933184>', '<:defence:498673023986171904>', '<:runecrafting:498673024032047106>', '<:hitpoints:498673024086835240>', '<:agility:500117467713241114>', '<:thieving:500117467981414410>', '<:crafting:498673023868600320>', '<:slayer:500117467788738582>', '<:hunter:500117467654389784>', '<:mining:498673023860080652>', '<:smithing:498673024317390849>', '<:fishing:498673024019595274>', '<:osrscooking:500117467545206785>', '<:firemaking:498673023768068107>', '<:woodcutting:498673024296288256>', '<:farming:500117467830681623>']        
    randChoice = random.sample(skills,4)
    await client.say("The Four Choices for SOTW this week are: " + " ".join(randChoice))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Welcome')
    await client.add_roles(member, role)
    await client.send_message(member, "Welcome to Air OSRS!\n\n\nYou have been automatically placed in the 'WELCOME' Role.\n\nTo be able to interact with the rest of the server, please fill out an application form, and a staff member will review it ASAP!\n\nIn the mean time, join us in game in the 'Air OSRS' cc and say hi!")   

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('ironman'):
        await client.send_message(message.channel, "BTW")
        
    if message.content.startswith('Cubert'):
        await client.send_message(message.channel, "What do you want from me, peasant?")
    if message.content.startswith('cubert'):
        await client.send_message(message.channel, "What do you want from me, peasant?")
    if message.content.startswith('CUBERT'):
        await client.send_message(message.channel, "WHAT DO YOU WANT FROM ME PEASANT?")
        
    await client.process_commands(message)
    
@client.command(pass_context=True)
async def rankup(ctx):
    if ctx.message.author.server_permissions.administrator:
        print("Started RankUp")
        connection = pymysql.connect(host='',
                                            user='',
                                            password='',
                                            db='',
                                            charset='',
                                            cursorclass=pymysql.cursors.DictCursor)
            
        def get_days_passed(before, after):
            a = datetime.datetime.strptime(after, '%Y-%m-%d')
            date1 = before.date()
            date2 = a.date()
            return abs(date1 - date2).days
        
                
        try:
            print("Connected to SQL Server")        
            with connection.cursor() as cursor:
                        
                #SQL
                sql = "SELECT * FROM user"
                     
                #Execute Query
                cursor.execute(sql)
                        
                for row in cursor:
                    memberNick = row['nickname']
                    memberName = row['username']
                    memberRank = row['rank']
                    memberJoined = row['joindate']
                    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
                    
                    if get_days_passed(memberJoined, currentDate) >= 30 and memberRank == "Trial":
                        await client.say(memberNick + " ranked up from Trial to Recruit")
                                    
                    if get_days_passed(memberJoined, currentDate) >= 90 and memberRank == "Recruit":
                        await client.say(memberNick + " ranked up from Recruit to Corporal")
                                        
                    if get_days_passed(memberJoined, currentDate) >= 182 and memberRank == "Corporal":
                        await client.say(memberNick + " ranked up from Corporal to Sergeant")
                                    
                    if get_days_passed(memberJoined, currentDate) >= 365 and memberRank == "Sergeant":
                        await client.say(memberNick + " ranked up from Sergeant to Lieutenant")
                        
        except Exception as e:
            print(e)                  
        finally:
            connection.close()
    else:
        client.say("You do not have permission to run that command")
    
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    
    while True:
        try:
            client.loop.run_until_complete(client.start(TOKEN))
        except BaseException:
            time.sleep(5)
            