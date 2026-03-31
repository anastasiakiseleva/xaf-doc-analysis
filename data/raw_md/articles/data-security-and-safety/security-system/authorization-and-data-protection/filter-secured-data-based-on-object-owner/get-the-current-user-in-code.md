---
uid: "113152"
seealso:
- linkId: "113436"
title: 'Access the Currently Logged User for Data Filtering, Business Logic, and Security Permissions'
---

# Access the Currently Logged User for Data Filtering, Business Logic, and Security Permissions

An application's functionality may depend on the user who is logged on. You may need to obtain the user name, user ID, or entire user object. This topic describes how to do that in popular scenarios. 

The following help topics describe how to use Dependency Injection to access an object that stores information about the current user:

* [Access Object Space, Security System, Caption Helper, and XAF Modules in the ASP.NET Core Environment](xref:403669#security-system)
* [Access Object Space, Security System, and Caption Helper in Custom Endpoint Methods](xref:403861#security-system)

## Access Current User in Criteria

Use the `CurrentUserId` [function criteria operator](xref:113307) to access the current user in a filter [criterion](xref:113052).

## Initialize the Object Owner (CreatedBy, UpdatedBy Properties)

To assign the current user reference to the `CreatedBy` and `UpdatedBy` properties of your business class, inherit your business class from `BaseObject` and override the `OnSaving` method. To set the property values, call the [BaseObject.SetPropertyValueWithSecurityBypass](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)) method. This method allows you to modify the value of a business object’s property even if write access to this property is denied for the current user by the [XAF Security System](xref:113366).

> [!IMPORTANT]
> `CreatedBy`, `UpdatedBy`, `UpdatedOn`, `CreatedOn`, and similar properties are supposed to be read-only in the UI for security and audit reasons (they can only be modified by developers in the program code). To make these properties read-only, add `[ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]` ([data annotation attributes](xref:112701)). Depending on your security and UI customization requirements, you may want to add additional constraints using [`HideInUI`](xref:DevExpress.Persistent.Base.HideInUIAttribute). You can make sure that end users cannot display these properties or their sub-fields in the UI. To accomplish this, do the following:
<!-- > - [Turn off Customization Forms](https://supportcenter.devexpress.com/ticket/details/t304667/xaf-how-to-completely-disable-adding-and-removing-fields-in-the-layout-customization) in ListView and DetailView completely.
> - [Hide unwanted properties](https://supportcenter.devexpress.com/ticket/details/q366279/xaf-how-to-hide-a-property-field-from-the-layout-customization-form-detailview-grid-s) in Customization Forms.
> - [Hide UI elements that add/remove fields](https://supportcenter.devexpress.com/ticket/details/t304667/xaf-how-to-completely-disable-adding-and-removing-fields-in-the-layout-customization) in Customization Forms (allow access to predefined fields only). -->

The following code snippet initializes a business object's `CreatedBy` and `UpdatedBy` properties:

**File:** _MySolution.Module/BusinessObjects/TestClass.cs_

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp{14-27}
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.Extensions.DependencyInjection;
// ...
public class TestClass : BaseObject {
    // ...
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
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
            SetPropertyValueWithSecurityBypass(nameof(UpdatedBy), GetCurrentUser());
        }
    }
} 
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp{28-41}
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
public class TestClass : BaseObject { 
    public TestClass(Session session) : base(session) { } 
    ApplicationUser _createdBy; 
    ApplicationUser _updatedBy; 

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

    protected override void OnSaving() {
        base.OnSaving();
        if (Session.IsNewObject(this)) {
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
        else {
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

### Initialize the Object Owner - Middle-Tier Security Specifics

In applications with middle-tier security, you need to take the following additional considerations into account:

- A business object's `OnCreated` and `AfterConstruction` methods are called on the client side, so property values initialized by these methods are available to the client application. Because of this, it is not secure to use these methods to initialize properties that store sensitive data (`CreatedBy`, `UpdatedBy`, and so on).
- In cases when you need to initialize properties that store sensitive data, we strongly recommend that you always use the [OnSaving](xref:DevExpress.ExpressApp.IXafEntityObject.OnSaving) method. This method is secure because it is called on the middle-tier server side only.
- In applications with middle tier security, the [BaseObject.SetPropertyValueWithSecurityBypass](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.SetPropertyValueWithSecurityBypass``1(System.String,``0)) method can only be called from the `OnSaving` method. Otherwise, an exception is thrown.

## Configure Permissions Based on the Object Owner

To grant access to objects that are owned by the current user and prohibit access to other objects, implement the `CreatedBy` property as demonstrated above, and configure the security permissions as follows:

* Add a Type Permission for the object type you wish to filter and set its `ReadState` property to `Deny` or leave it empty if the role's Permission Policy is `DenyAllByDefault`.
* Add an Object Permission that allows a user to read objects they own (user ID matches `CurrentUserId()`).

**File:** _MySolution.Module/DatabaseUpdate/Updater.cs_

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.SystemModule;
// ...
defaultRole.AddTypePermission<TestClass>(SecurityOperations.Read, SecurityPermissionState.Deny);
defaultRole.AddObjectPermissionFromLambda<TestClass>(
    SecurityOperations.Read, 
    e => e.CreatedBy.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), 
    SecurityPermissionState.Allow
);
// or
// userRole.AddObjectPermission<Note>(SecurityOperations.Read, 
//     "CreatedBy.ID = CurrentUserId()", SecurityPermissionState.Allow);
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.SystemModule;
// ...
defaultRole.AddTypePermission<TestClass>(SecurityOperations.Read, SecurityPermissionState.Deny);
defaultRole.AddObjectPermissionFromLambda<TestClass>(
    SecurityOperations.Read, 
    e => e.CreatedBy.Oid == (Guid)CurrentUserIdOperator.CurrentUserId(), 
    SecurityPermissionState.Allow
);
// or
// userRole.AddObjectPermission<Note>(SecurityOperations.Read, 
//     "CreatedBy.Oid = CurrentUserId()", SecurityPermissionState.Allow);
```
***

For more information, refer to [](xref:119065).

To try the described technique in your application and add several users, run the application and create an object of your business class under different user accounts  - only the currently logged-in user's objects are displayed in the List View:

![Result](~/images/show-objects-linked-to-user-result.png)

The following example implements a more complex use case scenario with cascading owner objects:

[!example[How to restrict inter-departmental data access using Security Permissions](https://github.com/DevExpress-Examples/xaf-separate-employees-data-in-different-departments-using-security-permissions)]

## Check Security Permissions in Code

The following help topic describes how to check if a user has a specific role or permission to perform a certain operation: [](xref:403824).

