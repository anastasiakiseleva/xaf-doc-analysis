---
uid: DevExpress.ExpressApp.CollectionSourceBase.AllowRemove
name: AllowRemove
type: Property
summary: Returns the value that indicates whether it is possible to remove objects from the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) or not.
syntax:
  content: public bool AllowRemove { get; }
  parameters: []
  return:
    type: System.Boolean
    description: A Boolean value that indicates whether it is possible to remove objects from the Collection Source's collection or not. **true** if it is possible to remove objects, otherwise **false**.
seealso: []
---
Generally, you do not need to use this property. However, you may check it to see whether objects can be removed from the Collection Source's collection. For instance, if the collection has not been instantiated or is read-only, this property will return **false**.