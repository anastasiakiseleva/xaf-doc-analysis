---
uid: DevExpress.ExpressApp.BaseObjectSpace
name: BaseObjectSpace
type: Class
summary: A base class for the classes that implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface.
syntax:
  content: 'public class BaseObjectSpace : IObjectSpace, IDisposable, IObjectSpaceTaskRunner, ICriteriaProcessor'
seealso:
- linkId: "113707"
- linkId: DevExpress.ExpressApp.NonPersistentObjectSpace
- linkId: DevExpress.ExpressApp.BaseObjectSpace._members
  altText: BaseObjectSpace Members
---
When using XAF for building business applications, you can choose which data access technology to use:

- [XPO ORM](https://www.devexpress.com/Products/NET/ORM/) 
- [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core)
- [Non-Persistent Objects](xref:116516)

XAF core does not depend on a specific data layer. The classes that are required to interact with a particular data layer are contained in separate libraries, _DevExpress.ExpressApp.Xpo_ and _DevExpress.ExpressApp.EFCore_. 

You can create a custom library for working with an alternative ORM system. All of these libraries should contain an Object Space class. It represents an instrument that enables managing a cache with persistent objects. For instance, the _DevExpress.ExpressApp.Xpo_ library contains the [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) class. It is a wrapper over the [](xref:DevExpress.Xpo.UnitOfWork) class, which represents a cache with persistent objects in XPO. The _DevExpress.ExpressApp.EFCore_ library contains the [](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace) class. It is a wrapper over the [ObjectContext](https://learn.microsoft.com/en-us/dotnet/api/system.data.objects.objectcontext), that defines a container for in-memory objects in the Entity Framework. 

Any Object Space class must implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface. This interface exposes the members that do not depend on the used ORM system and the members that are data layer-specific. XAF supplies the **BaseObjectSpace** class. Its members can serve as the implementation of the **IObjectSpace** interface members that do not depend on the ORM system used. Both the **XPObjectSpace** and **EFCoreObjectSpace** classes are inherited from the **BaseObjectSpace** class to support the **IObjectSpace** interface.

A particular Object Space object is assigned for each View. It helps to retrieve and create objects represented by a View. Moreover, an Object Space tracks all changes made to its objects and saves them to the database when required. To access a View's Object Space, use the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property. In addition, you can access the Object Space of an object collection to manage its entire content and individual objects. For this purpose, use the [CollectionSourceBase.ObjectSpace](xref:DevExpress.ExpressApp.CollectionSourceBase.ObjectSpace) property.

> [!NOTE]
> The [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property is not supposed to be used in scenarios where a large amount of data is processed, created or deleted. Instead, use an independent Object Space which is not used by a View. Such an Object Space can be instantiated via the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method.

Use an ObjectSpace object's [BaseObjectSpace.CreateObject](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject(System.Type)) method to create persistent objects. In this instance, this Object Space will manage the newly created object's life cycle. All the changes made to this object will be tracked until the Object Space's [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method is invoked. When executing custom features, use the **CommitChanges** method to save all the changes made to the persistent objects belonging to the current Object Space. The changes include: creating, modifying or deleting an object (see [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified), [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*), [BaseObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanged), and [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)). For instance, the **CommitChanges** method is called when executing the **Save**, **SaveAndClose** and other built-in Actions.

The Object Space class also allows you to perform auxiliary operations with objects: search for the required object ([BaseObjectSpace.FindObject](xref:DevExpress.ExpressApp.BaseObjectSpace.FindObject*)), getting information on the required object ([IObjectSpace.GetKeyPropertyName](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyPropertyName(System.Type)), [IObjectSpace.GetKeyPropertyType](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyPropertyType(System.Type)) and [IObjectSpace.GetKeyValue](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object))), getting the required objects ([BaseObjectSpace.GetObject](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObject(System.Object)) and [BaseObjectSpace.GetObjectByKey](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey(System.Type,System.Object))), and others.

When creating a new View, you will need to create a new Object Space. For this purpose, use the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method. Note that in specific situations, you can create a View in the current Object Space. For instance, nested List Views that define non-aggregated collections are created in the parent View's Object Space.

[!include[](~/templates/objectspace-snippets.md)]
