import bot 

@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(m):
    # If bot is not admin, then it will not be able to delete message.
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        if m.new_chat_member.id != bot.get_me().id:
            bot.send_message(m.chat.id,"Please make me an admin to be able to remove the join messeges!")
        else:
            bot.send_message(m.chat.id,"Hiya! I'm your trusty cleaner!")
        
@bot.message_handler(content_types=['left_chat_member'])
def delete_leave_message(m):
    # If bot is the one that is being removed, it will not be able to delete the leave message.
    if m.left_chat_member.id != bot.get_me().id:
        try:
            bot.delete_message(m.chat.id,m.message_id)
        except:
            bot.send_message(m.chat.id,"Please make me an admin to be able to remove leave msgs")

bot.polling()