from utils.password import (
    hash_password,
    verify_password
)

password = "Aman@123"

hashed = hash_password(password)

print("Original Password:")
print(password)

print()

print("Hashed Password:")
print(hashed)

print()

print("Password Verified:")
print(
    verify_password(
        password,
        hashed
    )
)