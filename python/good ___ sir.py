from datetime import datetime

current_time = datetime.now().time()
print(current_time )

if current_time.hour < 12:
    print("Good morning")
else:
    print("Good evening")
