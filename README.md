# Python_Learning
Here is a clean, professional **problem statement** you can **copy-paste directly into your README file**.
It perfectly matches the code you wrote, including inheritance, abstract classes, and overridden methods.

---

# 🧩 **Problem: Employee Bonus Calculation Using OOP (Abstract Classes & Inheritance)**

You are required to design a simple employee management system using **Object-Oriented Programming (OOP)** concepts in Python.
The system should calculate bonuses for different types of employees using:

* **Abstract classes**
* **Method overriding**
* **Inheritance**
* **Polymorphism**

---

## **Requirements**

### 🔹 1. Create an abstract class `Employee`

This class should contain:

* Attributes:

  * `name`
  * `salary`
* An **abstract method**:

  ```python
  calculate_bonus()
  ```
* A concrete method:

  ```python
  display_emp_details()
  ```

  which prints the employee name and base salary.

---

### 🔹 2. Create a class `Developer` that inherits from `Employee`

This class should:

* Implement `calculate_bonus()`

  * Developer bonus = **10% of salary**
* Override `display_emp_details()`
  to print details including the role: *Developer*

---

### 🔹 3. Create a class `SeniorDev` that inherits from `Developer`

This class should:

* Override `calculate_bonus()`

  * Senior Developer bonus = **2% of salary**
* Override `display_emp_details()`
  to print details including the role: *Senior Developer*

---

### 🔹 4. Create objects and demonstrate functionality

* Create a `Developer` object
* Create a `SeniorDev` object
* Display their details
* Calculate and print their respective bonuses

---

## **Expected Behavior**

Your program should:

* Demonstrate **method overriding**
* Show the difference in bonus calculation between Developer and Senior Developer
* Use an **abstract base class** that enforces implementation of `calculate_bonus()` in subclasses
* Use polymorphism through overridden methods

---

Let me know if you want me to also format it in **Markdown with headings**, **add examples**, or **attach diagrams** for your README!
