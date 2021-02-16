// IMPORTS
#include "SPI.h" // SPI library
#include "MFRC522.h" // RFID library

// GLOBAL VARIABLES
String rfidKey = "";
int rfidReadGood = 0;    //0 is false, 1 is true

// RFID MODULE SETUP
const int pinRST = 9;
const int pinSDA = 10;
MFRC522 mfrc522(pinSDA, pinRST);






void setup() {

  // RFID MODULE SETUP
  SPI.begin(); // open SPI connection
  mfrc522.PCD_Init(); // Initialize Proximity Coupling Device (PCD)

  //baud rate config - CONNECT TO RPI
  Serial.begin(9600);
  
}






void loop() {

  if (Serial.available() > 0)   // check if there are any avaibale data from the serial
  {
    String commandFromPi = Serial.readStringUntil('\n');     // read data from the PI, converted to string

    if (commandFromPi == "scanNOW")
    {
      read_RFID_key();            //read RFID function
      Serial.println(rfidKey);    //send rfid key read from above
      rfidKey = "";               //clears rfidKey value
    }
    
  }

}
