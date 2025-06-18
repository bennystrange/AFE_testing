# author: alekspop
# copy/paste code for RF SPI comm. MEP AFE

import busio
from digitalio import DigitalInOut
import microcontroller as mc

# def wr_bytes(bytes):
#   AFE_RX_CSn.value = 0
#   spi_rf.write(bytes)
#   AFE_RX_CSn.value = 1

print("Starting test RF SPI")
# RF SPI bus comm. to 4 RX, 2 TX (U7 and U44 MAX7317ATE+ GPIO chip)
AFE_RX_CSn = DigitalInOut(mc.pin.GPIO9)
AFE_RX_CSn.switch_to_output(value=True)
spi_rf = busio.SPI(mc.pin.GPIO18, mc.pin.GPIO19, mc.pin.GPIO20) #SCK,MOSI,MISO
spi_rf.try_lock()

# RX Filter Bypass SEL

# Write ON to all ADC (bypass selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x02,0x01,0x02,0x01,0x02,0x01,0x02,0x01]) # Port ON
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1
# Write OFF to ADC (filter selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x02,0x00,0x02,0x00,0x02,0x00,0x02,0x00]) # Port OFF
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1


# Write ON to ADC_D (bypass selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x20,0x00,0x20,0x00,0x20,0x00,0x02,0x01]) # Port ON
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1
# Write OFF to ADC_D (filter selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x20,0x00,0x20,0x00,0x20,0x00,0x02,0x00]) # Port OFF
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1


# Write ON to ADC_C (bypass selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x20,0x00,0x20,0x00,0x02,0x01,0x20,0x00]) # Port ON
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1
# Write OFF to ADC_C (filter selected)
AFE_RX_CSn.value = 0
wr_bytes = bytes([0x20,0x00,0x20,0x00,0x02,0x00,0x20,0x00]) # Port OFF
spi_rf.write(wr_bytes)
AFE_RX_CSn.value = 1

