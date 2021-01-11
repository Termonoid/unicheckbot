from aiogram.types import Message
from tgbot.nodes import nodes
from tgbot.middlewares.throttling import rate_limit

start_message = f"""
Привет! Добро пожаловать в @unicheckbot!\n
Данный бот позволяет получить различную информацию о хосте👌\n
Но он не обычный - эту информацию получит он с нескольких нод. На данный момент их {len(nodes)}!

Вот список команд:
 📌 /ping `<host>` - Произведёт пинг хоста
 📌 /tcp `<host> <port>` - Проверит, открыт ли порт по TCP
 📌 /web `<host>` - Произведёт проверку по протоколу HTTP и вернёт код ответа
 📌 /whois `<host>` - Вернёт информацию whois по домену
 📌 /minecraft `<host> <port>` - Вернёт информацию связанную с Minecraft-сервером
 📌 /ipcalc `<ip>` - Калькулятор подсетей
 
 🚩[Репозиторий бота здесь](https://github.com/catspace-dev/unicheckbot).
 🚩[Предложения или замечания можно оставлять здесь](https://github.com/catspace-dev/unicheckbot/issues).
 
 Сделано с ❤ от @kiriharu :3

"""


@rate_limit
async def start_cmd(msg: Message):
    await msg.answer(start_message, parse_mode='markdown')
