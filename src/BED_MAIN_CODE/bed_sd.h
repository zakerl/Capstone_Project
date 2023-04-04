#ifndef BED_SD_H
#define BED_SD_H

#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

/* 
  Lists all directories
  Params : &fs              : Sd card object.
           dirname          : Directory name.
           levels           : depth to search
  Outputs: N/A
*/
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

/* 
  Creates a new directory
  Params : &fs              : Sd card object.
           path             : File path to create a directory/
  Outputs: N/A
*/
void createDir(fs::FS &fs, const char * path){
  Serial.printf("Creating Dir: %s\n", path);
  if(fs.mkdir(path)){
    Serial.println("Dir created");
  } else {
    Serial.println("mkdir failed");
  }
}

/* 
  Deletes a directory.
  Params : &fs              : Sd card object.
           path             : File path of directory
  Outputs: N/A
*/
void removeDir(fs::FS &fs, const char * path){
  Serial.printf("Removing Dir: %s\n", path);
  if(fs.rmdir(path)){
    Serial.println("Dir removed");
  } else {
    Serial.println("rmdir failed");
  }
}

/* 
  Reads data in the file.
  Params : &fs              : Sd card object.
           path             : File path.
  Outputs: N/A
*/
void readFile(fs::FS &fs, const char * path){
  // Serial.println("ReadFile called");
  File file = fs.open(path);
  if(!file){
    SerialBT.println("File not available");
    return;
  }
  while(file.available()){
        Serial.write(file.read());
      if (SerialBT.available()) {
        SerialBT.write(file.read());
      }
  }
  file.close();
}

/* 
  Writes data into the file.
  Params : path             : File path.
           message          : Text to write into the file.
  Outputs: N/A
*/
void writeFile(const char * path, const char * message){
  File file = SD.open(path, FILE_WRITE);
  if(!file){
    Serial.println("Failed to open file for writing");
    return;
  }
  if(!file.print(message)){
    Serial.println("Write failed");
  }
  file.close();
}

/* 
  Appends data into the file.
  Params : &fs              : Sd card object.
           path             : File path.
           message          : Text to write into the file.
  Outputs: N/A
*/
void appendFile(fs::FS &fs, const char * path, const char * message){
  // Serial.printf("Appending to file: %s\n", path);

  File file = fs.open(path, FILE_APPEND);
  if(!file){
    Serial.println("Failed to open file for appending");
    return;
  }
  if(file.print(message)){
      Serial.println("Message appended");
  } else {
    Serial.println("Append failed");
  }
  file.close();
}

/* 
  Renames file.
  Params : &fs              : Sd card object.
           path1            : File path 1.
           path2            : File path 2.
  Outputs: N/A
*/
void renameFile(fs::FS &fs, const char * path1, const char * path2){
  Serial.printf("Renaming file %s to %s\n", path1, path2);
  if (fs.rename(path1, path2)) {
    Serial.println("File renamed");
  } else {
    Serial.println("Rename failed");
  }
}

/* 
  Deletes file in a directory.
  Params : &fs              : Sd card object.
           path1            : File path.
  Outputs: N/A
*/
void deleteFile(fs::FS &fs, const char * path){
  Serial.printf("Deleting file: %s\n", path);
  if(fs.remove(path)){
    Serial.println("File deleted");
  } else {
    Serial.println("Delete failed");
  }
}

/* 
  Test function for file IO.
  Params : &fs              : Sd card object.
           path1            : File path.
  Outputs: N/A
*/
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

#endif