"""autogenerated by genpy from kobuki_msgs/SensorState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SensorState(genpy.Message):
  _md5sum = "92e992cd3c66c18711c1ce707090fcc1"
  _type = "kobuki_msgs/SensorState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Kobuki Sensor Data Messages
#

# Buttons bitmasks to decode byte "buttons"
uint8 Button0 = 1  # 0x02
uint8 Button1 = 2  # 0x01
uint8 Button2 = 4  # 0x04

# Byte "charger" format:
# - first four bits distinguish between adapter or docking base charging
uint8 ADAPTER     = 16 # bitmask 0x10
# - last 4 bits specified the charging status
uint8 DISCHARGING = 0
uint8 CHARGED     = 2
uint8 CHARGING    = 6


Header header

###################
# Core Packet
###################
uint16 time_stamp
uint8  bumper
uint8  wheel_drop
uint8  cliff
uint16 left_encoder
uint16 right_encoder
int8  left_pwm
int8  right_pwm
uint8  buttons
uint8  charger
uint8  battery

###################
# Cliff Packet
###################
uint16[] bottom

###################
# Current Packet
###################
uint8[] current
uint8 over_current

###################
# GP Input Packet
###################
uint16 digital_input
uint16[] analog_input

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  # Pseudo-constants
  Button0 = 1
  Button1 = 2
  Button2 = 4
  ADAPTER = 16
  DISCHARGING = 0
  CHARGED = 2
  CHARGING = 6

  __slots__ = ['header','time_stamp','bumper','wheel_drop','cliff','left_encoder','right_encoder','left_pwm','right_pwm','buttons','charger','battery','bottom','current','over_current','digital_input','analog_input']
  _slot_types = ['std_msgs/Header','uint16','uint8','uint8','uint8','uint16','uint16','int8','int8','uint8','uint8','uint8','uint16[]','uint8[]','uint8','uint16','uint16[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,bumper,wheel_drop,cliff,left_encoder,right_encoder,left_pwm,right_pwm,buttons,charger,battery,bottom,current,over_current,digital_input,analog_input

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SensorState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.bumper is None:
        self.bumper = 0
      if self.wheel_drop is None:
        self.wheel_drop = 0
      if self.cliff is None:
        self.cliff = 0
      if self.left_encoder is None:
        self.left_encoder = 0
      if self.right_encoder is None:
        self.right_encoder = 0
      if self.left_pwm is None:
        self.left_pwm = 0
      if self.right_pwm is None:
        self.right_pwm = 0
      if self.buttons is None:
        self.buttons = 0
      if self.charger is None:
        self.charger = 0
      if self.battery is None:
        self.battery = 0
      if self.bottom is None:
        self.bottom = []
      if self.current is None:
        self.current = ''
      if self.over_current is None:
        self.over_current = 0
      if self.digital_input is None:
        self.digital_input = 0
      if self.analog_input is None:
        self.analog_input = []
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.bumper = 0
      self.wheel_drop = 0
      self.cliff = 0
      self.left_encoder = 0
      self.right_encoder = 0
      self.left_pwm = 0
      self.right_pwm = 0
      self.buttons = 0
      self.charger = 0
      self.battery = 0
      self.bottom = []
      self.current = ''
      self.over_current = 0
      self.digital_input = 0
      self.analog_input = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_H3B2H2b3B.pack(_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery))
      length = len(self.bottom)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(struct.pack(pattern, *self.bottom))
      _x = self.current
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BH.pack(_x.over_current, _x.digital_input))
      length = len(self.analog_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(struct.pack(pattern, *self.analog_input))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery,) = _struct_H3B2H2b3B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      end += struct.calcsize(pattern)
      self.bottom = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current = str[start:end].decode('utf-8')
      else:
        self.current = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.over_current, _x.digital_input,) = _struct_BH.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      end += struct.calcsize(pattern)
      self.analog_input = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_H3B2H2b3B.pack(_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery))
      length = len(self.bottom)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(self.bottom.tostring())
      _x = self.current
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BH.pack(_x.over_current, _x.digital_input))
      length = len(self.analog_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(self.analog_input.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery,) = _struct_H3B2H2b3B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      end += struct.calcsize(pattern)
      self.bottom = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current = str[start:end].decode('utf-8')
      else:
        self.current = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.over_current, _x.digital_input,) = _struct_BH.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      end += struct.calcsize(pattern)
      self.analog_input = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_H3B2H2b3B = struct.Struct("<H3B2H2b3B")
_struct_BH = struct.Struct("<BH")
