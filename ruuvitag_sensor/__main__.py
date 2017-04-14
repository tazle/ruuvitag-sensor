import sys
import argparse

import ruuvitag_sensor
from ruuvi import RuuviTagSensor
from log import logger  # pylint: disable=E0611
from common import Config


def my_excepthook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

    if not issubclass(exctype, KeyboardInterrupt):
        logger.critical(value)

sys.excepthook = my_excepthook

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--get', dest='mac_address', help='Get data')
    parser.add_argument('-f', '--find', action='store_true',
                        dest='find_action', help='Find broadcasting RuuviTags')
    parser.add_argument('-l', '--latest', action='store_true',
                        dest='latest_action', help='Get latest data for found RuuviTags')
    parser.add_argument('-s', '--stream', action='store_true',
                        dest='stream_action', help='Stream broadcasts from all RuuviTags')
    parser.add_argument('-d', '--device', dest='ble_device', help='Set BLE device (default hci0)')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(ruuvitag_sensor.__version__))
    args = parser.parse_args()

    config = Config()

    if args.ble_device:
        config.device = args.ble_device

    if args.mac_address:
        sensor = RuuviTagSensor(args.mac_address, config)
        state = sensor.update()
        print(state)
    elif args.find_action:
        RuuviTagSensor.find_ruuvitags(config)
    elif args.latest_action:
        datas = RuuviTagSensor.get_data_for_sensors(config)
        print(datas)
    elif args.stream_action:
        RuuviTagSensor.get_datas(lambda x: print('%s - %s' % (x[0], x[1]), config=config))
    else:
        parser.print_usage()
