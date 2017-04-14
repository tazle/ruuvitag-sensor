class RunFlag(object):
    """
    Wrapper for boolean run flag

    Attributes:
        running (bool): Defines if function should continue execution
    """

    running = True


class Config(object):
    """
    Configuration parameters

    Attributes:
        device (string): BLE device (default hci0)
    """

    device = 'hci0'
