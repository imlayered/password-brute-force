import itertools
import string
import time
import psutil  # pip install psutil 

chars = string.ascii_letters + string.digits

def check_system_resources():
    if psutil.cpu_percent() > 100 or psutil.virtual_memory().percent > 95:
        print("ERR: Your machine has reached its limits! We've stopped the program to prevent a crash or blue screen!")
        print("You can disable this by removing between where it says #START ANTICRASH and #END ANTICRASH")
        exit()

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def read_password_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

def try_passwords_from_list(word_list, attempt_count, description, start_time):
    total_words = len(word_list)
    for index, word in enumerate(word_list, start=1):
        # START ANTICRASH
        check_system_resources()
        # END ANTICRASH
        elapsed_time = time.time() - start_time
        list_percentage = (index / total_words) * 100
        print(f"Trying: {word:<20} ({description} ({list_percentage:.0f}% read) | Elapsed Time: {elapsed_time:.2f}s  | Total Attempts: {attempt_count})")
        attempt_count += 1
        if word == password:
            return word, attempt_count, description
    return None, attempt_count, description

def brute_force(attempt_count, start_time):
    for length in range(1, 180):  
        for guess in itertools.product(chars, repeat=length):
            # START ANTICRASH
            check_system_resources()
            # END ANTICRASH
            guess = ''.join(guess)
            elapsed_time = time.time() - start_time
            print(f"Trying: {guess:<20} (brute force | Elapsed Time: {elapsed_time:.2f}s  | Total Attempts: {attempt_count})")
            attempt_count += 1
            if guess == password:
                return guess, attempt_count, "brute force"
    return None, attempt_count, "brute force"

try:
    password = read_password_from_file("result.txt")

    attempt_count = 0
    start_time = time.time()

    english_words = read_words_from_file("english.txt")
    brand_names = read_words_from_file("brands.txt")
    common_passwords = read_words_from_file("passwords.txt")

    guessed_password, method = None, ""
    file_descriptions = [("Common passwords", common_passwords), ("English words", english_words), ("Brand names", brand_names)]
    for description, word_list in file_descriptions:
        guessed_password, attempt_count, method = try_passwords_from_list(word_list, attempt_count, description, start_time)
        if guessed_password:
            break
        print(f"Finished checking {description}, moving to the next step...")
        time.sleep(1) 

    end_time = time.time()
    total_time = end_time - start_time

    if guessed_password:
        print(f"Password guessed: {guessed_password} (found in {method})")
    else:
        print("Password not found in logged data. See v1 console as it is brute forcing.")
    print(f"Total passwords tried: {attempt_count}")
    print(f"Time taken: {total_time:.2f} seconds")

except KeyboardInterrupt:
    print("\nQuitting... Software by Layered (bagel.land)")

#
#  _                               _ 
# | |                             | |
# | | __ _ _   _  ___ _ __ ___  __| |
# | |/ _` | | | |/ _ \ '__/ _ \/ _` |
# | | (_| | |_| |  __/ | |  __/ (_| |
# |_|\__,_|\__, |\___|_|  \___|\__,_|
#           __/ |                    
#          |___/                     Developed on January 2nd, 2023. See GitHub for updates. Please leave this credit in <3