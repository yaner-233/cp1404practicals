from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi_fare():
    """Test fare calculation for SilverServiceTaxi with rounding."""
    taxi = SilverServiceTaxi("Test Taxi", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    assert taxi.get_fare() == 48.8


def test_flagfall_included():
    """Test that flagfall is added even for 0km trips."""
    taxi = SilverServiceTaxi("Test", 100, 1)
    taxi.start_fare()
    taxi.drive(0)
    assert taxi.get_fare() == 4.50


def test_fanciness_scaling():
    """Test that price_per_km scales with fanciness."""
    taxi = SilverServiceTaxi("Test", 100, 3)
    expected_price = 1.23 * 3
    assert taxi.price_per_km == expected_price


if __name__ == "__main__":
    test_silver_service_taxi_fare()
    test_flagfall_included()
    test_fanciness_scaling()
    print("All tests passed!")