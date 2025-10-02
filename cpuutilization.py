import psutil
import time

try:
    
   while True:
      cpu_usage = psutil.cpu_percent(interval=1)
      print("Monitoring CPU usage...")
      if cpu_usage > 90:
          print(f"Critical : High CPU usage detected! {cpu_usage}%")  
      elif cpu_usage > 75:
          print(f"Warning : Moderate CPU usage detected! {cpu_usage}%")
      else:
          print(f"CPU usage is normal! {cpu_usage}%")
except KeyboardInterrupt:
   print("Monitoring stopped by user.")
    