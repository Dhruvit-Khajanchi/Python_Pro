date = (input("Enter Date in MM/DD/YY format: "))
month = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
x = date.split('/')
print(month[x[0]], x[1],',', x[2])