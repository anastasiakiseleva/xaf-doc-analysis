---
uid: DevExpress.ExpressApp.EFCore.SecuredPropertySetter
name: SecuredPropertySetter
type: Class
summary: An axillary class that allows you to specify an EF Core persistent object's properties bypassing security checks.
syntax:
  content: public static class SecuredPropertySetter
seealso:
- linkId: DevExpress.ExpressApp.EFCore.SecuredPropertySetter._members
  altText: SecuredPropertySetter Members
- linkId: DevExpress.ExpressApp.EFCore.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)
  altText: SecuredPropertySetter.SetPropertyValueWithSecurityBypass
- linkId: "113152"
---

The `SecuredPropertySetter` class's [SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.EFCore.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) static method allows you to modify the value of a business object's property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366). If your business object class extends [BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) and you need to modify this object's own property, you can use the [BaseObject.SetPropertyValueWithSecurityBypass](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)) protected method instead.

[!include[set-property-value-with-security-bypass-description](~/templates/set-property-value-with-security-bypass-description.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.EFCore;
using DevExpress.Persistent.Base;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
public class TestClass : IXafEntityObject, IObjectSpaceLink { 
    // ...
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser CreatedBy { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser UpdatedBy { get; set; }
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    [ModelDefault(nameof(IModelCommonMemberViewItem.DisplayFormat), "G")]
    public virtual DateTime? UpdatedOn { get; set; }

    ApplicationUser GetCurrentUser() {
        return ObjectSpace.GetObjectByKey<ApplicationUser>(
            ObjectSpace.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }

    void OnSaving() {
        base.OnSaving();
        if (ObjectSpace.IsNewObject(this)) {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(UpdatedOn), DateTime.Now);
        }
    }
} 
```

***
