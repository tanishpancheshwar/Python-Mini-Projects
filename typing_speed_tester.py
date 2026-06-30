import time
import random
from tkinter.filedialog import test

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",    
]

def accuracy_test(sentence, user_input):
    correct_chars = sum(1 for a, b in zip(sentence, user_input) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100 if sentence else 0
    return accuracy

def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)
    #start after user presses enter
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("Your input: \n")
    end_time = time.time()
    
    total_time = end_time - start_time
    words = sentence.split(" ")
    speed = len(words) / (total_time / 60)  # words per minute
    accuracy = accuracy_test(sentence, user_input)

    print(f"Results:")
    print(f"Time taken: {total_time:.2f} seconds")
    print(f"Words per minute: {speed:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

typing_test() 