

class TrafficLight:
    """
    Class to simulate a traffic light
    """
    def __init__(self):
        self.state = "green"

    def change_state(self):
        """
        Function to change the state of the traffic light
        """
        if self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"
        else:
            self.state = "green"

def test_state_transition():
    """
    Function to test state transition using state transition testing
    """
    traffic_light = TrafficLight()

    # Test transition from green to yellow
    traffic_light.change_state()
    assert traffic_light.state == "yellow", f"Expected yellow but got {traffic_light.state}"

    # Test transition from yellow to red
    traffic_light.change_state()
    assert traffic_light.state == "red", f"Expected red but got {traffic_light.state}"

    # Test transition from red to green
    traffic_light.change_state()
    assert traffic_light.state == "green", f"Expected green but got {traffic_light.state}"

    # Test transition from green to yellow to red
    traffic_light.change_state()
    assert traffic_light.state == "yellow", f"Expected yellow but got {traffic_light.state}"
    traffic_light.change_state()
    assert traffic_light.state == "red", f"Expected red but got {traffic_light.state}"

    # Test transition from red to green to yellow
    traffic_light.change_state()
    assert traffic_light.state == "green", f"Expected green but got {traffic_light.state}"
    traffic_light.change_state()
    assert traffic_light.state == "yellow", f"Expected yellow but got {traffic_light.state}"

if __name__ == "__main__":
    test_state_transition()

    print("All tests passed!")
