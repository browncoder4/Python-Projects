from instabot import Bot
bot=Bot()
bot.login(username="harry.hi",password="blah123")  
bot.follow('ronaldo')
bot.upload_photo("C:\Users\project\___.jpg",caption="i love python")
bot.unfollow("ronaldo")
bot.send_message("fuck trump",["isreal_official","official_india"])
followers=bot.get_user_followers("ronaldo")
for follower in followers:
    print(bot.get_user_info(follower))
