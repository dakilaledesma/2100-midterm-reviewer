from utils.utils import subsubheader
def further_concepts(st):
    with st.expander("Multiple Assignment"):
        st.markdown("""
        Python supports multiple assignment, which allows you to assign multiple variables at once. For example, the
        following code assigns the value 1 to the variables `a`, `b`, and `c`.
        """)

        st.code("""
        a = b = c = 1
        """)

        st.markdown("""
        You can also assign multiple values to variables at once, such as in this example where we swap the values of `a` 
        and `b`.
        """)

        st.code("""
        a = 1
        b = 2
        a, b = b, a
        
        print(a)
        print(b)
        
        # Output: 2 (new value of a)
        #         1 (new value of b)
        """)

        st.markdown("""
        Note that the number of variables on the left side of the assignment operator must match the number of values
        on the right side of the assignment operator. Otherwise, you will get an error.
        """)


    with st.expander("Mutability"):
        st.markdown("""
        Mutability refers to whether or not a variable can be changed after it has been created. We have covered a 
        data type that is mutable: lists. We have also covered a data type that is immutable: tuples. For more 
        information on these datatypes, please refer to the [Python Basics](#python-basics) section.
        """)

    with st.expander("Multidimensional Collections"):
        st.markdown("""
        Python supports multidimensional collections. For example, you can have a list of lists, a list of tuples, a 
        tuple of lists, a tuple of tuples, etc. The following is an example of a list of lists.
        
        For simplicity's sake, we will simply be focusing on *lists of lists*, but the same concepts apply to other
        collections.
        """)

        st.subheader("1-Dimensional Lists")
        st.markdown("""
        A 1-dimensional list is a list that does not contain any inner lists, which you have seen numerous times
        throughout this course. For example, the following is a 1-dimensional list:
        """)
        st.code("""
        my_list = [1, 2, 3, 4, 5]
        """)

        st.subheader("2-Dimensional Lists")
        st.markdown("""
        A list within a list is called a 2-dimensional list. For example, the following is a 2-dimensional list:
        """)
        st.code("""
        my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """)

        st.markdown("""
        Note that each inner list has the same number of elements. This is not a requirement for 2-dimensional lists,
        but it is a common convention, and may be necessary when in use with certain libraries and functions (e.g.
        `numpy`).
        """)

        subsubheader(st, "Accessing elements")
        st.markdown("""
        To access an element in a 2-dimensional list, you need to specify the index of the inner list and the index of
        the element within the inner list. Watch what happens if we try to access the element at index 0 of `my_list`:
        """)

        st.code("""
        my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(my_list[0])
        # Output: [1, 2, 3]
        """)

        st.markdown("""
        As you can see, the element at index 0 of `my_list` is the inner list `[1, 2, 3]`. To access an element within
        the inner list, we need to specify the index of the element within the inner list. For example, to the value 5
        in `my_list`, see the following:
        """)

        st.code("""
        my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(my_list[1][1])
        # Output: 5
        """)

        st.markdown("""
        The first index, `1`, specifies which inner list. Because we want the second inner list, we use `1`. The second
        index, `1`, specifies which element within the inner list. Because we want the second element, we use `1`.
        Therefore, the value of `my_list[1][1]` is 5.
        """)

        subsubheader(st, "Common structures of 2-dimensional lists")
        st.markdown("""
        2-dimensional lists are commonly used to represent matrices and tables. For example, spreadsheets are often
        represented as 2-dimensional lists. 
        """)

        st.subheader("3-Dimensional Lists")
        st.markdown("""
        We can continue this pattern to create 3-dimensional lists, 4-dimensional lists, etc. For example, the
        following is a 3-dimensional list:
        """)
        st.code("""
        my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        """)

        subsubheader(st, "Common structures of 3-dimensional lists")
        st.markdown("""
        Why am I going as deep as 3-dimensional lists? Because 3-dimensional lists are commonly used to represent
        images. For example, a 3-dimensional list of shape `(32, 32, 3)` represents a color image with a height of 32
        pixels, a width of 32 pixels, and the 3 color channel values (red, green, and blue).
        """)

    with st.expander("Scope"):
        st.markdown("""
        Scope refers to the visibility of a variable. For example, if a variable is defined inside a function, then it
        is only visible inside that function. If a variable is defined outside of a function, then it is visible
        everywhere* in the program.
        
        <sup>*There are some exceptions to this, but we will not be covering them in this reviewer.</sup>
        """, unsafe_allow_html=True)

        st.markdown("""
        For example, the following code will result in an error:
        """)
        st.code("""
        def my_func():
            my_var = 5

        print(my_var)
        """)
        st.markdown("""
        This is because `my_var` is defined inside the function `my_func()`, so it is only visible inside the function.
        """)

        st.markdown("""
        Moving my_var outside of the function will fix this error, but note how the value of `my_var` being printed is
        5, not 10. That is because the `my_var` inside the function is a different variable (and in a different scope)
        than the `my_var` outside the function.
        """)
        st.code("""
        my_var = 5
        
        def my_func():
            my_var = 10
            
        my_func()
        print(my_var)
        
        # Output: 5
        """)

    with st.expander("Exceptions and try-except statements"):
        st.subheader("Overview")
        st.markdown("""
        Exceptions are errors that occur during the execution of a program. For example, if you try to access an
        element in a list that does not exist, you will get an `IndexError` exception.
        """)

        st.code("""
        my_list = [1, 2, 3]
        print(my_list[3])
        print("Hello")

        # Output: IndexError: list index out of range (index of 3 is trying to access a 4th element)
        """)

        st.markdown("""
        Note that the `print("Hello")` statement is never executed as the program has crashed.
        """)

        st.subheader("Exception handling: simple try-except")
        st.markdown("""
        Exceptions can be handled using `try-except` statements. This allows you to handle exceptions gracefully, 
        rather than having your program crash/halt when an exception occurs.
        """)

        st.code("""
        my_list = [1, 2, 3]
        try:
            print(my_list[3])
        except:
            print("Had an error")

        print("Hello")
        # Output: Had an error
        #         Hello
        """)

        st.markdown("""
        In the above example, the `print("Hello")` statement is executed even though an exception occurred. This is
        because the exception was handled by the `except` statement.""")

        subsubheader(st, "Handling specific exceptions")
        st.markdown("""
        You can also handle specific exceptions. This is useful if you want to handle different exceptions
        differently, or only deal with/debug a specific exception.
        """)

        st.code("""
        my_list = [1, 2, 3]
        try:
            my_list += 1
            print(my_list[3])
        except IndexError:
            print("IndexError occurred")

        print("Hello")

        # Output: TypeError: 'int' object is not iterable
        """)

        st.markdown("""
        In the above example, the `except IndexError` statement will only handle `IndexError` exceptions. Since there
        was a `TypeError` exception before it (adding a list and an integer), the `except IndexError` statement will
        not handle it, and the program will crash.

        You can either handle this by removing IndexError from the `except` statement (which will catch any and all
        exceptions), adding TypeError to the `except` statement through a tuple, or adding a second `except` statement 
        to handle the `TypeError` exception separately.
        """)

        st.code("""
        my_list = [1, 2, 3]
        try:
            my_list += 1
            print(my_list[3])
        except (IndexError, TypeError):
            print("IndexError or TypeError occurred")

        print("Hello")
        # Output: IndexError or TypeError occurred
        #         Hello
        """)

        st.code("""
        my_list = [1, 2, 3]
        try:
            my_list += 1
            print(my_list[3])
        except IndexError:
            print("IndexError occurred")
        except TypeError:
            print("TypeError occurred")

        print("Hello")
        # Output: TypeError occurred (since TypeError occurred first)
        #         Hello
        """)

        st.subheader("Exception handling: extending the simple try-except")
        st.markdown("""
        You can also extend the simple try-except statement to include `else` and `finally` statements. The `else`
        statement is executed if no exceptions occur, and the `finally` statement is executed regardless of whether
        an exception occurs or not.
        """)

        st.code("""
        my_list = [1, 2, 3]
        try:
            print(my_list[2])
        except IndexError:
            print("IndexError occurred")
        else:
            print("No exceptions occurred")
        finally:
            print("This will print regardless of whether an exception occurred")
            
        # Output: 3
        #         No exceptions occurred (since accessing my_list[2] is valid)
        #         Finally statement executed
        """)

    return {}
