mkdir -p build
cd build || exit 1
cmake .. && make && uf2topico rfid.uf2 && picoterm