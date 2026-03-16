---
uid: DevExpress.ExpressApp.Xpo.SecuredPropertySetter
name: SecuredPropertySetter
type: Class
summary: An axillary class that allows you to specify an XPO persistent object's properties bypassing security checks.
syntax:
  content: public static class SecuredPropertySetter
seealso:
- linkId: DevExpress.ExpressApp.Xpo.SecuredPropertySetter._members
  altText: SecuredPropertySetter Members
- linkId: DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)
  altText: SecuredPropertySetter.SetPropertyValueWithSecurityBypass
- linkId: "113152"
---

Use the `SecuredPropertySetter` class's [SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) static method allows you to modify the value of a business object's property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366). If your business object class extends [BaseObject](xref:DevExpress.Persistent.BaseImpl.BaseObject) and you need to modify this object's own property, you can use the [BaseObject.SetPropertyValueWithSecurityBypass](xref:DevExpress.Persistent.BaseImpl.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)) protected method instead.

[!include[set-property-value-with-security-bypass-description](~/templates/set-property-value-with-security-bypass-description.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using DevExpress.Xpo;
using System.ComponentModel;
// ...
public class TestClass : XPLiteObject {
    public TestClass(Session session) : base(session) { }
    // ...
    ApplicationUser _createdBy;
    ApplicationUser _updatedBy;
    DateTime? _updatedOn;
    
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public ApplicationUser CreatedBy {
        get { return _createdBy; }
        set { 
            SetPropertyValue("CreatedBy", ref _createdBy, value);
        }
    }
    
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public ApplicationUser UpdatedBy {
        get { return _updatedBy; }
        set {
            SetPropertyValue("UpdatedBy", ref _updatedBy, value);
        }
    }

    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    [ModelDefault(nameof(IModelCommonMemberViewItem.DisplayFormat), "G")]
    public DateTime? UpdatedOn {
        get { return _updatedOn; }
        set {
            SetPropertyValue("UpdatedOn", ref _updatedOn, value);
        }
    }

    protected override void OnSaving() {
        base.OnSaving();
        if (Session.IsNewObject(this)) {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(this, nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(this, nameof(UpdatedOn), DateTime.Now);
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(this, nameof(UpdatedBy), GetCurrentUser());
        }
    }

    ApplicationUser GetCurrentUser() { 
        return Session.GetObjectByKey<ApplicationUser>(
            Session.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }
    // ...
}
```

***
