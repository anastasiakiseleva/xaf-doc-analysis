---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace
name: NonPersistentObjectSpace
type: Class
summary: An [Object Space](xref:113707) used to manage [non-persistent objects](xref:116516).
syntax:
  content: 'public class NonPersistentObjectSpace : CompositeObjectSpace'
seealso:
- linkId: DevExpress.ExpressApp.NonPersistentObjectSpace._members
  altText: NonPersistentObjectSpace Members
---
To supply non-persistent objects for `NonPersistentObjectSpace`, use the @DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting event that occurs when `NonPersistentObjectSpace` creates an object collection. You can find examples  in the following topics:

* [How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471)
* [How to: Display Non-Persistent Objects in a Report](xref:114516)
* [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672)

To supply an object returned by the @DevExpress.ExpressApp.NonPersistentObjectSpace.GetObject(System.Object) method, use the @DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting event.

[!include[NonPersistentObjectSpace.ModifiedObjects Note](~/templates/nonpersistentobjectspace.modifiedobjects-note111302.md)]

The [IObjectSpaceLink.ObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace) property of non-persistent objects that support @DevExpress.ExpressApp.IObjectSpaceLink is initialized in these cases:

* An object is created using the [IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) method.
* An object is accessed using the [NonPersistentObjectSpace.GetObject](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.GetObject(System.Object)) method.
* A collection is accessed using the [IObjectSpace.GetObjects](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*) or [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) method.

If an object from another Object Space passed to the `GetObject` method implements `IObjectSpaceLink`, and its `ObjectSpace` property is `null`, the current `NonPersistentObjectSpace` assigns a link to itself in this property. Similar behavior is implemented for objects returned by the `GetObjects` and `CreateCollection` methods using the [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting) event.

### Enable the Non-Persistent Object Space in Your Application

The [Template Kit](xref:405447) automatically registers the non-persistent Object Space Provider in the application. However, for projects created with older XAF versions, you need to register it manually. Call the [AddNonPersistent](xref:DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderBuilderExtensions.AddNonPersistent``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions})) method in the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders property:

# [MySolution.Blazor.Server/Startup.cs | MySolution.Win/Startup.cs | MySolution.WebApi/Startup.cs](#tab/tabid-csharp)

```csharp
builder.ObjectSpaceProviders
    // ...
    .AddNonPersistent();
// ...
```

***


> [!NOTE]
> [!include[Object Space Providers Order](~/templates/objectspaceprovidersorder.md)]
