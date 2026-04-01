from exceptions import *

class DeviceRecord:
    def __init__(self, status, wifi_connection):
        self.status = status
        self.wifi_connection = wifi_connection

class ATMDeviceController:

    def withdraw(self, account_id: str, amount: float):
        handle = self._get_valid_handle()
        record = self._get_active_device(handle)
        self._ensure_network_connection(record)
        self._ensure_sufficient_balance(account_id, amount)

        self._dispense_cash(handle, amount)
        return "SUCCESS"

    def _get_valid_handle(self):
        handle = get_handle("DEV1")
        if handle == "INVALID":
            raise DeviceNotFoundException("Device not found")
        return handle

    def _get_active_device(self, handle):
        record = retrieve_device_record(handle)
        if record.status == "SUSPENDED":
            raise DeviceLockedException("Device is locked")
        return record

    def _ensure_network_connection(self, record):
        if record.wifi_connection != "CONNECTED":
            raise NetworkConnectionException("Network error")

    def _ensure_sufficient_balance(self, account_id, amount):
        if get_balance(account_id) < amount:
            raise InsufficientFundsException("Insufficient funds")

    def _dispense_cash(self, handle, amount):
        dispense_cash(handle, amount)

def get_handle(device_id):
    return "VALID"

def retrieve_device_record(handle):
    return DeviceRecord("ACTIVE", "CONNECTED")

def get_balance(account_id):
    return 1000

def dispense_cash(handle, amount):
    print(f"Dispensed {amount}")

if __name__ == "__main__":
    atm = ATMDeviceController()

    try:
        result = atm.withdraw("ACC123", 200)
        print(result)

    except DeviceLockedException as e:
        print(e)

    except InsufficientFundsException as e:
        print(e)

    except NetworkConnectionException as e:
        print(e)

    except DeviceNotFoundException as e:
        print(e)