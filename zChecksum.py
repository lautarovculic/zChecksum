# Lautaro Daniel Villarreal Culic'
# https://lautarovculic.com

# ver 4.0

# REQUIRE INSTALL COLORAMA & HASHLIB WITH:
#pip install hashlib
#pip install colorama

import sys
import hashlib
from colorama import init, Fore

init(autoreset=True)

def calculate_hash(file_name, algorithm):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()

            hash_object = hashlib.new(algorithm)
            hash_object.update(data)
            hash_checksum = hash_object.hexdigest()

            return hash_checksum
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except PermissionError:
        print(f"You don't have permission to access the file '{file_name}'.")

def calculate_hashes(file_name, algorithms):
    hashes = {}
    for algorithm in algorithms:
        hash_checksum = calculate_hash(file_name, algorithm)
        hashes[algorithm] = hash_checksum

    return hashes

def identify_hash_type(provided_hash, algorithms):
    for algorithm in algorithms:
        hash_object = hashlib.new(algorithm)
        if len(provided_hash) == hash_object.digest_size * 2:
            return algorithm
    return None

def main():
    algorithms = [
        'sha1', 'blake2b', 'sha3_256', 'sha384', 'sha224', 'md5', 'sha512',
        'sha3_384', 'sha3_512', 'sha3_224', 'blake2s', 'sha256'
    ]

    if len(sys.argv) >= 2:
        file = sys.argv[1]
        provided_hash = None
        if len(sys.argv) >= 3:
            provided_hash = sys.argv[2]
        
        print(f"Lautaro Villarreal Culic' - {Fore.BLUE}https://lautarovculic.com{Fore.RESET} - zChecksum v4.0")
        print(f"The hashes for {file} are:")
        hashes = calculate_hashes(file, algorithms)

        match_found = False
        for algorithm, checksum in hashes.items():
            colored_algorithm = f"{Fore.YELLOW}{algorithm}{Fore.RESET}"
            colored_separator = f"{Fore.YELLOW}: {Fore.RESET}"
            if provided_hash and checksum == provided_hash:
                checksum = f"{Fore.GREEN}{checksum}{Fore.RESET}"
                match_found = True
            print(f"{colored_algorithm}{colored_separator}{checksum}")

        if provided_hash:
            colored_provided_hash = f"{Fore.RED}{provided_hash}{Fore.RESET}"
            hash_type = identify_hash_type(provided_hash, algorithms)
            if hash_type:
                colored_hash_type = f"{Fore.YELLOW}{hash_type}{Fore.RESET}"
                print(f"The provided hash is of type {colored_hash_type}. Hash: {colored_provided_hash}")
                if not match_found:
                    print("The provided hash does not match any calculated hashes.")
            else:
                print(f"The provided hash does not match any calculated hashes. Hash: {colored_provided_hash}")
    else:
        print("Usage: zChecksum.py <file_name> [hash]")

if __name__ == "__main__":
    main()