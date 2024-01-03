import itertools
import string
import time
import psutil  #  pip install psutil 

chars = string.ascii_letters + string.digits

def check_system_resources():
    if psutil.cpu_percent() > 100 or psutil.virtual_memory().percent > 95:
        print("ERR: Your machine has reached its limits! We've stopped the program to prevent a crash or blue screen!")
        exit()

def read_password_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

# Brute force function
def brute_force(password, start_time):
    attempt_count = 0
    for length in range(1, 180):
        for guess in itertools.product(chars, repeat=length):
            # START ANTICRASH
            check_system_resources()
            # END ANTICRASH
            guess_str = ''.join(guess)
            elapsed_time = time.time() - start_time
            print(f"Trying: {guess_str:<20} | BRUTE FORCE (v1) | Elapsed Time: {elapsed_time:.2f}s | Total Attempts: {attempt_count}")
            attempt_count += 1
            if guess_str == password:
                print(f"Password guessed: {guess_str}")
                return guess_str
    return None

try:
    password = read_password_from_file("result.txt")

    start_time = time.time()

    guessed_password = brute_force(password, start_time)

    if not guessed_password:
        print("Password not guessed")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

except KeyboardInterrupt:
    print("\nQuitting... Software by Layered (bagel.land)")

