# [Entity Framework Core](#tab/tabid-efcore)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.CloneObject;
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.EntityFrameworkCore.Metadata;

namespace YourApplicationName.Module.Controllers;

public class CustomizeCloneObjectController: ObjectViewController {
    protected override void OnActivated() {
        base.OnActivated();
        var cloneObjectController = Frame.GetController<CloneObjectViewController>();
        if(cloneObjectController != null) {
            cloneObjectController.CustomCloneObject += cloneObjectController_CustomCloneObject;
        }
    }
    void cloneObjectController_CustomCloneObject(object sender, CustomCloneObjectEventArgs e) {
        e.TargetObjectSpace = e.CreateDefaultTargetObjectSpace();
        var cloner = new MyCloner(e.TargetObjectSpace);
        object objectFromTargetObjectSpace = e.TargetObjectSpace.GetObject(e.SourceObject);
        e.ClonedObject = cloner.CloneTo(objectFromTargetObjectSpace, e.TargetType);
    }
}

public class MyCloner: Cloner {
    public MyCloner(IObjectSpace objectSpace) : base(objectSpace) {
    }
    public override void CopyPropertyValue(
        IPropertyBase property, object sourceObject, object targetObject) {
        if(!(property is IReadOnlyNavigationBase)) {
            base.CopyPropertyValue(property, sourceObject, targetObject);
        }
    }
}
```

# [XPO](#tab/tabid-xpo)

```csharp
using DevExpress.ExpressApp.CloneObject;
using DevExpress.Xpo.Metadata;
using DevExpress.Xpo;
using DevExpress.Persistent.Base;
//...

namespace YourApplicationName.Module.Controllers;

public class CustomizeCloneObjectController : ObjectViewController {
    protected override void OnActivated() {
        base.OnActivated();
        var cloneObjectController = Frame.GetController<CloneObjectViewController>();
        if (cloneObjectController != null) {
            cloneObjectController.CustomCloneObject += cloneObjectController_CustomCloneObject;
        }
    }
    void cloneObjectController_CustomCloneObject(object sender, CustomCloneObjectEventArgs e) {
        var cloner = new MyCloner();
        e.TargetObjectSpace = e.CreateDefaultTargetObjectSpace();
        object objectFromTargetObjectSpace = e.TargetObjectSpace.GetObject(e.SourceObject);
        e.ClonedObject = cloner.CloneTo(objectFromTargetObjectSpace, e.TargetType);
    }
}
public class MyCloner : Cloner {
    public override void CopyMemberValue(
        XPMemberInfo memberInfo, IXPSimpleObject sourceObject, IXPSimpleObject targetObject) {
        if (!memberInfo.IsAssociation) {
            base.CopyMemberValue(memberInfo, sourceObject, targetObject);
        }
    }
}
```
***