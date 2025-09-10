# In this program we will see how to use function_attributes

def calls():
    if not hasattr(calls,"call_counter"):
        calls.call_counter=0 # Initialised  Attribute # Present in __dict__ default attribute
    calls.call_counter+=1
    return calls.call_counter

calls()
calls()
calls()
print(f"No. of calls made:{calls.call_counter}")
print(f"Function Attributes of the function are:{calls.__dict__}")

    