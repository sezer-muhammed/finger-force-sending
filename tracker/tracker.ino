/*
 * Created on 14/03/2014
 * Author: Cong Nguyen
 *
 * Using an Arduino Leonardo to interface with a TrackPoint
 * Pin 3 (int.0)	: CLOCK
 * Pin 2			: DATA
 * Pin 4			: RESET
 */
#include "TrackPoint.h"

#define	CLOCK		3
#define DATA		2
#define RESET		4
#define CLOCK_INT	3


TrackPoint trackpoint(CLOCK, DATA, RESET, true);

void setup()
{	
  Serial.begin(115200);
	trackpoint.reset();
	trackpoint.setSensitivityFactor(0xC0);
  trackpoint.setStreamMode();
	attachInterrupt(CLOCK_INT, clockInterrupt, FALLING);
}

void loop()
{
	
}

void clockInterrupt(void) {
  trackpoint.getDataBit();
  if(trackpoint.reportAvailable()) {
    TrackPoint::DataReport d = trackpoint.getStreamReport();
    Serial.print(d.x); Serial.print("  ");Serial.println(d.y);
  }
}
