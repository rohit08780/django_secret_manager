import hashlib
import json
import os

SECRETS_FILE = "secrets_store.json"

def load_secrets():
    if os.path.exists(SECRETS_FILE):
        with open(SECRETS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_secrets(secrets):
    with open(SECRETS_FILE, "w") as file:
        json.dump(secrets, file)

def hash_secret(secret):
    return hashlib.sha256(secret.encode()).hexdigest()

def add_secret(key_name, secret_value):
    secrets = load_secrets()
    if key_name in secrets:
        print("Key already exists.")
        return
    secrets[key_name] = hash_secret(secret_value)
    save_secrets(secrets)
    print(f" Secret stored securely for key: {key_name}")

def retrieve_secret(key_name, secret_guess):
    secrets = load_secrets()
    if key_name not in secrets:
        print(" Key not found.")
        return
    if hash_secret(secret_guess) == secrets[key_name]:
        print(f" Secret for '{key_name}' verified successfully.")
    else:
        print(" Secret mismatch. Unauthorized access!")

def list_keys():
    secrets = load_secrets()
    if not secrets:
        print(" No secrets stored yet.")
    else:
        print(" Stored Secret Keys:")
        for key in secrets:
            print(f" - {key}")

def menu():
    while True:
        print("\n Secret Manager CLI")
        print("1. Add Secret")
        print("2. Retrieve/Verify Secret")
        print("3. List Secret Keys")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key name: ")
            value = input("Enter secret value: ")
            add_secret(key, value)
        elif choice == "2":
            key = input("Enter key name: ")
            value = input("Enter secret value to verify: ")
            retrieve_secret(key, value)
        elif choice == "3":
            list_keys()
        elif choice == "4":
            print(" Exiting...")
            break
        else:
            print(" Invalid choice!")

if __name__ == "__main__":
    menu()
