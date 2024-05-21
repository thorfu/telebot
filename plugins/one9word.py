from pyrogram import Client, filters
import re, logging, random, nltk

logging.basicConfig(level=logging.INFO)

nltk.download('words')

ONE9 = False
starting_letter_pattern = r"start with ([A-Z])"
min_length_pattern = r"include at least (\d+) letters"


@Client.on_message(filters.command("one9", prefixes=".") & filters.me)
async def one9word(client, message):
    global ONE9
    msg = message.text.split(None, 1)
    if len(msg) > 1:
        if msg[1] in ["on", "start", "true"]:
            await message.reply("One9word plugin enabled")
            ONE9 = True
        elif msg[1] in ["off", "stop", "false"]:
            await message.reply("One9word plugin disabled")
            ONE9 = False


@Client.on_message(filters.text)
async def handle_incoming_message(client, message):
    global ONE9
    while True:
        if not ONE9:
            break
        me = client.get_me()
        profile_name = me.first_name if me.last_name is None else f"{me.first_name} {me.last_name}"
        trigger_pattern = f"Turn: {profile_name}."
        puzzle_text = message.text
        if re.search(trigger_pattern, puzzle_text):
            starting_letter_match = re.search(starting_letter_pattern, puzzle_text)
            min_length_match = re.search(min_length_pattern, puzzle_text)

            if starting_letter_match and min_length_match:
                starting_letter = starting_letter_match.group(1)
                min_length = int(min_length_match.group(1))

                english_words = set(nltk.corpus.words.words())

                valid_words = [word for word in english_words if word.startswith(starting_letter) and len(word) >= min_length]

                if valid_words:
                    random_word = random.choice(valid_words)

                    response_message = f"{random_word}"
                    await client.send_message(message.chat.id, response_message)
                else:
                    logging.error("No valid words found for the given criteria.")
            else:
                logging.error("Criteria not found in the puzzle text.")