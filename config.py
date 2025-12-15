# config.py

class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = '22amtics185@gmail.com'     # sender gmail
    MAIL_PASSWORD = 'fewdhodycjigrvli'   # MUST be App Password

    MAIL_DEFAULT_SENDER = '22amtics185@gmail.com'
    RECIPIENT_EMAIL = 'Info@satvarth.com'

    SECRET_KEY = 'any-random-secret-key'
