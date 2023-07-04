# python-challenge

From chatgpt on percent formatting a variable:
------
To format a variable as a percentage with two decimal places in Python, you can use string formatting or the `round()` function along with the `%` operator. Here's how you can do it using both methods:

1. Using String Formatting (f-string):
```python
percentage = 0.75321
formatted_percentage = f"{percentage:.2%}"
print(formatted_percentage)
```

2. Using `round()` and the `%` operator:
```python
percentage = 0.75321
formatted_percentage = "{:.2%}".format(percentage)
print(formatted_percentage)
```

Both of these methods will output the formatted percentage with two decimal places:
```
75.32%
```

In both cases, the `:.2%` specifies that the number should be formatted as a percentage with two decimal places. The `%` symbol represents the percentage sign. The `f-string` method uses the `f"{value}"` syntax, while the second method uses the `"{value}".format()` syntax for string formatting. Both approaches yield the same result.
--------

