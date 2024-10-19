import config as cfg


def get_telegram_token():
    return cfg.TELEGRAM_TOKEN


def get_aemet_token():
    return cfg.AEMET_TOKEN


def get_city_id(city):
    return cfg.CITY_ID[city]
