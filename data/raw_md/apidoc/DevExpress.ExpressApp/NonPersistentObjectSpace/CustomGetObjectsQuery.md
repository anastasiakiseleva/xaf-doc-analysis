---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.CustomGetObjectsQuery
name: CustomGetObjectsQuery
type: Event
summary: Occurs when the @DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsQuery``1(System.Boolean) method is executed.
syntax:
  content: public event EventHandler<CustomGetObjectsQueryEventArgs> CustomGetObjectsQuery
seealso: []
---
Handle this event to pass a custom [strongly-typed query](xref:System.Linq.IQueryable`1) of [non-persistent objects](xref:116516) to the @DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsQuery``1(System.Boolean) method. The following example shows how to handle this event in the Application Builder code:

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    NonPersistentObjectSpace nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
    if (nonPersistentObjectSpace != null) {
        nonPersistentObjectSpace.CustomGetObjectsQuery += NonPersistentObjectSpace_CustomGetObjectsQuery;
        //...
    }
};
// ...
List<Article> articles;
private void NonPersistentObjectSpace_CustomGetObjectsQuery(object sender, CustomGetObjectsQueryEventArgs e) {
    if (typeof(Article).IsAssignableFrom(e.ObjectType)) {
        e.Queryable = articles.AsQueryable();
    }
}
```

***

[`/\.(ObjectSpaceCreated)/`]: xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
[`NonPersistentObjectSpace`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace
[`/\.(CustomGetObjectsQuery)/`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace.CustomGetObjectsQuery
[`/\.(ObjectSpace) /`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs.ObjectSpace
[`ObjectSpaceCreatedEventArgs`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs
[`IsAssignableFrom`]: xref:DevExpress.ExpressApp.DC.ITypeInfo.IsAssignableFrom(DevExpress.ExpressApp.DC.ITypeInfo)
[`AsQueryable`]: xref:System.Linq.Queryable.AsQueryable*
