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
int switcher = 1;
int f_x, f_y, s_x, s_y;

TrackPoint trackpoint(CLOCK, DATA, RESET, true);

void setup()
{	
  Serial.begin(115200);
	trackpoint.reset();
	trackpoint.setSensitivityFactor(0xC0);
	trackpoint.setStreamMode();
  Serial.println("Update Done");
	attachInterrupt(CLOCK_INT, clockInterrupt, FALLING);
}

void loop()
{
	
}

void clockInterrupt(void) {
  trackpoint.getDataBit();
  if(trackpoint.reportAvailable()) {
    if(switcher == 1) {
    TrackPoint::DataReport d = trackpoint.getStreamReport();
    f_x = d.x;
    f_y = d.y;
   
    }
    if(switcher==-1)
    {
      TrackPoint::DataReport d = trackpoint.getStreamReport();
      s_x = d.x;
      s_y = d.y;
     
    }
    switcher = switcher * -1;
       Serial.print(switcher); Serial.print("  ");Serial.print(f_x); Serial.print("  ");Serial.print(f_y); Serial.print("  ");Serial.print(s_x); Serial.print("  "); Serial.println(s_y); 
  } 
}
