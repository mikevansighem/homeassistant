# Hardware

Below most of the hardware used in my smart home.

- To run Home Assistant a [Rasperry Pi 4 Model B 4GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/).
- Another [Rasperry Pi 4 Model B 2GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) for [PiHole](https://pi-hole.net/).

## Lights

- Lots of [Philips Hue](https://www.philips-hue.com/) light bulbs.
- Several [Innr](https://www.innr.com/nl/) light bulbs for in the hallways.
- Two [Ecodim turn dimmers](https://www.ecodim.nl/eco-dim07-zigbee-basic.html).
- A few [Zigbee Dimmers](https://www.robbshop.nl/robb-smarrt-zigbee-dimmer-400w?gclid=Cj0KCQiAu62QBhC7ARIsALXijXSm26du28rkAhJq5KfSUFwbzd4OrK-DDNy0gYTQ58hhwrf-2zIkSiIaAt2EEALw_wcB) for all light fixtures where smart bulbs are not a option.
- Several [Philips Hue Plugs](https://www.philips-hue.com/nl-nl/p/hue-smart-plug/8719514342309) mostly for Christmas decorations.

## Controls

- [Senic Gira friend of Hue smart switches](https://www.senic.com/products/friends-of-hue-smart-switch) for all light switches.
- A [Frient Zigbee keypad](https://www.robbshop.nl/frient-slimme-keypad) as a backup to switch off the alarm.

## Sensors

- [Hue motion sensors](https://www.philips-hue.com/nl-nl/p/hue-hue-motion-sensor/8718696743171).
- [Tuya Zigbee air quality sensor](https://www.amazon.nl/dp/B093Z3CNDL/ref=pe_28126711_487102941_TE_SCE_3p_dp_1).

## Audio

- Throughout the house [Nest Home Minis](https://store.google.com/nl/product/google_nest_mini?hl=nl).
- A single [Google Chromecast Audio](https://allaboutchromecast.com/chromecast-audio-guides/)

## Ventilation

My whlation fan is controlled by a [Weemos D1 mini Pro](https://www.reichelt.nl/nl/nl/d1-mini-pro-esp8266-cp2104-set-met-antenne-d1-mini-pro-ant-pole home venti266067.html?PROVID=2809&gclid=Cj0KCQiAu62QBhC7ARIsALXijXQn38Q0QUMiXuzFMO3BO-2k9uRrYD0neozTwTfkxbrbTWj1Ko_sDvkaAhOcEALw_wcB) running ESPHome. The AC fan has a power and a speed lead. By switching the speed connection the speed can be changed from medium to high. To handle the power required a [2 channel solid state relay board](https://www.kiwi-electronics.nl/nl/2-kanaals-solid-state-relais-module-3590?language=nl-nl&currency=EUR&gclid=Cj0KCQiAu62QBhC7ARIsALXijXQdtHvYIT8GQoag8DIRF1jLQdCzRRlR2_2QVZZVt1MnALTHdgkp2toaArXbEALw_wcB) is used. Previously I used regular relays but they were having "sticking" issues due to the ramp-up current spike produced by the fan.

![Fan-Controller-Layout](DOCS/images/hardware-fan-controller.png)

Checkout the [ESPHome code](esphome/fan-controller.yaml) and [Fritzing file](DOCS/layouts/fan-controller.fzz).

## Boiler

The Boiler is controlled by a [Weemos D1 mini Pro](https://www.reichelt.nl/nl/nl/d1-mini-pro-esp8266-cp2104-set-met-antenne-d1-mini-pro-ant-p266067.html?PROVID=2809&gclid=Cj0KCQiAu62QBhC7ARIsALXijXQn38Q0QUMiXuzFMO3BO-2k9uRrYD0neozTwTfkxbrbTWj1Ko_sDvkaAhOcEALw_wcB) with a [DIYLESS Thermostat shield](https://diyless.com/product/esp8266-thermostat-shield) to communicate using the Opentherm protocol.

## Sprinkler

For my sprinklers I run [OpenSprinkler](https://opensprinkler.com/) on a [Rasperry Pi 3 Model B 1GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/). To make it work:
- For power to the Raspberry Pi a 220v AC to 5v DC converter.
- 220v AC to 24v AC bell transformer to power the valves.
- A Generic watertight housing.
- Dual relay hat for the RaspberryPi.

## Other
 - [SlimmeLezer](https://www.zuidwijk.com/product/slimmelezer-plus/) for monitoring energy and gas usage.
 - [ESPHome Doorbell](https://www.zuidwijk.com/product/esphome-based-doorbell-v2/).
 - [AVM FRITZ!Box 7590](https://nl.avm.de/producten/fritzbox/fritzbox-7590/).
 - A generic Zigbee plug to control my floor heating pump.
