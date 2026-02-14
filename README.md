# pico-rfid
An RFID scanner that spits out the scanned text as if it was a USB keyboard.

# Installing on the rp2040

1. Connect the rp2040 in BOOTSEL mode.
2. Once it connects as a drive, copy the `adafruit-circuitpython-(etc.).uf2` file onto the drive.
3. The drive will disconnect, then reconnect itself as a drive with a new name, and different files.
5. Copy the `lib/`, `code.py` and `boot.py` to that drive, choosing "merge" and "overwrite existing" options as for everything.
Done!

If you have any issues re-flashing the rp2040 (it can sometimes get into a bad state),
connect in BOOTSEL mode, and copy `flash_nuke.uf2` onto the drive.
That will reset it back to a pristine state.
