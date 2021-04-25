

THIS is to use an alternative to adruino and c++/embedded c by using esp 8266 and micropython.
first go to https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html and follow steps to setup your esp 8266 and micropython setup in system.
YOU can use generally any os.
THE command for esp firmware on system is -
              "pip install esptool"

and then erase it using -
            " esptool.py --port /dev/ttyUSB0 erase_flash "
and then deploy it using
                   "esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin"

if it runs without error then micropython has been installed on the board.
I am not a expert on this , i was just enjoying esp 8266 and was shocked seeing it supports micropython and went on reading its documentation and applying so, you if you guys find a lot of errors please correct them and feel free  to check out espressif github page for learning more about esp 8266 and implementation on the board.   

 
YOU will need a esp 8266 connected to your pc on which you will code , and will need a usb cable for the connection.
