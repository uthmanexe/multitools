def kg_cm(weight, height):
    bmi = weight / (height * height)


def calculate():
    while True:
        metric = input(
            "Choose a metric system\n 1. kg & cm\n2. lbs & ft").strip().lower()

        if metric.lower() == "1":
            weight = input("Enter your weight(kg): ").strip()
            if weight.isdigit() and weight > 0:
                pass
            else:
                print("Invalid input!")
                weight = input("Enter a valid weight: ").strip()

            height = input("Enter your weight(cm): ")
            if height.isdigit() and height > 0:
                height = height/100
            else:
                print("Invalid input!")
                height = input("Enter a valid height: ").strip()

        elif metric.lower() == "2":
            weight = input("Enter your weight(lbs): ").strip()
            if weight.isdigit() and weight > 0:
                pass
            else:
                print("Invalid input!")
                weight = input("Enter a valid weight: ").strip()

            height = input("Enter your weight(ft): ")
            if height.isdigit() and height > 0:
                pass
            else:
                print("Invalid input!")
                height = input("Enter a valid height: ").strip()
