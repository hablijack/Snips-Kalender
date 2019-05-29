#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import random


class Tankerkoenig:

    def __init__(self, config):
        self.weather_api_base_url = "https://creativecommons.tankerkoenig.de/json/list.php"
        try:
            self.tankerkoenig_api_key = config['secret']['tankerkoenig_api_key']
        except KeyError:
            self.tankerkoenig_api_key = "XXXXXXXXXXXXXXXXXXXXX"
        try:
            self.latitude = config['general']['lat']
        except KeyError:
            self.latitude = "49.982334"
        try:
            self.longitude = config['general']['long']
        except KeyError:
            self.longitude = "12.0602148"

    def diesel_price(self, intent_message):
        fuel_prices = self.get_fuelprices(intent_message)
        if fuel_prices['status'] == 'ok':
            cheapest = {"diesel": 100.0}
            for station in fuel_prices['stations']:
                if station['diesel'] <= cheapest['diesel']:
                    cheapest = station
            response = "Der günstigste Diesel kostet gerade: {0}€, bei der Tankstelle {1}.".format(
                format(cheapest["diesel"], '.2f').replace('.', ','),
                cheapest["name"]
            )
            return response
        else:
            return random.choice(["Es ist leider kein Internet verfügbar.", "Ich bin nicht mit dem Internet verbunden.", "Es ist kein Internet vorhanden."])

    def benzin_price(self, intent_message):
        fuel_prices = self.get_fuelprices(intent_message)
        if fuel_prices['status'] == 'ok':
            cheapest = {"e5": 100.0}
            for station in fuel_prices['stations']:
                if station['e5'] < cheapest['e5']:
                    cheapest = station
            response = "Der günstigste Super kostet gerade: {0}€, bei der Tankstelle {1}.".format(
                format(cheapest["e5"], '.2f').replace('.', ','),
                cheapest["name"]
            )
            return response
        else:
            return random.choice(["Es ist leider kein Internet verfügbar.", "Ich bin nicht mit dem Internet verbunden.", "Es ist kein Internet vorhanden."])

    def get_fuelprices(self, intent_message):
        tankerkoenig_url = forecast_url = "{0}/json/list.php?lat={1}&lng={2}&rad={3}&sort={4}&type={5}&apikey={6}".format(
	       self.weather_api_base_url,
            self.latitude,
            self.longitude,
            5,
            "dist",
            "all",
            self.tankerkoenig_api_key
        )
        try:
            r = requests.get(tankerkoenig_url)
            json_obj = json.loads(r.content.decode('utf-8'))
            return json_obj
        except (requests.exceptions.ConnectionError, ValueError):
            return {"status": "error"}
