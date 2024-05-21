from pyrogram import Client, filters
import re, logging, random, nltk
from info import TG_NAME

logging.basicConfig(level=logging.INFO)

nltk.download('words')
english_words = set(nltk.corpus.words.words())

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
    if ONE9:
        trigger_pattern = f"Turn: {TG_NAME}"
        puzzle_text = message.text

        if re.search(trigger_pattern, puzzle_text):
            starting_letter_match = re.search(starting_letter_pattern, puzzle_text)
            min_length_match = re.search(min_length_pattern, puzzle_text)

            if starting_letter_match and min_length_match:
                starting_letter = starting_letter_match.group(1)
                min_length = int(min_length_match.group(1))

                valid_words = (word for word in english_words if word.startswith(starting_letter) and len(word) >= min_length)

                try:
                    random_word = next(valid_words)
                    response_message = f"{random_word}"
                    await client.send_message(message.chat.id, response_message)
                except StopIteration:
                    await message.reply("No valid words found for the given criteria.")
            else:
                await message.reply("Criteria not found in the puzzle text.")