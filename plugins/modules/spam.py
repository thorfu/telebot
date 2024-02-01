async def spam(message):
    _, *text_parts = message.text.split()
    try:
        number_of_messages = int(text_parts[0])
        text = ' '.join(text_parts[1:])
    except ValueError:
        number_of_messages = 10
        text = ' '.join(text_parts)
    if text:  # Only send messages if there's text to be spammed
        for _ in range(number_of_messages):
            await message.reply_text(text)