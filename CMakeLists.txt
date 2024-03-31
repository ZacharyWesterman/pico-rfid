cmake_minimum_required(VERSION 3.16)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

set(PICO_PLATFORM rp2040)
set(PICO_BOARD "pico_w")
set(PICO_COMPILER "pico_arm_gcc")
set(CMAKE_BUILD_TYPE Release)

set(BTSTACK_ROOT ${PICO_SDK_PATH}/lib/btstack)
set(BTSTACK_EXAMPLE_PATH ${BTSTACK_ROOT}/example)
set(BTSTACK_3RD_PARTY_PATH ${BTSTACK_ROOT}/3rd-party)
set(BT_EXAMPLE_COMMON_DIR "${CMAKE_CURRENT_LIST_DIR}")

# initialize the SDK based on PICO_SDK_PATH
# note: this must happen before project()
include(pico_sdk_import.cmake pico_extras_import.cmake)

project(rfid C CXX ASM)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

# rest of your project

add_executable(rfid
	main.c
)

target_include_directories(rfid PRIVATE
	${CMAKE_SOURCE_DIR}
	${CMAKE_CURRENT_LIST_DIR}
)

# Add pico_stdlib library which aggregates commonly used features
target_link_libraries(
	rfid
	pico_stdlib
	hardware_i2c
	hardware_spi
	pico_btstack_ble
	pico_btstack_classic
	pico_btstack_cyw43
	pico_cyw43_arch_none
)

# Enable USB debug, disable UART debug
pico_enable_stdio_usb(rfid 1)
pico_enable_stdio_uart(rfid 0)

# create map/bin/hex/uf2 file in addition to ELF.
pico_add_extra_outputs(rfid)

suppress_btstack_warnings()
