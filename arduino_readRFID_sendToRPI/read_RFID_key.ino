void read_RFID_key()
{
  rfidReadGood = 0;
  
  while(rfidReadGood == 0)
  {
    if (mfrc522.PICC_IsNewCardPresent())  //Check if card is available
    { 
    
 
      if(mfrc522.PICC_ReadCardSerial())    // Check if card was read successfully
      { 
        for (byte i = 0; i < mfrc522.uid.size; ++i) // read id (in parts)
        { 
          rfidKey.concat(String(mfrc522.uid.uidByte[i], HEX));
        } 
        rfidReadGood = 1;
      } 
    }

    
  }
  
 
}
