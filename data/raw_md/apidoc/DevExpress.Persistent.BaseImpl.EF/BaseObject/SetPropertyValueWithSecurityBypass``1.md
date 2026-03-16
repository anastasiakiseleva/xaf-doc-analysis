---
uid: DevExpress.Persistent.BaseImpl.EF.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)
name: SetPropertyValueWithSecurityBypass<T>(String, T)
type: Method
summary: Sets the object's property value bypassing security checks.
syntax:
  content: protected void SetPropertyValueWithSecurityBypass<T>(string propertyName, T value)
  parameters:
  - id: propertyName
    type: System.String
    description: The name of the property to set.
  - id: value
    type: '{T}'
    description: The value to assign to the property.
  typeParameters:
  - id: T
    description: The type of the value assigned to the property.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)
  altText: SecuredPropertySetter.SetPropertyValueWithSecurityBypass
- linkId: "113152"
---

The `SetPropertyValueWithSecurityBypass` method allows you to modify the value of a business object's property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366). If your business object is not an [BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) descendant, use the static [SecuredPropertySetter.SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.EFCore.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) method instead.

[!include[set-property-value-with-security-bypass-description](~/templates/set-property-value-with-security-bypass-description.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.EFCore;
using DevExpress.Persistent.Base;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
public class TestClass : BaseObject {
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

    public override void OnSaving() {
        base.OnSaving();
        if (ObjectSpace.IsNewObject(this)) {
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
            SetPropertyValueWithSecurityBypass(nameof(UpdatedOn), DateTime.Now);
        }
    }
} 
```

***
