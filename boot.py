from kernel import *

def loading_animation(duration):
    logger.info("START Boot process...")
    clear()
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in ['|', '/', '-', '\\']:
            sys.stdout.write('\rLoading ' + symbol)
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write('\rLoading complete!       \n')

def main():
    print("Initializing boot process...")
    time.sleep(1)  # Simulate some initialization delay
    loading_animation(5)  # Set loading duration to 5 seconds
    password_check()
    

if __name__ == "__main__":
    main()