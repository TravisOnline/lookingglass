import asyncio
from bleak import BleakScanner
import time

FILTER_ID = {
    0x01AB,
    0x058E,
    0x0D53,
    0x03C2,
}

def rssi_to_distance(rssi: int) -> str:
    if rssi >= -60:
        return "1 - 3m"
    elif rssi >= -70:
        return "3 - 10m"
    elif rssi > -80:
        return "10 - 20m"
    elif rssi > -90:
        return "20 - 40m"
    elif rssi > -100:
        return "30 100m or nearl signal loss"
    else:
        return "Very weak / likely out of range"

async def main():
    while True:
        devices = await BleakScanner.discover(timeout=5, return_adv=True)

        i = 0
        for device, adv in devices.values():

            manufacturer_data = adv.manufacturer_data

            if not manufacturer_data:
                continue

            for company_id in manufacturer_data.keys():
                if company_id in FILTER_ID:
                    i += 1
                    name = device.name or "Unknown"
                    rssi = adv.rssi
                    distance_estimate = rssi_to_distance(rssi)
                    print(f"{i:2} {name} | Manufacturer ID: 0x{company_id:04X} | Est Distance: {distance_estimate}")
        time.sleep(10)

asyncio.run(main())
