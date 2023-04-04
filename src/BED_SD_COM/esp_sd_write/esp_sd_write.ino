/*==========================================
 Title:  BED SD Test for ESP32 
 Author: Nish Shah
 Date:   4 April 2023
==========================================*/
#include "FS.h"
#include "SD.h"
#include "SPI.h"

void listDir(fs::FS &fs, const char * dirname, uint8_t levels){
  Serial.printf("Listing directory: %s\n", dirname);

  File root = fs.open(dirname);
  if(!root){
    Serial.println("Failed to open directory");
    return;
  }
  if(!root.isDirectory()){
    Serial.println("Not a directory");
    return;
  }

  File file = root.openNextFile();
  while(file){
    if(file.isDirectory()){
      Serial.print("  DIR : ");
      Serial.println(file.name());
      if(levels){
        listDir(fs, file.name(), levels -1);
      }
    } else {
      Serial.print("  FILE: ");
      Serial.print(file.name());
      Serial.print("  SIZE: ");
      Serial.println(file.size());
    }
    file = root.openNextFile();
  }
}

void createDir(fs::FS &fs, const char * path){
  Serial.printf("Creating Dir: %s\n", path);
  if(fs.mkdir(path)){
    Serial.println("Dir created");
  } else {
    Serial.println("mkdir failed");
  }
}

void removeDir(fs::FS &fs, const char * path){
  Serial.printf("Removing Dir: %s\n", path);
  if(fs.rmdir(path)){
    Serial.println("Dir removed");
  } else {
    Serial.println("rmdir failed");
  }
}

void readFile(fs::FS &fs, const char * path){
  File file = fs.open(path);
  if(!file){
    Serial.println("Failed to open file for reading");
    return;
  }

  // Serial.print("Read from file: ");
  while(file.available()){
    Serial.write(file.read());
  }
  file.close();
}

void writeFile(fs::FS &fs, const char * path, const char * message){
  File file = fs.open(path, FILE_WRITE);
  if(!file){
    Serial.println("Failed to open file for writing");
    return;
  }
  if(!file.print(message)){
    Serial.println("Write failed");
  }
  file.close();
}

void appendFile(fs::FS &fs, const char * path, const char * message){
  // Serial.printf("Appending to file: %s\n", path);

  File file = fs.open(path, FILE_APPEND);
  if(!file){
    Serial.println("Failed to open file for appending");
    return;
  }
  if(file.print(message)){
      // Serial.println("Message appended");
  } else {
    Serial.println("Append failed");
  }
  file.close();
}

void renameFile(fs::FS &fs, const char * path1, const char * path2){
  Serial.printf("Renaming file %s to %s\n", path1, path2);
  if (fs.rename(path1, path2)) {
    Serial.println("File renamed");
  } else {
    Serial.println("Rename failed");
  }
}

void deleteFile(fs::FS &fs, const char * path){
  Serial.printf("Deleting file: %s\n", path);
  if(fs.remove(path)){
    Serial.println("File deleted");
  } else {
    Serial.println("Delete failed");
  }
}

void testFileIO(fs::FS &fs, const char * path){
  File file = fs.open(path);
  static uint8_t buf[512];
  size_t len = 0;
  uint32_t start = millis();
  uint32_t end = start;
  if(file){
    len = file.size();
    size_t flen = len;
    start = millis();
    while(len){
      size_t toRead = len;
      if(toRead > 512){
        toRead = 512;
      }
      file.read(buf, toRead);
      len -= toRead;
    }
    end = millis() - start;
    // Serial.printf("%u bytes read for %u ms\n", flen, end);
    file.close();
  } else {
    Serial.println("Failed to open file for reading");
  }


  file = fs.open(path, FILE_WRITE);
  if(!file){
    Serial.println("Failed to open file for writing");
    return;
  }

  size_t i;
  start = millis();
  for(i=0; i<2048; i++){
    file.write(buf, 512);
  }
  end = millis() - start;
  // Serial.printf("%u bytes written for %u ms\n", 2048 * 512, end);
  file.close();
}

void setup(){
  Serial.begin(115200);
  char message1[50] = "08:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message2[50] = "09:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message3[50] = "10:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message4[50] = "11:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message5[50] = "12:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message6[50] = "13:20,4,23,65,20,18,Limping,yes,yes,7\n";
  char message7[50] = "14:20,4,23,65,20,18,Limping,yes,yes,7\n";

    // myFile.println(23);
    // myFile.println(65);
    // myFile.println(20);
    // myFile.println("18");
    // myFile.println("walking");
    // myFile.println("yes");
    // myFile.println("yes");
    // myFile.println(7);
  if(!SD.begin(5)){
    Serial.println("Card Mount Failed");
    return;
  }
  uint8_t cardType = SD.cardType();

  if(cardType == CARD_NONE){
    Serial.println("No SD card attached");
    return;
  }

  // Serial.print("SD Card Type: ");
  // if(cardType == CARD_MMC){
  //   Serial.println("MMC");
  // } else if(cardType == CARD_SD){
  //   Serial.println("SDSC");
  // } else if(cardType == CARD_SDHC){
  //   Serial.println("SDHC");
  // } else {
  //   Serial.println("UNKNOWN"); 
  // }

  uint64_t cardSize = SD.cardSize() / (1024 * 1024);
  // Serial.printf("SD Card Size: %lluMB\n", cardSize);

  // listDir(SD, "/", 0);
  // createDir(SD, "/mydir");
  // listDir(SD, "/", 0);
  // removeDir(SD, "/mydir");
  // listDir(SD, "/", 2);
  writeFile(SD, "/dataview.txt", message1);
  appendFile(SD, "/dataview.txt", message2);
  appendFile(SD, "/dataview.txt", message3);
  appendFile(SD, "/dataview.txt", message4);
  appendFile(SD, "/dataview.txt", message5);
  appendFile(SD, "/dataview.txt", message6);
  appendFile(SD, "/dataview.txt", message7);


  // appendFile(SD, "/hello.txt", "World!\n");
  readFile(SD, "/dataview.txt");
  // deleteFile(SD, "/foo.txt");
  // renameFile(SD, "/hello.txt", "/foo.txt");
  // readFile(SD, "/foo.txt");
  // testFileIO(SD, "/test.txt");
  // Serial.printf("Total space: %lluMB\n", SD.totalBytes() / (1024 * 1024));
  // Serial.printf("Used space: %lluMB\n", SD.usedBytes() / (1024 * 1024));
}

void loop(){

}
