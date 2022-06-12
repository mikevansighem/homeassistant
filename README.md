# Mike's Home Assistant Configuration

[![Last commit](https://img.shields.io/github/last-commit/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/commits/master)
[![Commits per month](https://img.shields.io/github/commit-activity/m/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/commits/master)
[![License](https://img.shields.io/github/license/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/blob/master/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mikevansighem/homeassistant/Home%20Assistant%20CI?style=flat-square)](https://github.com/mikevansighem/homeassistant/actions)
[![GitHub issues](https://img.shields.io/github/issues-raw/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/issues)

## :page_facing_up: About

This is my personal Home Assistant configuration.

![Home Dashboard](DOCS/images/dashboard-home.png)

## :computer: Hardware

A list of most hardware used can be found [here](DOCS/hardware.md).

## :house_with_garden: Automation based on "House state"

The house state is a template sensor used to schedule most automations. 
It takes into account precense, time of day and work schedule. 
I use this method to simplify the logic within all of my automations. Below table shows
devices using the house state sensor.

| House state        | Home         | Away       | Night           | Holiday    |
|--------------------|--------------|------------|-----------------|------------|
| Alarm              | Disarmed (1) | Armed away | Armed night (2) | Armed away |
| Central heating    | On (3,7)     | Off        | Off (4)         | Off        |
| Floor heating pump | On (3)       | Off        | Off (4)         | Off        |
| Hot water          | On (3)       | Off        | Off (4)         | Off        |
| Holiday lights     | Off          | Off        | Off             | On         |
| Ventilation fan    | On           | On         | On (5)          | Off        |
| Grow light         | Off          | On (6)     | Off             | On (6)     |
| Notifications      | On           | Off        | Off             | Off        |

Footnotes:

1. When going from night to home the alarm is disarmed early to prevent accidental triggers.
2. When going from home to night the alarm arming is delayed to prevent accidental triggers.
3. Switched on early using helper to pre-heat the home.
4. Switched off early using helper to preserve energy.
5. Speed limited to low.
6. If sun is above the horizon. This to give the plants a rest during the night.
7. Turned off if doors are left open to prevent unnecessary heating.

## :bell: Alarm

For the alarm the [manual alarm panel integration](https://www.home-assistant.io/integrations/manual/). Arming and disarming is done based on the house state. Additionally a Frient Zigbee Alarm panel is used as a backup in case your phone is dead.

## :thermometer: Climate

### Heating

The boiler is controlled by a Weemos D1 Mini with a [DIYLESS Thermostat shield](https://diyless.com/product/esp8266-thermostat-shield) to communicate using the Opentherm protocol.
This allows for modulation of the burner. The shield has a build in temperature sensor, however this is not used. Instead an average of various downstairs sensors is taken and send to the thermostat to be used as the current temperature.

### Floor heating pump

Using a simple Zigbee plug the floor heating pump is turned off whenever the central heating is off. If the pump has been of for 12 hours, it will run for several minutes to prevent it from getting stuck.

### Hot water

The same boiler that serves the central heating systems is used for hot water. This is controlled in a similar manner as the boiler using the Weemos D1 Mini.

## :sunflower: Plants

### Sprinklers

My sprinkler systems is controlled by Home Assistant trough a Raspberry Pi running OpenSprinkler. Full hardware list can be found [here](https://github.com/mikevansighem/homeassistant/blob/master/DOCS/hardware.md#sprinkler). Originally I used OpenSprinkler its built in watering prediction. However I found it always was a bit off, especially in spring and autumn. I switched to calculating the watering amount based on Buienradar weather data, specifically ground temperature, humidity and rain in the last 24 hours.

### Indoor grow light

Some of my indoor plants are in rather dark corners. To ensure they get enough light I use purple grow lights. Since they are in the living room and you don't want them on when you home theay are switched on and off based on the house state. Since the lights itself are not smart I control them with a Hue plug.

## :star: Custom extras

A full list of all custom add-ons, integrations and cards can be found [here](DOCS/custom_extras.md).

## :bookmark_tabs: License

Copyright (c) 2021 Mike van Sighem. Licensed under the [MIT license](/LICENSE?raw=true).
