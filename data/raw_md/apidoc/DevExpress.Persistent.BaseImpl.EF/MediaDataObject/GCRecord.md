---
uid: DevExpress.Persistent.BaseImpl.EF.MediaDataObject.GCRecord
name: GCRecord
type: Property
summary: Defines whether the object is marked as deleted.
syntax:
  content: public override int GCRecord { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: '`1` if the object is marked as deleted; otherwise, `0`'
seealso: []
---
When [soft (deferred) object deletion](xref:405259) is enabled, XAF marks records as deleted instead of removing them from the data store. This requires an additional system column to indicate the deleted state.

The `GCRecord` (GC—garbage collection) property serves as a marker for removed objects. When an object is marked as deleted, XAF assigns the `1` value to the property.