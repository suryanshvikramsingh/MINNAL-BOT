from pyrogram import Client, filters
app = Client('1BJWap1sBu0let_yfAfQYseESxLaUncqOE89aWOpc3IrMXTCD7F83rKi4aYIAGEdTBiqL26GU6Wa1n-kOKEVUGQ8wq8_4R72GV--EuBVlCh0zu7uH1WnR8rtQIy4guH-6Q_dn_gC9OKI2DT78jTWVCArO4pRoYfNO4jk8w1-j3W5pjuQa3nQi3UMERC3vA9_bAQ1sTbs0nSWyCnPnCew3YpFwLeLzLQMhbPcVf_zQbEuUQyKKlgGbie8NE7r8aCJkKrPBqWGIkw0nozT_HIZOrvo75DCfq6sEwZ9Pc3BUrhd-m9vUu1326g3brw9p_aSCoYG1puu98hgReChK9mosgxApOeTluDU')



@Client.on_message(filters.command("tag"))
def tag(client, message):
    try:
        list5 = []
        ted1 = 0
        text = 'Members List :\n'
        num = '⚜'
        if int(message.text.split('g')[1]) > 0:
            ted = int(message.text.split('g')[1])
            
        for member in client.iter_chat_members(message.chat.id):
            list5.append(member.user.id)
            s = member.user.username if member.user.username else member.user.first_name
            text += f'{num}:[{s}](tg://user?id={member.user.id}) \n'

            if len(list5) == 5:
                text += '---------------'
                client.send_message(message.chat.id, text)
                text = ''
                list5 = []
                ted1 += 1
            if ted1 == ted:
                return
    except Exception as r:
        print(r)
