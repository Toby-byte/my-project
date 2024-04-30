from pynput import mouse
import time
import threading

class ClickCounter:
    def __init__(self):
        self.click_count = 0
        self.start_time = None
        self.time_taken = None
        self.running = True  # Control the running state of the listener
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        # Increment click count on press only (not on release)
        if pressed and self.running:
            self.click_count += 1

    def start_task(self):
        print("Task started. Click anywhere to count clicks.")
        self.start_time = time.time()
        self.listener.start()

    def end_task(self):
        self.running = False  # Stop counting clicks
        self.listener.stop()  # Stop the listener
        self.time_taken = time.time() - self.start_time
        return self.click_count, self.time_taken

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

click_count, time_taken = click_counter.end_task()
print("Task Completed!")
print(f"Number of Clicks: {click_count}")
print(f"Task Completion Time: {time_taken} seconds")