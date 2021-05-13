# coding=utf-8
import os


# Slack
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "xoxb-461422697699-1023036851697-9Yh3xUrnolqBXN9djZ21vI8F")
SLACK_DEFAULT_CHANNEL = os.environ.get("SLACK_DEFAULT_CHANNEL", "#test_bot")
SLACK_PATTERN = {
    "daily": ["[daily]"],
    "morning": ["good", "morning"],
    "chao_buoi_sang": ["chao", "buoi", "sang"],
    "bye": ["bye"],
    "Bye": ["Bye"]
}
SLACK_REACTION_EMOJI = os.environ.get("SLACK_REACTION_EMOJI", "+1")

# AirTable
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN", "keyWk5bt8Enu6ZPA0")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE", "appp7hAGJr6m0rFqo")
AIRTABLE_TABLE_CHECKIN = os.environ.get("AIRTABLE_TABLE_CHECKIN", "Checkin")
AIRTABLE_TABLE_ABSENT = os.environ.get("AIRTABLE_TABLE_ABSENT", "Absent")
