def task1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22, 33]
    words = ["apple", "Banana", "cherry", "Date", "Elderberry"]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    squares=[n**2 for n in numbers if n%2==0]
    print(squares)
    long_lower=[n.lower() for n in words if len(n)>5]
    print(long_lower)
    word_lengths={word: len(word) for word in words}
    print(word_lengths)
    initials={n[0] for n in words}
    print(initials)
    flat=[n for row in matrix for n in row]
    print(flat)
def example2_1():
    def cont_up(n):
        i=0
        while i<n:
            yield i
            i+=1
    for x in cont_up(5):
        print(x)    
def example2_2():
    squares=[n**2 for n in range(1000000)]
    print(squares)
#squares = (n ** 2 for n in range(1000000))   # ничего не посчитано
#for x in squares:                            # считает по одному
#    ...
def task_2_1():
    logs = [
    "INFO: server started",
    "ERROR: db connection failed",
    "INFO: retry",
    "ERROR: timeout",
    ]
    def read_log_lines(logs):
        for line in logs:
            if line .startswith("ERROR"):
                yield line
    for line in read_log_lines(logs):
        print(line)
print(task_2_1())
def task_2_2():
    def fibonacci(n):
        a, b= 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    print(list(fibonacci(8)))                       
print(task_2_2())
   


    
