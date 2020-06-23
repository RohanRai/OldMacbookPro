import time, datetime
for i in range(10):
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print(current_time + "   " + str(i), end="\r", flush=True)
	time.sleep(1)


