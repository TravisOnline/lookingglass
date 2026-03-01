import asyncio
from bleak import BleakScanner

FILTER_ID = {
    0x01AB,
    0x058E,
    0x0D53,
    0x03C2,
}

async def main():
    devices = await BleakScanner.discover(timeout=5, return_adv=True)

    i = 0
    for device, adv in devices.values():
        manufacturer_data = adv.manufacturer_data

        if not manufacturer_data:
            continue

        for company_id in manufacturer_data.keys():
            if company_id not in FILTER_ID:
                i += 1
                name = device.name or "Unknown"
                print(f"{i:2} {name} | Manufacturer ID: 0x{company_id:04X}")


asyncio.run(main())