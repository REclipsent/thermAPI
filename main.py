from fastapi import FastAPI
import adafruit_dht as dht
import board
import time

#SENSOR = dht.DHT22(board.D4)

app = FastAPI()

def temp_f_to_c(temp_c: int):
    temp = (temp_c * 1.8) + 32
    return temp

@app.get("/")
def read_root():
    SENSOR = dht.DHT22(board.D4)
    temp_c = SENSOR.temperature
    temp = temp_f_to_c(temp_c)
    humid = SENSOR.humidity
    SENSOR.exit()
    return {"Temperature": temp,
            "Humidty": humid}

@app.get("/temperature")
def get_temp():
    SENSOR = dht.DHT22(board.D4)
    temp_c = SENSOR.temperature
    temp = temp_f_to_c(temp_c)
    SENSOR.exit()
    return {"Temperature": temp}

@app.get("/humidty")
def get_humidty():
    SENSOR = dht.DHT22(board.D4)
    humid = SENSOR.humidity
    SENSOR.exit()
    return {"Humidty": humid}
