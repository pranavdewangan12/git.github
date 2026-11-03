# 💼 Advanced Employee Salary Management System (Employee Salary Calculator)

![Python](https://img.shields.io/badge/Language-Python_3-blue.svg)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-green.svg)
![University](https://img.shields.io/badge/University-Rungta_International_Skills_University-red.svg)

A professional, console-based Python application designed to calculate employee net salaries from basic pay, allowances, role-based bonuses, and deductions, while maintaining an interactive in-memory database (CRUD) of payroll records.

---

## 👨‍💻 Author & Academic Details

* **Name:** Pranav Dewangan
* **ERP ID:** RU-26-02469
* **Email:** [pranav.dewangan@rungta.org](mailto:pranav.dewangan@rungta.org)
* **Section:** 1M
* **Course & Semester:** Bachelor of Technology (B.Tech) in Computer Science and Engineering (1st Semester)
* **Institute:** School of Computer Science and Engineering, Rungta International Skills University, Bhilai

---

## 📋 Problem Statement & University Specifications

* **PS No.:** 3
* **Project Title:** Employee Salary Calculator
* **Problem Statement:** Create a program that calculates an employee's net salary from basic pay, allowances (HRA, DA) and deductions (PF, tax) and prints a salary slip.
* **Language:** Python 3
* **Core Concepts Used:** Functions, Operators, Conditions, Loops, Exception Handling, and Object-Oriented Programming (OOP).
* **Calculation Note:** HRA $20\%$ and DA $10\%$ of basic; PF $12\%$ of basic. Tax on gross: up to $25000$ none, $25001$–$50000$ is $5\%$, above $50000$ is $10\%$.

### 🎯 Bare Minimum Requirements
1. Write the solution in Python 3 and run it from the console.
2. Take employee name, ID, and basic salary as input.
3. Calculate HRA, DA, PF, and tax using operators and conditions.
4. Create modular functions/methods to calculate gross salary and print the salary slip.
5. Print a neat salary slip and allow adding more employees using a loop.

### 📝 Project Instructions Followed
1. Understand the problem statement and define the problem clearly.
2. Develop the solution using proper logic and programming concepts.
3. Implement all required features and pass the given test cases.
4. Test and debug the project to ensure correct output.
5. Prepare the documentation/report and upload the code and report to GitHub.
6. Complete and submit the project within the given deadline.

---

## 🚀 Additional "Pro" Features Implemented

Beyond the bare minimum requirements, this project includes several advanced features built using **100% Core Python** (no external dependencies required):

1. **Object-Oriented Architecture (OOP):** Encapsulates data and behaviors cleanly into dedicated classes (`Colors`, `Employee`, `SalaryManagementSystem`).
2. **Colored Terminal UI:** Uses native ANSI escape sequences to color-code headers, success messages, warnings, and errors for a modern CLI experience.
3. **Designation-Based Bonus Logic:** Automatically awards a role-specific bonus based on the employee's designation:
   * **Manager:** ₹$10,000$
   * **SDE:** ₹$5,000$
   * **Intern:** ₹$1,000$
   * **Other:** ₹$0$ *(Used for standard baseline test cases)*
4. **In-Memory CRUD Operations:** Maintains a session history using Python lists, allowing users to **View** tabular audit reports, **Search** by Employee ID, **Filter** by minimum net salary, and **Delete** records dynamically.
5. **Robust Error Handling:** Utilizes `try-except` blocks and input validation loops to prevent crashes from non-numeric inputs, empty strings, or negative salary values.

---

## 🧮 Mathematical Payroll Formulas

The payroll engine computes the salary components in the following sequence:

1. **House Rent Allowance (HRA):**
   HRA= Basic Salary times 0.20

2. **Dearness Allowance (DA):**
   $$\text{DA} = \text{Basic Salary} \times 0.10$$

3. **Role Bonus:**
   $$\text{Bonus} = \begin{cases} 10000 & \text{if Designation is Manager} \\ 5000 & \text{if Designation is SDE} \\ 1000 & \text{if Designation is Intern} \\ 0 & \text{if Designation is Other} \end{cases}$$

4. **Gross Salary:**
   $$\text{Gross Salary} = \text{Basic Salary} + \text{HRA} + \text{DA} + \text{Bonus}$$

5. **Provident Fund (PF):**
   $$\text{PF} = \text{Basic Salary} \times 0.12$$

6. **Income Tax (Based on Gross Salary Slabs):**
   Tax = cases 0 & if Gross Salary  25000 Gross Salary 0.05 & if  25000 < Gross Salary 50000 Gross Salary times 0.10 & if Gross Salary > 50000 cases

7. **Net Salary (Take-Home Pay):**
   $$\text{Net Salary} = \text{Gross Salary} - (\text{PF} + \text{Tax})$$

---

## 🔄 Flow of the Program

The execution flow of the application follows a structured lifecycle:

```text
[Start Program]
       │
       ▼
[Instantiate SalaryManagementSystem] ──► Initializes empty `history` list
       │
       ▼
[Display Main Menu (Infinite Loop)]
       │
       ├─► Option 1: Process New Salary
       │     ├─► Prompt for ID, Name, Designation, Basic Salary
       │     ├─► Validate inputs (Non-empty, Basic Salary >= 0, Numeric check)
       │     ├─► Create `Employee` object & call `compute_payroll()`
       │     ├─► Call `display_salary_slip()` & append object to `history`
       │     └─► Ask to process another employee (Loop or return to Menu)
       │
       ├─► Option 2: View All Stored Records
       │     └─► Iterate through `history` and print formatted tabular report
       │
       ├─► Option 3: Search Employee by ID
       │     └─► Filter `history` by matching `emp_id` and display full slip
       │
       ├─► Option 4: Filter by Minimum Net Salary
       │     └─► Prompt for threshold, filter `history` where `net_salary >= min_sal`
       │
       ├─► Option 5: Delete an Employee Record
       │     └─► Locate record by `emp_id` and remove from `history` using `del`
       │
       └─► Option 6: Terminate Program
             └─► Break main loop ──► [End Program]
```

---

## 🔍 Detailed Code & Function Explanation

The codebase is modularized into three main classes. Below is a complete breakdown of every class and method:

### 1. `class Colors`
A utility class that stores standard ANSI escape sequences as class attributes (`HEADER`, `CYAN`, `GREEN`, `WARNING`, `FAIL`, `BOLD`, `RESET`). These are interpolated into `f-strings` to render colored text in the console without needing third-party packages like `colorama`.

### 2. `class Employee`
Represents an individual employee entity and encapsulates all data and logic related to their personal salary slip.

* **`__init__(self, emp_id: str, emp_name: str, designation: str, basic_salary: float) -> None`**
  * **Purpose:** The class constructor that initializes a new employee object.
  * **Working:** Stores the passed `emp_id`, `emp_name`, `designation` (formatted to Title Case using `.title()`), and `basic_salary`. It also initializes all calculated financial attributes (`hra`, `da`, `bonus`, `gross_salary`, `pf`, `tax`, `net_salary`) to `0.0`.
* **`compute_payroll(self) -> None`**
  * **Purpose:** Executes the core mathematical calculations for the employee's payroll.
  * **Working:** Calculates `hra` ($20\%$) and `da` ($10\%$). Evaluates `self.designation` using `if-elif-else` conditions to assign the role bonus. Computes `gross_salary`, calculates `pf` ($12\%$ of basic), applies conditional slab logic to determine `tax`, and finally computes `net_salary`.
* **`display_salary_slip(self) -> None`**
  * **Purpose:** Prints an itemized, visually formatted official salary statement to the terminal.
  * **Working:** Uses Python string alignment (`:^60`), thousand-separator formatting (`:,.2f`), and `Colors` attributes to clearly separate earnings (marked with green `(+)`) and deductions (marked with red `(-)`).

### 3. `class SalaryManagementSystem`
Acts as the controller for the application, managing the interactive CLI menu, user input validation, and the historical list of processed employees.

* **`__init__(self) -> None`**
  * **Purpose:** Initializes the management system.
  * **Working:** Creates an empty list `self.history: list[Employee] = []` to store `Employee` objects during the active session.
* **`run(self) -> None`**
  * **Purpose:** Launches the main interactive control loop.
  * **Working:** Runs a `while True` loop that displays the 6-option main menu, captures the user's choice, and routes execution to the corresponding helper method. Exits cleanly via `break` when Option `6` is chosen.
* **`_handle_salary_processing(self) -> None`**
  * **Purpose:** Handles Option 1 (Data Entry, Validation, Calculation, and Logging).
  * **Working:** Uses a `while True` loop wrapped in a `try-except` block. It checks that `emp_id` and `emp_name` are not empty, defaults empty designations to `"Other"`, and verifies that `basic_salary` is a valid non-negative `float`. It instantiates an `Employee`, triggers payroll computation and slip printing, appends the object to `self.history`, and prompts the user if they want to add another employee immediately.
* **`_display_history_report(self, records=None) -> None`**
  * **Purpose:** Handles Option 2 (and assists Option 4) by rendering a tabular summary of stored employee records.
  * **Working:** Accepts an optional `records` parameter (defaults to `self.history`). If empty, it prints a warning notice. Otherwise, it prints a neatly aligned table displaying `Emp ID`, `Name`, `Role`, `Gross (₹)`, and `Net (₹)` for every record.
* **`_search_employee(self) -> None`**
  * **Purpose:** Handles Option 3 (Read/Search operation by ID).
  * **Working:** Prompts for an Employee ID and uses a list comprehension `[emp for emp in self.history if emp.emp_id == search_id]` to find matches. If found, it invokes `display_salary_slip()` on the matched employee object; otherwise, it displays a `[Not Found]` message.
* **`_filter_employees(self) -> None`**
  * **Purpose:** Handles Option 4 (Filter records by minimum Net Salary).
  * **Working:** Prompts for a numeric salary threshold inside a `try-except` block. Uses list comprehension to filter employees whose `net_salary` is greater than or equal to the threshold, and passes that filtered list to `_display_history_report()`.
* **`_delete_employee(self) -> None`**
  * **Purpose:** Handles Option 5 (Delete operation by ID).
  * **Working:** Prompts for an Employee ID to delete. Iterates through `self.history` using `enumerate()`. When a matching `emp_id` is found, it removes the object from the list using `del self.history[i]` and returns a success message.

---

## 🧪 Test Cases & Verification

> **💡 Note on Test Cases:** To test the standard university test cases without adding the extra Role Bonus, select **`Other`** (or press `Enter` to leave blank) when prompted for the Designation. This sets the Role Bonus to ₹$0.00$, matching the exact baseline formulas in the problem statement.

### Standard University Test Cases

| Test Case | Scenario | Input (Basic Salary) | Expected Output | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Test Case 1** | Normal Input ($5\%$ Tax Slab) | `30000` | **HRA:** $6000$ \| **DA:** $3000$ \| **Gross:** $39000$<br>**PF:** $3600$ \| **Tax:** $1950$ \| **Net Salary:** $33450$ | ✅ Passed |
| **Test Case 2** | Boundary / Minimum Input ($0\%$ Tax Slab) | `10000` | **HRA:** $2000$ \| **DA:** $1000$ \| **Gross:** $13000$<br>**PF:** $1200$ \| **Tax:** $0$ \| **Net Salary:** $11800$ | ✅ Passed |
| **Test Case 3** | Invalid Input (Negative & String) | `-5000`, then `abc` | `[Error] Invalid salary amount. Must be a positive number.`<br>`[Error] Invalid format. Please input numeric values for salary fields.` | ✅ Passed |
| **Test Case 4** | Different Valid Scenario ($10\%$ Tax Slab) | `50000` | **HRA:** $10000$ \| **DA:** $5000$ \| **Gross:** $65000$<br>**PF:** $6000$ \| **Tax:** $6500$ \| **Net Salary:** $52500$ | ✅ Passed |

### Sample Console Output (Test Case 1)

```text
Enter Employee ID: EMP101
Enter Employee Name: Pranav Dewangan
Available Designations: Manager, SDE, Intern, Other
Enter Designation: Other
Enter Basic Salary (₹): 30000

============================================================
                 OFFICIAL SALARY STATEMENT                  
============================================================
Employee ID    : EMP101
Employee Name  : Pranav Dewangan
Designation    : Other
------------------------------------------------------------
Basic Salary   : ₹ 30,000.00
HRA (20%)      : ₹ 6,000.00
DA (10%)       : ₹ 3,000.00
Role Bonus     : ₹ 0.00 (+)
Gross Salary   : ₹ 39,000.00
------------------------------------------------------------
PF (12%)       : ₹ 3,600.00 (-)
Income Tax     : ₹ 1,950.00 (-)
------------------------------------------------------------
Net Salary     : ₹ 33,450.00
============================================================
```

---

## 💻 How to Run the Program

1. **Prerequisites:** Ensure you have **Python 3.x** installed on your system.
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. **Run the Script:**
   ```bash
   python "Employee Salary Calculator.py"
   ```

---
*Developed with ❤️ by **Pranav Dewangan (RU-26-02469)** — Rungta International Skills University.*
