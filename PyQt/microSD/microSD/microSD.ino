#include <SPI.h>
#include <SD.h>

File myFile;
File myFile2;
String read;
#define SD_CARD_EVENT_TIME 6000

const int chipSelect = 4;
String readString;
unsigned long prevTime = 0;

void setup() {
  Serial.begin(9600);

  pinMode(SS, OUTPUT);

  if (!SD.begin(chipSelect)) {
    Serial.println("initialization failed!");
    return;
  }
  //Serial.println("initialization done.");

  // WRITING INTO THE SD
  // myFile = SD.open("dataview.txt", FILE_WRITE);
  
  // if (myFile) {
  //   Serial.print("Writing to test.txt...");
  //   myFile.println("08:20");
  //   myFile.println(4);
  //   myFile.println(23);
  //   myFile.println(65);
  //   myFile.println(20);
  //   myFile.println("18");
  //   myFile.println("walking");
  //   myFile.println("yes");
  //   myFile.println("yes");
  //   myFile.println(7);

  //   myFile.close();
  //   Serial.println("done.");
  // } else {
  //   Serial.println("error opening dataview.txt");
  // }
  
  
  // READ FROM THE SD
  myFile = SD.open("dataview.txt");

  if (myFile) {    
    while (myFile.available()) {
    	Serial.write(myFile.read());
    }
    myFile.close();
  } 
}

void loop() {
  // put your main code here, to run repeatedly:

}
