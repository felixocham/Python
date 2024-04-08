# Analysis in Python
## Source:
Worthy Tutorial: [TechWorld with Nana](https://www.youtube.com/watch?v=t8pPdKYpowI)
## Introduction
This project covers various hands-on demo projects in Python for Data Analysis.
## Skills Covered
1. Data Cleaning

A program that cleans a dataset to accommodate analysis with Python Lists and Dictionaries.
```
transactions_clean = []
for transaction in daily_transactions_split:
  temp_list = []
  for attribute in transaction:
    attr_clean = attribute.replace("\n", "").strip(" ")
    temp_list.append(attr_clean)
  transactions_clean.append(temp_list)
pprint.pprint(transactions_clean, width = 120)

# creating empty lists to hold customer, sales and thread_sold
customer = []
sales = []
thread_sold = []
```
2. Lists and Dictionaries

A program that calculates points scored in the game of Scrabble.
```
player_to_points = {}
#print(player_to_words.items())
for player in player_to_words.keys():
    player_points = 0
    for word in player_to_words.get(player, 0):
        player_points += score_word(word)
    player_to_points[player] = player_points
```
3. Countdown

A program that counts down to the due date using the datetime module.
```
deadline_date = datetime.strptime(deadline,'%d.%m.%Y')
today_date = datetime.today()
time_till = deadline_date - today_date

time_till_hrs = int(time_till.total_seconds()/(60*60))
```
4. Working with openpyxl

A program that analyses an inventory worksheet.
```
inventory_file = openpyxl.load_workbook('inventory.xlsx')
product_list = inventory_file['Sheet 1']
```
5. Classes

A program that utilizes Classes to analyze data in csv format using the csv module.
The analysis was for sales data according to region, categories, and year.
```
with open("sales.csv") as sales_csv:
    sales_record = list(csv.DictReader(sales_csv))...
    def unique_list(self):
        self.new_list = []
        for item in sales_record:
            if item[self.column] not in self.new_list:
                self.new_list.append(item[self.column])
        return self.new_list
```
### Why I Picked This Dataset
I liked working with Python because I felt like it was designed with the consideration of data analysis and it has useful libraries for common tasks in that field.
I also have room to collaborate with mates because Python has many users in data.
Now, combining that with my curiosity about business performance adds more flavor to it.
