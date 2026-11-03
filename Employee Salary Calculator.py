"""
====================================================================
© COPYRIGHT & OWNERSHIP DETAILS
====================================================================
Author / Developer : PRANAV DEWANGAN
Course & Semester  : B.Tech Computer Science and Engineering (1st Semester)
University         : Rungta University, Bhilai
ERP ID             : [Enter your ERP ID here]
Section            : [Enter your Section here]

====================================================================
Project Title: Advanced Employee Salary Management System
Description: A professional Python application featuring OOP, dynamic history, 
             CRUD operations, Designation-based logic, and a Colored UI.

====================================================================
MAIN REQUIRED FEATURES (University Project Specifications):
====================================================================
1. Data Input: Employee ID, Name, Basic Salary.
2. Standard Payroll Calculations: HRA (20%), DA (10%), PF (12%), Tax Slabs.
3. Robust Error Handling: Try-Except blocks for inputs.
4. Object-Oriented Programming (OOP): Class-based architecture.

====================================================================
ADDITIONAL 'PRO' FEATURES ADDED (Using Only Core Python):
====================================================================
1. Colored Terminal UI: Uses basic ANSI string codes for warnings, success, and headers.
2. Designation-Based Bonus: Auto-adds bonus (Manager: ₹10k, SDE: ₹5k, Intern: ₹1k) using if-else.
3. CRUD in History: Search by ID, Filter by Minimum Salary, and Delete Records using standard List operations.
4. Continuous Entry Prompt: Fast-track entry workflow using while loops.
====================================================================
"""

# ANSI Color Codes for Terminal UI (Core Python string formatting, no library needed)
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class Employee:
    """Represents an individual employee and encapsulates payroll computation logic."""
    
    def __init__(self, emp_id: str, emp_name: str, designation: str, basic_salary: float) -> None:
        self.emp_id: str = emp_id
        self.emp_name: str = emp_name
        self.designation: str = designation.title()
        self.basic_salary: float = basic_salary
        self.hra: float = 0.0
        self.da: float = 0.0
        self.bonus: float = 0.0
        self.gross_salary: float = 0.0
        self.pf: float = 0.0
        self.tax: float = 0.0
        self.net_salary: float = 0.0

    def compute_payroll(self) -> None:
        """Executes full payroll calculations including designation bonus."""
        self.hra = self.basic_salary * 0.20
        self.da = self.basic_salary * 0.10
        
        # Designation-based Bonus Logic (Simple if-else)
        if self.designation == "Manager":
            self.bonus = 10000.0
        elif self.designation == "Sde":
            self.designation = "SDE" # Formatting fix
            self.bonus = 5000.0
        elif self.designation == "Intern":
            self.bonus = 1000.0
        else:
            self.bonus = 0.0

        # Gross Salary now includes the Bonus
        self.gross_salary = self.basic_salary + self.hra + self.da + self.bonus
        
        self.pf = self.basic_salary * 0.12
        
        # Tax calculation slabs
        if self.gross_salary <= 25000:
            self.tax = 0.0
        elif self.gross_salary <= 50000:
            self.tax = self.gross_salary * 0.05
        else:
            self.tax = self.gross_salary * 0.10

        self.net_salary = self.gross_salary - (self.pf + self.tax)

    def display_salary_slip(self) -> None:
        """Renders a formally formatted, colorful itemized salary statement."""
        print(f"\n{Colors.CYAN}{Colors.BOLD}" + "=" * 60)
        print(f"{'OFFICIAL SALARY STATEMENT':^60}")
        print("=" * 60 + f"{Colors.RESET}")
        print(f"Employee ID    : {Colors.BOLD}{self.emp_id}{Colors.RESET}")
        print(f"Employee Name  : {Colors.BOLD}{self.emp_name}{Colors.RESET}")
        print(f"Designation    : {self.designation}")
        print("-" * 60)
        print(f"Basic Salary   : ₹ {self.basic_salary:,.2f}")
        print(f"HRA (20%)      : ₹ {self.hra:,.2f}")
        print(f"DA (10%)       : ₹ {self.da:,.2f}")
        print(f"Role Bonus     : ₹ {self.bonus:,.2f} {Colors.GREEN}(+){Colors.RESET}")
        print(f"Gross Salary   : ₹ {self.gross_salary:,.2f}")
        print("-" * 60)
        print(f"PF (12%)       : ₹ {self.pf:,.2f} {Colors.FAIL}(-){Colors.RESET}")
        print(f"Income Tax     : ₹ {self.tax:,.2f} {Colors.FAIL}(-){Colors.RESET}")
        print("-" * 60)
        print(f"{Colors.GREEN}{Colors.BOLD}Net Salary     : ₹ {self.net_salary:,.2f}{Colors.RESET}")
        print(f"{Colors.CYAN}" + "=" * 60 + f"{Colors.RESET}\n")


class SalaryManagementSystem:
    """Manages system execution flow, interactive menus, and audit history using lists."""
    
    def __init__(self) -> None:
        self.history: list[Employee] = []

    def run(self) -> None:
        """Launches the primary interactive control loop for the application."""
        while True:
            print(f"\n{Colors.HEADER}{Colors.BOLD}" + "=" * 60)
            print(f"{'EMPLOYEE SALARY MANAGEMENT SYSTEM':^60}")
            print("=" * 60 + f"{Colors.RESET}")
            print("1. Process & Save New Employee Salary")
            print("2. View All Stored Salary Records")
            print("3. Search Employee by ID")
            print("4. Filter Employees by Minimum Net Salary")
            print("5. Delete an Employee Record")
            print(f"{Colors.FAIL}6. Terminate Program{Colors.RESET}")

            choice = input(f"\n{Colors.BOLD}Enter your option (1-6): {Colors.RESET}").strip()

            if choice == '1':
                self._handle_salary_processing()
            elif choice == '2':
                self._display_history_report()
            elif choice == '3':
                self._search_employee()
            elif choice == '4':
                self._filter_employees()
            elif choice == '5':
                self._delete_employee()
            elif choice == '6':
                print(f"\n{Colors.CYAN}Terminating session. Thank you for using the system!{Colors.RESET}")
                break
            else:
                print(f"\n{Colors.FAIL}[Error] Invalid option selected. Please enter a value between 1 and 6.{Colors.RESET}")

    def _handle_salary_processing(self) -> None:
        """Handles continuous data entry and logs records."""
        while True:
            try:
                emp_id = input(f"\nEnter Employee ID: ").strip()
                if not emp_id:
                    print(f"{Colors.FAIL}[Error] Employee ID cannot be empty.{Colors.RESET}")
                    continue

                emp_name = input("Enter Employee Name: ").strip()
                if not emp_name:
                    print(f"{Colors.FAIL}[Error] Employee Name cannot be empty.{Colors.RESET}")
                    continue
                
                print("Available Designations: Manager, SDE, Intern, Other")
                designation = input("Enter Designation: ").strip()
                if not designation: designation = "Other"

                basic_salary = float(input("Enter Basic Salary (₹): "))
                if basic_salary < 0:
                    print(f"{Colors.FAIL}[Error] Invalid salary amount. Must be a positive number.{Colors.RESET}")
                    continue

                # Compute and Display
                employee = Employee(emp_id, emp_name, designation, basic_salary)
                employee.compute_payroll()
                employee.display_salary_slip()

                # Save to History List
                self.history.append(employee)
                print(f"{Colors.GREEN}[Success] Record successfully logged to session history.{Colors.RESET}")

                cont = input(f"\n{Colors.WARNING}Would you like to process another employee? (yes/no): {Colors.RESET}").strip().lower()
                if cont not in ['yes', 'y']:
                    print("Returning to Main Menu...")
                    break

            except ValueError:
                print(f"{Colors.FAIL}[Error] Invalid format. Please input numeric values for salary fields.{Colors.RESET}")
            except Exception as ex:
                print(f"{Colors.FAIL}[Error] An unexpected exception occurred: {ex}{Colors.RESET}")

    def _display_history_report(self, records=None) -> None:
        """Displays historical records in a structured tabular format using core print formatting."""
        data_to_show = records if records is not None else self.history
        
        if not data_to_show:
            print(f"\n{Colors.WARNING}[Notice] No records found to display.{Colors.RESET}")
            return

        print(f"\n{Colors.HEADER}" + "=" * 85)
        print(f"{'AUDIT REPORT: STORED SALARY RECORDS':^85}")
        print("=" * 85 + f"{Colors.RESET}")
        print(f"{'Emp ID':<8} | {'Name':<15} | {'Role':<10} | {'Gross (₹)':<12} | {'Net (₹)':<12}")
        print("-" * 85)
        for emp in data_to_show:
            print(f"{emp.emp_id:<8} | {emp.emp_name:<15} | {emp.designation:<10} | {emp.gross_salary:<12.2f} | {Colors.GREEN}{emp.net_salary:<12.2f}{Colors.RESET}")
        print(f"{Colors.HEADER}" + "=" * 85 + f"{Colors.RESET}")

    def _search_employee(self) -> None:
        """CRUD - Search employee by ID using basic list comprehension."""
        search_id = input(f"\n{Colors.BOLD}Enter Employee ID to search: {Colors.RESET}").strip()
        found = [emp for emp in self.history if emp.emp_id == search_id]
        if found:
            print(f"\n{Colors.GREEN}[Match Found]{Colors.RESET} Displaying details for ID: {search_id}")
            found[0].display_salary_slip()
        else:
            print(f"{Colors.FAIL}[Not Found] No employee exists with ID: {search_id}{Colors.RESET}")

    def _filter_employees(self) -> None:
        """CRUD - Filter by net salary using basic list comprehension."""
        try:
            min_sal = float(input(f"\n{Colors.BOLD}Enter minimum Net Salary to filter by (₹): {Colors.RESET}"))
            filtered_list = [emp for emp in self.history if emp.net_salary >= min_sal]
            print(f"\nFiltering employees earning ₹{min_sal:,.2f} or more...")
            self._display_history_report(records=filtered_list)
        except ValueError:
            print(f"{Colors.FAIL}[Error] Please enter a valid numeric amount.{Colors.RESET}")

    def _delete_employee(self) -> None:
        """CRUD - Delete employee record using standard loop and list deletion."""
        del_id = input(f"\n{Colors.BOLD}Enter Employee ID to delete: {Colors.RESET}").strip()
        for i, emp in enumerate(self.history):
            if emp.emp_id == del_id:
                del self.history[i]
                print(f"{Colors.GREEN}[Success] Record for ID '{del_id}' has been permanently deleted.{Colors.RESET}")
                return
        print(f"{Colors.FAIL}[Error] No employee found with ID: {del_id}{Colors.RESET}")


if __name__ == "__main__":
    system = SalaryManagementSystem()
    system.run()