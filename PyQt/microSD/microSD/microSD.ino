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
  myFile = SD.open("dataview.txt", FILE_WRITE);
  
  if (myFile) {
    //Serial.print("Writing to test.txt...");
    myFile.println("Time, 08:20");
    myFile.println("Steps, 23");
    myFile.println("HeartRate, 65");
    myFile.println("ActivityTime, 18");
    myFile.println("ActivityType, walking");
    myFile.println("PromptGen, yes");
    myFile.println("Pain, yes");
    myFile.println("PainLevel, 7");

    myFile.close();
    //Serial.println("done.");
  } else {
    Serial.println("error opening dataview.txt");
  }
  
  
  // READ FROM THE SD
  myFile = SD.open("dataview.txt");

  if (myFile) {
    Serial.println("test.txt:");
    
    while (myFile.available()) {
    	Serial.write(myFile.read());
    }
    myFile.close();
  } else {
    Serial.println("error opening dataview.txt");
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
