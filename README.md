THIS is to use an alternative to adruino and c++/embedded c by using esp 8622 and micropython.
first go to https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html and follow steps to setup your esp 8622 and micropython setup in system.
YOU can use generally any os.
THE command for esp firmware on system is 
pip install esptool

and then erase it using 
esptool.py --port /dev/ttyUSB0 erase_flash
and then deploy it using
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin

if it runs without error then micropython has been installed on the board.


