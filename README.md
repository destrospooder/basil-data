# basil-data
**Pesto and yummy yummy linguine aglio e oilo!**

**How to Run:**

Google Colab includes a badge to run a copy of the code on its webpage when exported to GitHub. You could also just clone the git repo and run [basil.py](./basil.py).

**Abstract:**

In my EID101: Engineering Design section, we created a basil hydroponics system incorporating a microcontroller and several sensors that collected data using existing infrastructure from the Cooper Union Sustainable Agriculture Project (CUSAP). The list of system names and data can be found at https://cusap-iot.uc.r.appspot.com/system/listSystems. One of the assignments was to use Pandas and Matplotlib that isolated a reading from a sensor and graphed it against time.

First, I made a GET request to https://cusap-iot.uc.r.appspot.com/system/getReadings, which takes in three query parameters: `systemId`, `timePeriod`, and `reading`. From the "reading" query parameter, I isolated `Air-Humidity`.

I also had to learn how to use "timestamps", a Pythonic way of representing what time a reading was recorded at. In order to make these timestamps readable, I had to use the `datetime` module.

When run, the code will create a DataFrame with two columns: timestamps and values of the readings from the hydroponics system's humidity sensor. It will also create a graph of the data over the span of one week, with axes marking % air humidity and time.

![peepeepoopoocheck](https://memegenerator.net/img/instances/54966675.jpg)
