---
uid: DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaData
name: MediaData
type: Property
summary: Specifies a byte array with media data that is loaded from a database on demand when required.
syntax:
  content: |-
    [EditorAlias("ImagePropertyEditor")]
    [NotMapped]
    [VisibleInDetailView(false)]
    [VisibleInListView(false)]
    [VisibleInLookupListView(false)]
    public virtual byte[] MediaData { get; set; }
  parameters: []
  return:
    type: System.Byte[]
    description: A byte array object that is loaded from a database on demand when required.
seealso: []
---
It is not loaded together with the [](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject) itself and may contain any type of media.