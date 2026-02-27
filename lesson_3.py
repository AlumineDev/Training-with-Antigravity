# --- ANTIGRAVITY ACADEMY: LESSON 3 ---
# Concept: Functions (The "Reusable Recipes")

# A FUNCTION is like a custom tool. 
# It's an "Engine" that takes an INPUT and gives an OUTPUT.

def calculate_net_salary(gross):
    """
    This function takes a gross salary and calculates the net (after 20% tax).
    """
    tax = gross * 0.20
    net = gross - tax
    
    # MISSION: You need to "deliver" the result.
    # When you call a function, it does the work, but you need to tell it 
    # which variable to "return" to the main program.
    
    return net # <--- REPLACE THIS 0 WITH THE VARIABLE YOU WANT TO SEND BACK!

# --- USING OUR CUSTOM TOOL ---

print("--- PAYROLL REPORT ---")

# Department A
marketing_salaries = [2000, 2500, 3000]
for s in marketing_salaries:
    # We "Call" our function here!
    result = calculate_net_salary(s)
    print(f"Marketing Net: ${result}")

print(f"Total salaries department A: ${sum(marketing_salaries)}") # This is the sum of all salaries in the marketing department.

# Department B
it_salaries = [4500, 5000, 6000]
for s in it_salaries:
    # We reuse the EXACT SAME logic without re-writing the math!
    result = calculate_net_salary(s)
    print(f"IT Net: ${result}")

print(f"Total salaries department B: ${sum(it_salaries)}") # This is the sum of all salaries in the IT department.

print(f"Total Payroll: ${sum(marketing_salaries) + sum(it_salaries)}") # Also we make this, the sum of all salaries, so we take the first list and the second list and we sum them.
# 1. Fix the 'return' statement in the function.
# 2. Save and tell me "Done!".
