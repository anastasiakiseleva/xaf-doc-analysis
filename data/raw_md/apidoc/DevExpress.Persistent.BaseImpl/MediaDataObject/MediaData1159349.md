---
uid: DevExpress.Persistent.BaseImpl.MediaDataObject.MediaData
name: MediaData
type: Property
summary: Specifies a byte array with media data that is loaded from a database on demand when required.
syntax:
  content: |-
    [Browsable(false)]
    [Delayed(true)]
    [Size(-1)]
    public byte[] MediaData { get; set; }
  parameters: []
  return:
    type: System.Byte[]
    description: A byte array object that is loaded from a database on demand when required.
seealso: []
---
It is not loaded together with the [](xref:DevExpress.Persistent.BaseImpl.MediaDataObject) itself and may contain any type of media.