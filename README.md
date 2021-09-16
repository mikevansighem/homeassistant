# Mike's Home Assistant Configuration

[![License](https://img.shields.io/github/license/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant/blob/master/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant)
[![Commits per month](https://img.shields.io/github/commit-activity/m/mikevansighem/homeassistant?style=flat-square)](https://github.com/mikevansighem/homeassistant)

## About

This is my personal Home Assistant configuration.

## House state

The house state is used to schedule automations. Below table shows devices used by the house state.

| House state        | Home     | Away       | Night       | Holiday    |
|--------------------|----------|------------|-------------|------------|
| Alarm              | Disarmed | Armed away | Armed night | Armed away |
| Central heating    | On       | Off        | Off         | Off        |
| Floor heating pump | On       | Off        | Off         | Off        |
| Hot water          | On       | Off        | Off         | Off        |
| Holiday lights     | Off      | Off        | Off         | On         |
