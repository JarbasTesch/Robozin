# SAP Automation with PyAutoGUI

This project is an automation tool developed using Python and the `pyautogui` library. It provides a graphical user interface (GUI) with buttons to automate interactions with SAP, streamlining login and specific transaction processes.

---

## Features

### GUI Functionalities
1. **Login SAP**:
   - Automatically opens SAP using the specified path and logs into the system using credentials stored in a local Excel spreadsheet.
   - The login process includes opening SAP, filling in the username and password, and pressing "Enter" to log in.
   - The credentials are fetched from a local file (`usuario.xlsx`), located at my local `Documents`, you must change to yours.

2. **Transaction 1301**:
   - Automates the process of entering transaction 1301, performing predefined steps, and exporting the results to a predefined directory.

3. **Transaction 2301**:
   - Automates the process of entering transaction 2301, performing predefined steps, and exporting the results to a predefined directory.

### Additional Functions (Not Assigned to Buttons)
- **Transaction FMEDDW**: Prepares and automates steps for FMEDDW.
- **Transaction FMRP**: Prepares and automates steps for FMRP.

> Note: The FMEDDW and FMRP functionalities are implemented in the code but are not currently linked to any button in the GUI.

---

## Technologies Used

- **Python**: Core programming language.
- **PyAutoGUI**: For image recognition and automation of keyboard/mouse actions.
- **Tkinter**: To create the GUI for user interaction.
- **Pandas**: For reading user credentials from a local Excel file.

---

## Prerequisites

1. **Python Environment**:
   - Python 3.x installed on your machine.
   - Install required libraries:
     ```bash
     pip install pyautogui pandas
     ```

2. **SAP Installed**:
   - Ensure that SAP is installed and accessible from your machine.

3. **Local Spreadsheet**:
   - Create a spreadsheet containing user login credentials in the following format:
     |  usuario |   senha  |
     |----------|----------|
     |   user1  |   pass1  |
     - Save the file locally at your defined `login` at `loginSAP.py` file.

---

## How to Use

1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script:
     ```bash
     python sap_automation.py
     ```

2. **Use the GUI**:
   - **Login SAP**: Click this button to log into SAP automatically. The login credentials will be read from the `usuario.xlsx` file, and the login process will be performed with `pyautogui` and `fcs` functions.
   - **1301**: Automates transaction 1301 and saves the output to the predefined directory.
   - **2301**: Automates transaction 2301 and saves the output to the predefined directory.

---

## Limitations and Notes

- **Transaction-Specific Steps**:
  - Ensure that the SAP screens are set up correctly for the automation to work.
  - Modifications might be required if SAP UI elements differ due to customization.

- **GUI Buttons for FMEDDW and FMRP**:
  - These functionalities are coded but not linked to any GUI buttons. To use them, assign them to new buttons in the GUI or execute them manually from the code.

- **Login Credentials**:
  - The login credentials must be stored in the file `usuario.xlsx` located at `C:\Users\jbtesch\Documents\usuario.xlsx`. Ensure the file format is correct.

---

## Personal Note

This project was developed to automate repetitive SAP tasks and streamline user interaction. While basic functionalities are implemented, there’s room for future enhancements, including adding more transactions and improving error handling. Feel free to customize it for your specific use case!
