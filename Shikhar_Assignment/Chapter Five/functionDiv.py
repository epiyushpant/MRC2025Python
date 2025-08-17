def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def analyze_age(age):
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"

def display_result(name, category):
    print(f"{name} is a {category}")

# Main program
def main():
    name, age = get_user_data()
    category = analyze_age(age)
    display_result(name, category)

if __name__ == "__main__":
    main()