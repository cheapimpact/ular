import ezsheets

# print(ezsheets.listSpreadsheets())
ssTask = ezsheets.Spreadsheet("1D9K2A92K3TACVnH4zu0QsiX1trFzAyUQYkjZB2pavaA")
# ss = ezsheets.createSpreadsheet(title="My New Spreadsheet")
sheet = ssTask[0]

print(sheet.getRow(2))
