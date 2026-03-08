import asyncio
import argparse
from bleak import BleakScanner

FILTER_IDS = {
    0x01AB,
    0x058E,
    0x0D53,
    0x03C2,
}

output_file = None


def rssi_to_distance(rssi: int) -> str:
    if rssi >= -60:
        return "1–3m"
    elif rssi >= -70:
        return "3–10m"
    elif rssi >= -80:
        return "10–20m"
    elif rssi >= -90:
        return "20–40m"
    elif rssi >= -100:
        return "30–100m+ or near signal loss"
    else:
        return "Very weak / likely out of range"


def detection_callback(device, adv_data):

    manufacturer_data = adv_data.manufacturer_data
    if not manufacturer_data:
        return

    for company_id in manufacturer_data.keys():
        if company_id not in FILTER_IDS:

            name = device.name or "Unknown"
            rssi = adv_data.rssi
            distance = rssi_to_distance(rssi)

            line = (
                f"Device: {name} | "
                f"Manufacturer: 0x{company_id:04X} | "
                f"RSSI: {rssi} dBm | "
                f"Est. Distance: {distance}"
            )

            print(line)

            if output_file:
                output_file.write(line + "\n")
                output_file.flush()


async def main():
    global output_file

    parser = argparse.ArgumentParser(description="Bluetooth scanner for smart glasses")
    parser.add_argument("-o", "--output", help="Output results to file")

    args = parser.parse_args()

    if args.output:
        output_file = open(args.output, "a")

    scanner = BleakScanner(detection_callback=detection_callback)

    print("Scanning for devices... Press CTRL+C to stop.")

    try:
        async with scanner:
            while True:
                await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping scan...")
    finally:
        if output_file:
            output_file.close()


if __name__ == "__main__":
    asyncio.run(main())
