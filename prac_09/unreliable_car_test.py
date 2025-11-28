from unreliable_car import UnreliableCar


def test_unreliable_car():
    """Test the driving performance of UnreliableCars with different reliabilities."""
    high_reliability_car = UnreliableCar("High-Reliable", 1000, 90.0)
    total_attempts = 100
    successful_drives = 0
    total_distance_driven = 0

    for i in range(total_attempts):
        distance = high_reliability_car.drive(10)
        if distance > 0:
            successful_drives += 1
            total_distance_driven += distance
        high_reliability_car.fuel = 1000
    print("Test 1: High-reliability vehicle (90%)")
    print(f"Number of tests:{total_attempts}")
    print(f"Number of successful driving trips:{successful_drives}")
    print(f"Actual driving probability:{successful_drives / total_attempts * 100:.2f}%")
    print(f"Total driving distance:{total_distance_driven}km")

    low_reliability_car = UnreliableCar("Low-Reliable", 1000, 10.0)
    successful_drives = 0
    total_distance_driven = 0

    for i in range(total_attempts):
        distance = low_reliability_car.drive(10)
        if distance > 0:
            successful_drives += 1
            total_distance_driven += distance
        low_reliability_car.fuel = 1000
    print("Test 2: Low reliability (10%)")
    print(f"Number of tests:{total_attempts}")
    print(f"Number of successful driving trips:{successful_drives}")
    print(f"Actual driving probability:{successful_drives / total_attempts * 100:.2f}%")
    print(f"Total driving distance:{total_distance_driven}km")


if __name__ == "__main__":
    test_unreliable_car()