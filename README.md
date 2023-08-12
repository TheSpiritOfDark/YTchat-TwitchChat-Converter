# YTchat-TwitchChat-Converter
A simple python script that reads a YT chat and sends the messages to a twitch stream, made by me (TheSpiritOfDark, WafflingTitan31, ect, etc)

# how to get your API keys and put it in the script

Youtube: 

Follow https://blog.hubspot.com/website/how-to-get-youtube-api-key to get your API key on youtube, one you have your API key, put it on line 12, (eg: api_key = 'yourapikeyhere' #Youtube api key)

Do NOT share this API key with anybody, if you recognise your API key or twitch OAUTH token in any error messages, remove them before posting any issue about it

Twitch:

Create a Twitch account if you havent already, put your twitch username on line 38 (eg: nick = "Yourtwitchusername" #your twitch username)

Use https://twitchapps.com/tmi/ to generate your OAUTH token for twitch, put your OAUTH token in line 39 (eg: token = "oauth:abc123")
Do NOT share this token key with anybody, if you recognise your API key or twitch OAUTH token in any error messages, remove them before posting any issue about it

finally, put the username of the streamer that you want to send the messages in line 46 (eg: channel = "#streamername" #the name of the streamer whos chat you wish to send to, preceded by a #) be sure to put a # before the name of the streamer

also install the dependecys, google the error and it will tell you to do "pip install pakageabc" or something


# which script to use?

api (copy).py has a filter to only send messages that start with "!", this helps limit your usage of the twitch api when using this for twitch commands only, you can go to line 87 and change the letter(s) that the messages will have to start with to be sent to twitch.

api (another copy).py doesnt have the filter on it
