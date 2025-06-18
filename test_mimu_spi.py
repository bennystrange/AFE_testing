# author: alekspop
# copy/paste for testing MIMU SPI comm.
import busio
from digitalio import DigitalInOut
import microcontroller as mc

# MIMU SPI bus comm. to magnetometer, IMU and U28 MAX7317ATE+ GPIO chip
print("Starting test MIMU SPI")
MAG_CSn = DigitalInOut(mc.pin.GPIO14)
MAG_CSn.switch_to_output(value=True)
IMU_CSn = DigitalInOut(mc.pin.GPIO13)
IMU_CSn.switch_to_output(value=True)
GPIO_CSn = DigitalInOut(mc.pin.GPIO8)
GPIO_CSn.switch_to_output(value=True)
spi = busio.SPI(mc.pin.GPIO10, mc.pin.GPIO11, mc.pin.GPIO12) #SCK,MOSI,MISO
print("SPI initialized and locked: ", spi.try_lock())

# Read MAG ID
MAG_CSn.value = 0
recv2bytes = bytearray(2)
mag_rdbk = bytes([0xb6, 0x00])
spi.write_readinto(mag_rdbk, recv2bytes)
print("Received Mag REVID: ", hex(recv2bytes[1]), " (correct response is 0x22)")
MAG_CSn.value = 1

# Read IMU ID
IMU_CSn.value = 0
recv2bytes = bytearray(2)
imu_rdbk = bytes([0x8f, 0x00]) #
spi.write_readinto(imu_rdbk, recv2bytes)
print("Received IMU ID: ", hex(recv2bytes[1]), " (correct response is 0x6c)")
IMU_CSn.value = 1

# Write ON for U28 Ports 0-9
#GPIO_CSn.value = 0
#wr_bytes = bytes([0x0A, 0x01]) # Ports 0-9 ON
#spi.write(wr_bytes)
#GPIO_CSn.value = 1
# Write OFF for U28 Ports 0-9
#GPIO_CSn.value = 0
#wr_bytes = bytes([0x0A, 0x00]) # Ports 0-9 OFF
#spi.write(wr_bytes)
#GPIO_CSn.value = 1

# External Bias
# Turn ON external bias voltage output (3.3V for MEP demo)
GPIO_CSn.value=0
wr_bytes = bytes([0x05, 0x01]) # Port 5 to ON
spi.write(wr_bytes)
GPIO_CSn.value=1
# Turn OFF external bias voltage output
GPIO_CSn.value=0
wr_bytes = bytes([0x05, 0x00]) # Port 5 to OFF
spi.write(wr_bytes)
GPIO_CSn.value=1

# Ref Select
# Turn ON ref select to choose OCXO 10 MHz ref
GPIO_CSn.value=0
wr_bytes = bytes([0x08, 0x01])
spi.write(wr_bytes)
GPIO_CSn.value=1
# Turn OFF ref select to choose external ref (not connected by default)
GPIO_CSn.value=0
wr_bytes = bytes([0x08, 0x00])
spi.write(wr_bytes)
GPIO_CSn.value=1

# GPS Antenna
# Choose external antenna (OFF on P9)
GPIO_CSn.value=0
wr_bytes = bytes([0x09, 0x00])
spi.write(wr_bytes)
GPIO_CSn.value=1
# Choose internal antenna (ON on P9, default)
GPIO_CSn.value=0
wr_bytes = bytes([0x09, 0x01])
spi.write(wr_bytes)
GPIO_CSn.value=1

# Test "LOCKED" LED
#locked = DigitalInOut(mc.pin.GPIO21)
#locked.switch_to_output(value=True)
#locked.value = 0 #OFF
#locked.value = 1 #ON

# Deinit when finished running as a program
#MAG_CSn.deinit()
#spi.deinit()
