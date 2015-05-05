#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time

def read_raw_val(data, chip_select, clock):
  GPIO.setup(data, GPIO.IN)
  GPIO.setup(chip_select, GPIO.OUT)
  GPIO.setup(clock, GPIO.OUT)

  a = 0
  output = 0
  readbit = 0
  GPIO.output(chip_select, GPIO.HIGH)
  time.sleep(0.01)
  GPIO.output(clock, GPIO.HIGH)
  time.sleep(0.01)
  GPIO.output(chip_select, GPIO.LOW)
  time.sleep(0.01)
  GPIO.output(clock, GPIO.LOW)
  time.sleep(0.01)
  while a < 16:
    GPIO.output(clock, GPIO.HIGH)
    time.sleep(0.01)
    readbit = GPIO.input(data)
    output = ((output << 1) + readbit)
    GPIO.output(clock, GPIO.LOW)
    time.sleep(0.01)
    a += 1
  return output

while 1:
  rawval = read_raw_val(“P9_15″, “P9_11″, “P9_12″)
  print “read: ” + str(rawval)
  print “raw rotation: ” + str(rawval >> 6)
  time.sleep(1)
