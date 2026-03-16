---
uid: DevExpress.ExpressApp.PropertyCollectionSource.MasterObject
name: MasterObject
type: Property
summary: Provides access to the object that contains a collection property represented by the current [](xref:DevExpress.ExpressApp.PropertyCollectionSource).
syntax:
  content: public object MasterObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An object that contains a collection property represented by the current [](xref:DevExpress.ExpressApp.PropertyCollectionSource).
seealso:
- linkId: DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectChanged
- linkId: DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectType
---
When an object contains a collection property, this property is displayed in a [Detail View](xref:112611) via a nested List View. If a Detail View's [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) has not been assigned, the `MasterObject` property of the nested List View's Collection Source may return `null`.

To track changes of the `MasterObject`, subscribe to the [PropertyCollectionSource.MasterObjectChanged](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectChanged) event.

To see an example of accessing this property, refer to the [How to: Access the Master Object from a Nested List View](xref:113161) help topic.