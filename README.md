# Mike's Home Assistant Configuration

[![Last commit](https://img.shields.io/github/last-commit/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/commits/master)
[![Commits per month](https://img.shields.io/github/commit-activity/m/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/commits/master)
[![License](https://img.shields.io/github/license/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/blob/master/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mikevansighem/homeassistant/Home%20Assistant%20CI?style=flat-square)](https://github.com/mikevansighem/homeassistant/actions)
[![GitHub issues](https://img.shields.io/github/issues-raw/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/issues)

## :page_facing_up: About

This is my personal Home Assistant configuration.

## :house_with_garden: House state

The house state is used to schedule automations. Below table shows devices used 
by the house state.

| House state        | Home         | Away       | Night           | Holiday    |
|--------------------|--------------|------------|-----------------|------------|
| Alarm              | Disarmed (1) | Armed away | Armed night (2) | Armed away |
| Central heating    | On (3)       | Off        | Off (4)         | Off        |
| Floor heating pump | On (3)       | Off        | Off (4)         | Off        |
| Hot water          | On (3)       | Off        | Off (4)         | Off        |
| Holiday lights     | Off          | Off        | Off             | On         |
| ventilation        | On           | On         | On (5)          | Off        |

Footnotes:

1. When going from night to home the alarm is disarmed early to prevent accidental triggers.
2. When going from home to night the alarm arming is delayed to prevent accidental triggers.
3. Switched on early using helper to pre-heat the home.
4. Switched off early using helper to preserve energy.
5. Speed limited to low.

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

## :bookmark_tabs: License

Copyright (c) 2021 Mike van Sighem. Licensed under the [MIT license](/LICENSE?raw=true).
