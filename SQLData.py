import pymysql.cursors
from discord.ext import commands

class SQLData:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def userdata(self, ctx, *, arg):
        #Connect to Database
        connection = pymysql.connect(host='',
                                     user='',
                                     password='',
                                     db='',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            
            with connection.cursor() as cursor:
                print("Connected!")
                #SQL
                sql = "SELECT * FROM user WHERE nickname LIKE %s"
                
                userinput = arg
             
                #Execute Query
                cursor.execute(sql,userinput)
                print("User Typed: " + userinput)
                print()
                
                for row in cursor:
                    if row['nickname'] != userinput:
                        await self.client.say("Nickname: " + row['nickname'] + "\nUsername: " + row['username'] + "\nJoin Date: " + str(row['joindate']) + "\nRank: " + row['rank'])
                    else:
                        await self.client.say("That name is not in our database")
                    if not row:
                        await self.client.say("That name is not in our database")
        except Exception as e:
            print(e)
        finally:
            #Close the Connection
            connection.close()
            
    @commands.command(pass_context=True)
    async def memberlist(self):
        #Connect to Database
        connection = pymysql.connect(host='',
                                     user='',
                                     password='',
                                     db='',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            
            with connection.cursor() as cursor:
                
                #SQL
                sql = "SELECT * FROM user"
             
                #Execute Query
                cursor.execute(sql)
                
                with open('memberlist.txt', 'w+') as f:
                    for row in cursor:
                        f.write("Nickname: " + row['nickname'] + " Username: " + row['username'] + " Join Date: " + str(row['joindate']) + " Rank: " + row['rank'] + "\n")
                f.close()
                
                await self.client.send_file(self.client.get_channel('499040841881616395'),"memberlist.txt")
                print("Message Sent")
                    
        finally:
            #Close the Connection
            connection.close()
            
    @commands.command(pass_context=True)
    async def updatehighscores(self):
        #Connect to Database
        connection = pymysql.connect(host='',
                                     user='',
                                     password='',
                                     db='',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            
            with connection.cursor() as cursor:
                
                #SQL
                sql = "SELECT * FROM High_Scores"
             
                #Execute Query
                cursor.execute(sql)
                
                for row in cursor:
                    
                    await self.client.send_message(self.client.get_channel('571447326787502080'), row['achievement'] + " - " + row['achievement_num'] + " - " + row['username'])
    
                print("Message Sent")
                    
        finally:
            #Close the Connection
            connection.close()
    
def setup(client):
    client.add_cog(SQLData(client))