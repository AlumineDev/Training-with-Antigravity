# --- ANTIGRAVITY ACADEMY: PHASE 1 FINAL EXAM ---
# This challenge combines: Variables, Math, Lists, Loops, If/Else, and Functions.

# --- YOUR TOOLS (FUNCTIONS) ---

# TASK 1: Complete this function
    
def process_payout(salary):
    """
    If salary is >= 5000, apply 30% tax (0.30)
    If salary is < 5000, apply 15% tax (0.15)
    Return the NET salary
    """
    # Write your logic here!
    if salary >= 5000:
        tax = salary * 0.30
        net = salary - tax
    else:
        tax = salary * 0.15
        net = salary - tax
    return net

# --- THE DATA ---
branch_a = [4200, 5500, 3100, 7200, 1500]
branch_b = [2800, 6100, 4900, 8000, 2200]

# --- THE ENGINE ---

def run_payroll_system(department_name, salary_list):
    print(f"\n[SYSTEM] Processing Branch: {department_name}")
    print("-" * 30)
    
    # TASK 2: Initialize your "Piggy Bank" (Bucket) here
    department_total_net = 0
    # TASK 3: Loop through the 'salary_list'
    for i, salary in enumerate(salary_list):
        net_salary = process_payout(salary)
        department_total_net += net_salary
        # This print is now inside the loop so we see every employee!
        print(f"ID {i+1}: Net ${net_salary:.2f}")

    print("-" * 30)
    print(f"BALANCE: Branch {department_name} Total Net: ${department_total_net}")
    return department_total_net

# --- THE GRAND FINALE ---

# TASK 4: Run the system for both branches and calculate the FINAL total.
# (Hint: use the 'run_payroll_system' function)
total_a = run_payroll_system("Branch A", branch_a)  
total_b = run_payroll_system("Branch B", branch_b)
final_total = total_a + total_b # Replace with your math!   

print(f"\n========================================")
print(f"GRAND TOTAL: ANTIGRAVITY GLOBAL PAYROLL TOTAL: ${final_total}")
print(f"========================================")

# MISSION:
# Complete all 4 Tasks, save the file, and run it. 
# If you get it right, you have graduated from Phase 1!
