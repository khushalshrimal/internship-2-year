import csv

# Open CSV file in write mode
with open("address_book.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Column names
    writer.writerow(["Name", "Address", "Mobile", "Email"])

    # Taking input from user
    for i in range(3):

        print(f"\nEnter details for Person {i+1}")

        name = input("Enter Name: ")
        address = input("Enter Address: ")
        mobile = input("Enter Mobile: ")
        email = input("Enter Email: ")

        # Writing data into CSV file
        writer.writerow([name, address, mobile, email])

print("\nData inserted successfully into address_book.csv")