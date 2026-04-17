int led = 13;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char dato = Serial.read();

    if (dato == '1') {
      digitalWrite(led, HIGH);
    }
    if (dato == '0') {
      digitalWrite(led, LOW);
    }
  }
}