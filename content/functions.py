from content.generators import for_loop_ind_gen, for_loop_val_gen
from utils.utils import subsubheader

def funcs(st):
    with st.expander("Basics"):
        st.markdown("""
        Functions are used to group together lines of code that perform a specific task, making them useful for 
        organizing your code and code reuse. 
        
        New functions are created using the `def` keyword, followed by the function
        name, and then the parameters enclosed in parentheses. After the function body, it is common to include a
        `return` statement, which specifies the value that the function will return when called.
        """)

        st.code("""
        def add(a, b):
            return a + b
        """)

        st.markdown("""
        To call a function, simply use the function name followed by the arguments enclosed in parentheses. If the
        function returns a value, you can assign it to a variable. Above, we defined a function called `add` that
        returns a + b. When we assign this function to a variable `x`, `x` will take on the return value.
        """)

        st.code("""
        x = add(1, 2)
        # Output: x = 3
        """)

        st.markdown("""
        It is important to note that not all functions return a value. Some functions are used to perform a task, and
        do not return anything. For example, the `print` function is used to print a value to the console, but does
        not return anything. Setting a variable equal to the `print` function will result in the variable being set
        to `None`.
        """)

    with st.expander("Recursion (know concept for midterm)"):
        subsubheader(st, "Basics")
        st.markdown("""
        Recursion is a technique in programming where a function calls itself. This is useful for solving problems
        that can be broken down into smaller subproblems. A recursive function has two parts: 
        1. The base case, where the function stops calling itself
        2. The recursive case, where the function calls itself again and simulates a loop. Note that it is usually
        the case that the parameters passed to the recursive call are different from the parameters passed to the
        original call, so that the function will eventually reach the base case.
        """)

        st.code("""
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n - 1)
        """)

        st.markdown("""
        The above function is an example of a recursive function that computes the factorial of a number. The base
        case is when `n == 1`, and the recursive case is when `n > 1`. The function will continue to call itself
        until `n == 1`, at which point it will return 1. The function will then return the product of `n` and the
        return value of the recursive call.
        """)

        st.code("""
        factorial(4)
        # Output: 24
        """)

        subsubheader(st, "Differences to loops")
        st.markdown("""
        Note that unlike loops, recursive functions don't replace themselves every iteration. Instead, each recursive
        call creates a new instance of the function. This means that each recursive call has its own set of local
        variables, and the function will not "remember" the values of the local variables from previous calls.
        
        What does this mean? Let's look at an example.
        """)

        st.code("""
        def print_i(i):
            if i >= 10:
                return
            else:
                print(i)
                print_i(i + 1)
        
        print_i(0)
        """)

        st.markdown("""
        The above recursion will print the numbers 0 through 9. However, every time the function calls itself, it
        creates a new instance of the function. This means:
        - `print_i(i)` will be called 10 times, once for each value of i from 0 to 9
        - a new local variable `i` will be created for each call to print_i(i), which is `i + 1`
        - Each call to `print_i(i)` will have its own local variable `i`, which will be set to the value of `i` passed to
        the function (i.e. 0 for the first call, 1 for the second call (i -> 0 + 1), 2 for the second call (i -> 1 + 1)
        etc.)
        """)

        st.markdown("""
        This is different from a for loop, where the variable `i` is updated/replaced every iteration. In the above 
        example, if
        we were to use a for loop instead of recursion, the variable i would be updated every iteration, and the
        function would print the numbers 0 through 9.
        """)

        st.code("""
        for i in range(10):
            print(i)
        """)


    with st.expander("Optional reading: Why use recursion? (one reason is coding interviews)"):
        st.subheader("Disclaimer")
        st.markdown("""
        :blue[Before I scare anyone away, I want to say that]
        - :blue[a) recursion is not something you need to know very deeply for the midterm]
        - :blue[b) not all job interviews have coding portions/coding interviews (though many do, especially for 
        software engineering roles at tech companies).]
        """)

        st.subheader("Why use recursion?")
        st.markdown("""
        To keep it simple, there are problems that are easier to think about recursively than iteratively (by 
        iteratively, I mean using loops). This is a broad and somewhat nuanced topic, but just know it is common
        in coding interviews at jobs:
        - a) that the task they give you may be easier to think about and implement recursively
        - b) they may ask you to implement a recursive solution to a problem, either from the start or after you have
        provided an iterative solution
        
        Below, I provide both an iterative and recursive solution to the quicksort algorithm, which is considered a
        "medium" difficulty problem on LeetCode (the bane of most of our existences).
        """)

        subsubheader(st, "Iterative solution")
        st.code("""
        def quicksort(arr):
            stack = [(0, len(arr) - 1)]
            while stack:
                lo, hi = stack.pop()
                if lo < hi:
                    p = partition(arr, lo, hi)
                    stack.append((lo, p - 1))
                    stack.append((p + 1, hi))
            return arr
        """)

        subsubheader(st, "Recursive solution")
        st.code("""
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            p = partition(arr, 0, len(arr) - 1)
            return quicksort(arr[:p]) + [arr[p]] + quicksort(arr[p + 1:])
        """)

        st.markdown("""
        As you can see, the recursive solution is much more concise. For those of you who are quite advanced and know 
        the quicksort algorithm, you may also agree that it's easier to think about the problem rather than 
        implementing it iteratively using a stack.
        """)

    return {}
