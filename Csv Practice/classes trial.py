import csv

with open("sales.csv") as sales_csv:
    sales_record = list(csv.DictReader(sales_csv))


class SalesAnalysis:

    def __init__(self, column, new_list):
        self.column = column
        self.new_list = new_list

    def unique_list(self):
        self.new_list = []
        for item in sales_record:
            if item[self.column] not in self.new_list:
                self.new_list.append(item[self.column])
        return self.new_list

    def attr_sub_total(self):
        sub_tot_list = []
        for category in self.new_list:
            cat_sub_total = 0
            for item in sales_record:
                if category == item[self.column]:
                    cat_sub_total += int(item["Revenue"])
            sub_tot_list.append(cat_sub_total)
        return sub_tot_list

    def cat_sales_dict(self):
        sub_tot_list = self.attr_sub_total()
        return {cat: sales for cat, sales in zip(self.new_list, sub_tot_list)}


Category_list = SalesAnalysis("Product_Category", "product_categories")
print(Category_list.unique_list())
print(Category_list.attr_sub_total())
print(Category_list.cat_sales_dict())

Sub_Category_list = SalesAnalysis("Sub_Category", "product_sub_categories")
print(Sub_Category_list.unique_list())
print(Sub_Category_list.cat_sales_dict())

years = SalesAnalysis("Year", "years")
print(years.unique_list())
print(years.cat_sales_dict())

age_groups = SalesAnalysis("Age_Group", "age_groups")
print(age_groups.unique_list())
print(age_groups.cat_sales_dict())

countries = SalesAnalysis("Country", "countries")
print(countries.unique_list())
print(countries.cat_sales_dict())
