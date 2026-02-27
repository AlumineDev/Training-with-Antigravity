import csv

# --- ANTIGRAVITY ACADEMY: LESSON 4 ---
# Concept: External Data (CSV) + ALL PREVIOUS KNOWLEDGE

# ==========================================================
# 📐 TASK 1: THE BRAIN (Functions & Math)
# ==========================================================
def calculate_net_with_bonus(salary, branch):
    # ==========================================================
    # 🏁 STYLE 1: THE "SPECIFIC" METHOD (Your initial approach)
    # Use this if every branch has a COMPLETELY different rule.
    # ==========================================================
    if branch == 'A':
        bonus = 200
        tax = (salary + bonus) * 0.20 # Specific tax calculation for A
    elif branch == 'B':
        bonus = 500
        tax = (salary + bonus) * 0.20 # Specific tax calculation for B
    else:
        bonus = 0
        tax = salary * 0.20
    
    net_specific = (salary + bonus) - tax
    
    # ==========================================================
    # 🏁 STYLE 2: THE "GLOBAL" METHOD (The Optimized approach)
    # Use this if parts of the math are the same for everyone.
    # ==========================================================
    # 1. First, handle ONLY the things that change (the bonus)
    if branch == 'A':
        current_bonus = 200
    elif branch == 'B':
        current_bonus = 500
    else:
        current_bonus = 0
    
    # 2. Then, handle the things that are the SAME (the 20% tax)
    # We do this math once, at the very end.
    total_gross = salary + current_bonus
    net_global = total_gross * 0.80 # 0.80 means "Keep 80% / Lose 20%"
    
    # --- TEACHER NOTE ---
    # Both 'net_specific' and 'net_global' give the SAME result ($3360 for 4000).
    # Style 1 is better for complex, different rules.
    # Style 2 is better for clean, professional code.
    
    return net_global # We return this one for our reports!

# ==========================================================
# 📂 TASK 2: THE DATA COLLECTOR (Lists & File Reading)
# ==========================================================
def read_and_process_file(filename):
    grand_total_net = 0 #this is the piggy bank
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
                net = calculate_net_with_bonus(gross, branch) # Replace with function call
                
                # B. Accumulate into 'grand_total_net'
                grand_total_net += net
                # C. IF/ELSE: If net > 5000, add their NAME to the 'high_earners' list
                if net > 5000:
                    high_earners.append(name)
                
                print(f"Processed: {name} | Net: ${net:.2f}")

    except Exception as e:
        print(f"Error: {e}")

    # TASK 4: REPORTING
    print("-" * 40)
    print(f"[REPORT] GRAND TOTAL PAYROLL: ${grand_total_net:.2f}")
    print(f"[ALERTS] HIGH EARNERS LIST: {high_earners}")

# --- START THE SYSTEM ---
read_and_process_file('employees.csv')

# MISSION:
# 1. Complete Task 1 (Function with logic).
# 2. Complete Task 3 (Loop, function usage, accumulation, and if/else list building).
# This uses EVERY skill you have, plus the new 'csv' skill!
