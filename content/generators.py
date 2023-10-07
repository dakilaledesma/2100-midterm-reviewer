import streamlit as st


def for_loop_ind_gen():
    num = 0
    phase = 0
    while True:
        if phase == 0:
            code_str = f"""
            for i in range(10):             ←
                print(i)
            # Output: (start of loop)
            """
            phase = 1
        elif phase == 1:
            code_str = f"""
            for i → {num} in range(10):         ←
                print(i)
            # Output: (i currently has a value of {num})
            """
            phase = 2
        elif phase == 2:
            code_str = f"""
            for i → {num} in range(10): 
                print(i → {num})                ←
            # Output: (therefore, i in the print statement has a value of {num})
            """
            phase = 3
        elif phase == 3:
            code_str = f"""
            for i → {num} in range(10): 
                print(i)                
            # Output: {num}                     ←
            """
            phase = 4
        else:
            code_str = f"""
            for i → {num} + 1 in range(10):     ←
                print(i)                
            # Output: (restarting to top of loop, increment i by 1)                 
            """

            if num == 9:
                code_str = f"""
                for i in range(10):
                    print(i)                
                # Output: (end of loop, range(10) has been exhausted)                 
                """
                phase = 0
                num = 0
            else:
                code_str = f"""
                for i → {num} + 1 in range(10):     ←
                    print(i)                
                # Output: (restarting to top of loop, increment i by 1)                 
                """
                phase = 1
                num += 1

        yield code_str


def for_loop_val_gen():
    num = 0
    phase = 0
    while True:
        if phase == 0:
            code_str = f"""
            for i in range(10):
                print(i)
            # Output: (start of loop)
            """
            phase = 1
        elif phase == 1:
            code_str = f"""
            for i → {num} in range(10):
                print(i)
            # Output: (i currently has a value of {num})
            """
            phase = 2
        elif phase == 2:
            code_str = f"""
            for i → {num} in range(10): 
                print(i → {num})                
            # Output: (therefore, i in the print statement has a value of {num})
            """
            phase = 3
        elif phase == 3:
            code_str = f"""
            for i → {num} in range(10): 
                print(i)                
            # Output: {num}
            """
            phase = 4
        else:
            code_str = f"""
            for i → {num} + 1 in range(10):
                print(i)                
            # Output: (restarting to top of loop, increment i by 1)                 
            """

            if num == 9:
                code_str = f"""
                for i in range(10):
                    print(i)                
                # Output: (end of loop, range(10) has been exhausted)                 
                """
                phase = 0
                num = 0
            else:
                code_str = f"""
                for i → {num} + 1 in range(10):
                    print(i)                
                # Output: (restarting to top of loop, increment i by 1)                 
                """
                phase = 1
                num += 1

        yield code_str
