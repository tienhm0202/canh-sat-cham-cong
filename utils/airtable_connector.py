# coding=utf-8
from datetime import datetime

import config
import pytz
from airtable import Airtable


def get_air_table_instance(table_name):
    return Airtable(config.AIRTABLE_BASE,
                    table_name,
                    api_key=config.AIRTABLE_TOKEN)


def get_user_check_in(user_email, date):
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    is_checked = air_table.get_all(
        view="Raw",
        formula="AND({Email}=\"%s\",{Date}=\"%s\")" % (user_email, date))
    return len(is_checked)


def check_in(user_email, channel):
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    air_table.insert({"Email": user_email, "Team": channel})
    return True


def get_user_bye(user_email, date):
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    checked_data = air_table.get_all(
        view="Raw",
        formula="AND({Email}=\"%s\",{Date}=\"%s\")" % (user_email, date))
    try:
        return checked_data[0]["id"]
    except Exception:
        return None


def bye(checked_id):
    date = datetime.utcnow().isoformat()
    air_table = get_air_table_instance(config.AIRTABLE_TABLE_CHECKIN)
    air_table.update(checked_id, {"Checkout Hour": date + "Z"})
    return True
