name = input()
id = int(input())
chinese = int(input())
computerScience = int(input())
programmingDesign = int(input())

if chinese >= 0 and computerScience >= 0 and programmingDesign >= 0:
    total = chinese + computerScience + programmingDesign
    print(f"Name:{name}")
    print(f"Id:{id}")
    print(f"Total:{total}")
    print(f"Average:{int(total / 3)}")
