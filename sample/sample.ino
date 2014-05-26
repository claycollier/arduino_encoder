int pin = 13;

void setup() {
	pinMode(pin, OUTPUT);
}

void loop() {
	dot();
	dot();
	dot();
	dash();
	dash();
	dash();
	dot();
	dot();
	dot();
	gap();
	dash();
	dot();
	dot();
	dot();
	dot();
	dot();
	dot();
	dot();
	dot();
	dot();
	gap();
	dot();
	dot();
	dot();
	dot();
	dot();
	gap();
	dash();
	dash();
	dash();
	dash();
	dot();
	dot();
	dash();
	dot();
	dot();
	dash();
	dot();
	dash();
	dash();
	gap();
	dot();
	dash();
	gap();
	dash();
	dot();
	dot();
	dot();
	dot();
	dash();
	gap();
	dot();
	dot();
	dot();
	dash();
	dash();
	dash();
	dot();
	dot();
	dot();
	gap();
	gap();

}

void dot() { digitalWrite(pin, HIGH); delay(250); digitalWrite(pin, LOW); delay(250); }

void dash() { digitalWrite(pin, HIGH); delay(1000); digitalWrite(pin, LOW); delay(250); }
void gap() { digitalWrite(pin, LOW);delay(1000);}

