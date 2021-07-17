import discord
from discord import message
import requests
import json
import os
import html
from discord.utils import get
from discord.ext import commands
# from dotenv import load_dotenv
# load_dotenv(".env")

intents = discord.Intents.default()
intents.members = True

qn = ["No questions asked", "No questions asked"]

def get_question():
  qn1= requests.get("https://opentdb.com/api.php?amount=1")
  json_data= json.loads(qn1.text)
  question= "Here's a question '" + json_data['results'][0]['question'] + "'"
  answer= json_data['results'][0]['correct_answer']
  return [html.unescape(question), html.unescape(answer)]

def get_useless_fact():
  qn1= requests.get("https://useless-facts.sameerkumar.website/api")
  json_data= json.loads(qn1.text)
  question= "Here's a useless fact: '" + json_data['data']+ "'"
  return html.unescape(question)



def get_cat_fact():
  qn1= requests.get("https://catfact.ninja/fact?max_length=14000")
  json_data= json.loads(qn1.text)
  question= "Here's a cat fact: '" + json_data['fact']+ "'"
  return html.unescape(question)


client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global qn
  if message.author == client.user:
    return

  if message.content.startswith('$question'):
    qn= get_question()
    await message.channel.send(qn[0])
  
  if message.content.startswith('$answer'):
    await message.channel.send(qn[1])

  if message.content.startswith('$about'):
    text = "My name is Quizzo!\n I am the official bot for Les Quizerables i.e. the Quizzing Society of Kalyani Government Engineering college."
    await message.channel.send(text)

  if message.content.startswith('$uselessFact'):
    text = get_useless_fact()
    await message.channel.send(text)      
  
  if message.content.startswith('$catFact'):
    text = get_cat_fact()
    await message.channel.send(text)   


  #check DM channel

  if isinstance(message.channel, discord.DMChannel)and client.user is not message.author:

    
    if(message.content.lower()=='yes' or message.content.lower()=='y'):
      guild= client.get_guild(862347310121877558)
      for m in guild.members:
        if(m == message.author):
          role = get(m.guild.roles, id=862350627739664425)
          await m.add_roles(role)
        
        


    elif(message.content.lower()=='no' or message.content.lower()=='n'):
      guild= client.get_guild(862347310121877558)
      for m in guild.members:
        if(m == message.author):
          role = get(m.guild.roles, id=862350532537352242)
          await m.add_roles(role)





    elif (all(x.isalpha or x == " " for x in  message.content) and (message.content.lower()!='no' or message.content.lower()!='n' or message.content.lower()!='yes' or message.content.lower()!='y')):
      guild= client.get_guild(862347310121877558)
      for m in guild.members:
        if(m == message.author):
          await m.edit(nick=message.content)
          await m.send(qns[1])

    else:
      message.author.send("Looking into it")  






@client.event
async def on_member_join(member):
  global name, college, current, qns
  role = get(m.guild.roles, id=865927707027832884)
  await m.add_roles(role)
  qns=  ["Please provide your name", "Are you a current member of Les Quizerables, KGEC?"]
  await member.send(qns[0])
  
    



my_secret = "ODYyNTkyOTUyOTQ1OTk5OTIy.YOamSg.hVgrjsWHqbioDW4Y2SdrfhDXQjk"
print(my_secret)
client.run(my_secret)
