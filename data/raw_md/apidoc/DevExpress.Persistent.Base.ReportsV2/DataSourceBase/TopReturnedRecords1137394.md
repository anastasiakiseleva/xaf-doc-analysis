---
uid: DevExpress.Persistent.Base.ReportsV2.DataSourceBase.TopReturnedRecords
name: TopReturnedRecords
type: Property
summary: Specifies the maximum number of records to be retrieved from a data store.
syntax:
  content: |-
    [XtraSerializableProperty]
    public int TopReturnedRecords { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the maximum number of records to be retrieved from a data store.
seealso: []
---
The **TopReturnedRecords** value is passed to the [IObjectSpace.SetTopReturnedObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)) method.