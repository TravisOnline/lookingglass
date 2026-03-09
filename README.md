# 🔍 Meta Lookingglass

Python Bluetooth scanner/monitor used to detect nearby **Ray-Ban Meta smart glasses**.

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

By analyzing the **RSSI (Received Signal Strength Indicator)** value from BLE advertisements, an approximate distance can be estimated.
As the script will return adertisement packets in real-time and at high frequencies, the approximate location of META hardware
can be easily ascertained.

---

## ⚠️ Important Disclaimer

As noted in Yves Jeanrenaud’s original research, this method may detect devices from the listed manufacturers that are **not surveillance glasses**, such as:

- VR headsets  
- Other wearable devices  
- Experimental hardware  

This tool should be used responsibly and with sound judgment.
