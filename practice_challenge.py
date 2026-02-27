# --- ANTIGRAVITY ACADEMY: PRACTICE CHALLENGE ---
# Concept: Combining Everything + Logic (IF statements)

# 1. Our Data
salaries = [1500, 2500, 1900, 3200, 1700]
total_with_bonuses = 0

print("--- PAYROLL WITH BONUSES ---")

# 2. THE LOOP
# This loop takes one item from 'salaries' and calls it 'salariesbase'
for salariesbase in salaries:
    
    # Starting point for this specific employee
    final_salary = salariesbase 
    
    # LOGIC: Check for bonus
    if salariesbase < 2000:
        # If true, add the bonus
        final_salary = salariesbase + 500
        print(f"Salary ${salariesbase} gets a bonus! New total: ${final_salary}")
    else:
        # If false, just keep it the same
        print(f"Salary ${salariesbase} stays the same: ${final_salary}")
    
    # ACCUMULATION: Add this employee's final result to our "grand total"
    # We must do this INSIDE the loop so it happens for everyone.
    total_with_bonuses = total_with_bonuses + final_salary 
for specificsalarie in salaries:
    print(salaries[0])
    print(salaries[1])
    print(salaries[2])
    print(salaries[3])
    print(salaries[4])
    if specificsalarie >= 3000:
        best_salarie = specificsalarie
        print(f"{best_salarie} This is the best salary")
    else:
        print(f"{specificsalaries} This is not the best salary")
        


# 3. FINAL RESULT
# This is OUTSIDE the loop (no indentation) so it only prints once at the end.
print("-" * 30)
print(f"FINAL TOTAL COST FOR COMPANY: ${total_with_bonuses}")
