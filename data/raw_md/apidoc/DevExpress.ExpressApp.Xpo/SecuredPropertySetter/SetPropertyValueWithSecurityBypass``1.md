---
uid: DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)
name: SetPropertyValueWithSecurityBypass<T>(Object, String, T)
type: Method
summary: Sets a persistent object's property value bypassing security checks.
syntax:
  content: public static void SetPropertyValueWithSecurityBypass<T>(object obj, string propertyName, T value)
  parameters:
  - id: obj
    type: System.Object
    description: The specified persistent object.
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
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)
  altText: BaseObject.SetPropertyValueWithSecurityBypass
- linkId: "113152"
---

The `SetPropertyValueWithSecurityBypass` static method allows you to modify the value of a business object's property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366). If your business object class extends [BaseObject](xref:DevExpress.Persistent.BaseImpl.BaseObject) and you need to modify this object's own property, you can use the [BaseObject.SetPropertyValueWithSecurityBypass](xref:DevExpress.Persistent.BaseImpl.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)) protected method instead.

[!include[set-property-value-with-security-bypass-description](~/templates/set-property-value-with-security-bypass-description.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using DevExpress.Xpo;
using System.ComponentModel;
// ...
public class TestClass : IXafEntityObject, IObjectSpaceLink {
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
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(UpdatedOn), DateTime.Now);
            SecuredPropertySetter.SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
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
