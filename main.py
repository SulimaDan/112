# def display_quote():
#     quote = (
#         "Don't compare yourself with anyone in this world…\n"
#         "if you do so, you are insulting yourself.\n"
#         "Bill Gates"
#     )
#     print(quote)

# display_quote()






def display_even_numbers(start, end):
    if start > end:
        start, end = end, start
    
    print(f"Even numbers between {start} and {end} are:")
    
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

display_even_numbers(3, 15)