/* Implementation file for useful I2C elements*/

/*
    Author    : Anish Rangarajan
    Date      : 11/19/2022
    Defintion : Returns i2c status of device based on address.
*/
int32_t bed_get_i2c_status(uint8_t address)
{
  int32_t b32_error_code = BED_ERR_NONE;
  int8_t transmissionError = -5;
  
  Wire.beginTransmission(address);
  delay(10);
  transmissionError = Wire.endTransmission();
  Serial.println(transmissionError);
  if(transmissionError != 0)
  {
     b32_error_code = BED_ERR_I2C_CONNECTION;
  }
  return b32_error_code;
}