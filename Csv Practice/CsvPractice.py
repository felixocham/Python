import csv
total_sales = 0
product_categories = []
sales_by_category = []
product_sub_categories = []
sales_by_sub_category = []
sales_qty_by_sub_category = []
age_groups = []
age_groups_sales = []
countries = []
sales_by_country = []
years = []
sales_by_year = []

with open("sales.csv") as sales_csv:
    sales_record = list(csv.DictReader(sales_csv))

# calculating the total revenue generated
for row in sales_record:
    total_sales += int(row["Revenue"])

# generating a unique list of product categories.
for row in sales_record:
    if row["Product_Category"] not in product_categories:
        product_categories.append(row["Product_Category"])

# calculating sales by category and storing in sales by category list
for category in product_categories:
    category_sub_total = 0
    for row in sales_record:
        if category == row["Product_Category"]:
            category_sub_total += int(row["Revenue"])
    sales_by_category.append(category_sub_total)

for row in sales_record:
    if row["Country"] not in countries:
        countries.append(row["Country"])

for country in countries:
    country_sales_subtotal = 0
    for row in sales_record:
        if country == row["Country"]:
            country_sales_subtotal += int(row["Revenue"])
    sales_by_country.append(country_sales_subtotal)


# generating a unique list of product sub categories.
for row in sales_record:
    if row["Sub_Category"] not in product_sub_categories:
        product_sub_categories.append(row["Sub_Category"])

# generating  a list of sub_categories totals
for sub_category in product_sub_categories:
    sub_cat_sub_tot = 0
    for row in sales_record:
        if sub_category == row["Sub_Category"]:
            sub_cat_sub_tot += int(row["Revenue"])
    sales_by_sub_category.append(sub_cat_sub_tot)

# calculating the order quantity for each category
for sub_category in product_sub_categories:
    sub_cat_qty = 0
    for row in sales_record:
        if sub_category == row["Sub_Category"]:
            sub_cat_qty += int(row["Order_Quantity"])
    sales_qty_by_sub_category.append(sub_cat_qty)

# generating a unique list of age groups
for row in sales_record:
    if row["Age_Group"] not in age_groups:
        age_groups.append(row["Age_Group"])

# calculating sales revenue for each age group
for age_group in age_groups:
    sales_subtotal_age_group = 0
    for row in sales_record:
        if age_group == row["Age_Group"]:
            sales_subtotal_age_group += int(row["Revenue"])
    age_groups_sales.append(sales_subtotal_age_group)

# generating a unique list of years
for row in sales_record:
    if row["Year"] not in years:
        years.append(row["Year"])

# calculating sales by year
for year in years:
    year_sales = 0
    for row in sales_record:
        if year == row["Year"]:
            year_sales += int(row["Revenue"])
    sales_by_year.append(year_sales)

years_sales_rpt = {year: sales for year, sales in zip(years, sales_by_year)}
product_categories_sales_rpt = {product_cat: sales for product_cat, sales in zip(product_categories, sales_by_category)}
sub_cat_sales_rpt = {sub_cat: sales for sub_cat, sales in zip(product_sub_categories, sales_by_sub_category)}
age_groups_sales_rpt = {age_groups: sales for age_groups, sales in zip(age_groups, age_groups_sales)}
country_sales_rpt = {country: sales for country, sales in zip(countries, sales_by_country)}

# comb_rpt = [years_sales_rpt, product_categories_sales_rpt, sub_cat_sales_rpt, age_groups_sales_rpt, country_sales_rpt]
#
# output_file = "sales_report_by_category.csv"
# field_names = max(comb_rpt, key=len).keys()
#
# with open(output_file, "w", newline="") as output_csv:
#     sales_report = csv.DictWriter(output_csv, fieldnames=field_names)
#
#     sales_report.writeheader()
#     sales_report.writerows(comb_rpt)
#
# print("CSV file generated successfully:", output_file)

# print(total_sales)
# print(product_categories)
# print(sales_by_category)
# print(product_sub_categories)
# print(sales_by_sub_category)
# print(sales_qty_by_sub_category)
# print(age_groups)
# print(age_groups_sales)
# print(countries)
# print(sales_by_country)
# print(years)
# print(sales_by_year)
print(years_sales_rpt)
print(product_categories_sales_rpt)
print(sub_cat_sales_rpt)
print(age_groups_sales_rpt)
print(country_sales_rpt)
