---
uid: DevExpress.ExpressApp.IXafEntityObject
name: IXafEntityObject
type: Interface
summary: Declares methods that are called automatically when a business object is being created, loaded and saved.
syntax:
  content: public interface IXafEntityObject
seealso:
- linkId: DevExpress.ExpressApp.IXafEntityObject._members
  altText: IXafEntityObject Members
---

When a business object supports `IXafEntityObject`, the [Object Space](xref:113707) automatically calls the [IXafEntityObject.OnCreated](xref:DevExpress.ExpressApp.IXafEntityObject.OnCreated), [IXafEntityObject.OnLoaded](xref:DevExpress.ExpressApp.IXafEntityObject.OnLoaded) and [IXafEntityObject.OnSaving](xref:DevExpress.ExpressApp.IXafEntityObject.OnSaving) methods of this interface when an object is being created, loaded and saved. Thus, you can implement these methods and add certain business logic directly in the business object code, without the use of [Controllers](xref:112621). Usually, you may need to access other business objects from your code, so you can implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface to access an [](xref:DevExpress.ExpressApp.IObjectSpace) instance and use its methods to query objects.

> [!NOTE]
> * The `IXafEntityObject` interface is intended for use with Entity Framework and [Non-Persistent Objects](xref:116516). For XPO ORM, use the [BaseObject.AfterConstruction](xref:DevExpress.Persistent.BaseImpl.BaseObject.AfterConstruction) and `BaseObject.OnSaving` methods.
> * You can use the DevExpress [Template Kit](xref:405447#create-a-new-item) to add a new **EF Core Business Object** that supports both `IXafEntityObject` and `IObjectSpaceLink` in your project.

In the following code snippet, the `CreatedBy` property refers to the user who created the current object, and the `UpdatedBy` property specifies the user who last changed the object. Note that the example code uses the [SecuredPropertySetter.SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.EFCore.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) method to set values of these properties from the `OnSaving` method. This method allows you to modify the value of a business object’s property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366).

# [C#](#tab/tabid-csharp-ef)

```csharp{14-17,32-39}
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
// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

You can also inherit your class from the [DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) class that implements this interface.

# [C#](#tab/tabid-csharp-ef)

```csharp{12-15,22-32}
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using YourApplicaionName.Module.BusinessObjects;
[DefaultClassOptions]
public class MyEntityObject : BaseObject {
    public virtual string Name { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser CreatedBy { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser UpdatedBy { get; set; }

    ApplicationUser GetCurrentUser() {
        return ObjectSpace.GetObjectByKey<ApplicationUser>(
            ObjectSpace.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }

    public override void OnSaving() {
        base.OnSaving();
        if (ObjectSpace.IsNewObject(this)) {
            // You can use BaseObject.SetPropertyValueWithSecurityBypass
            // to set the property value.
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
        }
    }
    // ...
}
```

***
