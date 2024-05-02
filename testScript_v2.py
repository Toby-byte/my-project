from pynput import mouse
import time
import threading

class ClickCounter:
    def __init__(self, inactivity_threshold=3):
        self.click_count = 0
        self.inactivity_times = []
        self.last_click_time = None
        self.inactivity_threshold = inactivity_threshold
        self.start_time = None
        self.time_taken = None
        self.running = True  # Control the running state of the listener
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        # Check for inactivity on mouse press only
        if pressed:
            current_time = time.time()
            if self.last_click_time is not None:
                inactivity_duration = current_time - self.last_click_time
                if inactivity_duration >= self.inactivity_threshold:
                    self.inactivity_times.append(inactivity_duration)
            self.last_click_time = current_time
            self.click_count += 1

    def start_task(self):
        print("Task started. Click anywhere to count clicks. Inactivity longer than 3 seconds will be recorded.")
        self.start_time = time.time()
        self.last_click_time = self.start_time  # Initialize last click time
        self.listener.start()

    def end_task(self):
        self.running = False  # Stop counting clicks
        self.listener.stop()  # Stop the listener
        self.time_taken = time.time() - self.start_time
        return self.click_count, self.time_taken, self.inactivity_times

def wait_for_end_command():
    command = ""
    while command != "end":
        command = input("Type 'end' to finish the task: ")

# Example usage
click_counter = ClickCounter()
click_counter.start_task()

# Use a thread to wait for the 'end' command without blocking other operations
end_thread = threading.Thread(target=wait_for_end_command)
end_thread.start()
end_thread.join()  # Wait for the end command

click_count, time_taken, inactivity_periods = click_counter.end_task()
print("Task Completed!")
print(f"Number of Clicks: {click_count}")
print(f"Task Completion Time: {time_taken} seconds")
if inactivity_periods:
    for period in inactivity_periods:
        print(f"Inactivity Periods Longer Than 3 Seconds: {period:.2f} seconds")
else:
    print("No significant inactivity periods.")