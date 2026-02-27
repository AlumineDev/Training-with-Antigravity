import csv

# --- ANTIGRAVITY ACADEMY: LESSON 4 ---
# Concept: External Data (CSV) + ALL PREVIOUS KNOWLEDGE

# ==========================================================
# 📐 TASK 1: THE BRAIN (Functions & Math)
# ==========================================================
def calculate_net_with_bonus(salary, branch):
    """
    Apply the rules we learned:
    - If Branch is 'A', bonus is $200.
    - If Branch is 'B', bonus is $500.
    - Tax is 20% flat.
    - RETURN the final net amount.
    """
    # MISSION: Implement the logic here
    return 0

# ==========================================================
# 📂 TASK 2: THE DATA COLLECTOR (Lists & File Reading)
# ==========================================================
def read_and_process_file(filename):
    grand_total_net = 0
    high_earners = [] # List to store names of people making > 5000 net
    
    print(f"[SYSTEM] Opening file: {filename}")
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # TASK 3: THE LOOP (Processing every row)
            for row in reader:
                name = row['Name']
                gross = float(row['Salary'])
                branch = row['Branch']
                
                # A. Apply your 'calculate_net_with_bonus' function
                net = 0 # Replace with function call
                
                # B. Accumulate into 'grand_total_net'
                
                # C. IF/ELSE: If net > 5000, add their NAME to the 'high_earners' list
                
                print(f"Processed: {name} | Net: ${net:.2f}")

    except Exception as e:
        print(f"Error: {e}")

    # TASK 4: REPORTING
    print("-" * 40)
    print(f"📊 GRAND TOTAL PAYROLL: ${grand_total_net:.2f}")
    print(f"🚀 HIGH EARNERS LIST: {high_earners}")

# --- START THE SYSTEM ---
read_and_process_file('employees.csv')

# MISSION:
# 1. Complete Task 1 (Function with logic).
# 2. Complete Task 3 (Loop, function usage, accumulation, and if/else list building).
# This uses EVERY skill you have, plus the new 'csv' skill!
