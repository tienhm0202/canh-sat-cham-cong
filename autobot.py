# coding=utf-8
from datetime import datetime

from slackclient import SlackClient

import config
from utils import airtable_connector


slack_cli = SlackClient(config.SLACK_BOT_TOKEN)


def get_user(user_id):
    info = slack_cli.api_call("users.info", user=user_id)

    if info["ok"]:
        return info["user"]["profile"]["email"]
    return None


def get_channel(channel_id):
    """
    Ref: https://api.slack.com/methods/conversations.info
    :param channel_id: channel id
    :return: channel readable name
    """
    info = slack_cli.api_call("conversations.info", channel=channel_id)

    if info["ok"]:
        return info["channel"]["name"]
    print(info)
    return None


def morning(user_id, channel_id, ts):
    email = get_user(user_id)
    if not email:
        print("Invalid email! Do nothing")
        return None, None

    to_day = datetime.today().strftime("%-d/%-m/%Y")
    if not airtable_connector.get_user_check_in(email, to_day):
        print("checkin for this user: ", email)
        channel_name = get_channel(channel_id)
        airtable_connector.check_in(email, channel_name)
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name=config.SLACK_REACTION_EMOJI,
                           timestamp=ts)
    else:
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name="+1",
                           timestamp=ts)
    print("added reaction")
    return


def bye(user_id, channel_id, ts):
    print("User send a bye command")
    email = get_user(user_id)
    if not email:
        print(" * Invalid email! Do nothing")
        return None, None

    to_day = datetime.today().strftime("%-d/%-m/%Y")
    checked_in_id = airtable_connector.get_user_bye(email, to_day)
    if checked_in_id:
        print(" * checkout for this user: ", email, "on", to_day)
        airtable_connector.bye(checked_in_id)
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name=config.SLACK_REACTION_EMOJI,
                           timestamp=ts)
    else:
        slack_cli.api_call("reactions.add",
                           channel=channel_id,
                           name="+1",
                           timestamp=ts)
    print(" * added reaction")
    return
