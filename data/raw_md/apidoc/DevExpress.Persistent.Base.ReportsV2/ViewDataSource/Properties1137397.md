---
uid: DevExpress.Persistent.Base.ReportsV2.ViewDataSource.Properties
name: Properties
type: Property
summary: Gets the list of fields to be loaded from the data store.
syntax:
  content: |-
    [XtraSerializableProperty(XtraSerializationVisibility.Collection, true)]
    public ViewPropertiesCollection Properties { get; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ReportsV2.ViewPropertiesCollection
    description: A **ViewPropertiesCollection** object that specifies the list of fields to be loaded from the data store.
seealso:
- linkId: "113591"
---
A collection of [](xref:DevExpress.ExpressApp.Utils.DataViewExpression) objects is populated based on this property, and then passed to the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method as the _expressions_ parameter.