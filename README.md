# pico-rfid
An RFID scanner that spits out the scanned text as a USB keyboard.

# Installing on the rp2040

1. Connect the rp2040 in BOOTSEL mode.
2. Once it connects as a drive, copy the `adafruit-circuitpython-(etc.).uf2` file onto the drive.
3. The drive will disconnect, then unplug the rp2040.
4. Plug in the rp2040 (NOT in BOOTSEL mode). Again, it will connect as a drive, but this time there will be different files.
5. Copy the `lib/` and `code.py` to that drive, choosing "merge" and "overwrite existing" options as for everything.

Done!
If there are any updates to this project, the code can be updated by just plugging in the rp2040 and copying `code.py` over.
