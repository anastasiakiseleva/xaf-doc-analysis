---
uid: DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanging
name: ModifiedChanging
type: Event
summary: Occurs before the @DevExpress.ExpressApp.BaseObjectSpace.IsModified property is changed to **true**. Handle this event to cancel the property change or force the **IsModified** property to change.
syntax:
  content: public event EventHandler<ObjectSpaceModificationEventArgs> ModifiedChanging
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Edit-Linked-Persistent-Objects-Demo
  altText: How to edit a collection of Persistent Objects linked to a Non-Persistent Object
---
The following example shows how to cancel the **IsModified** property change when you modify the **Category** property of a **ProductView** object. In this case, the current Object Space does not add this object to the @DevExpress.ExpressApp.BaseObjectSpace.ModifiedObjects collection.

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    var npos = context.ObjectSpace as NonPersistentObjectSpace;
    if (npos != null) {
        npos.ModifiedChanging += Npos_ModifiedChanging;
    }
};
// ...
private void Npos_ModifiedChanging(object sender, ObjectSpaceModificationEventArgs e) {
    if(e.MemberInfo!= null) {
        if(e.MemberInfo.Owner.Type == typeof(ProductView) && 
        e.MemberInfo.Name == nameof(ProductView.Category)) {
            e.Cancel = true;
        }
    }
}
```

***