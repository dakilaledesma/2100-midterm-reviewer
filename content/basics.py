from content.generators import for_loop_ind_gen, for_loop_val_gen
from utils.utils import subsubheader


def basics(st):
    if not st.session_state.get("for_loop_ind_gen"):
        st.session_state["for_loop_ind_gen"] = for_loop_ind_gen()

    if not st.session_state.get("for_loop_val_gen"):
        st.session_state["for_loop_val_gen"] = for_loop_val_gen()

    with st.expander("Variables"):
        st.subheader("Overview")
        st.markdown("""
        Variables are used to store data. They are used to make code more readable and easier to understand. 
        Variables are declared by assigning a value to a name. For example:
        ```python
        x = 5
        ```
        In the above example, `x` is the variable name and `5` is the value. Variables can be assigned to any data 
        type. For example:
        ```python
        y = "hello world"
        z = [1, 2, 3]
        ```
        In the above example, `y` is a string and `z` is a list. Variables can also be reassigned to a different value.
        For example:
        ```python
        x = 5
        x = 10
        ```
        In the above example, `x` is reassigned to `10`. Variables can also be used in expressions. For example:
        ```python
        x = 5
        y = 10
        z = x + y
        ```
        In the above example, `z` is assigned to the value of `x + y`, which is `15`. 
        
        <br>
        """, unsafe_allow_html=True)

        subsubheader(st, "Variable Naming Conventions")
        st.markdown("""
        Variable names can be any combination of letters, numbers, and underscores. However, they cannot start with a 
        number. Variable names are also case sensitive. For example:
        ```python
        x = 5
        X = 10
        ```
        In the above example, `x` and `X` are two different variables. 
        
        <br>
        """, unsafe_allow_html=True)

    with st.expander("Default Data Types"):
        st.subheader("Overview")
        st.markdown("""
        Data types are used to classify one piece of data from another. They are used to determine what operations
        can be performed on the data. In Python, there are 4 main data types:
        - Numeric Types (Integers, Floats)
        - Boolean Types (True, False)
        - Strings
        - Collections (Lists, Tuples, Sets, Dictionaries)
        """)

        numeric_tab, boolean_tab, string_tab, collection_tab = st.tabs(["Numeric", "Boolean", "Strings", "Collections"])
        with numeric_tab:
            st.subheader("Numeric Types")
            st.markdown("""
                Used to represent numbers
                - Integers: Numbers without decimal points
                - Floats: Numbers with decimal points
                
                <br>
                They are compatible with your typical operators, such as:
                
                - Arithmetic Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
                    - `//` is floor division
                    - `%` is modulo
                    - `**` is exponentiation
                - Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
                    - `==` is equal to
                    - `!=` is not equal to
                More operators may be found in the common operations section of this reviewer (`Python Basics -> 
                Common Operators`).
                <br>
                """, unsafe_allow_html=True)

        with boolean_tab:
            st.subheader("Boolean Types")
            st.markdown("""
                Used to represent truth values, primarily in conditional statements
                - `True` or `False`
                <br>
                """, unsafe_allow_html=True)

        with string_tab:
            st.subheader("Strings")
            st.markdown("""
            Commonly used to represent text. Strings are enclosed in either single or double quotes. They can also be 
            thought as a collection of characters, and behave similarly to lists (without the associated list methods).
            """)
            subsubheader(st, "Commonly used string methods")
            str_method_dict = {
                "str.upper()": """  
                                    my_str = "hello world"
                                    my_str.upper()  
                                    # Output: "HELLO WORLD"
                                    """,
                "str.lower()": """
                                    my_str = "HELLO WORLD"
                                    my_str.lower()
                                    # Output: "hello world"
                                    """,
                "str.replace()": """
                                    my_str = "hello world"
                                    my_str.replace("hello", "goodbye")
                                    # Output: "goodbye world"
                                    """,
                "str.split()": """
                                    my_str = "hello world"
                                    my_str.split("o")
                                    # Output: ["hell", " w", "rld"] (note that str becomes a list)
                                    """,
                "str.join()": """
                                    my_list = ["hello", "world"]
                                    " ".join(my_str)
                                    # Output: "hello world" (note that list becomes a str)
                                    """
            }
            for method, desc in str_method_dict.items():
                method_col, desc_col = st.columns([0.25, 0.75])
                method_col.code(method)
                desc_col.code(desc)

            subsubheader(st, "Commonly used string operations")
            str_op_dict = {
                "str + str": """
                                    my_str = "hello" + "world"
                                    # Output: "helloworld" (concatenation)
                                    """,
                "str * int": """
                                    my_str = "hello" * 3
                                    # Output: "hellohellohello" (repetition)
                                    """,
                "str in str": """
                                    "hello" in "hello world"
                                    # Output: True (you can use 'not in' as well)
                                    """
            }
            for op, desc in str_op_dict.items():
                op_col, desc_col = st.columns([0.25, 0.75])
                op_col.code(op)
                desc_col.code(desc)

        with collection_tab:
            st.subheader("Collections")
            st.markdown("""
            Collections are used to store multiple pieces of data. There are 4 main types of collections:
            - Lists
            - Tuples
            - Sets
            - Dictionaries
            """)

            lists_tab, tuples_tab, sets_tab, dicts_tab = st.tabs(["Lists", "Tuples", "Sets", "Dictionaries"])
            with lists_tab:
                subsubheader(st, "Lists")
                st.markdown("""
                Lists are used to store multiple pieces of data. They are mutable, meaning that you can change the 
                elements of a list after it has been created.
                """)
                subsubheader(st, "Setting and accessing values")
                st.markdown("""
                Lists are created using square brackets `[]`. Values are separated by commas `,`. Lists can contain
                values of different data types.
                """)
                st.code("""
                my_list = [1, 2, 3, 4, 5]
                my_list = ["hello", "world"]
                my_list = [1, "hello", True]
                """)

                st.markdown("""
                Values in a list can be accessed using their index. The index of a list starts at 0. Negative indices
                can also be used to access values from the end of the list.
                """)

                st.code("""
                my_list = [1, 2, 3, 4, 5]
                # Index:   0  1  2  3  4
                # Index:  -5 -4 -3 -2 -1    ← Negative indices
                
                my_list[0]      # Output: 1
                my_list[2]      # Output: 3
                my_list[-1]     # Output: 5
                """)

                subsubheader(st, "Commonly used list methods")
                list_method_dict = {
                    "list.append()": """
                                        my_list = [1, 2, 3]
                                        my_list.append(4)
                                        # Output: [1, 2, 3, 4] (adds a value to the end of the list)
                                        """,
                    "list.extend()": """
                                        my_list = [1, 2, 3]
                                        my_list.extend([4, 5])
                                        # Output: [1, 2, 3, 4, 5] (adds a list of values to the end of the list)
                                        """,
                    "list.insert()": """
                                        my_list = [1, 2, 3]
                                        my_list.insert(0, 0)
                                        # Output: [0, 1, 2, 3] (inserts a value at a given index)
                                        """,
                    "list.remove()": """
                                        my_list = [1, 2, 3]
                                        my_list.remove(1)
                                        # Output: [2, 3] (removes the first occurrence of a *value* [not at an index])
                                        """,
                    "list.pop()": """
                                        my_list = [1, 2, 3]
                                        a = my_list.pop()
                                        # Output: 
                                        # my_list   → [1, 2]
                                        # a         → 3
                                        """,
                    "list.index()": """
                                        my_list = [1, 2, 3]
                                        my_list.index(2)
                                        # Output: 1 (returns the index of the first occurrence of a value)
                                        """}
                for method, desc in list_method_dict.items():
                    method_col, desc_col = st.columns([0.25, 0.75])
                    method_col.code(method)
                    desc_col.code(desc)

                subsubheader(st, "Commonly used list operations")
                list_op_dict = {
                    "list + list": """
                                        my_list = [1, 2, 3] + [4, 5]
                                        # Output: [1, 2, 3, 4, 5] (concatenation)
                                        """,
                    "list * int": """
                                        my_list = [1, 2, 3] * 3
                                        # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3] (repetition)
                                        """,
                    "value in list": """
                                        1 in [1, 2, 3]
                                        # Output: True (you can use 'not in' as well)
                                        """
                }
                for op, desc in list_op_dict.items():
                    op_col, desc_col = st.columns([0.25, 0.75])
                    op_col.code(op)
                    desc_col.code(desc)

            with tuples_tab:
                subsubheader(st, "Tuples")
                st.markdown("""
                Tuples are used to store multiple pieces of data. They are *immutable*, meaning that you cannot change 
                the elements of a tuple after it has been created.
                """)
                subsubheader(st, "Setting and accessing values")
                st.markdown("""
                Tuples are created using parentheses `()`. Values are separated by commas `,`. Tuples can contain
                values of different data types.
                """)
                st.code("""
                my_tuple = (1, 2, 3, 4, 5)
                my_tuple = ("hello", "world")
                my_tuple = (1, "hello", True)
                """)

                st.markdown("""
                Like lists, values in a tuple can be accessed using their index. The index of a tuple starts at 0. 
                Negative indices can also be used to access values from the end of the tuple.
                """)

                st.code("""
                my_tuple = (1, 2, 3, 4, 5)
                # Index:    0  1  2  3  4
                # Index:   -5 -4 -3 -2 -1    ← Negative indices
                
                my_tuple[0]      # Output: 1
                my_tuple[2]      # Output: 3
                my_tuple[-1]     # Output: 5
                """)

                subsubheader(st, "Immutability")
                st.markdown("""
                Immutable/immutability means that you cannot change the elements of a tuple after it has been created.
                For example, you cannot append a value to a tuple, or remove a value from a tuple.
                
                See below how trying to change a tuple will result in an error, and that tuples do not contain 
                `append()` or `remove()` methods which are used to change values/modify lists.
                """)
                st.code("""
                my_tuple = (1, 2, 3)
                my_tuple[0] = 0         # TypeError: 'tuple' object does not support item assignment
                my_tuple.append(4)      # AttributeError: 'tuple' object has no attribute 'append'
                """)

            with sets_tab:
                subsubheader(st, "Sets")
                st.markdown("""
                Sets are used to store multiple pieces of data, but differ from lists in that they do not allow
                duplicate values. Like lists, they are *mutable*. Unlike lists, they are *unordered*, 
                meaning that the values in a set are not stored in any particular order (and you cannot access
                values in a set using their index).
                
                Sets are useful for storing unique values, and for performing mathematical set operations such as
                unions, intersections, and differences between sets. Most commonly, sets are used to remove duplicate
                values from a list, and to check if a value within the collection (e.g. `if 1 in my_set: ...`).
                """)
                subsubheader(st, "Setting values")
                st.markdown("""
                Sets are created using curly braces `{}`. Values are separated by commas `,`. Sets can contain
                values of different data types.
                """)
                st.code("""
                my_set = {1, 2, 3, 4, 5}
                my_set = {"hello", "world"}
                my_set = {1, "hello", True}
                """)

                st.markdown("""
                The values in a set can be accessed using their index. However, since sets are unordered, the index
                of a value is not fixed. Therefore, you cannot use the index to access a value from a set.
                """)

                st.code("""
                my_set = {1, 2, 3, 4, 5}
                my_set[0]       # TypeError: 'set' object is not subscriptable (cannot use index)
                """)

                subsubheader(st, "Commonly used set methods")
                set_method_dict = {
                    "set.add()": """
                                        my_set = {1, 2, 3}
                                        my_set.add(4)
                                        # Output: {1, 2, 3, 4} (adds a value to the set)
                                        """,
                    "set.remove()": """
                                        my_set = {1, 2, 3}
                                        my_set.remove(1)
                                        # Output: {2, 3} (removes a value from the set)
                                        """,
                    "set.union()": """
                                        my_set = {1, 2, 3}
                                        my_set.union({4, 5})
                                        # Output: {1, 2, 3, 4, 5} (combines two sets)
                                        """,
                    "set.intersection()": """
                                        my_set = {1, 2, 3}
                                        my_set.intersection({2, 3, 4})
                                        # Output: {2, 3} (finds the common values between two sets)
                                        """,
                    "set.difference()": """
                                        my_set = {1, 2, 3}
                                        my_set.difference({2, 3, 4})
                                        # Output: {1} (finds the values in the first set that are not in the second set)
                                        """}

                for method, desc in set_method_dict.items():
                    op_col, desc_col = st.columns([1, 4])
                    op_col.code(method)
                    desc_col.code(desc)

            with dicts_tab:
                st.subheader("Dictionaries")
                st.markdown("""
                Dictionaries are used to store multiple pieces of data, but differ from lists in that they do not
                store values in a particular order. Instead, dictionaries store values in *key-value pairs*.
                
                Dictionaries are useful for storing data that is related to each other, and for quickly accessing
                values using their key. For example, a dictionary can be used to store information about a person,
                where the keys are the names of the attributes (e.g. "name", "age", "height"), and the values are
                the values of those attributes (e.g. "John", 25, 1.8).
                
                Most APIs return data in the form of a dictionary, where the keys are the names of the attributes,
                and the values are the values of those attributes. For example, the following is the return response
                from the [Pirate Weather API](https://www.pirateweather.net/api):
                """)
                st.code("""
                {
                  "latitude": 45.42,
                  "longitude": -75.69,
                  "timezone": "America/Toronto",
                  "offset": -5.0,
                  "elevation": 69,
                  "currently": {
                    "time": 1674318840,
                    "summary": "Clear",
                    "icon": "clear-day",
                    "nearestStormDistance": 0,
                    "nearestStormBearing": 0,
                    "precipIntensity": 0.0,
                    "precipProbability": 0.0,
                    "precipIntensityError": 0.0,
                    "precipType": "none",
                    # ...
                  }
                  # ...
                }
                """)

                st.subheader("Setting and accessing values")
                st.markdown("""
                Dictionaries are created using curly braces `{}`. Key-value pairs are separated by commas `,`.
                The key and value are separated by a colon `:`. Keys must be unique, but values can be duplicated.
                """)
                st.code("""
                my_dict = {"name": "John", "age": 25, "height": 1.8}
                """)

                st.markdown("""
                Values in a dictionary can be accessed using their key. You cannot use the index to access a value
                from a dictionary.
                """)
                st.code("""
                my_dict = {"name": "John", "age": 25, "height": 1.8}
                my_dict["name"]     # Output: "John"
                my_dict[0]          # TypeError: 'dict' object is not subscriptable (dictionaries do not have an index)
                """)

                st.markdown("""
                Values in a dictionary can be changed by assigning a new value to the key, even if the key does not
                already exist in the dictionary.
                """)
                st.code("""
                my_dict = {"name": "John", "age": 25, "height": 1.8}
                my_dict["age"] = 26
                my_dict["weight"] = 80
                # Output: {"name": "John", "age": 26, "height": 1.8, "weight": 80}
                """)

                st.markdown("""
                You can check if a key exists in a dictionary using the `in` operator within the dictionary.
                """)
                st.code("""
                my_dict = {"name": "John", "age": 25, "height": 1.8}
                "name" in my_dict       # Output: True
                "weight" in my_dict     # Output: False
                """)

                st.subheader("Commonly used dictionary methods")
                st.markdown("""
                Dictionary methods are most commonly used for iterating through the keys, values, or key-value pairs 
                within a loop.
                """)
                dict_method_dict = {
                    "dict.keys()": """
                                        my_dict = {"name": "John", "age": 25, "height": 1.8}
                                        my_dict.keys()
                                        # Output: dict_keys(["name", "age", "height"]) (returns a list of all the keys)
                                        """,
                    "dict.values()": """
                                        my_dict = {"name": "John", "age": 25, "height": 1.8}
                                        my_dict.values()
                                        # Output: dict_values(["John", 25, 1.8]) (returns a list of all the values)
                                        """,
                    "dict.items()": """
                                        my_dict = {"name": "John", "age": 25, "height": 1.8}
                                        my_dict.items()
                                        # Output: dict_items([("name", "John"), ("age", 25), ("height", 1.8)]) (returns 
                                        a list of all the key-value pairs)
                                        """}

                for method, desc in dict_method_dict.items():
                    op_col, desc_col = st.columns([1, 4])
                    op_col.code(method)
                    desc_col.code(desc)

                st.subheader("Iterating through a dictionary")
                st.markdown("""
                Dictionaries can be iterated through using a `for` loop. The default behaviour is to iterate through
                the keys, but you can also iterate through the values (using `.values()`) or the key-value pairs
                (using `.items()`).
                """)

                st.markdown("Assume we have the following dictionary:")
                st.code("""
                my_dict = {"name": "John", "age": 25, "height": 1.8}
                
                # Iterate through the keys
                for key in my_dict:
                    print(key)
                # Output: name
                #         age
                #         height
                
                # Iterate through the values
                for value in my_dict.values():
                    print(value)
                # Output: John
                #         25
                #         1.8
                
                # Iterate through the key-value pairs
                for key, value in my_dict.items():
                    print(key, value)
                # Output: name John
                #         age 25
                #         height 1.8
                """)

    with st.expander("Common Operators"):
        st.markdown("""
            - Arithmetic Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
                - `//` is floor division
                - `%` is modulo
                - `**` is exponentiation
            - Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
                - `==` is equal to
                - `!=` is not equal to
            - Logical Operators: `and`, `or`, `not`
            - Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
                - `+=` is add and assign, e.g. `x += 1` is equivalent to `x = x + 1`
                - `-=` is subtract and assign, e.g. `x -= 1` is equivalent to `x = x - 1`
                - ...etc.
            - Membership Operators: `in`, `not in`
                - `in` checks if an element is in a collection, e.g. `1 in [1, 2, 3]` equates to `True` and `4 in 
                [1, 2, 3]` equates to `False`
            - Identity Operators: `is`, `is not`
                - `is` checks if two objects are the same, e.g. `1 is 1` equates to `True` and `1 is 2` equates to 
                `False`
                - `is` differs to `==` in that `is` checks if two objects are the same object, whereas `==` checks if 
                two objects have the same value (e.g. `1 == 1.0` equates to `True`)
            """)

    with st.expander("If Statements"):
        st.markdown("""
        If statements are used to execute a block of code if a certain condition is met.
        """)
        st.code("""
        x = 1
        if x == 1:
            print("x is equal to 1")
        # Output: x is equal to 1
        """)

        st.markdown("""
        If statements can also be chained together using `elif` and `else` statements.
        """)
        st.code("""
        x = 1
        if x == 1:
            print("x is equal to 1")
        elif x == 2:
            print("x is equal to 2")
        else:
            print("x is not equal to 1 or 2")
        # Output: x is equal to 1
        """)

        st.markdown("""
        If statements can also be nested within each other.
        """)
        st.code("""
        x = 1
        y = 2
        if x == 1:
            if y == 2:
                print("x is equal to 1 and y is equal to 2")
        # Output: x is equal to 1 and y is equal to 2
        """)

    with st.expander("Loops"):
        st.markdown("""
        Loops are used to repeat a block of code a certain number of times. There are two types of loops in Python:
        for-loops and while-loops.
        """)

        for_tab, while_tab = st.tabs(["For Loops", "While Loops"])
        with for_tab:
            st.subheader("For Loops")
            subsubheader(st, "Index for-loops")
            st.write(
                "These for-loops typically use the `range()` function to generate a sequence of numbers to iterate over.")
            st.checkbox("Play Simulation (check to play, uncheck to pause)", value=False,
                        key="for_loop_ind_play")
            loop_ind_container = st.empty()
            loop_ind_container.code(st.session_state["for_loop_ind_gen"].__next__())

            subsubheader(st, "Value for-loops")
            st.write("""Analogous to Java's `for each` loops, these for-loops typically iterate over a collection of 
            values, such as a list or a string.""")
            st.checkbox("Play Simulation (check to play, uncheck to pause)", value=False,
                        key="for_loop_val_play")
            loop_val_container = st.empty()
            loop_val_container.code(st.session_state["for_loop_val_gen"].__next__())

        with while_tab:
            st.subheader("While Loops")
            st.write("While loops are used to repeat a block of code while a condition is true.")
            st.code("""
            i = 0
            while i < 10:
                print(i)
                i += 1
            # Output: 0
            #         1
            #         2
            #       ...
            #         9
            """)
            st.write("While loops can also be used to create infinite loops, which can be useful in some situations.")
            st.code("""
            while True:
                print("Hello")
            """)
            st.markdown("""To exit an infinite loop, you can use the `break` keyword to exit the loop. It is common 
            practice to use an `if` statement to check for a condition to exit the loop. For more keywords, see
            the Loop Control Statements section below.""")
            st.code("""
            i = 0
            while True:
                print("Hello")
                if i >= 10:
                    break # This will exit the loop
                else:
                    i += 1
                    
            # Output: Hello (10 times)
            """)

        st.subheader("Loop Control Statements")
        st.markdown("""There are two common control statements that can be used in loops:""")
        control_statements_dict = {
            "break": "Exits the loop",
            "continue": "Skips the current iteration of the loop. The loop will not exit, but will continue to the "
                        "next iteration by skipping the *rest of the code* in the current iteration."
        }

        for control_statement, description in control_statements_dict.items():
            control_col, desc_col = st.columns([0.25, 0.75])
            with control_col:
                st.code(control_statement)

            with desc_col:
                st.write(description)


        st.code("""
        for i in range(10):
            if i == 5:
                break       # Completely exits the loop
            elif i == 3:
                continue    # Skips the current iteration of the loop, i.e. skips printing 3 below
                            # Note that the rest of the code in the current iteration is skipped, as if we 
                            # went all the way back to the top of the loop code block.
            
            print(i)
            
        # Output: 0
        #         1
        #         2
        #         4
        """)

    return {"for_loop_ind_con": loop_ind_container, "for_loop_val_con": loop_val_container}
