import discord
import requests
import json
import os
import html
from dotenv import load_dotenv
load_dotenv(".env")

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


client = discord.Client()

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



my_secret = os.environ['TOKEN']
client.run(my_secret)
