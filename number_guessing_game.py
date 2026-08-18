import random

print("--- नंबर गेसिंग गेम में आपका स्वागत है! ---")
secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("1 से 50 के बीच एक नंबर का अंदाज़ा लगाओ: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        print(f"बधाई हो! आपने {attempts} बार में सही नंबर ढूंढ लिया! 🎉")
        break
    elif guess < secret_number:
        print("थोड़ा बड़ा नंबर सोचो! ⬆️")
    else:
        print("थोड़ा छोटा नंबर सोचो! ⬇️")
      
