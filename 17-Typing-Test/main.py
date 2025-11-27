import time

text = "The quick brown fox jumps over the lazy dog"
print("Type this sentence as fast as you can:")
print(f"'{text}'")

input("Press Enter to start...")
start = time.time()
user_input = input("\nType here: ")
end = time.time()

if user_input == text:
    print(f"\nTime: {end - start:.2f} seconds")
else:
    print("\nMistake made!")