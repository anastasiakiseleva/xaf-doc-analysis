---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateServerCollection(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: CreateServerCollection(Type, CriteriaOperator)
type: Method
summary: Creates and initializes a new instance of the [](xref:DevExpress.Xpo.XPServerCollectionSource) class with the current Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) and criteria-specific options.
syntax:
  content: public override object CreateServerCollection(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of persistent objects to include into the collection.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The **DevExpress.Data.Filtering.CriteriaOperator** that specifies the criteria for object selection in a data store.
  return:
    type: System.Object
    description: A server collection that includes the persistent objects of the specified type. In addition, only objects that satisfy the specified criteria will be retrieved to this collection.
seealso: []
---
The newly created collection will use the current Object Space to load and save persistent objects.

This method is used by Collection Sources (see [](xref:DevExpress.ExpressApp.CollectionSource) and [](xref:DevExpress.ExpressApp.PropertyCollectionSource)) to create a collection in server mode. For details on the **XPServerCollectionSource** class, refer to the [](xref:DevExpress.Xpo.XPServerCollectionSource) topic in the XPO documentation.