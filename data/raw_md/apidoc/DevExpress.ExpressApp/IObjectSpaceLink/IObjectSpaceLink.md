---
uid: DevExpress.ExpressApp.IObjectSpaceLink
name: IObjectSpaceLink
type: Interface
summary: Implemented by [business classes](xref:113664) that provide a reference to an associated [Object Space](xref:113707).
syntax:
  content: public interface IObjectSpaceLink
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpaceLink._members
  altText: IObjectSpaceLink Members
---
XAF automatically adds the `IObjectSpaceLink` interface to all persistent EF Core classes at runtime. Cast an existing object to the `IObjectSpaceLink` type to use this interface from the Controller:

```csharp{5}
private void MyAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
    var cnt = View.CurrentObject as Contact;
    if(cnt == null)
        return;
    var cntOS = ((IObjectSpaceLink)cnt).ObjectSpace;
}
```

The code below uses the `IObjectSpaceLink` interface directly in the object:

```csharp{43}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.EFCore;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using Microsoft.Extensions.DependencyInjection;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
[DefaultClassOptions]
public class MyEntityObject : IXafEntityObject {
    [Key, Browsable(false)]
    public virtual Guid ID { get; protected set; }
    public virtual string Name { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser CreatedBy { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser UpdatedBy { get; set; }

    ApplicationUser GetCurrentUser() {
        return ObjectSpace.GetObjectByKey<ApplicationUser>(
            ObjectSpace.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }

    void IXafEntityObject.OnCreated() {
        // ...
    }

    void IXafEntityObject.OnLoaded() {
        // ...
    }

    void IXafEntityObject.OnSaving() {
        if (ObjectSpace.IsNewObject(this)) {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(this, nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(this, nameof(UpdatedBy), GetCurrentUser());
        }
    }

    IObjectSpace ObjectSpace {
        get {
            return ((IObjectSpaceLink)this).ObjectSpace;
        }
    }
    // ...
}
```


The snippet below uses the `IObjectSpaceLink` interface in a non-persistent class:

```csharp
[DomainComponent]
public class MyNonPersistentClass : IObjectSpaceLink {
    //...
    IObjectSpace objectSpace;
    IObjectSpace IObjectSpaceLink.ObjectSpace {
        get { return objectSpace; }
        set { objectSpace = value; }
    }
}
```

An Object Space reference is automatically assigned to the [IObjectSpaceLink.ObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace) property when [](xref:DevExpress.ExpressApp.IObjectSpace) methods are used to create a business object that supports `IObjectSpaceLink`. Data management is performed using these methods in internal XAF code, and we recommended that you use `IObjectSpace` in your custom code as well. You can implement this interface and access other business objects directly in the current object code. For example, you can write certain business logic in the [IXafEntityObject.OnCreated](xref:DevExpress.ExpressApp.IXafEntityObject.OnCreated), [IXafEntityObject.OnLoaded](xref:DevExpress.ExpressApp.IXafEntityObject.OnLoaded) and [IXafEntityObject.OnSaving](xref:DevExpress.ExpressApp.IXafEntityObject.OnSaving) methods, as demonstrated in the [](xref:DevExpress.ExpressApp.IXafEntityObject) interface description.

> [!NOTE]
> * The Object Space reference is set to `null` when an object is being deleted.
> * [!include[NonPersistentObjectsWithIObjectSpaceLink](~/templates/NonPersistentObjectsWithIObjectSpaceLink.md)]