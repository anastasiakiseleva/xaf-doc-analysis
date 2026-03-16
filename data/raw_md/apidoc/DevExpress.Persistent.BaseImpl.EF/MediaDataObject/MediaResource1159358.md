---
uid: DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaResource
name: MediaResource
type: Property
summary: Specifies the **MediaResourceObject** object which exposes the **MediaData** property of the byte array type.
syntax:
  content: |-
    [Aggregated]
    [VisibleInDetailView(false)]
    [VisibleInListView(false)]
    [VisibleInLookupListView(false)]
    public virtual MediaResourceObject MediaResource { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.BaseImpl.EF.MediaResourceObject
    description: The **MediaResourceObject** object which exposes the **MediaData** property of the byte array type.
seealso: []
---
The **MediaData** property of the **MediaResourceObject** object is persistent and stores the byte array returned by the [MediaDataObject.MediaData](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaData) property.