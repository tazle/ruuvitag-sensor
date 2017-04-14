class RunFlag(object):
    """
    Wrapper for boolean run flag

    Attributes:
        running (bool): Defines if function should continue execution
    """

    running = True


class BleConfig(object):
    """
    Bluetooth configuration parameters

    Attributes:
        device (bool): BLE device (default hci0)
    """

    device = 'hci0'
