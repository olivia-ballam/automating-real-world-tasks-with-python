#! /usr/bin/env python3

import emails
import json
import reports 

emails.generate(ge)

def sales_summary(json_file):
    
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Find the car that generated the most revenue 
    for id in json_data:
        price = float() 

    # Find the 

    # Find the most popular year with number of sales 


    sales_summary = f"""
    The {car_revenue} generated the most revenue: {total_revenue} \n
    The {car_sales} had the most sales: {amount_sales} \n
    The most popular year was {popular_year} with {year_sales} sales.
    """


#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0, "car_model": ""}
  pop_car_yr = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price

    
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    if item["total_sales"] > max_sales["total_sales"]:
      max_sales["total_sales"] = item["total_sales"]
      max_sales["car_model"] = item["car"]["car_model"]

    # TODO: also handle most popular car_year
    pop_car_yr[item["car"]["car_year"]] = pop_car_yr.get(item["car"]["car_year"], 0) +  item["total_sales"]

  pop_car_yr_sorted = sorted(pop_car_yr.items(), key=lambda a: a[1], reverse=True)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales['car_model'], max_sales['total_sales']),
    "The most popular year was {} with {} sales.".format(pop_car_yr_sorted[0][0], pop_car_yr_sorted[0][1]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_cols = [["ID", "Car", "Price", "Total Sales"]]
  cars_list = []
  for item in car_data:
    cars_list.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  cars_list.sort(key=lambda a: int(a[3]), reverse=True)
  return table_cols + cars_list


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)

  # TODO: turn this into a PDF report
  car_data = cars_dict_to_table(data)
  reports.generate("/tmp/cars.pdf", "Sales summary for last month", "<br/>".join(summary), car_data)


  # TODO: send the PDF report as an email attachment
  message = emails.generate("automation@example.com", "student-04-9849759230b1@example.com", "Sales summary for last month", "\n".join(summary), "/tmp/cars.pdf")
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)