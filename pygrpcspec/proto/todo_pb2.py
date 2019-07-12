# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/todo.proto',
  package='gogrpcspec',
  syntax='proto3',
  serialized_pb=_b('\n\x10proto/todo.proto\x12\ngogrpcspec\"\x18\n\x08\x45mployee\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x04Task\x12&\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x14.gogrpcspec.Employee\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"C\n\x07Summary\x12\x11\n\ttodoTasks\x18\x01 \x01(\x05\x12\x12\n\ndoingTasks\x18\x02 \x01(\x05\x12\x11\n\tdoneTasks\x18\x03 \x01(\x05\"_\n\x0fSpecificSummary\x12&\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x14.gogrpcspec.Employee\x12$\n\x07summary\x18\x02 \x01(\x0b\x32\x13.gogrpcspec.Summary2\xb5\x02\n\x0bTaskManager\x12\x41\n\nGetSummary\x12\x14.gogrpcspec.Employee\x1a\x1b.gogrpcspec.SpecificSummary\"\x00\x12:\n\x07\x41\x64\x64Task\x12\x10.gogrpcspec.Task\x1a\x1b.gogrpcspec.SpecificSummary\"\x00\x12\x35\n\x08\x41\x64\x64Tasks\x12\x10.gogrpcspec.Task\x1a\x13.gogrpcspec.Summary\"\x00(\x01\x12\x36\n\x08GetTasks\x12\x14.gogrpcspec.Employee\x1a\x10.gogrpcspec.Task\"\x00\x30\x01\x12\x38\n\x0c\x43hangeToDone\x12\x10.gogrpcspec.Task\x1a\x10.gogrpcspec.Task\"\x00(\x01\x30\x01\x62\x06proto3')
)




_EMPLOYEE = _descriptor.Descriptor(
  name='Employee',
  full_name='gogrpcspec.Employee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gogrpcspec.Employee.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=56,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='gogrpcspec.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='employee', full_name='gogrpcspec.Task.employee', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='gogrpcspec.Task.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='gogrpcspec.Task.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=134,
)


_SUMMARY = _descriptor.Descriptor(
  name='Summary',
  full_name='gogrpcspec.Summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todoTasks', full_name='gogrpcspec.Summary.todoTasks', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doingTasks', full_name='gogrpcspec.Summary.doingTasks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doneTasks', full_name='gogrpcspec.Summary.doneTasks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=203,
)


_SPECIFICSUMMARY = _descriptor.Descriptor(
  name='SpecificSummary',
  full_name='gogrpcspec.SpecificSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='employee', full_name='gogrpcspec.SpecificSummary.employee', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary', full_name='gogrpcspec.SpecificSummary.summary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=300,
)

_TASK.fields_by_name['employee'].message_type = _EMPLOYEE
_SPECIFICSUMMARY.fields_by_name['employee'].message_type = _EMPLOYEE
_SPECIFICSUMMARY.fields_by_name['summary'].message_type = _SUMMARY
DESCRIPTOR.message_types_by_name['Employee'] = _EMPLOYEE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Summary'] = _SUMMARY
DESCRIPTOR.message_types_by_name['SpecificSummary'] = _SPECIFICSUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Employee = _reflection.GeneratedProtocolMessageType('Employee', (_message.Message,), dict(
  DESCRIPTOR = _EMPLOYEE,
  __module__ = 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:gogrpcspec.Employee)
  ))
_sym_db.RegisterMessage(Employee)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:gogrpcspec.Task)
  ))
_sym_db.RegisterMessage(Task)

Summary = _reflection.GeneratedProtocolMessageType('Summary', (_message.Message,), dict(
  DESCRIPTOR = _SUMMARY,
  __module__ = 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:gogrpcspec.Summary)
  ))
_sym_db.RegisterMessage(Summary)

SpecificSummary = _reflection.GeneratedProtocolMessageType('SpecificSummary', (_message.Message,), dict(
  DESCRIPTOR = _SPECIFICSUMMARY,
  __module__ = 'proto.todo_pb2'
  # @@protoc_insertion_point(class_scope:gogrpcspec.SpecificSummary)
  ))
_sym_db.RegisterMessage(SpecificSummary)



_TASKMANAGER = _descriptor.ServiceDescriptor(
  name='TaskManager',
  full_name='gogrpcspec.TaskManager',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=303,
  serialized_end=612,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSummary',
    full_name='gogrpcspec.TaskManager.GetSummary',
    index=0,
    containing_service=None,
    input_type=_EMPLOYEE,
    output_type=_SPECIFICSUMMARY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTask',
    full_name='gogrpcspec.TaskManager.AddTask',
    index=1,
    containing_service=None,
    input_type=_TASK,
    output_type=_SPECIFICSUMMARY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTasks',
    full_name='gogrpcspec.TaskManager.AddTasks',
    index=2,
    containing_service=None,
    input_type=_TASK,
    output_type=_SUMMARY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTasks',
    full_name='gogrpcspec.TaskManager.GetTasks',
    index=3,
    containing_service=None,
    input_type=_EMPLOYEE,
    output_type=_TASK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeToDone',
    full_name='gogrpcspec.TaskManager.ChangeToDone',
    index=4,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASK,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKMANAGER)

DESCRIPTOR.services_by_name['TaskManager'] = _TASKMANAGER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TaskManagerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetSummary = channel.unary_unary(
          '/gogrpcspec.TaskManager/GetSummary',
          request_serializer=Employee.SerializeToString,
          response_deserializer=SpecificSummary.FromString,
          )
      self.AddTask = channel.unary_unary(
          '/gogrpcspec.TaskManager/AddTask',
          request_serializer=Task.SerializeToString,
          response_deserializer=SpecificSummary.FromString,
          )
      self.AddTasks = channel.stream_unary(
          '/gogrpcspec.TaskManager/AddTasks',
          request_serializer=Task.SerializeToString,
          response_deserializer=Summary.FromString,
          )
      self.GetTasks = channel.unary_stream(
          '/gogrpcspec.TaskManager/GetTasks',
          request_serializer=Employee.SerializeToString,
          response_deserializer=Task.FromString,
          )
      self.ChangeToDone = channel.stream_stream(
          '/gogrpcspec.TaskManager/ChangeToDone',
          request_serializer=Task.SerializeToString,
          response_deserializer=Task.FromString,
          )


  class TaskManagerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetSummary(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AddTask(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AddTasks(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetTasks(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ChangeToDone(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TaskManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetSummary': grpc.unary_unary_rpc_method_handler(
            servicer.GetSummary,
            request_deserializer=Employee.FromString,
            response_serializer=SpecificSummary.SerializeToString,
        ),
        'AddTask': grpc.unary_unary_rpc_method_handler(
            servicer.AddTask,
            request_deserializer=Task.FromString,
            response_serializer=SpecificSummary.SerializeToString,
        ),
        'AddTasks': grpc.stream_unary_rpc_method_handler(
            servicer.AddTasks,
            request_deserializer=Task.FromString,
            response_serializer=Summary.SerializeToString,
        ),
        'GetTasks': grpc.unary_stream_rpc_method_handler(
            servicer.GetTasks,
            request_deserializer=Employee.FromString,
            response_serializer=Task.SerializeToString,
        ),
        'ChangeToDone': grpc.stream_stream_rpc_method_handler(
            servicer.ChangeToDone,
            request_deserializer=Task.FromString,
            response_serializer=Task.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'gogrpcspec.TaskManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTaskManagerServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSummary(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AddTask(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AddTasks(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetTasks(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ChangeToDone(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTaskManagerStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSummary(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetSummary.future = None
    def AddTask(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    AddTask.future = None
    def AddTasks(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    AddTasks.future = None
    def GetTasks(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def ChangeToDone(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_TaskManager_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('gogrpcspec.TaskManager', 'AddTask'): Task.FromString,
      ('gogrpcspec.TaskManager', 'AddTasks'): Task.FromString,
      ('gogrpcspec.TaskManager', 'ChangeToDone'): Task.FromString,
      ('gogrpcspec.TaskManager', 'GetSummary'): Employee.FromString,
      ('gogrpcspec.TaskManager', 'GetTasks'): Employee.FromString,
    }
    response_serializers = {
      ('gogrpcspec.TaskManager', 'AddTask'): SpecificSummary.SerializeToString,
      ('gogrpcspec.TaskManager', 'AddTasks'): Summary.SerializeToString,
      ('gogrpcspec.TaskManager', 'ChangeToDone'): Task.SerializeToString,
      ('gogrpcspec.TaskManager', 'GetSummary'): SpecificSummary.SerializeToString,
      ('gogrpcspec.TaskManager', 'GetTasks'): Task.SerializeToString,
    }
    method_implementations = {
      ('gogrpcspec.TaskManager', 'AddTask'): face_utilities.unary_unary_inline(servicer.AddTask),
      ('gogrpcspec.TaskManager', 'AddTasks'): face_utilities.stream_unary_inline(servicer.AddTasks),
      ('gogrpcspec.TaskManager', 'ChangeToDone'): face_utilities.stream_stream_inline(servicer.ChangeToDone),
      ('gogrpcspec.TaskManager', 'GetSummary'): face_utilities.unary_unary_inline(servicer.GetSummary),
      ('gogrpcspec.TaskManager', 'GetTasks'): face_utilities.unary_stream_inline(servicer.GetTasks),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TaskManager_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('gogrpcspec.TaskManager', 'AddTask'): Task.SerializeToString,
      ('gogrpcspec.TaskManager', 'AddTasks'): Task.SerializeToString,
      ('gogrpcspec.TaskManager', 'ChangeToDone'): Task.SerializeToString,
      ('gogrpcspec.TaskManager', 'GetSummary'): Employee.SerializeToString,
      ('gogrpcspec.TaskManager', 'GetTasks'): Employee.SerializeToString,
    }
    response_deserializers = {
      ('gogrpcspec.TaskManager', 'AddTask'): SpecificSummary.FromString,
      ('gogrpcspec.TaskManager', 'AddTasks'): Summary.FromString,
      ('gogrpcspec.TaskManager', 'ChangeToDone'): Task.FromString,
      ('gogrpcspec.TaskManager', 'GetSummary'): SpecificSummary.FromString,
      ('gogrpcspec.TaskManager', 'GetTasks'): Task.FromString,
    }
    cardinalities = {
      'AddTask': cardinality.Cardinality.UNARY_UNARY,
      'AddTasks': cardinality.Cardinality.STREAM_UNARY,
      'ChangeToDone': cardinality.Cardinality.STREAM_STREAM,
      'GetSummary': cardinality.Cardinality.UNARY_UNARY,
      'GetTasks': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'gogrpcspec.TaskManager', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
