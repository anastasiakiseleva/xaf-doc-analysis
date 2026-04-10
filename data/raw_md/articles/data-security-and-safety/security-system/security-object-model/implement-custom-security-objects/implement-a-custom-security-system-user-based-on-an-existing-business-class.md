---
uid: "113452"
title: 'Implement a Custom Security System User Based on an Existing Business Class'
seealso:
- linkId: "404875"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_How-to-get-role-code-from-the-UI
  altText: 'GitHub Example: XAF - Generate Database Updater Code for Security Roles Created in Application UI in Development Environment'

---
# Implement a Custom Security System User Based on an Existing Business Class

Consider the following situation. You have an unsecure XAF application, and its business model includes the `Employee` business class. This class exposes information such as personal data, the associated department, and assigned tasks. When enabling the [Security System](xref:113366), a `User` object is added to the business model, but the _Users_ who log in to your application are _Employees_. This topic explains how to merge the `User` and `Employee` into a single entity. For this purpose, multiple security-related interfaces in the `Employee` class will be supported, and as a result, the Security System will recognize the `Employee` type as one of the possible `User` types. You assign the `Employee` type to the [SecurityStrategy.UserType](xref:DevExpress.ExpressApp.Security.SecurityStrategy.UserType) property. As an additional benefit, it will be possible to use the _CurrentUserId()_ [Function Criteria Operator](xref:113307) to get the identifier of the current `Employee` (for example, to define a "tasks assigned to me" List View filter).

> [!Tip]
> [!include[CodeCentralObjectE4160](~/templates/CodeCentralExampleNote.md)] [https://supportcenter.devexpress.com/ticket/details/e4160/xaf-how-to-implement-a-security-system-user-based-on-an-existing-business-class](https://supportcenter.devexpress.com/ticket/details/e4160/xaf-how-to-implement-a-security-system-user-based-on-an-existing-business-class).

> [!NOTE]
> * A similar example for Entity Framework Core is available at [https://github.com/DevExpress-Examples/xaf-how-to-implement-a-security-system-user-based-on-an-existing-business-class](https://github.com/DevExpress-Examples/xaf-how-to-implement-a-security-system-user-based-on-an-existing-business-class).
> * As an alternative to the technique described in this topic, you can inherit the `Employee` class from [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser). To see an example, refer to the following topic: [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384).

## Initial Business Model

Start with a new XAF solution. Add the following `Employee` and `EmployeeTask` business classes to the [module project](xref:118045).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
public class Employee : Person {
    public virtual IList<EmployeeTask> OwnTasks { get; set; } = new ObservableCollection<EmployeeTask>();
}

public class Person : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
}

[DefaultClassOptions,ImageName("BO_Task")]
public class EmployeeTask : BaseObject {
    public virtual string Subject { get; set; }
    public virtual Employee Owner { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class Employee : Person {
    public Employee(Session session)
        : base(session) { }
    [Association("Employee-Task")]
    public XPCollection<EmployeeTask> OwnTasks {
        get { return GetCollection<EmployeeTask>(nameof(OwnTasks)); }
    }
}
[DefaultClassOptions, ImageName("BO_Task")]
public class EmployeeTask : Task {
    public EmployeeTask(Session session)
        : base(session) { }
    private Employee owner;
    [Association("Employee-Task")]
    public Employee Owner {
        get { return owner; }
        set { SetPropertyValue(nameof(Owner), ref owner, value); }
    }
}
```

***

## Support the ISecurityUser Interface

Add a reference to the _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_ assembly for the project that contains the `Employee` class. Extend the `Employee` class with the following code:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Validation;
// ...
public class Employee : Person, ISecurityUser {
    // ...
    #region ISecurityUser Members
    public virtual bool IsActive { get; set; } = true;
    [RuleRequiredField("EmployeeUserNameRequired", DefaultContexts.Save)]
    [RuleUniqueValue("EmployeeUserNameIsUnique", DefaultContexts.Save, 
        "The login with the entered user name was already registered within the system.")]
    public virtual string UserName { get; set; }
    #endregion
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Validation;
// ...
public class Employee : Person, ISecurityUser {
    // ...
    #region ISecurityUser Members
    private bool isActive = true;
    public bool IsActive {
        get { return isActive; }
        set { SetPropertyValue(nameof(IsActive), ref isActive, value); }
    }
    private string userName = String.Empty;
    [RuleRequiredField("EmployeeUserNameRequired", DefaultContexts.Save)]
    [RuleUniqueValue("EmployeeUserNameIsUnique", DefaultContexts.Save, 
        "The login with the entered user name was already registered within the system.")]
    public string UserName {
        get { return userName; }
        set { SetPropertyValue(nameof(UserName), ref userName, value); }
    }
    #endregion
}
```

***

Refer to the [](xref:DevExpress.ExpressApp.Security.ISecurityUser) interface description for details on this interface and its members.

## Support the IAuthenticationStandardUser Interface

> [!NOTE]
> If you are not planning to use the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication type, skip this section.

Extend the `Employee` class with the following code:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.ComponentModel;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
// ...
public class Employee : Person, ISecurityUser, IAuthenticationStandardUser {
    // ...
    #region IAuthenticationStandardUser Members
    public virtual bool ChangePasswordOnFirstLogon { get; set; }
    [Browsable(false), FieldSize(FieldSizeAttribute.Unlimited), SecurityBrowsable]
    public virtual string StoredPassword { get; set; }
    public bool ComparePassword(string password) {
        return PasswordCryptographer.VerifyHashedPasswordDelegate(this.StoredPassword, password);
    }
    public void SetPassword(string password) {
        this.StoredPassword = PasswordCryptographer.HashPasswordDelegate(password);
    }
    #endregion
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using System.ComponentModel;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
// ...
public class Employee : Person, ISecurityUser, IAuthenticationStandardUser {
    // ...
    #region IAuthenticationStandardUser Members
    private bool changePasswordOnFirstLogon;
    public bool ChangePasswordOnFirstLogon {
        get { return changePasswordOnFirstLogon; }
        set { 
            SetPropertyValue(nameof(ChangePasswordOnFirstLogon), ref changePasswordOnFirstLogon, value);
        }
    }
    private string storedPassword;
    [Browsable(false), Size(SizeAttribute.Unlimited), Persistent, SecurityBrowsable]
    public string StoredPassword {
        get { return storedPassword; }
        set { storedPassword = value; }
    }
    public bool ComparePassword(string password) {
        return PasswordCryptographer.VerifyHashedPasswordDelegate(this.storedPassword, password);
    }
    public void SetPassword(string password) {
        this.storedPassword = PasswordCryptographer.HashPasswordDelegate(password);
        OnChanged(nameof(StoredPassword));
    }
    #endregion
}
```

***

Refer to the [](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser) interface description for details on this interface and its members.

## Support the IAuthenticationActiveDirectoryUser Interface

> [!NOTE]
> If you are not planning to use the [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication type, skip this section.

Add the [](xref:DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser) interface to the supported interfaces list of the `Employee` class.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base.Security;
// ...
public class Employee : Person, ISecurityUser, 
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser {
    // ...
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base.Security;
// ...
public class Employee : Person, ISecurityUser, 
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser {
    // ...
}
```

***

The [IAuthenticationActiveDirectoryUser.UserName](xref:DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser.UserName) property declared by this interface has already been implemented in your code as a part of the `ISecurityUser` interface.

## Support the ISecurityUserWithRoles Interface

Extend the `Employee` class with the following code:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base.Security;
using DevExpress.Persistent.Validation;
using System.Collections.ObjectModel;
//...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser, 
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser, ISecurityUserWithRoles {
    // ...
    #region ISecurityUserWithRoles Members
    IList<ISecurityRole> ISecurityUserWithRoles.Roles {
        get {
            IList<ISecurityRole> result = new List<ISecurityRole>();
            foreach (EmployeeRole role in EmployeeRoles) {
                result.Add(role);
            }
            return result;
        }
    }
    [RuleRequiredField("EmployeeRoleIsRequired", DefaultContexts.Save,
        TargetCriteria = "IsActive",
        CustomMessageTemplate = "An active employee must have at least one role assigned")]
    public virtual IList<EmployeeRole> EmployeeRoles { get; set; } = new ObservableCollection<EmployeeRole>();
    #endregion
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base.Security;
using DevExpress.Persistent.Validation;
//...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    ISecurityUserWithRoles {
    // ...
    #region ISecurityUserWithRoles Members
    IList<ISecurityRole> ISecurityUserWithRoles.Roles {
        get {
            IList<ISecurityRole> result = new List<ISecurityRole>();
            foreach (EmployeeRole role in EmployeeRoles) {
                result.Add(role);
            }
            return result;
        }
    }
    #endregion
    [Association("Employees-EmployeeRoles")]
    [RuleRequiredField("EmployeeRoleIsRequired", DefaultContexts.Save,
        TargetCriteria = "IsActive",
        CustomMessageTemplate = "An active employee must have at least one role assigned")]
    public XPCollection<EmployeeRole> EmployeeRoles {
        get {
            return GetCollection<EmployeeRole>(nameof(EmployeeRoles));
        }
    }
}
```

***

Refer to the [](xref:DevExpress.ExpressApp.Security.ISecurityUserWithRoles) interface description for details on this interface and its members.

A many-to-many association with the built-in [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole) class cannot be defined (this class is already associated with the [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser)), which is why the following custom Role class should be implemented in the [module project](xref:118045).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.Linq;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using System.Collections.ObjectModel;
// ...
[ImageName("BO_Role")]
public class EmployeeRole : PermissionPolicyRoleBase, IPermissionPolicyRoleWithUsers {
    public virtual IList<Employee> Employees { get; set; } = new ObservableCollection<Employee>();
    IEnumerable<IPermissionPolicyUser> IPermissionPolicyRoleWithUsers.Users {
        get { return Employees.OfType<IPermissionPolicyUser>(); }
    } 
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using System.Linq;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// ...
[ImageName("BO_Role")]
public class EmployeeRole : PermissionPolicyRoleBase, IPermissionPolicyRoleWithUsers {
    public EmployeeRole(Session session)
        : base(session) {
    }
    [Association("Employees-EmployeeRoles")]
    public XPCollection<Employee> Employees {
        get {
            return GetCollection<Employee>(nameof(Employees));
        }
    }
    IEnumerable<IPermissionPolicyUser> IPermissionPolicyRoleWithUsers.Users {
        get { return Employees.OfType<IPermissionPolicyUser>(); }
    } 
}
```

***

## Support the IPermissionPolicyUser Interface

Extend the `Employee` class with the following code:

# [C#](#tab/tabid-csharp)

```csharp
using System.Linq;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
// ...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser {
    // ...
    #region IPermissionPolicyUser Members
    IEnumerable<IPermissionPolicyRole> IPermissionPolicyUser.Roles {
        get { return EmployeeRoles.OfType<IPermissionPolicyRole>(); }
    }
    #endregion
}
```

***

Refer to the [](xref:DevExpress.Persistent.Base.IPermissionPolicyUser) interface description for details on this interface and its members.

## Support the ICanInitialize Interface

The `ICanInitialize.Initialize` method is used to assign the default role when you use the [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication and set the [AuthenticationActiveDirectory.CreateUserAutomatically](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically) property to `true`. If you do not need to support user autocreation, skip this step. Otherwise, extend the `Employee` class with the following code:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
// ...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser, ICanInitialize {
    // ...
    #region ICanInitialize Members
    void ICanInitialize.Initialize(IObjectSpace objectSpace, SecurityStrategyComplex security) {
        EmployeeRole newUserRole = objectSpace.FirstOrDefault<EmployeeRole>(role => role.Name == security.NewUserRoleName);
        if (newUserRole == null) {
            newUserRole = objectSpace.CreateObject<EmployeeRole>();
            newUserRole.Name = security.NewUserRoleName;
            newUserRole.IsAdministrative = true;
            newUserRole.Employees.Add(this);
        }
    }
    #endregion
}
```

***

## Support the ISecurityUserWithLoginInfo Interface

In applications that support multiple authentication schemes, a user type must implement the [](xref:DevExpress.ExpressApp.Security.ISecurityUserWithLoginInfo) interface so that a user account record can store login information for all available schemes. Implement this interface as follows:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser, ICanInitialize, ISecurityUserWithLoginInfo {
    // ...
    #region ISecurityUserWithLoginInfo Members
    public Employee() : base() {
        // ...
        EmployeeLogins = new ObservableCollection<EmployeeLoginInfo>();
    }

    [Browsable(false)]
    [DevExpress.ExpressApp.DC.Aggregated]
    public virtual IList<EmployeeLoginInfo> EmployeeLogins { get; set; }

    IEnumerable<ISecurityUserLoginInfo> IOAuthSecurityUser.UserLogins => EmployeeLogins.OfType<ISecurityUserLoginInfo>();

    ISecurityUserLoginInfo ISecurityUserWithLoginInfo.CreateUserLoginInfo(string loginProviderName, string providerUserKey) {
        EmployeeLoginInfo result = ((IObjectSpaceLink)this).ObjectSpace.CreateObject<EmployeeLoginInfo>();
        result.LoginProviderName = loginProviderName;
        result.ProviderUserKey = providerUserKey;
        result.User = this;
        return result;
    }
    #endregion
}

public class EmployeeLoginInfo : ISecurityUserLoginInfo {

    public EmployeeLoginInfo() { }

    [Browsable(false)]
    public virtual Guid ID { get; protected set; }

    [Appearance("PasswordProvider", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public virtual string LoginProviderName { get; set; }

    [Appearance("PasswordProviderUserKey", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public virtual string ProviderUserKey { get; set; }

    [Browsable(false)]
    public virtual Guid UserForeignKey { get; set; }

    [Required]
    [ForeignKey(nameof(UserForeignKey))]
    public virtual Employee User { get; set; }

    object ISecurityUserLoginInfo.User => User;
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.Security;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser, ICanInitialize, ISecurityUserWithLoginInfo {
    // ...
    #region ISecurityUserWithLoginInfo Members
    [Browsable(false)]
    [Aggregated, Association("User-LoginInfo")]
    public XPCollection<EmployeeLoginInfo> LoginInfo {
        get { return GetCollection<EmployeeLoginInfo>(nameof(LoginInfo)); }
    }

    IEnumerable<ISecurityUserLoginInfo> IOAuthSecurityUser.UserLogins => LoginInfo.OfType<ISecurityUserLoginInfo>();

    ISecurityUserLoginInfo ISecurityUserWithLoginInfo.CreateUserLoginInfo(string loginProviderName, string providerUserKey) {
        EmployeeLoginInfo result = new EmployeeLoginInfo(Session);
        result.LoginProviderName = loginProviderName;
        result.ProviderUserKey = providerUserKey;
        result.User = this;
        return result;
    }
    #endregion
}

[DeferredDeletion(false)]
[Persistent("PermissionPolicyUserLoginInfo")]
public class EmployeeLoginInfo : BaseObject, ISecurityUserLoginInfo {
    private string loginProviderName;
    private Employee user;
    private string providerUserKey;
    public EmployeeLoginInfo(Session session) : base(session) { }

    [Indexed("ProviderUserKey", Unique = true)]
    [Appearance("PasswordProvider", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public string LoginProviderName {
        get { return loginProviderName; }
        set { SetPropertyValue(nameof(LoginProviderName), ref loginProviderName, value); }
    }

    [Appearance("PasswordProviderUserKey", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public string ProviderUserKey {
        get { return providerUserKey; }
        set { SetPropertyValue(nameof(ProviderUserKey), ref providerUserKey, value); }
    }

    [Association("User-LoginInfo")]
    public Employee User {
        get { return user; }
        set { SetPropertyValue(nameof(User), ref user, value); }
    }

    object ISecurityUserLoginInfo.User => User;
}
```

***

## Support the ISecurityUserLockout Interface (.NET 8+)

Implement the @DevExpress.ExpressApp.Security.ISecurityUserLockout interface to support the user lockout feature (the ability to lock out users who fail to enter the correct password several times in a row).

# [EF Core](#tab/tabid-csharp-ef)
```csharp
using System.Collections.ObjectModel;
using System.ComponentModel;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser, ICanInitialize, ISecurityUserWithLoginInfo, ISecurityUserLockout{
    // ...
    #region ISecurityUserLockout Members
    [Browsable(false)]
    public virtual int AccessFailedCount { get; set; }
    
    [Browsable(false)]
    public virtual DateTime LockoutEnd { get; set; }
    #endregion
}
```

# [XPO](#tab/tabid-csharp-xpo)
```csharp
using System.ComponentModel;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using DevExpress.Xpo;
// ...
public class Employee : Person, ISecurityUser,
    IAuthenticationStandardUser, IAuthenticationActiveDirectoryUser,
    IPermissionPolicyUser, ICanInitialize, ISecurityUserWithLoginInfo, ISecurityUserLockout {
    // ...
    #region ISecurityUserLockout Members
    private int accessFailedCount;
    private DateTime lockoutEnd;

    [Browsable(false)]
    public int AccessFailedCount {
        get { return accessFailedCount; }
        set { SetPropertyValue(nameof(AccessFailedCount), ref accessFailedCount, value); }
    }

    [Browsable(false)]
    public DateTime LockoutEnd {
        get { return lockoutEnd; }
        set { SetPropertyValue(nameof(LockoutEnd), ref lockoutEnd, value); }
    }
    #endregion
}
```
***

## Configure the Security System in Order to Utilize Custom User, Role, and Login Info Types

To use the custom `EmployeeRole`, custom `Employee` user, and custom `EmployeeLoginInfo` instead of the default types, modify the [SecurityStrategyComplex.RoleType](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.RoleType) and [SecurityStrategy.UserType](xref:DevExpress.ExpressApp.Security.SecurityStrategy.UserType) values, as shown below.

### In an ASP.NET Core Blazor application

**File**: _MyApplication.Blazor\Startup.cs_

# [C#](#tab/tabid-csharp1)

```csharp
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    options.RoleType = typeof(EmployeeRole);
                    options.UserType = typeof(Employee);
                    options.UserLoginInfoType = typeof(EmployeeLoginInfo);
                })           

            // ...
        })
        // ...
    }
}
```
***

### In WinForms Applications 

**File**: _MyApplication.Win\Startup.cs_

# [C#](#tab/tabid-csharp1)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    // ...
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ..
        builder.Security
            .UseIntegratedMode(options => {
                options.RoleType = typeof(EmployeeRole);
                options.UserType = typeof(Employee);
                options.UserLoginInfoType = typeof(EmployeeLoginInfo);
                // ...
            })
            // ..
    };
}
```
***

## Create an Administrative Account
If you decide to utilize Active Directory authentication, you can skip this section.  The minimum requirements for starting with Standard Authentication is an `Administrator` role and the `Administrator` user associated with this role. To add these objects, edit the _Updater.cs_ file located in the _DatabaseUpdate_ folder of your module project. Override the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method in the following manner.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security.Strategy;
// ...
public override void UpdateDatabaseAfterUpdateSchema() {
    base.UpdateDatabaseAfterUpdateSchema();
    EmployeeRole adminEmployeeRole = ObjectSpace.FirstOrDefault<EmployeeRole>(role => role.Name == SecurityStrategy.AdministratorRoleName);
    if (adminEmployeeRole == null) {
        adminEmployeeRole = ObjectSpace.CreateObject<EmployeeRole>();
        adminEmployeeRole.Name = SecurityStrategy.AdministratorRoleName;
        adminEmployeeRole.IsAdministrative = true;
    }
    Employee adminEmployee = ObjectSpace.FirstOrDefault<Employee>(employee => employee.UserName == "Administrator");
    if (adminEmployee == null) {
        adminEmployee = ObjectSpace.CreateObject<Employee>();
        adminEmployee.UserName = "Administrator";
        adminEmployee.SetPassword("");
        adminEmployee.EmployeeRoles.Add(adminEmployeeRole);
        ((ISecurityUserWithLoginInfo)adminEmployee).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(adminEmployee));
    }
    ObjectSpace.CommitChanges();
}
```

***

## Enable User Lockout (.NET 8+)

In the application builder code, set the [LockoutOptions.Enabled](xref:DevExpress.ExpressApp.Security.LockoutOptions.Enabled) property to `true`.

**File**: _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)
```csharp
//...
using DevExpress.ExpressApp.Security;

namespace YourApplicationName.Blazor.Server;

public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        
        services.AddXaf(Configuration, builder => {
            //...
            builder.Security
                .UseIntegratedMode(options => {
                    options.Lockout.Enabled = true;
                })
        });
    }
}
```
# [C# (WinForms)](#tab/tabid-csharp-winforms)
```csharp
//...
using DevExpress.ExpressApp.Security;

namespace YourApplicationName.Win;

public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        //...
        builder.Security
            .UseIntegratedMode(options => {
                options.Lockout.Enabled = true;
                //...
            })
        //...
    }
}
```
***

## Run the Application
You can now run the application to see the result. You will see that the Employee objects are utilized as a custom user type.

![EmployeeAsUserExample_Runtime](~/images/employeeasuserexample_runtime117152.png)

## Filter Tasks that Belong to the Current Employee
Apply the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute) attributes to the `EmployeeTask` class to define List View filters. To refer to the current Employee identifier, use the `CurrentUserId()` function.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
// ...
[ListViewFilter("All Tasks", "")]
[ListViewFilter("My Tasks", "[Owner.Id] = CurrentUserId()")]
public class EmployeeTask : Task {
    // ...
}
```

***

The image below shows the result.

![EmployeeAsUserExample_RuntimeFilters](~/images/employeeasuserexample_runtimefilters117153.png)
