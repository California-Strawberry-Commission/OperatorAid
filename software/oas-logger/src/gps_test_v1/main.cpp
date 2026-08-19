// Minimal sanity check: does Serial output work at all?
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  // No while(!Serial), no early prints we depend on — just loop forever.
}

void loop() {
  static uint32_t n = 0;
  Serial.printf("[hello] tick=%u millis=%u\n", n++, (unsigned)millis());
  Serial.flush();
  delay(500);
}
