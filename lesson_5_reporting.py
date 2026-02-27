import csv

# --- ANTIGRAVITY ACADEMY: LESSON 5 ---
# Concept: Output Reporting (Writing Files) + TOTAL INTEGRATION

# 📐 TASK 1: THE ENGINE (Reusing our Logic)
def calculate_net(salary, branch):
    bonus = 500 if branch == 'B' else 200
    return (salary + bonus) * 0.80
    # I saw this method it is a shortcut to write the code in one line
    # It is called a ternary operator
    # The code is like this: variable = value_if_true if condition else value_if_false
    # In this case, if the branch is 'B', the bonus is 500, otherwise the bonus is 200
    # Then, the net salary is calculated by adding the bonus to the salary and multiplying by 0.80

# 📂 TASK 2: THE PROCESSOR
def generate_payroll_report(input_csv, output_report):
    print(f"[SYSTEM] Reading from {input_csv} and creating {output_report}...")
    
    total_net_payout = 0
    
    try:
        # A. We open the INPUT to read and the OUTPUT to write!
        with open(input_csv, mode='r') as infile, open(output_report, mode='w') as outfile:
            reader = csv.DictReader(infile)
            
            # Writing the Header of our new text report
            outfile.write("========================================\n")
            outfile.write("   ANTIGRAVITY OFFICIAL PAYROLL REPORT  \n")
            outfile.write("========================================\n\n")
            
            # TASK 3: THE LOOP & INTEGRATION
            for row in reader:
                name = row['Name']
                net_salary = calculate_net(float(row['Salary']), row['Branch'])
                total_net_payout += net_salary
                
                # MISSION: Write each employee's data to the file
                # Use outfile.write(f"TEXT HERE\n")
                line = f"PAYEE: {name:15} | NET REMITTANCE: ${net_salary:,.2f}\n"
                outfile.write(line)
            
            # TASK 4: THE GRAND TOTAL
            outfile.write("\n" + "-"*40 + "\n")
            # MISSION: Write the Final Total variable at the bottom of the file
            # (Your code here)
            outfile.write(f"TOTAL COMPANY OUTFLOW: ${total_net_payout}\n") # REPLACE THE 0!
            outfile.write("-"*40 + "\n")
            
        print("[SUCCESS] Report generated successfully!")

    except Exception as e:
        print(f"[ERROR] Could not generate report: {e}")

# --- START ---
generate_payroll_report('employees.csv', 'final_payroll_report.txt')

# CHALLENGE:
# 1. Complete Task 4 to write the 'total_net_payout' to the bottom of the file.
# 2. Run the code and then OPEN 'final_payroll_report.txt' in your editor to see your work!
