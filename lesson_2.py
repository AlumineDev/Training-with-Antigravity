# --- ANTIGRAVITY ACADEMY: LESSON 2 ---
# Concept: Lists and Loops

# 1. This is a LIST of monthly salaries
monthly_salaries = [2500, 3100, 1800, 4200, 2900]
tax_percentage = 0.20

print("--- PAYROLL REPORT ---")

# 2. CHALLENGE: Use a 'for' loop to process Every item in the list
# We want to print the Net Salary for each person automatically.

# I've started the loop for you:
for salary in monthly_salaries:
    # A. Calculate the net for this specific 'salary' inside the loop
    # (Hint: Use the same math from Lesson 1)
    net = salary - (salary * tax_percentage)
    
    # B. MISSION: Print the net salary for this person.
    # Replace the underscore (_) below with the correct variable name!
    print(f"Employee Net Salary: ${ net }")


# 3. ADVANCED CHALLENGE (Bonus):
# Can you think of how we could sum ALL the net salaries together?
print("\n--- ADVANCED CHALLENGE ---")
print("This is the sum of all net salaries:")
print (f"sum of all net salaries: ${sum(monthly_salaries)}")
# This is the sum of all net salaries.
print("\n--- ADVANCED CHALLENGE this is my solution ---")
print("This is the sum of all net salaries after applying 20% tax:")
print(f"Appling 20% tax to all salaries: ${sum(monthly_salaries) * tax_percentage}")




# Don't worry about it yet if you're not sure, let's finish the loop first!
