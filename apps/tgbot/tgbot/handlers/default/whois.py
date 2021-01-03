from aiogram.types import Message
import whois

whois_help_message = """
❓ Вернёт информацию о домене.

 Использование: `/whois <домен>`
"""

no_domain_text = """
❗Не указан домен или указан неверный/несуществующий домен.

Напишите /whois чтобы посмотреть справку.
"""


def create_whois_message(domain: str) -> str:
    domain_info = whois.whois(domain)
    domain_name = domain_info.get("domain_name")
    if domain_name is None:
        return no_domain_text

    if isinstance(domain_name, list):
        domain_name = domain_name[0]

    message = f"\n📝 Информация о домене {domain_name.lower()}:" \
              f"\n\n👤 Регистратор: {domain_info.get('registrar')}" \

    if creation_date := domain_info.get('creation_date'):
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        message += f"\n📅 Дата создания: {creation_date}"

    if expiration_date := domain_info.get('expiration_date'):
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        message += f"\n📅 Дата окончания:: {expiration_date}\n"

    if address := domain_info.get("address"):
        message += f"\n📖 Адрес: {address}"
    if city := domain_info.get("city"):
        message += f"\n🏘 Город: {city}"
    if country := domain_info.get("country"):
        message += f"\n🏳️ Страна: {country}"
    if name := domain_info.get("name"):
        message += f"\n💬 Имя: {name}"
    if org := domain_info.get("org"):
        message += f"\n💼 Организация: {org}"
    if zipcode := domain_info.get("zipcode"):
        message += f"\n🖥 Zipcode: {zipcode}"
    if emails := domain_info.get("emails"):
        message += "\n✉️ Почта: \n" + str.join("\n", [f" * <code>{email}</code>" for email in emails])

    if name_servers := domain_info.get('name_servers'):
        message += "\n\n📌 NS: \n" + str.join("\n", [f" * <code>{ns}</code>" for ns in
                                                     list(set(map(str.lower, name_servers)))])
    if dnssec := domain_info.get("dnssec"):
        message += f"\n🔐 DNSSec: {dnssec}"
    return message


async def whois_cmd(msg: Message):
    args = msg.text.split(" ")
    if len(args) == 1:
        return await msg.answer(no_domain_text)
    if len(args) >= 2:
        host = args[1]
        await msg.bot.send_chat_action(msg.chat.id, 'typing')
        await msg.answer(create_whois_message(host), parse_mode='html')
