'''
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
'''
from micropython import const


FLAG_BROADCAST = const(0x0001)
FLAG_READ = const(0x0002)
FLAG_WRITE_NO_RESPONSE = const(0x0004)
FLAG_WRITE = const(0x0008)
FLAG_NOTIFY = const(0x0010)
FLAG_INDICATE = const(0x0020)
FLAG_AUTHENTICATED_SIGNED_WRITE = const(0x0040)

FLAG_AUX_WRITE = const(0x0100)
FLAG_READ_ENCRYPTED = const(0x0200)
FLAG_READ_AUTHENTICATED = const(0x0400)
FLAG_READ_AUTHORIZED = const(0x0800)
FLAG_WRITE_ENCRYPTED = const(0x1000)
FLAG_WRITE_AUTHENTICATED = const(0x2000)
FLAG_WRITE_AUTHORIZED = const(0x4000)


class BLEConst(object):
    class IRQ(object):
        IRQ_CENTRAL_CONNECT = const(1)
        IRQ_CENTRAL_DISCONNECT = const(2)
        IRQ_GATTS_WRITE = const(3)
        IRQ_GATTS_READ_REQUEST = const(4)
        IRQ_SCAN_RESULT = const(5)
        IRQ_SCAN_DONE = const(6)
        IRQ_PERIPHERAL_CONNECT = const(7)
        IRQ_PERIPHERAL_DISCONNECT = const(8)
        IRQ_GATTC_SERVICE_RESULT = const(9)
        IRQ_GATTC_SERVICE_DONE = const(10)
        IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
        IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
        IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
        IRQ_GATTC_DESCRIPTOR_DONE = const(14)
        IRQ_GATTC_READ_RESULT = const(15)
        IRQ_GATTC_READ_DONE = const(16)
        IRQ_GATTC_WRITE_DONE = const(17)
        IRQ_GATTC_NOTIFY = const(18)
        IRQ_GATTC_INDICATE = const(19)
        IRQ_GATTS_INDICATE_DONE = const(20)
        IRQ_MTU_EXCHANGED = const(21)
        IRQ_L2CAP_ACCEPT = const(22)
        IRQ_L2CAP_CONNECT = const(23)
        IRQ_L2CAP_DISCONNECT = const(24)
        IRQ_L2CAP_RECV = const(25)
        IRQ_L2CAP_SEND_READY = const(26)
        IRQ_CONNECTION_UPDATE = const(27)
        IRQ_ENCRYPTION_UPDATE = const(28)
        IRQ_GET_SECRET = const(29)
        IRQ_SET_SECRET = const(30)


    class ADDRESS_MODE(object):
        '''
        Address mode for BLE.config()
        '''
        PUBLIC = const(0x00)
        RANDOM = const(0x01)
        RPA = const(0x02)
        NRPA = const(0x03)


    class IO_CAPABILITIES(object):
        '''
        I/O capabilities for BLE.config()
        '''
        IO_CAPABILITY_DISPLAY_ONLY = const(0)
        IO_CAPABILITY_DISPLAY_YESNO = const(1)
        IO_CAPABILITY_KEYBOARD_ONLY = const(2)
        IO_CAPABILITY_NO_INPUT_OUTPUT = const(3)
        IO_CAPABILITY_KEYBOARD_DISPLAY = const(4)


    class GATTS_READ_REQUEST_RETURN_CODE(object):
        GATTS_NO_ERROR = const(0x00)
        GATTS_ERROR_READ_NOT_PERMITTED = const(0x02)
        GATTS_ERROR_WRITE_NOT_PERMITTED = const(0x03)
        GATTS_ERROR_INSUFFICIENT_AUTHENTICATION = const(0x05)
        GATTS_ERROR_INSUFFICIENT_AUTHORIZATION = const(0x08)
        GATTS_ERROR_INSUFFICIENT_ENCRYPTION = const(0x0f)


    class PASSKEY_ACTION(object):
        '''
        Available actions for IRQ_PASSKEY_ACTION event
        '''
        PASSKEY_ACTION_NONE = const(0)
        PASSKEY_ACTION_INPUT = const(2)
        PASSKEY_ACTION_DISPLAY = const(3)
        PASSKEY_ACTION_NUMERIC_COMPARISON = const(4)


    class ADType(object):
        '''
        Advertising Data Type
        '''
        AD_TYPE_FLAGS = const(0x01) # Flags for discoverability.
        AD_TYPE_16BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x02) # Partial list of 16 bit service UUIDs.
        AD_TYPE_16BIT_SERVICE_UUID_COMPLETE = const(0x03) # Complete list of 16 bit service UUIDs.
        AD_TYPE_32BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x04) # Partial list of 32 bit service UUIDs.
        AD_TYPE_32BIT_SERVICE_UUID_COMPLETE = const(0x05) # Complete list of 32 bit service UUIDs.
        AD_TYPE_128BIT_SERVICE_UUID_MORE_AVAILABLE = const(0x06) # Partial list of 128 bit service UUIDs.
        AD_TYPE_128BIT_SERVICE_UUID_COMPLETE = const(0x07) # Complete list of 128 bit service UUIDs.
        AD_TYPE_SHORT_LOCAL_NAME = const(0x08) # Short local device name.
        AD_TYPE_COMPLETE_LOCAL_NAME = const(0x09) # Complete local device name.
        AD_TYPE_TX_POWER_LEVEL = const(0x0A) # Transmit power level.
        AD_TYPE_CLASS_OF_DEVICE = const(0x0D) # Class of device.
        AD_TYPE_SIMPLE_PAIRING_HASH_C = const(0x0E) # Simple Pairing Hash C.
        AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R = const(0x0F) # Simple Pairing Randomizer R.
        AD_TYPE_SECURITY_MANAGER_TK_VALUE = const(0x10) # Security Manager TK Value.
        AD_TYPE_SECURITY_MANAGER_OOB_FLAGS = const(0x11) # Security Manager Out Of Band Flags.
        AD_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE = const(0x12) # Slave Connection Interval Range.
        AD_TYPE_SOLICITED_SERVICE_UUIDS_16BIT = const(0x14) # List of 16-bit Service Solicitation UUIDs.
        AD_TYPE_SOLICITED_SERVICE_UUIDS_128BIT = const(0x15) # List of 128-bit Service Solicitation UUIDs.
        AD_TYPE_SERVICE_DATA = const(0x16) # Service Data - 16-bit UUID.
        AD_TYPE_PUBLIC_TARGET_ADDRESS = const(0x17) # Public Target Address.
        AD_TYPE_RANDOM_TARGET_ADDRESS = const(0x18) # Random Target Address.
        AD_TYPE_APPEARANCE = const(0x19) # Appearance.
        AD_TYPE_ADVERTISING_INTERVAL = const(0x1A) # Advertising Interval. 
        AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS = const(0x1B) # LE Bluetooth Device Address.
        AD_TYPE_LE_ROLE = const(0x1C) # LE Role.
        AD_TYPE_SIMPLE_PAIRING_HASH_C256 = const(0x1D) # Simple Pairing Hash C-256.
        AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R256 = const(0x1E) # Simple Pairing Randomizer R-256.
        AD_TYPE_SERVICE_DATA_32BIT_UUID = const(0x20) # Service Data - 32-bit UUID.
        AD_TYPE_SERVICE_DATA_128BIT_UUID = const(0x21) # Service Data - 128-bit UUID.
        AD_TYPE_3D_INFORMATION_DATA = const(0x3D) # 3D Information Data.
        AD_TYPE_MANUFACTURER_SPECIFIC_DATA = const(0xFF) # Manufacturer Specific Data.


    class ADVType(object):
        '''
        Advertising Event Type
        '''
        ADV_IND = const(0x00) # connectable and scannable undirected advertising
        ADV_DIRECT_IND = const(0x01) # connectable directed advertising
        ADV_SCAN_IND = const(0x02) # scannable undirected advertising
        ADV_NONCONN_IND = const(0x03) # non-connectable undirected advertising
        SCAN_RSP = const(0x04) # scan response
        # SCAN_REQ = 0
        # CONNECT_REQ = 0


    class Appearance(object):
        Unknown = const(0) # None
        GENERIC_PHONE = const(64) # Generic category
        GENERIC_COMPUTER = const(128) # Generic category
        GENERIC_WATCH = const(192) # Generic category
        WATCH_SPORTS_WATCH = const(193) # Watch subtype
        GENERIC_CLOCK = const(256) # Generic category
        GENERIC_DISPLAY = const(320) # Generic category
        GENERIC_REMOTE_CONTROL = const(384) # Generic category
        GENERIC_EYE_GLASSES = const(448) # Generic category
        GENERIC_TAG = const(512) # Generic category
        GENERIC_KEYRING = const(576) # Generic category
        GENERIC_MEDIA_PLAYER = const(640) # Generic category
        GENERIC_BARCODE_SCANNER = const(704) # Generic category
        GENERIC_THERMOMETER = const(768) # Generic category
        THERMOMETER_EAR = const(769) # Thermometer subtype
        GENERIC_HEART_RATE_SENSOR = const(832) # Generic category
        HEART_RATE_SENSOR_HEART_RATE_BELT = const(833) # Heart Rate Sensor subtype

        # Added Blood pressure support on December 09, 2011
        GENERIC_BLOOD_PRESSURE = const(896) # Generic category
        BLOOD_PRESSURE_ARM = const(897) # Blood Pressure subtype
        BLOOD_PRESSURE_WRIST = const(898) # Blood Pressure subtype

        # Added HID Related appearance values on January 03, 2012 approved by BARB 
        HUMAN_INTERFACE_DEVICE_HID = const(960) # HID Generic
        KEYBOARD = const(961) # HID subtype
        MOUSE = const(962) # HID subtype
        JOYSTICK = const(963) # HID subtype
        GAMEPAD = const(964) # HID subtype
        DIGITIZER_TABLET = const(965) # HID subtype
        CARD_READER = const(966) # HID subtype
        DIGITAL_PEN = const(967) # HID subtype
        BARCODE_SCANNER = const(968) # HID subtype

        # Added Generic Glucose Meter value on May 10, 2012 approved by BARB 
        GENERIC_GLUCOSE_METER = const(1024) # Generic category

        # Added additional appearance values on June 26th, 2012 approved by BARB 
        GENERIC_RUNNING_WALKING_SENSOR = const(1088) # Generic category
        RUNNING_WALKING_SENSOR_IN_SHOE = const(1089) # Running Walking Sensor subtype
        RUNNING_WALKING_SENSOR_ON_SHOE = const(1090) # Running Walking Sensor subtype
        RUNNING_WALKING_SENSOR_ON_HIP = const(1091) # Running Walking Sensor subtype
        GENERIC_CYCLING = const(1152) # Generic category
        CYCLING_CYCLING_COMPUTER = const(1153) # Cycling subtype
        CYCLING_SPEED_SENSOR = const(1154) # Cycling subtype
        CYCLING_CADENCE_SENSOR = const(1155) # Cycling subtype
        CYCLING_POWER_SENSOR = const(1156) # Cycling subtype
        CYCLING_SPEED_AND_CADENCE_SENSOR = const(1157) # Cycling subtype

        # Added appearance values for Pulse Oximeter on July 30th, 2013 approved by BARB 
        GENERIC_PULSE_OXIMETER = const(3136) # Pulse Oximeter Generic Category
        FINGERTIP = const(3137) # Pulse Oximeter subtype
        WRIST_WORN = const(3138) # Pulse Oximeter subtype

        # Added appearance values for Generic Weight Scale on May 21, 2014 approved by BARB 
        GENERIC_WEIGHT_SCALE = const(3200) # Weight Scale Generic Category

        # Added additional appearance values on October 2nd, 2016 approved by BARB 
        GENERIC_PERSONAL_MOBILITY_DEVICE = const(3264) # Personal Mobility Device
        POWERED_WHEELCHAIR = const(3265) # Personal Mobility Device
        MOBILITY_SCOOTER = const(3266) # Personal Mobility Device
        GENERIC_CONTINUOUS_GLUCOSE_MONITOR = const(3328) # Continuous Glucose Monitor

        # Added additional appearance values on February 1st, 2018 approved by BARB 
        GENERIC_INSULIN_PUMP = const(3392) # Insulin Pump
        INSULIN_PUMP_DURABLE_PUMP = const(3393) # Insulin Pump
        INSULIN_PUMP_PATCH_PUMP = const(3396) # Insulin Pump
        INSULIN_PEN = const(3400) # Insulin Pump
        GENERIC_MEDICATION_DELIVERY = const(3456) # Medication Delivery

        # Added appearance values for L&N on July 30th, 2013 approved by BARB 
        GENERIC_OUTDOOR_SPORTS_ACTIVITY = const(5184) # Outdoor Sports Activity Generic Category
        LOCATION_DISPLAY_DEVICE = const(5185) # Outdoor Sports Activity subtype
        LOCATION_AND_NAVIGATION_DISPLAY_DEVICE = const(5186) # Outdoor Sports Activity subtype
        LOCATION_POD = const(5187) # Outdoor Sports Activity subtype
        LOCATION_AND_NAVIGATION_POD = const(5188) # Outdoor Sports Activity subtype


    class Services(object):
        GENERIC_ACCESS = const(0x1800)
        ALERT_NOTIFICATION_SERVICE = const(0x1811)
        AUTOMATION_IO = const(0x1815)
        BATTERY_SERVICE = const(0x180F)
        BINARY_SENSOR = const(0x183B)
        BLOOD_PRESSURE = const(0x1810)
        BODY_COMPOSITION = const(0x181B)
        BOND_MANAGEMENT_SERVICE = const(0x181E)
        CONTINUOUS_GLUCOSE_MONITORING = const(0x181F)
        CURRENT_TIME_SERVICE = const(0x1805)
        CYCLING_POWER = const(0x1818)
        CYCLING_SPEED_AND_CADENCE = const(0x1816)
        DEVICE_INFORMATION = const(0x180A)
        EMERGENCY_CONFIGURATION = const(0x183C)
        ENVIRONMENTAL_SENSING = const(0x181A)
        FITNESS_MACHINE = const(0x1826)
        GENERIC_ATTRIBUTE = const(0x1801)
        GLUCOSE = const(0x1808)
        HEALTH_THERMOMETER = const(0x1809)
        HEART_RATE = const(0x180D)
        HTTP_PROXY = const(0x1823)
        HUMAN_INTERFACE_DEVICE = const(0x1812)
        IMMEDIATE_ALERT = const(0x1802)
        INDOOR_POSITIONING = const(0x1821)
        INSULIN_DELIVERY = const(0x183A)
        INTERNET_PROTOCOL_SUPPORT_SERVICE = const(0x1820)
        LINK_LOSS = const(0x1803)
        LOCATION_AND_NAVIGATION = const(0x1819)
        MESH_PROVISIONING_SERVICE = const(0x1827)
        MESH_PROXY_SERVICE = const(0x1828)
        NEXT_DST_CHANGE_SERVICE = const(0x1807)
        OBJECT_TRANSFER_SERVICE = const(0x1825)
        PHONE_ALERT_STATUS_SERVICE = const(0x180E)
        PULSE_OXIMETER_SERVICE = const(0x1822)
        RECONNECTION_CONFIGURATION = const(0x1829)
        REFERENCE_TIME_UPDATE_SERVICE = const(0x1806)
        RUNNING_SPEED_AND_CADENCE = const(0x1814)
        SCAN_PARAMETERS = const(0x1813)
        TRANSPORT_DISCOVERY = const(0x1824)
        TX_POWER = const(0x1804)
        USER_DATA = const(0x181C)
        WEIGHT_SCALE = const(0x181D)


    class Characteristics(object):
        AEROBIC_HEART_RATE_LOWER_LIMIT = const(0x2A7E)
        AEROBIC_HEART_RATE_UPPER_LIMIT = const(0x2A84)
        AEROBIC_THRESHOLD = const(0x2A7F)
        AGE = const(0x2A80)
        AGGREGATE = const(0x2A5A)
        ALERT_CATEGORY_ID = const(0x2A43)
        ALERT_CATEGORY_ID_BIT_MASK = const(0x2A42)
        ALERT_LEVEL = const(0x2A06)
        ALERT_NOTIFICATION_CONTROL_POINT = const(0x2A44)
        ALERT_STATUS = const(0x2A3F)
        ALTITUDE = const(0x2AB3)
        ANAEROBIC_HEART_RATE_LOWER_LIMIT = const(0x2A81)
        ANAEROBIC_HEART_RATE_UPPER_LIMIT = const(0x2A82)
        ANAEROBIC_THRESHOLD = const(0x2A83)
        ANALOG = const(0x2A58)
        ANALOG_OUTPUT = const(0x2A59)
        APPARENT_WIND_DIRECTION = const(0x2A73)
        APPARENT_WIND_SPEED = const(0x2A72)
        APPEARANCE = const(0x2A01)
        BAROMETRIC_PRESSURE_TREND = const(0x2AA3)
        BATTERY_LEVEL = const(0x2A19)
        BATTERY_LEVEL_STATE = const(0x2A1B)
        BATTERY_POWER_STATE = const(0x2A1A)
        BLOOD_PRESSURE_FEATURE = const(0x2A49)
        BLOOD_PRESSURE_MEASUREMENT = const(0x2A35)
        BODY_COMPOSITION_FEATURE = const(0x2A9B)
        BODY_COMPOSITION_MEASUREMENT = const(0x2A9C)
        BODY_SENSOR_LOCATION = const(0x2A38)
        BOND_MANAGEMENT_CONTROL_POINT = const(0x2AA4)
        BOND_MANAGEMENT_FEATURES = const(0x2AA5)
        BOOT_KEYBOARD_INPUT_REPORT = const(0x2A22)
        BOOT_KEYBOARD_OUTPUT_REPORT = const(0x2A32)
        BOOT_MOUSE_INPUT_REPORT = const(0x2A33)
        BSS_CONTROL_POINT = const(0x2B2B)
        BSS_RESPONSE = const(0x2B2C)
        CGM_FEATURE = const(0x2AA8)
        CGM_MEASUREMENT = const(0x2AA7)
        CGM_SESSION_RUN_TIME = const(0x2AAB)
        CGM_SESSION_START_TIME = const(0x2AAA)
        CGM_SPECIFIC_OPS_CONTROL_POINT = const(0x2AAC)
        CGM_STATUS = const(0x2AA9)
        CLIENT_SUPPORTED_FEATURES = const(0x2B29)
        CROSS_TRAINER_DATA = const(0x2ACE)
        CSC_FEATURE = const(0x2A5C)
        CSC_MEASUREMENT = const(0x2A5B)
        CURRENT_TIME = const(0x2A2B)
        CYCLING_POWER_CONTROL_POINT = const(0x2A66)
        CYCLING_POWER_FEATURE = const(0x2A65)
        CYCLING_POWER_MEASUREMENT = const(0x2A63)
        CYCLING_POWER_VECTOR = const(0x2A64)
        DATABASE_CHANGE_INCREMENT = const(0x2A99)
        DATABASE_HASH = const(0x2B2A)
        DATE_OF_BIRTH = const(0x2A85)
        DATE_OF_THRESHOLD_ASSESSMENT = const(0x2A86)
        DATE_TIME = const(0x2A08)
        DATE_UTC = const(0x2AED)
        DAY_DATE_TIME = const(0x2A0A)
        DAY_OF_WEEK = const(0x2A09)
        DESCRIPTOR_VALUE_CHANGED = const(0x2A7D)
        DEW_POINT = const(0x2A7B)
        DIGITAL = const(0x2A56)
        DIGITAL_OUTPUT = const(0x2A57)
        DST_OFFSET = const(0x2A0D)
        ELEVATION = const(0x2A6C)
        EMAIL_ADDRESS = const(0x2A87)
        EMERGENCY_ID = const(0x2B2D)
        EMERGENCY_TEXT = const(0x2B2E)
        EXACT_TIME_100 = const(0x2A0B)
        EXACT_TIME_256 = const(0x2A0C)
        FAT_BURN_HEART_RATE_LOWER_LIMIT = const(0x2A88)
        FAT_BURN_HEART_RATE_UPPER_LIMIT = const(0x2A89)
        FIRMWARE_REVISION_STRING = const(0x2A26)
        FIRST_NAME = const(0x2A8A)
        FITNESS_MACHINE_CONTROL_POINT = const(0x2AD9)
        FITNESS_MACHINE_FEATURE = const(0x2ACC)
        FITNESS_MACHINE_STATUS = const(0x2ADA)
        FIVE_ZONE_HEART_RATE_LIMITS = const(0x2A8B)
        FLOOR_NUMBER = const(0x2AB2)
        CENTRAL_ADDRESS_RESOLUTION = const(0x2AA6)
        DEVICE_NAME = const(0x2A00)
        PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS = const(0x2A04)
        PERIPHERAL_PRIVACY_FLAG = const(0x2A02)
        RECONNECTION_ADDRESS = const(0x2A03)
        SERVICE_CHANGED = const(0x2A05)
        GENDER = const(0x2A8C)
        GLUCOSE_FEATURE = const(0x2A51)
        GLUCOSE_MEASUREMENT = const(0x2A18)
        GLUCOSE_MEASUREMENT_CONTEXT = const(0x2A34)
        GUST_FACTOR = const(0x2A74)
        HARDWARE_REVISION_STRING = const(0x2A27)
        HEART_RATE_CONTROL_POINT = const(0x2A39)
        HEART_RATE_MAX = const(0x2A8D)
        HEART_RATE_MEASUREMENT = const(0x2A37)
        HEAT_INDEX = const(0x2A7A)
        HEIGHT = const(0x2A8E)
        HID_CONTROL_POINT = const(0x2A4C)
        HID_INFORMATION = const(0x2A4A)
        HIP_CIRCUMFERENCE = const(0x2A8F)
        HTTP_CONTROL_POINT = const(0x2ABA)
        HTTP_ENTITY_BODY = const(0x2AB9)
        HTTP_HEADERS = const(0x2AB7)
        HTTP_STATUS_CODE = const(0x2AB8)
        HTTPS_SECURITY = const(0x2ABB)
        HUMIDITY = const(0x2A6F)
        IDD_ANNUNCIATION_STATUS = const(0x2B22)
        IDD_COMMAND_CONTROL_POINT = const(0x2B25)
        IDD_COMMAND_DATA = const(0x2B26)
        IDD_FEATURES = const(0x2B23)
        IDD_HISTORY_DATA = const(0x2B28)
        IDD_RECORD_ACCESS_CONTROL_POINT = const(0x2B27)
        IDD_STATUS = const(0x2B21)
        IDD_STATUS_CHANGED = const(0x2B20)
        IDD_STATUS_READER_CONTROL_POINT = const(0x2B24)
        IEEE_11073_20601_REGULATORY_CERTIFICATION_DATA_LIST = const(0x2A2A)
        INDOOR_BIKE_DATA = const(0x2AD2)
        INDOOR_POSITIONING_CONFIGURATION = const(0x2AAD)
        INTERMEDIATE_CUFF_PRESSURE = const(0x2A36)
        INTERMEDIATE_TEMPERATURE = const(0x2A1E)
        IRRADIANCE = const(0x2A77)
        LANGUAGE = const(0x2AA2)
        LAST_NAME = const(0x2A90)
        LATITUDE = const(0x2AAE)
        LN_CONTROL_POINT = const(0x2A6B)
        LN_FEATURE = const(0x2A6A)
        LOCAL_EAST_COORDINATE = const(0x2AB1)
        LOCAL_NORTH_COORDINATE = const(0x2AB0)
        LOCAL_TIME_INFORMATION = const(0x2A0F)
        LOCATION_AND_SPEED = const(0x2A67)
        LOCATION_NAME = const(0x2AB5)
        LONGITUDE = const(0x2AAF)
        MAGNETIC_DECLINATION = const(0x2A2C)
        MAGNETIC_FLUX_DENSITY_2D = const(0x2AA0)
        MAGNETIC_FLUX_DENSITY_3D = const(0x2AA1)
        MANUFACTURER_NAME_STRING = const(0x2A29)
        MAXIMUM_RECOMMENDED_HEART_RATE = const(0x2A91)
        MEASUREMENT_INTERVAL = const(0x2A21)
        MODEL_NUMBER_STRING = const(0x2A24)
        NAVIGATION = const(0x2A68)
        NETWORK_AVAILABILITY = const(0x2A3E)
        NEW_ALERT = const(0x2A46)
        OBJECT_ACTION_CONTROL_POINT = const(0x2AC5)
        OBJECT_CHANGED = const(0x2AC8)
        OBJECT_FIRST_CREATED = const(0x2AC1)
        OBJECT_ID = const(0x2AC3)
        OBJECT_LAST_MODIFIED = const(0x2AC2)
        OBJECT_LIST_CONTROL_POINT = const(0x2AC6)
        OBJECT_LIST_FILTER = const(0x2AC7)
        OBJECT_NAME = const(0x2ABE)
        OBJECT_PROPERTIES = const(0x2AC4)
        OBJECT_SIZE = const(0x2AC0)
        OBJECT_TYPE = const(0x2ABF)
        OTS_FEATURE = const(0x2ABD)
        PLX_CONTINUOUS_MEASUREMENT = const(0x2A5F)
        PLX_FEATURES = const(0x2A60)
        PLX_SPOT_CHECK_MEASUREMENT = const(0x2A5E)
        PNP_ID = const(0x2A50)
        POLLEN_CONCENTRATION = const(0x2A75)
        POSITION_2D = const(0x2A2F)
        POSITION_3D = const(0x2A30)
        POSITION_QUALITY = const(0x2A69)
        PRESSURE = const(0x2A6D)
        PROTOCOL_MODE = const(0x2A4E)
        PULSE_OXIMETRY_CONTROL_POINT = const(0x2A62)
        RAINFALL = const(0x2A78)
        RC_FEATURE = const(0x2B1D)
        RC_SETTINGS = const(0x2B1E)
        RECONNECTION_CONFIGURATION_CONTROL_POINT = const(0x2B1F)
        RECORD_ACCESS_CONTROL_POINT = const(0x2A52)
        REFERENCE_TIME_INFORMATION = const(0x2A14)
        REGISTERED_USER = const(0x2B37)
        REMOVABLE = const(0x2A3A)
        REPORT = const(0x2A4D)
        REPORT_MAP = const(0x2A4B)
        RESOLVABLE_PRIVATE_ADDRESS_ONLY = const(0x2AC9)
        RESTING_HEART_RATE = const(0x2A92)
        RINGER_CONTROL_POINT = const(0x2A40)
        RINGER_SETTING = const(0x2A41)
        ROWER_DATA = const(0x2AD1)
        RSC_FEATURE = const(0x2A54)
        RSC_MEASUREMENT = const(0x2A53)
        SC_CONTROL_POINT = const(0x2A55)
        SCAN_INTERVAL_WINDOW = const(0x2A4F)
        SCAN_REFRESH = const(0x2A31)
        SCIENTIFIC_TEMPERATURE_CELSIUS = const(0x2A3C)
        SECONDARY_TIME_ZONE = const(0x2A10)
        SENSOR_LOCATION = const(0x2A5D)
        SERIAL_NUMBER_STRING = const(0x2A25)
        SERVER_SUPPORTED_FEATURES = const(0x2B3A)
        SERVICE_REQUIRED = const(0x2A3B)
        SOFTWARE_REVISION_STRING = const(0x2A28)
        SPORT_TYPE_FOR_AEROBIC_AND_ANAEROBIC_THRESHOLDS = const(0x2A93)
        STAIR_CLIMBER_DATA = const(0x2AD0)
        STEP_CLIMBER_DATA = const(0x2ACF)
        STRING = const(0x2A3D)
        SUPPORTED_HEART_RATE_RANGE = const(0x2AD7)
        SUPPORTED_INCLINATION_RANGE = const(0x2AD5)
        SUPPORTED_NEW_ALERT_CATEGORY = const(0x2A47)
        SUPPORTED_POWER_RANGE = const(0x2AD8)
        SUPPORTED_RESISTANCE_LEVEL_RANGE = const(0x2AD6)
        SUPPORTED_SPEED_RANGE = const(0x2AD4)
        SUPPORTED_UNREAD_ALERT_CATEGORY = const(0x2A48)
        SYSTEM_ID = const(0x2A23)
        TDS_CONTROL_POINT = const(0x2ABC)
        TEMPERATURE = const(0x2A6E)
        TEMPERATURE_CELSIUS = const(0x2A1F)
        TEMPERATURE_FAHRENHEIT = const(0x2A20)
        TEMPERATURE_MEASUREMENT = const(0x2A1C)
        TEMPERATURE_TYPE = const(0x2A1D)
        THREE_ZONE_HEART_RATE_LIMITS = const(0x2A94)
        TIME_ACCURACY = const(0x2A12)
        TIME_BROADCAST = const(0x2A15)
        TIME_SOURCE = const(0x2A13)
        TIME_UPDATE_CONTROL_POINT = const(0x2A16)
        TIME_UPDATE_STATE = const(0x2A17)
        TIME_WITH_DST = const(0x2A11)
        TIME_ZONE = const(0x2A0E)
        TRAINING_STATUS = const(0x2AD3)
        TREADMILL_DATA = const(0x2ACD)
        TRUE_WIND_DIRECTION = const(0x2A71)
        TRUE_WIND_SPEED = const(0x2A70)
        TWO_ZONE_HEART_RATE_LIMIT = const(0x2A95)
        TX_POWER_LEVEL = const(0x2A07)
        UNCERTAINTY = const(0x2AB4)
        UNREAD_ALERT_STATUS = const(0x2A45)
        URI = const(0x2AB6)
        USER_CONTROL_POINT = const(0x2A9F)
        USER_INDEX = const(0x2A9A)
        UV_INDEX = const(0x2A76)
        VO2_MAX = const(0x2A96)
        WAIST_CIRCUMFERENCE = const(0x2A97)
        WEIGHT = const(0x2A98)
        WEIGHT_MEASUREMENT = const(0x2A9D)
        WEIGHT_SCALE_FEATURE = const(0x2A9E)
        WIND_CHILL = const(0x2A79)


    class CharacteristicFlags(object):
        AEROBIC_HEART_RATE_LOWER_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        AEROBIC_HEART_RATE_UPPER_LIMIT1_ = const(FLAG_READ | FLAG_WRITE)
        AEROBIC_THRESHOLD_ = const(FLAG_READ | FLAG_WRITE)
        AGE_ = const(FLAG_READ | FLAG_WRITE)
        AGGREGATE_ = const(FLAG_READ | FLAG_NOTIFY)
        # ALERT_CATEGORY_ID_ = const()
        # ALERT_CATEGORY_ID_BIT_MASK_ = const()
        ALERT_LEVEL_ = const(FLAG_READ | FLAG_WRITE)
        ALERT_NOTIFICATION_CONTROL_POINT_ = const(FLAG_WRITE)
        ALERT_STATUS_ = const(FLAG_READ | FLAG_NOTIFY)
        ALTITUDE_ = const(FLAG_READ | FLAG_WRITE)
        ANAEROBIC_HEART_RATE_LOWER_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        ANAEROBIC_HEART_RATE_UPPER_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        ANAEROBIC_THRESHOLD_ = const(FLAG_READ | FLAG_WRITE)
        ANALOG_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        # ANALOG_OUTPUT_ = const()
        APPARENT_WIND_DIRECTION_ = const(FLAG_READ | FLAG_NOTIFY)
        APPARENT_WIND_SPEED_ = const(FLAG_READ | FLAG_NOTIFY)
        APPEARANCE_ = const(FLAG_READ)
        BAROMETRIC_PRESSURE_TREND_ = const(FLAG_READ | FLAG_NOTIFY)
        BATTERY_LEVEL_ = const(FLAG_READ | FLAG_NOTIFY)
        # BATTERY_LEVEL_STATE_ = const()
        # BATTERY_POWER_STATE_ = const()
        BLOOD_PRESSURE_FEATURE_ = const(FLAG_READ)
        BLOOD_PRESSURE_MEASUREMENT_ = const(FLAG_NOTIFY)
        BODY_COMPOSITION_FEATURE_ = const(FLAG_READ)
        BODY_COMPOSITION_MEASUREMENT_ = const(FLAG_NOTIFY)
        BODY_SENSOR_LOCATION_ = const(FLAG_READ)
        BOND_MANAGEMENT_CONTROL_POINT_ = const(FLAG_WRITE)
        BOND_MANAGEMENT_FEATURES_ = const(FLAG_READ)
        BOOT_KEYBOARD_INPUT_REPORT_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        BOOT_KEYBOARD_OUTPUT_REPORT_ = const(FLAG_READ | FLAG_WRITE)
        BOOT_MOUSE_INPUT_REPORT_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        # BSS_CONTROL_POINT_ = const()
        # BSS_RESPONSE_ = const()
        CGM_FEATURE_ = const(FLAG_READ)
        CGM_MEASUREMENT_ = const(FLAG_NOTIFY)
        CGM_SESSION_RUN_TIME_ = const(FLAG_READ)
        CGM_SESSION_START_TIME_ = const(FLAG_READ | FLAG_WRITE)
        CGM_SPECIFIC_OPS_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        CGM_STATUS_ = const(FLAG_READ)
        # CLIENT_SUPPORTED_FEATURES_ = const()
        CROSS_TRAINER_DATA_ = const(FLAG_NOTIFY)
        CSC_FEATURE_ = const(FLAG_READ)
        CSC_MEASUREMENT_ = const(FLAG_NOTIFY)
        CURRENT_TIME_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        CYCLING_POWER_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        CYCLING_POWER_FEATURE_ = const(FLAG_READ)
        CYCLING_POWER_MEASUREMENT_ = const(FLAG_NOTIFY)
        CYCLING_POWER_VECTOR_ = const(FLAG_NOTIFY)
        DATABASE_CHANGE_INCREMENT_ = const(FLAG_READ | FLAG_WRITE)
        # DATABASE_HASH_ = const()
        DATE_OF_BIRTH_ = const(FLAG_READ | FLAG_WRITE)
        DATE_OF_THRESHOLD_ASSESSMENT_ = const(FLAG_READ | FLAG_WRITE)
        # DATE_TIME_ = const()
        # DATE_UTC_ = const()
        # DAY_DATE_TIME_ = const()
        # DAY_OF_WEEK_ = const()
        DESCRIPTOR_VALUE_CHANGED_ = const(FLAG_NOTIFY)
        DEW_POINT_ = const(FLAG_READ | FLAG_NOTIFY)
        DIGITAL_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        # DIGITAL_OUTPUT_ = const()
        # DST_OFFSET_ = const()
        ELEVATION_ = const(FLAG_READ | FLAG_NOTIFY)
        EMAIL_ADDRESS_ = const(FLAG_READ | FLAG_WRITE)
        # EMERGENCY_ID_ = const()
        # EMERGENCY_TEXT_ = const()
        # EXACT_TIME_100_ = const()
        # EXACT_TIME_256_ = const()
        FAT_BURN_HEART_RATE_LOWER_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        FAT_BURN_HEART_RATE_UPPER_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        FIRMWARE_REVISION_STRING_ = const(FLAG_READ)
        FIRST_NAME_ = const(FLAG_READ | FLAG_WRITE)
        FITNESS_MACHINE_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        FITNESS_MACHINE_FEATURE_ = const(FLAG_READ)
        FITNESS_MACHINE_STATUS_ = const(FLAG_NOTIFY)
        FIVE_ZONE_HEART_RATE_LIMITS_ = const(FLAG_READ | FLAG_WRITE)
        FLOOR_NUMBER_ = const(FLAG_READ | FLAG_WRITE)
        CENTRAL_ADDRESS_RESOLUTION_ = const(FLAG_READ)
        DEVICE_NAME_ = const(FLAG_READ | FLAG_WRITE)
        PERIPHERAL_PREFERRED_CONNECTION_PARAMETERS_ = const(FLAG_READ)
        PERIPHERAL_PRIVACY_FLAG_ = const(FLAG_READ)
        RECONNECTION_ADDRESS_ = const(FLAG_WRITE)
        SERVICE_CHANGED_ = const(FLAG_NOTIFY)
        GENDER_ = const(FLAG_READ | FLAG_WRITE)
        GLUCOSE_FEATURE_ = const(FLAG_READ)
        GLUCOSE_MEASUREMENT_ = const(FLAG_NOTIFY)
        GLUCOSE_MEASUREMENT_CONTEXT_ = const(FLAG_NOTIFY)
        GUST_FACTOR_ = const(FLAG_READ | FLAG_NOTIFY)
        HARDWARE_REVISION_STRING_ = const(FLAG_READ)
        HEART_RATE_CONTROL_POINT_ = const(FLAG_WRITE)
        HEART_RATE_MAX_ = const(FLAG_READ | FLAG_WRITE)
        HEART_RATE_MEASUREMENT_ = const(FLAG_NOTIFY)
        HEAT_INDEX_ = const(FLAG_READ | FLAG_NOTIFY)
        HEIGHT_ = const(FLAG_READ | FLAG_WRITE)
        HID_CONTROL_POINT_ = const(FLAG_WRITE)
        HID_INFORMATION_ = const(FLAG_READ)
        HIP_CIRCUMFERENCE_ = const(FLAG_READ | FLAG_WRITE)
        HTTP_CONTROL_POINT_ = const(FLAG_WRITE)
        HTTP_ENTITY_BODY_ = const(FLAG_READ | FLAG_WRITE)
        HTTP_HEADERS_ = const(FLAG_READ | FLAG_WRITE)
        HTTP_STATUS_CODE_ = const(FLAG_NOTIFY)
        HTTPS_SECURITY_ = const(FLAG_READ)
        HUMIDITY_ = const(FLAG_READ | FLAG_NOTIFY)
        IDD_ANNUNCIATION_STATUS_ = const(FLAG_READ | FLAG_NOTIFY)
        IDD_COMMAND_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        IDD_COMMAND_DATA_ = const(FLAG_NOTIFY)
        IDD_FEATURES_ = const(FLAG_READ)
        IDD_HISTORY_DATA_ = const(FLAG_NOTIFY)
        IDD_RECORD_ACCESS_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        IDD_STATUS_ = const(FLAG_READ | FLAG_NOTIFY)
        IDD_STATUS_CHANGED_ = const(FLAG_READ | FLAG_NOTIFY)
        IDD_STATUS_READER_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        IEEE_11073_20601_REGULATORY_CERTIFICATION_DATA_LIST_ = const(FLAG_READ)
        INDOOR_BIKE_DATA_ = const(FLAG_NOTIFY)
        INDOOR_POSITIONING_CONFIGURATION_ = const(FLAG_READ | FLAG_WRITE)
        INTERMEDIATE_CUFF_PRESSURE_ = const(FLAG_NOTIFY)
        INTERMEDIATE_TEMPERATURE_ = const(FLAG_NOTIFY)
        IRRADIANCE_ = const(FLAG_READ | FLAG_NOTIFY)
        LANGUAGE_ = const(FLAG_READ | FLAG_WRITE)
        LAST_NAME_ = const(FLAG_READ | FLAG_WRITE)
        LATITUDE_ = const(FLAG_READ | FLAG_WRITE)
        LN_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY  )
        LN_FEATURE_ = const(FLAG_READ)
        LOCAL_EAST_COORDINATE_ = const(FLAG_READ | FLAG_WRITE)
        LOCAL_NORTH_COORDINATE_ = const(FLAG_READ | FLAG_WRITE)
        LOCAL_TIME_INFORMATION_ = const(FLAG_READ | FLAG_WRITE)
        LOCATION_AND_SPEED_ = const(FLAG_NOTIFY)
        LOCATION_NAME_ = const(FLAG_READ | FLAG_WRITE)
        LONGITUDE_ = const(FLAG_READ | FLAG_WRITE)
        MAGNETIC_DECLINATION_ = const(FLAG_READ | FLAG_NOTIFY)
        MAGNETIC_FLUX_DENSITY_2D_ = const(FLAG_READ | FLAG_NOTIFY)
        MAGNETIC_FLUX_DENSITY_3D_ = const(FLAG_READ | FLAG_NOTIFY)
        MANUFACTURER_NAME_STRING_ = const(FLAG_READ)
        MAXIMUM_RECOMMENDED_HEART_RATE_ = const(FLAG_READ | FLAG_WRITE)
        MEASUREMENT_INTERVAL_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        MODEL_NUMBER_STRING_ = const(FLAG_READ)
        NAVIGATION_ = const(FLAG_NOTIFY)
        # NETWORK_AVAILABILITY_ = const()
        NEW_ALERT_ = const(FLAG_NOTIFY)
        OBJECT_ACTION_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        OBJECT_CHANGED_ = const(FLAG_NOTIFY)
        OBJECT_FIRST_CREATED_ = const(FLAG_READ | FLAG_WRITE)
        OBJECT_ID_ = const(FLAG_READ)
        OBJECT_LAST_MODIFIED_ = const(FLAG_READ | FLAG_WRITE)
        OBJECT_LIST_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        OBJECT_LIST_FILTER_ = const(FLAG_READ | FLAG_WRITE)
        OBJECT_NAME_ = const(FLAG_READ | FLAG_WRITE)
        OBJECT_PROPERTIES_ = const(FLAG_READ | FLAG_WRITE)
        OBJECT_SIZE_ = const(FLAG_READ)
        OBJECT_TYPE_ = const(FLAG_READ)
        OTS_FEATURE_ = const(FLAG_READ)
        PLX_CONTINUOUS_MEASUREMENT_ = const(FLAG_NOTIFY)
        PLX_FEATURES_ = const(FLAG_READ)
        PLX_SPOT_CHECK_MEASUREMENT_ = const(FLAG_NOTIFY)
        PNP_ID_ = const(FLAG_READ)
        POLLEN_CONCENTRATION_ = const(FLAG_READ | FLAG_NOTIFY)
        # POSITION_2D_ = const()
        # POSITION_3D_ = const()
        POSITION_QUALITY_ = const(FLAG_READ)
        PRESSURE_ = const(FLAG_READ | FLAG_NOTIFY)
        PROTOCOL_MODE_ = const(FLAG_READ | FLAG_WRITE)
        # PULSE_OXIMETRY_CONTROL_POINT_ = const()
        RAINFALL_ = const(FLAG_READ | FLAG_NOTIFY)
        RC_FEATURE_ = const(FLAG_READ)
        RC_SETTINGS_ = const(FLAG_READ | FLAG_NOTIFY)
        RECONNECTION_CONFIGURATION_CONTROL_POINT_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        RECORD_ACCESS_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        REFERENCE_TIME_INFORMATION_ = const(FLAG_READ)
        # REGISTERED_USER_ = const()
        # REMOVABLE_ = const()
        REPORT_ = const(FLAG_READ | FLAG_WRITE | FLAG_NOTIFY)
        REPORT_MAP_ = const(FLAG_READ)
        # RESOLVABLE_PRIVATE_ADDRESS_ONLY_ = const()
        RESTING_HEART_RATE_ = const(FLAG_READ | FLAG_WRITE)
        RINGER_CONTROL_POINT_ = const(FLAG_WRITE)
        RINGER_SETTING_ = const(FLAG_READ | FLAG_NOTIFY)
        ROWER_DATA_ = const(FLAG_NOTIFY)
        RSC_FEATURE_ = const(FLAG_READ)
        RSC_MEASUREMENT_ = const(FLAG_NOTIFY)
        SC_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        SCAN_INTERVAL_WINDOW_ = const(FLAG_WRITE)
        SCAN_REFRESH_ = const(FLAG_NOTIFY)
        # SCIENTIFIC_TEMPERATURE_CELSIUS_ = const()
        # SECONDARY_TIME_ZONE_ = const()
        SENSOR_LOCATION_ = const(FLAG_READ)
        SERIAL_NUMBER_STRING_ = const(FLAG_READ)
        # SERVER_SUPPORTED_FEATURES_ = const()
        # SERVICE_REQUIRED_ = const()
        SOFTWARE_REVISION_STRING_ = const(FLAG_READ)
        SPORT_TYPE_FOR_AEROBIC_AND_ANAEROBIC_THRESHOLDS_ = const(FLAG_READ | FLAG_WRITE)
        STAIR_CLIMBER_DATA_ = const(FLAG_NOTIFY)
        STEP_CLIMBER_DATA_ = const(FLAG_NOTIFY)
        # STRING_ = const()
        SUPPORTED_HEART_RATE_RANGE_ = const(FLAG_READ)
        SUPPORTED_INCLINATION_RANGE_ = const(FLAG_READ)
        SUPPORTED_NEW_ALERT_CATEGORY_ = const(FLAG_READ)
        SUPPORTED_POWER_RANGE_ = const(FLAG_READ)
        SUPPORTED_RESISTANCE_LEVEL_RANGE_ = const(FLAG_READ)
        SUPPORTED_SPEED_RANGE_ = const(FLAG_READ)
        SUPPORTED_UNREAD_ALERT_CATEGORY_ = const(FLAG_READ)
        SYSTEM_ID_ = const(FLAG_READ)
        TDS_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        TEMPERATURE_ = const(FLAG_READ | FLAG_NOTIFY)
        # TEMPERATURE_CELSIUS_ = const()
        # TEMPERATURE_FAHRENHEIT_ = const()
        TEMPERATURE_MEASUREMENT_ = const(FLAG_NOTIFY)
        TEMPERATURE_TYPE_ = const(FLAG_READ)
        THREE_ZONE_HEART_RATE_LIMITS_ = const(FLAG_READ | FLAG_WRITE)
        # TIME_ACCURACY_ = const()
        # TIME_BROADCAST_ = const()
        # TIME_SOURCE_ = const()
        TIME_UPDATE_CONTROL_POINT_ = const(FLAG_WRITE)
        TIME_UPDATE_STATE_ = const(FLAG_READ)
        TIME_WITH_DST_ = const(FLAG_READ)
        # TIME_ZONE_ = const()
        TRAINING_STATUS_ = const(FLAG_READ | FLAG_NOTIFY)
        TREADMILL_DATA_ = const(FLAG_NOTIFY)
        TRUE_WIND_DIRECTION_ = const(FLAG_READ | FLAG_NOTIFY)
        TRUE_WIND_SPEED_ = const(FLAG_READ | FLAG_NOTIFY)
        TWO_ZONE_HEART_RATE_LIMIT_ = const(FLAG_READ | FLAG_WRITE)
        TX_POWER_LEVEL_ = const(FLAG_READ)
        UNCERTAINTY_ = const(FLAG_READ | FLAG_WRITE)
        UNREAD_ALERT_STATUS_ = const(FLAG_NOTIFY)
        URI_ = const(FLAG_WRITE)
        USER_CONTROL_POINT_ = const(FLAG_WRITE | FLAG_NOTIFY)
        USER_INDEX_ = const(FLAG_READ)
        UV_INDEX_ = const(FLAG_READ | FLAG_NOTIFY)
        VO2_MAX_ = const(FLAG_READ | FLAG_WRITE)
        WAIST_CIRCUMFERENCE_ = const(FLAG_READ | FLAG_WRITE)
        WEIGHT_ = const(FLAG_READ | FLAG_WRITE)
        WEIGHT_MEASUREMENT_ = const(FLAG_NOTIFY)
        WEIGHT_SCALE_FEATURE_ = const(FLAG_READ)
        WIND_CHILL_ = const(FLAG_READ | FLAG_NOTIFY)


    class Descriptors(object):
        CHARACTERISTIC_AGGREGATE_FORMAT = const(0x2905)
        CHARACTERISTIC_EXTENDED_PROPERTIES = const(0x2900)
        CHARACTERISTIC_PRESENTATION_FORMAT = const(0x2904)
        CHARACTERISTIC_USER_DESCRIPTION = const(0x2901)
        CLIENT_CHARACTERISTIC_CONFIGURATION = const(0x2902)
        ENVIRONMENTAL_SENSING_CONFIGURATION = const(0x290B)
        ENVIRONMENTAL_SENSING_MEASUREMENT = const(0x290C)
        ENVIRONMENTAL_SENSING_TRIGGER_SETTING = const(0x290D)
        EXTERNAL_REPORT_REFERENCE = const(0x2907)
        NUMBER_OF_DIGITALS = const(0x2909)
        REPORT_REFERENCE = const(0x2908)
        SERVER_CHARACTERISTIC_CONFIGURATION = const(0x2903)
        TIME_TRIGGER_SETTING = const(0x290E)
        VALID_RANGE = const(0x2906)
        VALUE_TRIGGER_SETTING = const(0x290A)


    class Eddystone(object):
        EDDYSTONE_UUID = const(0xFEAA)
        EDDYSTONE_URL = const(0x10)
        EDDYSTONE_UID = const(0x00)
        EDDYSTONE_EID = const(0x30)


    class iBeacon(object):
        IBEACON_PREFIX = b'\x4C\x00\x02\x15'


    class BeaconType(object):
        BEACON_UNKNOWN = 0
        BEACON_IBEACON = 1
        BEACON_EDDYSTONE_URL = 2
        BEACON_EDDYSTONE_UID = 3
        BEACON_EDDYSTONE_EID = 4
        BEACON_ALL = [BEACON_IBEACON, BEACON_EDDYSTONE_URL, BEACON_EDDYSTONE_UID, BEACON_EDDYSTONE_EID]