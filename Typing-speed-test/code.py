import time

def typing_speed_test(passage):
    print(passage)
    input("Press Enter when ready...")
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    total_time = end_time - start_time
    words = len(user_input.split())
    speed = words / total_time * 60  # Words per minute

    print(f"You typed {words} words in {total_time:.2f} seconds.")
    print(f"Your typing speed is {speed:.2f} words per minute.")

passage = "The quick brown fox jumps over the lazy dog."
typing_speed_test(passage)