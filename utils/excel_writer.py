from openpyxl import Workbook
from datetime import datetime

def write_to_excel(products, filename="products.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.append(["Product Name", "Price", "Description", "Timestamp"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for p in products:
        ws.append([p["name"], p["price"], p["description"], timestamp])
    wb.save(filename)