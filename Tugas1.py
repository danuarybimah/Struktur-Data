# Nomer 1 A
# def print_item(n):
#     for i in range(n):
#         print(f"Loop 1: {i}")

#     for j in range(n):
#         print(f"Loop 2: {j}")

# print_item(5)

def Print_item(n):
    for i in range(n):
        print(i)
    for i in range(n):
        for j in range(n):
            print(i, j)

Print_item(5)