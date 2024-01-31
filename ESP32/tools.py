"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
Reference repo: https://github.com/micropython/micropython/tree/master/examples/bluetooth
"""
import struct
from const import BLEConst
from ubluetooth import UUID

"""
struct.pack format

<: swap lower bit to high
>: normal
upper case: unsigned, integer start with 0
lower case: signed
h: integer size 2, looks like b'\x01\x00'
b: integer size 1, looks like b'\x01'
s: string
prefix numeric: repeated times
"""
PACK = struct.pack
UNPACK = struct.unpack

class BLETools(object):
    """
    Payload Generator Functions
    """
    # Advertising payloads are repeated packets of the following form:
    #   1 byte data length (N + 1)
    #   1 byte type (see constants below)
    #   N bytes type-specific data
    @staticmethod
    def advertising_generic_payload(limited_disc=False, br_edr=False, name=None, services=None, appearance=0):
        """
        Generate a payload to be passed to gap_advertise(adv_data=...).
        """
        payload = bytearray()

        def _append(adv_type, value):
            nonlocal payload
            payload += PACK('BB', len(value) + 1, adv_type) + value

        _append(BLEConst.ADType.AD_TYPE_FLAGS, PACK('B', (0x01 if limited_disc else 0x02) + (0x00 if br_edr else 0x04)))

        if name:
            _append(BLEConst.ADType.AD_TYPE_COMPLETE_LOCAL_NAME, name)

        if services:
            for uuid in services:
                b = bytes(uuid)
                if len(b) == 2:
                    _append(BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 4:
                    _append(BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 16:
                    _append(BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE, b)

        # See org.bluetooth.characteristic.gap.appearance.xml
        _append(BLEConst.ADType.AD_TYPE_APPEARANCE, PACK('<h', appearance))

        return payload

    @staticmethod
    def advertising_hid_payload(services=None, appearance=0):
        """
        Generate paylaod for HID device
        """
        payload = bytearray()

        def _append(adv_type, value):
            nonlocal payload
            payload += PACK('BB', len(value) + 1, adv_type) + value

        _append(BLEConst.ADType.AD_TYPE_FLAGS, PACK('B', 0x06))

        if services:
            for uuid in services:
                b = bytes(uuid)
                if len(b) == 2:
                    _append(BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 4:
                    _append(BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 16:
                    _append(BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE, b)

        _append(BLEConst.ADType.AD_TYPE_APPEARANCE, PACK('<h', appearance))
        _append(BLEConst.ADType.AD_TYPE_MANUFACTURER_SPECIFIC_DATA, PACK('<h3b', 0x0006, 0x03, 0x00, 0x80)) # 0x004c, 0x02, 0x00, 0x80))

        return payload

    @staticmethod
    def advertising_resp_payload(name=None, services=None):
        """
        Generate payload for Scan Response
        """
        payload = bytearray()

        def _append(adv_type, value):
            nonlocal payload
            payload += PACK('BB', len(value) + 1, adv_type) + value

        if name:
            _append(BLEConst.ADType.AD_TYPE_COMPLETE_LOCAL_NAME, name)

        if services:
            for uuid in services:
                b = bytes(uuid)
                if len(b) == 2:
                    _append(BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 4:
                    _append(BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE, b)
                elif len(b) == 16:
                    _append(BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE, b)

        return payload

    @staticmethod
    def advertising_eddystone_payload(frame_type, **kwargs):
        """
        According to frame_type generate payload for Eddystone.

        frame_type:
            BLEConst.Eddystone.EDDYSTONE_URL
            BLEConst.Eddystone.EDDYSTONE_UID
            BLEConst.Eddystone.EDDYSTONE_EID
        """    
        payload = bytearray()

        def _append(adv_type, value):
            nonlocal payload
            payload += PACK('BB', len(value) + 1, adv_type) + value

        _append(BLEConst.ADType.AD_TYPE_FLAGS, PACK('B', 0x06))
        _append(BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, bytes(UUID(BLEConst.Eddystone.EDDYSTONE_UUID)))

        # https://github.com/google/eddystone/tree/master/eddystone-url
        if frame_type == BLEConst.Eddystone.EDDYSTONE_URL:
            assert kwargs.get("url") is not None, ValueError("missing url param for Eddystone-URL")
            assert kwargs.get("tx_power") is not None, ValueError("missing tx_power param for Eddystone-URL")

            url = kwargs.get("url")
            tx_power = kwargs.get("tx_power")
            url, proto = BLETools.__shorten_beacon_url(url)

            _append(BLEConst.ADType.AD_TYPE_SERVICE_DATA, bytes(UUID(BLEConst.Eddystone.EDDYSTONE_UUID)) + PACK("3B", BLEConst.Eddystone.EDDYSTONE_URL, tx_power, proto) + url.encode())
        # https://github.com/google/eddystone/tree/master/eddystone-uid
        elif frame_type == BLEConst.Eddystone.EDDYSTONE_UID:
            assert kwargs.get("namespace_id") is not None, ValueError("missing namespace_id param for Eddystone-UID")
            assert kwargs.get("instance_id") is not None, ValueError("missing instance_id param for Eddystone-UID")
            assert kwargs.get("tx_power") is not None, ValueError("missing tx_power param for Eddystone-UID")

            namespace_id = kwargs.get("namespace_id")
            instance_id = kwargs.get("instance_id")
            tx_power = kwargs.get("tx_power")

            _append(BLEConst.ADType.AD_TYPE_SERVICE_DATA, bytes(UUID(BLEConst.Eddystone.EDDYSTONE_UUID)) + PACK("2B", BLEConst.Eddystone.EDDYSTONE_UID, tx_power) + namespace_id + instance_id)
        # elif frame_type == BLEConst.Eddystone.EDDYSTONE_EID:
        #     assert kwargs.get("ephemeral_id") is not None, ValueError("missing ephemeral_id param for Eddystone-EID")
        #     assert kwargs.get("tx_power") is not None, ValueError("missing tx_power param for Eddystone-EID")
            
        #     ephemeral_id = kwargs.get("ephemeral_id")
        #     tx_power = kwargs.get("tx_power")

        #     _append(BLEConst.ADType.AD_TYPE_SERVICE_DATA, bytes(UUID(BLEConst.Eddystone.EDDYSTONE_UUID)) + PACK("2B", BLEConst.Eddystone.EDDYSTONE_EID, tx_power) + ephemeral_id)
        else:
            raise ValueError("Unknown frame_type")

        return payload

    @staticmethod
    def advertising_ibeacon_payload(proximity_uuid, major, minor, tx_power):
        """
        Generate paylaod for Apple iBeacon device
        """
        assert isinstance(proximity_uuid, UUID), TypeError("proximity uuid must be type of UUID")

        payload = bytearray()
        proximity_uuid = list(bytes(proximity_uuid))
        proximity_uuid.reverse()
        proximity_uuid = bytes(proximity_uuid)

        def _append(adv_type, value):
            nonlocal payload
            payload += PACK('BB', len(value) + 1, adv_type) + value

        _append(BLEConst.ADType.AD_TYPE_FLAGS, PACK('B', 0x06))
        _append(BLEConst.ADType.AD_TYPE_MANUFACTURER_SPECIFIC_DATA, PACK('<H2B', 0x004C, 0x02, 0x15) + proximity_uuid + PACK(">2HB", major, minor, tx_power))

        return payload

    """
    Payload Decode Functions
    """
    @staticmethod
    def __decode_field(payload, adv_type):
        i = 0
        result = []

        if isinstance(payload, memoryview):
            payload = bytes(payload)

        while i + 1 < len(payload):
            if payload[i + 1] == adv_type:
                result.append(payload[i + 2:i + payload[i] + 1])
            i += 1 + payload[i]
        return result

    @staticmethod
    def decode_name(payload):
        """
        Decode advertising device name from payload
        """
        n = BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_COMPLETE_LOCAL_NAME)
        return str(n[0], 'utf-8') if n else ''

    @staticmethod
    def decode_services_data(payload):
        """
        Decode and split Service Data from payload
        
        Return: Service UUID and their Data in separated list
        """
        services = []
        data = []
        for u in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_SERVICE_DATA):
            services.append(UUID(u[:2]))
            data.append(u[2:])
        return services, data

    @staticmethod
    def decode_beacon_data(payload):
        """
        Decode beacon payload into a sequence list
        
        Return:
            for iBeacon: BeaconType, proximity_uuid, major, minor, tx_power
        """
        for msd in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_MANUFACTURER_SPECIFIC_DATA):
            if msd.find(BLEConst.iBeacon.IBEACON_PREFIX) == 0:
                return BLEConst.BeaconType.BEACON_IBEACON, BLETools.__decode_uuid(msd[4:20]), BLETools.bytes_to_int(msd[-5:-3]), BLETools.bytes_to_int(msd[-3:-1]), BLETools.convert_tx_power_level(level_int=ord(msd[-1:]))

        # for sd in self.__decode_field(payload, BLEConst.ADType.AD_TYPE_SERVICE_DATA):
        #     return BLEConst.BeaconType.BEACON_EDDYSTONE_UID, tx_power, namespace_id, instance_id

        return None,

    @staticmethod
    def __decode_uuid(uuid):
        assert isinstance(uuid, bytes) and len(uuid) == 16, ValueError("uuid value error")

        result = ""
        minus_pos = [4, 6, 8, 10]

        for index in range(16):
            if index in minus_pos:
                result += "-"
            result += '%02x' % uuid[index]

        return result

    @staticmethod
    def decode_mac(addr):
        """
        Decode readable mac address from advertising addr
        """
        if isinstance(addr, memoryview):
            addr = bytes(addr)

        assert isinstance(addr, bytes) and len(addr) == 6, ValueError("mac address value error")
        return ":".join(['%02X' % byte for byte in addr])

    @staticmethod
    def decode_services(payload):
        """
        Decode Service UUIDs from payload
        """
        services = []
        for u in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE):
            services.append(UUID(UNPACK('<h', u)[0]))
        for u in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE):
            services.append(UUID(UNPACK('<d', u)[0]))
        for u in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE):
            services.append(UUID(u))
        return services

    """
    Other Functions
    """
    @staticmethod
    def is_ibeacon_payload(payload):
        """
        Determine if it is iBeacon payload
        """
        for msd in BLETools.__decode_field(payload, BLEConst.ADType.AD_TYPE_MANUFACTURER_SPECIFIC_DATA):
            if msd.find(BLEConst.iBeacon.IBEACON_PREFIX) == 0:
                return True
        
        return False

    @staticmethod
    def convert_tx_power_level(level_dBm=None, level_int=None):
        """
        Convert tx power level between dBm and int

        How to determine tx power level: https://github.com/google/eddystone/tree/master/eddystone-url#tx-power-level
        
        In short:
            0xED-0xFF=237-255=-18
            0x12=18
        """
        result = None

        if level_int:
            result = level_int
            assert level_int in range(156, 256) or level_int in range(21), ValueError("tx power level int must be in range 156 to 255 or 0 to 20")

            if level_int > 20:
                result = level_int - 0xFF - 1
        else:
            result = level_dBm
            assert level_dBm in range(-100, 21), ValueError("tx power level dBm must be in range -100 to +20")

            if level_dBm < 0:
                result = level_dBm + 0xFF + 1

        return result

    @staticmethod
    def validate_intervals(min_interval, max_interval, latency, timeout):
        """
        Verify parameters match the requirements of Apple Connection Parameters
        """

        """
        The connection parameter request may be rejected if it does not comply with all of these rules:
        Slave Latency ≤ 30 1
        2s ≤ connSupervisionTimeout ≤ 6s 1
        Interval Min modulo 15ms == 0
        Interval Min ≥ 15ms 1
        One of the following:
            Interval Min + 15ms ≤ Interval Max 1
            Interval Min == Interval Max == 15ms
        Interval Max * (Slave Latency + 1) ≤ 2s 1
        Interval Max * (Slave Latency + 1) * 3 < connSupervisionTimeout
        """
        rate = 1.25 # unit ms
        timeout_rate = 10 * rate # unit ms

        min_interval *= rate
        max_interval *= rate
        timeout *= timeout_rate

        print("min: {}, max: {}, latency: {}, timeout: {}".format(min_interval, max_interval, latency, timeout))

        if latency > 30:
            print("error: latency must <= 30")
            return False

        if timeout < 2000 and timeout > 6000:
            print("error: timeout must between 2s~6s")
            return False

        if min_interval < 15:
            print("error: min must >= 15ms")
            return False
        elif min_interval + 15 > max_interval:
            print("error: min + 15ms must <= max")
            return False
        
        if max_interval * (latency + 1) > 2000:
            print("error: max * (latency + 1) must <= 2s")
            return False

        if max_interval * (latency + 1) * 3 >= timeout:
            print("error: max * (latency + 1) * 3 must < timeout")
            return False

        return True

    @staticmethod
    def bytes_to_int(value, big_end=True, signed=False):
        assert isinstance(value, bytes), ValueError("value must be bytes")
        return int.from_bytes(value, "big" if big_end else "little", signed)

    @staticmethod
    def __shorten_beacon_url(url):
        """
        Shorten the url for Eddystone-URL
        
        Reference: http://www.espruino.com/modules/ble_eddystone.js
        """
        proto = 3 # https
        repl = ["com", "org", "edu", "net", "info", "biz", "gov"]

        if url[:12] == "https://www.":
            proto = 1
            url = url[12:]
        elif url[:4] == "www.":
            proto = 1
            url = url[4:]
        elif url[:8] == "https://":
            url = url[8:]
        elif url[:7] == "http://":
            raise ValueError("Eddystone URL need to be HTTPS")

        for index in range(len(repl)):
            url = url.replace("." + repl[index] + "/", str(index))
            url = url.replace("." + repl[index], str(index + 7))

        if len(url) > 17:
            raise ValueError("Max URL length is 17")

        return url, proto

"""
Demos
"""
def demo_validate_intervals():
    BLETools.validate_intervals(40, 80, 10, 300)

def demo_hid():
    payload = BLETools.advertising_hid_payload()
    print(payload)

def demo_beacon_url():
    url = "https://walkline.com"
    tx_power = BLETools.convert_tx_power_level(-50)

    payload = BLETools.advertising_eddystone_payload(BLEConst.Eddystone.EDDYSTONE_URL, url=url, tx_power=tx_power)
    print(payload)
    # bytearray(b'\x02\x01\x04\x03\x03\xaa\xfe\x0f\x16\xaa\xfe\x10\xce\x03walkline7')

def demo_beacon_uid():
    namespace_id = b'\xf33wu\xaf\x7f\xe0S\xed\x93'
    instance_id = b'\xb6\x12\xffK\x917'
    tx_power = BLETools.convert_tx_power_level(-50)

    payload = BLETools.advertising_eddystone_payload(BLEConst.Eddystone.EDDYSTONE_UID, namespace_id=namespace_id, instance_id=instance_id, tx_power=tx_power)
    print(payload)
    # bytearray(b'\x02\x01\x04\x03\x03\xaa\xfe\x15\x16\xaa\xfe\x00\xce\xf33wu\xaf\x7f\xe0S\xed\x93\xb6\x12\xffK\x917')

def demo_decode_beacon_data():
    result = BLETools.decode_beacon_data(b"\x02\x01\x06\x1a\xffL\x00\x02\x15MyA\x9f\xb1\x80O\xf6\x8c\xb6\x9f\xa1\xb5\x7f\xb1h'\x1a'f\xc7")
    print(result)

# def demo():
#     payload = advertising_generic_payload(name='micropython', services=[bluetooth.UUID(0x181A), bluetooth.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')])
#     print(payload)
#     print(BLETools.decode_name(payload))
#     print(BLETools.decode_services(payload))

if __name__ == '__main__':
    # demo()
    # demo_hid()
    # demo_beacon_url()
    demo_decode_beacon_data()
    # demo_beacon_uid()
    # demo_validate_intervals()
    # print(decode_services_data(b'\x02\x01\x06\x0f\x16\x95\xfe0X[\x05\xef\xfd\x15\x0c8\xc1\xa4\x08')[0])
