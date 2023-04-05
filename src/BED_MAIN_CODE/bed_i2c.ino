/* Implementation file for useful I2C elements*/

/* 
  Sets up the I2C system.
  Params : N/A
  Outputs: Error Code.
*/
int32_t bed_get_i2c_status(uint8_t address)
{
  int32_t b32_error_code = BED_ERR_NONE;
  int8_t transmissionError = -1;
  
  Wire.beginTransmission(address);
  delay(10);
  transmissionError = Wire.endTransmission();
  if(transmissionError != 0)
  {
     b32_error_code = BED_ERR_I2C_CONNECTION;
  }
  return b32_error_code;
}