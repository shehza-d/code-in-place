import random

def main():
    print("Khansole Academy")
    
	random_num_1 = random.randint(10, 99)
    random_num_2 = random.randint(10, 99)
    
	print("What is ", random_num_1," + ", random_num_2,"?")
    
	user_ans = int(input("Your answer: "))
    total = random_num_1 + random_num_2
    
	if user_ans == total:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is ", total)
    
    
if __name__ == '__main__':
    main()