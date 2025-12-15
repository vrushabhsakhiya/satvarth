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
import os

class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret')
