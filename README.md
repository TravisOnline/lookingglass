# 🔍 Meta Lookingglass

A simple Python Bluetooth scanner used to detect nearby **Ray-Ban Meta smart glasses**.

This project is intended as a lightweight proof-of-concept, with future plans to deploy it on a Raspberry Pi or other portable embedded device.

---

## 📚 Credits

This project is heavily inspired by the work of  
[Yves Jeanrenaud – yj_nearbyglasses](https://github.com/yjeanrenaud/yj_nearbyglasses)

---

## ⚙️ How It Works

The script uses the **Bleak** Python library to collect Bluetooth Low Energy (BLE) advertising packets from nearby devices.

It then filters devices based on specific **Bluetooth Manufacturer IDs** associated with smart glasses manufacturers:

- `0x01AB` — Meta Platforms, Inc. (formerly Facebook)  
- `0x058E` — Meta Platforms Technologies, LLC  
- `0x0D53` — Luxottica Group S.p.A (manufacturer of Ray-Ban Meta glasses)  
- `0x03C2` — Snapchat, Inc. (manufacturer of Spectacles)

Only devices broadcasting these identifiers are flagged.

---

## 📡 Distance Estimation (RSSI-Based)

The script uses the **RSSI (Received Signal Strength Indicator)** value from BLE advertisements to estimate approximate distance.

> ⚠️ **Important:** RSSI-based distance estimation is highly approximate.

Signal strength can be affected by:

- Walls and physical obstructions  
- Human body blocking  
- Signal reflections (multipath interference)  
- Antenna orientation  
- Device transmit power (TX power)  

Because of these factors, calculated distances may not be accurate.

---

## ⚠️ Important Disclaimer

As noted in Yves Jeanrenaud’s original research, this method may detect devices from the listed manufacturers that are **not surveillance glasses**, such as:

- VR headsets  
- Other wearable devices  
- Experimental hardware  

This tool should be used responsibly and with sound judgment.
