import aiohttp
import asyncio
from pyrogram import Client, filters

async def urban(message):
    word = message.text.split(maxsplit=1)[1]
    m = await message.edit(f"**Searching for** `{word}`")
    try:
        response =  await get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = f"**Text: {replacetext(word)}**\n**Meaning:**\n`{replacetext(definition)}`\n\n**Example:**\n`{replacetext(example)}`"
        await m.edit(result)
    except IndexError:
        await m.edit(
            text="`Sorry pal, we couldn't find meaning for the word you were looking for.`",
        )
    except Exception as e:
        await m.edit(text="`The Urban Dictionary API could not be reached`")


async def meaning(message):
    word = message.text.split(maxsplit=1)[1]
    m = await message.edit(f"**Searching for** `{word}`")
    await asyncio.sleep(2)
    try:
        ft = f"<b>Search Query: </b><code>{word.title()}</code>\n\n"
        response = await get_json(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
        )
        if "message" not in response:
            result = response[0]
            if "phonetic" in result:
                if phonetic := result["phonetic"]:
                    ft += f"<b>Phonetic: </b>\n<code>{phonetic}</code>\n\n"
            meanings = result["meanings"]
            synonyms = []
            antonyms = []
            for content in meanings:
                ft += f"<u><b>Meaning ({content['partOfSpeech']}):</b></u>\n"
                for count, text in enumerate(content["definitions"], 1):
                    ft += f"<b>{count}.</b> {text['definition']}\n"
                if content["synonyms"]:
                    synonyms.extend(content["synonyms"])
                if content["antonyms"]:
                    antonyms.extend(content["antonyms"])
                ft += "\n"
            if synonyms:
                ft += f"<b>Synonyms: </b><code>{', '.join(synonyms)}</code>\n"
            if antonyms:
                ft += f"<b>Antonyms: </b><code>{', '.join(antonyms)}</code>\n"
        else:
            ft += "`Sorry pal, we couldn't find Meaning for the word you were looking for.`"
        await m.edit(ft, parse_mode="html")
    except Exception as e:
        await m.edit(text="`The Dictionary API could not be reached`")


def replacetext(text):
    return (
        text.replace(
            '"',
            "",
        )
        .replace(
            "\\r",
            "",
        )
        .replace(
            "\\n",
            "",
        )
        .replace(
            "\\",
            "",
        )
    )

async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


