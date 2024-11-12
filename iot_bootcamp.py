import RPi.GPIO as GPIO
import time

'''There may be irregularities in the code 
since I'm a beginner. You may require to
counter some out of place or unnecessary logic.
Buckle up!''' 


'Ultrasound sensor'
GPIO.setmode(GPIO.BOARD)
TRIG PIN=16
ECHO PIN=18
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(37,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35,GPIO.OUT, initial=GPIO.LOW)
pulse_start=0
pulse_end=0

'Buzzer'
GPIO.setup(11,GPIO.OUT, initial=GPIO.LOW)

'Servo Motor'
SERVO PIN = 12
GPIO.setup(SERVO_PIN,GPIO.OUT)
pwm_freq= 50
pwm= GPIO.PWM(SERVO_PIN,pwm_freq)
pwm.start(0)

def set_servo_angle(angle):
   duty_cycle (angle/18)+2.5
   pwm.Change DutyCycle(duty_cycle)

def get_distance():
   GPIO.output(TRIG_PIN, GPIO.HIGH) 
   time.sleep(0.00001) 
   GPIO.output(TRIG_PIN,GPIO.LOW) 
   while GPIO.input(ECHO_PIN) == 00: 
      pulse_start = time.time() 
   while GPIO.input(ECHO_PIN) == 1: 
      pulse_end = time.time()
   pulse_duration=pulse_end - pulse_start 
   distance = pulse_duration *34300/2
   return distance

try:
   while True:
      distance = get_distance()
      print("Distance: (:.2f}cm". format(distance))
      if distance >30:
         GPIO.output(35,GPIO.LOW)
         print("Too far away')
         GPIO.output(37,GPIO.HIGH)
         GPIO.output(11,GPIO.HIGH)
         print('Servo Motor Not working')
         time.sleep(1)
         GPIO.output(11,GPIO.LOW)
         GPIO.output(37,GPIO.LOW)
         time.sleep(1)
      elif distance <30:
         print('Distance Okay.')
         print('Servo Motor Working')
         GPIO.output(35,GPIO.HIGH)
         for x in range(10000): 
            for angle in range(0, 180, 10):
               set_servo_angle(angle) 
            for angle in range(180, -1, -10): 
               set_servo_angle(angle)
except KeyboardInterrupt:
   pwm.stop()
   GPIO.cleanup()
