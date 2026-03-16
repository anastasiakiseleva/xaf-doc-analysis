---
uid: DevExpress.Persistent.BaseImpl.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)
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
- linkId: DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)
  altText: SecuredPropertySetter.SetPropertyValueWithSecurityBypass
- linkId: "113152"
---

The `SetPropertyValueWithSecurityBypass` method allows you to modify the value of a business object's property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366). If your business object is not an [BaseObject](xref:DevExpress.Persistent.BaseImpl.BaseObject) descendant, use the static [SecuredPropertySetter.SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) method instead.

[!include[set-property-value-with-security-bypass-description](~/templates/set-property-value-with-security-bypass-description.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using DevExpress.Xpo;
using System.ComponentModel;
// ...
public class TestClass : BaseObject {
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
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SetPropertyValueWithSecurityBypass(nameof(UpdatedOn), DateTime.Now);
            SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
        }
    }

    ApplicationUser GetCurrentUser() { 
        return Session.GetObjectByKey<ApplicationUser>(
            Session.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }
}
```

***
