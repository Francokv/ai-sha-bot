from decouple import config

OPENAI_API_KEY  = config("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = config("DISCORD_BOT_TOKEN")

BASE_CHAT_PROMPT =""""
Eres bot de discord. Puedes hablar con los usuarios y responder a sus preguntas.
Usuario: {}
Bot: """
