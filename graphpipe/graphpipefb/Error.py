# automatically generated by the FlatBuffers compiler, do not modify

# namespace: graphpipe

import flatbuffers

class Error(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsError(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Error()
        x.Init(buf, n + offset)
        return x

    # Error
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Error
    def Code(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Error
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def ErrorStart(builder): builder.StartObject(2)
def ErrorAddCode(builder, code): builder.PrependInt64Slot(0, code, 0)
def ErrorAddMessage(builder, message): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(message), 0)
def ErrorEnd(builder): return builder.EndObject()
