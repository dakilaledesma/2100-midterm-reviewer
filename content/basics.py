from content.generators import for_loop_ind_gen
from utils.utils import subsubheader
def basics(st):
    if not st.session_state.get("for_loop_ind_gen"):
        st.session_state["for_loop_ind_gen"] = for_loop_ind_gen()

    st.header("Python Basics")
    with st.expander("Common Data Types"):
        st.subheader("Numeric Types")
        st.markdown("""
            Used to represent numbers
            - Integers: Numbers without decimal points
            - Floats: Numbers with decimal points
            """)
        st.subheader("Boolean Types")
        st.markdown("""
            Used to represent truth values, primarily in conditional statements
            - `True` or `False`
            """)
        st.subheader("Strings")

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
                - `in` checks if an element is in a collection, e.g. `1 in [1, 2, 3]` equates to `True` and `4 in [1, 2, 3]` equates to `False`
            - Identity Operators: `is`, `is not`
                - `is` checks if two objects are the same, e.g. `1 is 1` equates to `True` and `1 is 2` equates to `False`
                - `is` differs to `==` in that `is` checks if two objects are the same object, whereas `==` checks if two objects have the same value (e.g. `1 == 1.0` equates to `True`)
            """)

    with st.expander("Loops"):
        st.subheader("For Loops")
        subsubheader(st, "Index for-loops")
        st.write(
            "These for-loops typically use the `range()` function to generate a sequence of numbers to iterate over.")
        st.checkbox("Play Simulation (check to play, uncheck to pause)", value=False,
                                           key="for_loop_ind_play")
        loop_ind_container = st.empty()
        loop_ind_container.code(st.session_state["for_loop_ind_gen"].__next__())

        subsubheader(st, "Value for-loops")
        st.write(
            "Analogous to Java's `for each` loops, these for-loops typically iterate over a collection of values, such as a list or a string.")



    return {"for_loop_ind_con": loop_ind_container}
