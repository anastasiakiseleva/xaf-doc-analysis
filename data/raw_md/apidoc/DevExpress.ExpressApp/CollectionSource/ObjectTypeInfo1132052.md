---
uid: DevExpress.ExpressApp.CollectionSource.ObjectTypeInfo
name: ObjectTypeInfo
type: Property
summary: Provides metadata information on the type of the objects contained in the [](xref:DevExpress.ExpressApp.CollectionSource)'s collection.
syntax:
  content: public override ITypeInfo ObjectTypeInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An **ITypeInfo** object which provides metadata information on the type of the objects contained in the Collection Source's collection.
seealso: []
---
The **ObjectTypeInfo**'s properties supply metadata on the objects contained in the Collection Source's collection. Use the following members of the object returned by this property to get information on the type of the objects contained in the Collection Source's collection:

* **Type** - a type of the objects contained in the Collection Source's collection
* **Name** - a name of the **Type** type
* **FullName** - a fully qualified name of the **Type** type (includes namespace)
* **IsPersistent** - **true** if the **Type** is persistent; otherwise false
* **IsAbstract** - **true** if the **Type** is abstract; otherwise false