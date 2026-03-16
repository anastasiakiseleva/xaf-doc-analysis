---
uid: DevExpress.ExpressApp.CompositeView.ObjectSpace
name: ObjectSpace
type: Property
summary: The current View's Object Space.
syntax:
  content: public override IObjectSpace ObjectSpace { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the current View's Object Space.
seealso: []
---
An Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)) is an instrument that allows you to manage a cache with persistent objects that are currently used in a View. Use the Object Space to retrieve a particular object set from the database, make changes to objects within this data set, or cancel changes. This does not influence the general database.

> [!NOTE]
> Do not use a root View's Object Space for the creation of another root View in it. Instead, create a new Object Space using the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method for the new root View.

> [!NOTE]
> The `ObjectSpace` property is not supposed to be used when a large amount of data is processed, created, or deleted. Instead, use an independent Object Space that is not used by a View. Such an Object Space can be instantiated using the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method.