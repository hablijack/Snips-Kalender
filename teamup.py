#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import json
import dateparser
import re
import sys


class Teamup:

    def __init__(self, config):
        try:
            self.teamup_url = config['general']['teamup_url']
        except KeyError:
            self.teamup_url = "XXXXXXXXXXXXXXXXXXXXX"
        try:
            self.teamup_token = config['secret']['teamup_token']
        except KeyError:
            self.teamup_token = "XXXXXXXXX"
        try:
            self.teamup_calendar_id = config['secret']['teamup_calendar_id']
        except KeyError:
            self.teamup_calendar_id = "XXXXXXXXXXX"

    def today_info(self, intent_message):
        TEAMUP_USER = [
            {"name": "Christoph", "calendar_id": "4377398"},
            {"name": "Barbara", "calendar_id": "4377397"},
            {"name": "Family", "calendar_id": "4377538"},
            {"name": "Feiertage", "calendar_id": "4377396"},
            {"name": "Geburtstage", "calendar_id": "4377496"}
        ]
        start_date = str(datetime.date.today())
        end_date = str(datetime.date.today())
        url = self.teamup_url + self.teamup_token + "/events" + "?startDate=" + start_date + "&endDate=" + end_date
        headers = {'Teamup-Token': self.teamup_token}
        req = requests.get(url, headers=headers)
        calendar = json.loads(req.text)
        print(req.text)
        return "Jaja das ist ein Kalender"
