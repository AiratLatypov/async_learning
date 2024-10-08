from chapter_14.custom_future_class_14_8 import CustomFuture

future = CustomFuture()

i = 0

while True:
    try:
        print("Checking future...")
        gen = future.__await__()
        gen.send(None)
        print("Future is not done...")
        if i == 1:
            print("Setting future value...")
            future.set_result("Finished!")
        i = i + 1
    except StopIteration as si:
        print(f"Value is: {si.value}")
        break

# Checking future...
# Future is not done...
# Checking future...
# Future is not done...
# Setting future value...
# Checking future...
# Value is: Finished!
        