---
uid: DevExpress.ExpressApp.Model.IModelClass.KeyProperty
name: KeyProperty
type: Property
summary: Specifies the property that is considered a key.
syntax:
  content: string KeyProperty { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the name of the property that is considered a key.
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.Oid
---
By default, this property is set to the [](xref:DevExpress.Persistent.BaseImpl.BaseObject) node's **KeyProperty** property value, which is set to **Oid**.

Key properties can be read-only in XAF applications. For details, see **KeyProperty** in the [Data Annotations in Data Model](xref:112701) topic.