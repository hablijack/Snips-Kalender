#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import json
import re
import sys


class Teamup:

    def __init__(self, config):
        self.teamup_url = "https://teamup.com/"
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
        url = self.teamup_url + self.teamup_calendar_id + "/" + "events?startDate=" + start_date + "&endDate=" + end_date
        headers = {'Teamup-Token': self.teamup_token}
        req = requests.get(url, headers=headers)
        calendar = json.loads(req.text)
        agenda = "Du hast heute: "
        for event in calendar['events']:
            time_string = event["start_dt"]
            event_time = datetime.datetime.strptime(time_string[:len(time_string)-3] + time_string[len(time_string)-2:], '%Y-%m-%dT%H:%M:%S%z')
            agenda += "um " + "{0:%H:%M}".format(event_time) + "Uhr " + event['title'] + ". "
        return agenda
