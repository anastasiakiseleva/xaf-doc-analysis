---
uid: DevExpress.ExpressApp.CollectionSourceBase.AllowAdd
name: AllowAdd
type: Property
summary: Returns the value that indicates whether it is possible to add objects to the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) or not.
syntax:
  content: public bool AllowAdd { get; }
  parameters: []
  return:
    type: System.Boolean
    description: A Boolean value that indicates whether it is possible to add objects to the Collection Source's collection or not. **true** if it is possible to add objects, otherwise **false**.
seealso: []
---
Generally, you do not need to use this property. However, you may check it to see whether new objects can be added to the Collection Source's collection. For instance, if the collection has not been instantiated or is read-only, this property will return **false**.