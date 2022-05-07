# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x62_service.proto\"\"\n\x04\x42ody\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\x05\"!\n\x12\x44\x42ServiceGetAllReq\x12\x0b\n\x03nid\x18\x01 \x01(\x05\",\n\x12\x44\x42ServiceGetAllRsp\x12\x16\n\x07results\x18\x01 \x03(\x0b\x32\x05.Body\"0\n\x15\x44\x42ServiceGetSingleReq\x12\x0b\n\x03nid\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\".\n\x15\x44\x42ServiceGetSingleRsp\x12\x15\n\x06result\x18\x01 \x01(\x0b\x32\x05.Body\"3\n\x0f\x44\x42ServiceSetReq\x12\x0b\n\x03nid\x18\x01 \x01(\x05\x12\x13\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x05.Body\"$\n\x0f\x44\x42ServiceSetRsp\x12\x11\n\top_stutas\x18\x01 \x01(\x05\"6\n\x12\x44\x42ServiceUpdateReq\x12\x0b\n\x03nid\x18\x01 \x01(\x05\x12\x13\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x05.Body\"\'\n\x12\x44\x42ServiceUpdateRsp\x12\x11\n\top_stutas\x18\x01 \x01(\x05\x32\xf3\x01\n\tDBService\x12\x38\n\nGetAllData\x12\x13.DBServiceGetAllReq\x1a\x13.DBServiceGetAllRsp\"\x00\x12\x41\n\rGetSingleData\x12\x16.DBServiceGetSingleReq\x1a\x16.DBServiceGetSingleRsp\"\x00\x12/\n\x07SetData\x12\x10.DBServiceSetReq\x1a\x10.DBServiceSetRsp\"\x00\x12\x38\n\nUpdateData\x12\x13.DBServiceUpdateReq\x1a\x13.DBServiceUpdateRsp\"\x00\x62\x06proto3')



_BODY = DESCRIPTOR.message_types_by_name['Body']
_DBSERVICEGETALLREQ = DESCRIPTOR.message_types_by_name['DBServiceGetAllReq']
_DBSERVICEGETALLRSP = DESCRIPTOR.message_types_by_name['DBServiceGetAllRsp']
_DBSERVICEGETSINGLEREQ = DESCRIPTOR.message_types_by_name['DBServiceGetSingleReq']
_DBSERVICEGETSINGLERSP = DESCRIPTOR.message_types_by_name['DBServiceGetSingleRsp']
_DBSERVICESETREQ = DESCRIPTOR.message_types_by_name['DBServiceSetReq']
_DBSERVICESETRSP = DESCRIPTOR.message_types_by_name['DBServiceSetRsp']
_DBSERVICEUPDATEREQ = DESCRIPTOR.message_types_by_name['DBServiceUpdateReq']
_DBSERVICEUPDATERSP = DESCRIPTOR.message_types_by_name['DBServiceUpdateRsp']
Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), {
  'DESCRIPTOR' : _BODY,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:Body)
  })
_sym_db.RegisterMessage(Body)

DBServiceGetAllReq = _reflection.GeneratedProtocolMessageType('DBServiceGetAllReq', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEGETALLREQ,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceGetAllReq)
  })
_sym_db.RegisterMessage(DBServiceGetAllReq)

DBServiceGetAllRsp = _reflection.GeneratedProtocolMessageType('DBServiceGetAllRsp', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEGETALLRSP,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceGetAllRsp)
  })
_sym_db.RegisterMessage(DBServiceGetAllRsp)

DBServiceGetSingleReq = _reflection.GeneratedProtocolMessageType('DBServiceGetSingleReq', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEGETSINGLEREQ,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceGetSingleReq)
  })
_sym_db.RegisterMessage(DBServiceGetSingleReq)

DBServiceGetSingleRsp = _reflection.GeneratedProtocolMessageType('DBServiceGetSingleRsp', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEGETSINGLERSP,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceGetSingleRsp)
  })
_sym_db.RegisterMessage(DBServiceGetSingleRsp)

DBServiceSetReq = _reflection.GeneratedProtocolMessageType('DBServiceSetReq', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICESETREQ,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceSetReq)
  })
_sym_db.RegisterMessage(DBServiceSetReq)

DBServiceSetRsp = _reflection.GeneratedProtocolMessageType('DBServiceSetRsp', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICESETRSP,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceSetRsp)
  })
_sym_db.RegisterMessage(DBServiceSetRsp)

DBServiceUpdateReq = _reflection.GeneratedProtocolMessageType('DBServiceUpdateReq', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEUPDATEREQ,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceUpdateReq)
  })
_sym_db.RegisterMessage(DBServiceUpdateReq)

DBServiceUpdateRsp = _reflection.GeneratedProtocolMessageType('DBServiceUpdateRsp', (_message.Message,), {
  'DESCRIPTOR' : _DBSERVICEUPDATERSP,
  '__module__' : 'db_service_pb2'
  # @@protoc_insertion_point(class_scope:DBServiceUpdateRsp)
  })
_sym_db.RegisterMessage(DBServiceUpdateRsp)

_DBSERVICE = DESCRIPTOR.services_by_name['DBService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BODY._serialized_start=20
  _BODY._serialized_end=54
  _DBSERVICEGETALLREQ._serialized_start=56
  _DBSERVICEGETALLREQ._serialized_end=89
  _DBSERVICEGETALLRSP._serialized_start=91
  _DBSERVICEGETALLRSP._serialized_end=135
  _DBSERVICEGETSINGLEREQ._serialized_start=137
  _DBSERVICEGETSINGLEREQ._serialized_end=185
  _DBSERVICEGETSINGLERSP._serialized_start=187
  _DBSERVICEGETSINGLERSP._serialized_end=233
  _DBSERVICESETREQ._serialized_start=235
  _DBSERVICESETREQ._serialized_end=286
  _DBSERVICESETRSP._serialized_start=288
  _DBSERVICESETRSP._serialized_end=324
  _DBSERVICEUPDATEREQ._serialized_start=326
  _DBSERVICEUPDATEREQ._serialized_end=380
  _DBSERVICEUPDATERSP._serialized_start=382
  _DBSERVICEUPDATERSP._serialized_end=421
  _DBSERVICE._serialized_start=424
  _DBSERVICE._serialized_end=667
# @@protoc_insertion_point(module_scope)
