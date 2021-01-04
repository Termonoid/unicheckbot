from aiogram.types import Message
from tgbot.nodes import nodes

start_message = f"""
Привет! Добро пожаловать в @hostinfobot!\n
Данный бот позволяет получить различную информацию о хосте👌\n
Но он не обычный - эту информацию получит он с нескольких нод. На данный их {len(nodes)}!

Вот список команд:
 📌 /ping `<host>` - Произведёт пинг хоста
 📌 /tcp `<host> <port>` - Проверит, открыт ли порт по TCP
 📌 /web `<host>` - Произведёт проверку по протоколу HTTP и вернёт код ответа
 📌 /whois `<host>` - Вернёт информацию whois по домену
 📌 /minecraft `<host> <port>` - Вернёт информацию связанную с Minecraft-сервером
 
 🚩[Репозиторий бота здесь](https://github.com/catspace-dev/hostinfobot).
 🚩[Предложения или замечания можно оставлять здесь](https://github.com/catspace-dev/hostinfobot/issues).
 
 Сделано с ❤️ от @kiriharu :3

"""


async def start_cmd(msg: Message):
    await msg.answer(start_message, parse_mode='markdown')