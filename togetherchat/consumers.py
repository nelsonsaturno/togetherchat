# channel_session_user_from_http, decorator que copia usuario de la sesion http
# from channels.auth import channel_session_user_from_http


# @channel_session_user_from_http
# def connect_handler(message):
#     message.reply_channel.send({'accept': True})


def message_handler(message):
    test = {'text': 'test'}

    # Responder al cliente
    message.reply_channel.send(test)


# def disconnect_handler(message):
