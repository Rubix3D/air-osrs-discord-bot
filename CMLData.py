import urllib.request
from urllib.request import Request
import csv
import itertools
import codecs
from discord.ext import commands

class CMLData:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def comprankings(self, ctx, *, arg):
        channel = ctx.message.channel
        
        url = Request("https://crystalmathlabs.com/tracker/api.php?type=comprankings&competition=" + str(arg), headers={'User-Agent': 'Mozilla/5.0'})

        dd = urllib.request.urlopen(url)
        csv_data = csv.reader(codecs.iterdecode(dd, 'utf-8'), delimiter=",")

        await self.client.say("RSN | START_EXP | CURRENT_EXP | EXP_GAINED")
        for i in range(3):
            await self.client.say(" ".join(next(csv_data)))

        try:
            for row in csv_data:
                if row == "-4":
                    await self.client.say("Server is under heavy load, api temporarily disabled")
                    print("Server is under heavy load, api temporarily disabled")
                elif row == "-1":
                    await self.client.say("User is not in database")
                    print("User is not in database")
                elif row == "-3":
                    await self.client.say("Database Error")
                    print("Database Error")
                elif row == "-2":
                    await self.client.say("Invalid username")
                    print("Invalid username")
        except StopIteration:
            pass
        
def setup(client):
    client.add_cog(CMLData(client))