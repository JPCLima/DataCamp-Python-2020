# Run_n_times()
# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

# HTML Generator
# Wrap the result of hello_goodbye() in <div> and </div>
html('<div>', '</div>')


def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))
