# Data Processing Module

This project provides utility functions for data processing.

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/data-processing.git
Usage
Functions:
filter_by_state(data, state='EXECUTED')
Filters a list of dictionaries by the 'state' key.

Example:

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
filtered_data = filter_by_state(data, state='EXECUTED')
print(filtered_data)
sort_by_date(data, reverse=True)
Sorts a list of dictionaries by the 'date' key.

Example:

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
sorted_data = sort_by_date(data, reverse=True)
print(sorted_data)
Contributing
Feel free to contribute by forking the repository and creating pull requests.


Эти шаги помогут вам создать структуру проекта, разработать необходимые функции обработки данных и предоставить полезную документацию для пользователя.
