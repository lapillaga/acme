def get_employee_data(line):
    """Get employee data in pattern"""
    line_values = line.split('=')
    employee_name = line_values[0]
    work_days = line_values[1]

    return employee_name, work_days

