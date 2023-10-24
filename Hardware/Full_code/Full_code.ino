#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define SS_PIN 10
#define RST_PIN 9
int led1 = A0;
int led2 = A1;
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.

#define beep_pin 8
#define DHTPIN 8
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

LiquidCrystal lcd(2, 3, 4, 5, 6, 7);

void setup()
{
  Serial.begin(9600); // Initiate a serial communication

  pinMode(beep_pin, OUTPUT);
  digitalWrite(beep_pin, LOW);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  lcd.begin(16, 2);
  lcd.setCursor(3, 1);
  lcd.print("Welcome!!");
  lcd.setCursor(0, 0);
  lcd.print("System all set");
  delay(1500);
  lcd.clear();

  SPI.begin();      // Initiate SPI bus
  mfrc522.PCD_Init(); // Initiate MFRC522
  Serial.println("Put your card to the reader...");
  Serial.println();

  dht.begin(); // Initiate DHT sensor
}

void loop()
{
  // Collect DHT data every 5 seconds
  static unsigned long lastDHTRead = 0;
  if (millis() - lastDHTRead >= 30000)
  {
    lastDHTRead = millis();

    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float f = dht.readTemperature(true);

    if (!isnan(h) && !isnan(t) && !isnan(f))
    {
      // Create a JSON object for DHT11 sensor data
      StaticJsonDocument<100> jsonDoc;
      jsonDoc["Humidity"] = h;
      jsonDoc["TemperatureC"] = t;
      jsonDoc["TemperatureF"] = f;
      jsonDoc["HeatIndexC"] = dht.computeHeatIndex(t, h, false);
      jsonDoc["HeatIndexF"] = dht.computeHeatIndex(f, h);

      // Serialize JSON data and send it to Serial
      serializeJson(jsonDoc, Serial);
      Serial.println(); // Add a newline for clarity
    }
    else
    {
      Serial.println(F("Failed to read from DHT sensor!"));
    }
  }

  // Look for new cards and process RFID data
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())
  {
    // Show UID on serial monitor
    Serial.print("UID tag :");
    String content = "";
    for (byte i = 0; i < mfrc522.uid.size; i++)
    {
      Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
      Serial.print(mfrc522.uid.uidByte[i], HEX);
      content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
      content.concat(String(mfrc522.uid.uidByte[i], HEX));
    }
    Serial.println();
    Serial.print("Message : ");
    content.toUpperCase();

    // Create a JSON object
    StaticJsonDocument<128> jsonDoc;
    jsonDoc["UID"] = content.substring(1);

    // Check access and add "Message" field to the JSON object
    if (content.substring(1) == "C1 29 15 31") // Change here the UID of the card/cards that you want to give access
    {
      jsonDoc["Message"] = "Access granted";
      digitalWrite(beep_pin, HIGH);
      digitalWrite(led1, HIGH);
      delay(1000);
      digitalWrite(led1, LOW);
      digitalWrite(beep_pin, LOW);
      lcd.setCursor(0, 0);
      lcd.print("ID : ");
      lcd.print(content.substring(1));
      lcd.setCursor(0, 1);
      lcd.print("Authorized access");
      Serial.println("Authorized access");
      delay(3500);
    }
    else
    {
      jsonDoc["Message"] = "Access denied";
      digitalWrite(beep_pin, HIGH);
      digitalWrite(led2, HIGH);
      delay(1000);
      digitalWrite(led2, LOW);
      lcd.setCursor(0, 0);
      lcd.print("ID : ");
      lcd.print(content.substring(1));
      lcd.setCursor(0, 1);
      lcd.print("Access denied");
      Serial.println(" Access denied");
      delay(1500);
    }

    // Serialize the JSON object to a string
    String jsonString;
    serializeJson(jsonDoc, jsonString);

    // Print the JSON data to the serial monitor
    Serial.println("RFID Data:");
    Serial.println(jsonString);
  }
}
