---
uid: "404875"
title: Implement a Security System User (ApplicationUser) Based on XAF Business Classes
seealso:
- linkId: "113452"
---

# Implement a Security System User (ApplicationUser) Based on XAF Business Classes

XAF has a built-in `PermissionPolicyUser` class for XPO and EF Core-based applications. This class implements basic functionality required to store Security System user data. The major limitation of the `PermissionPolicyUser` class is that it can be used directly only in applications with a single authentication method: either password-based or Windows Active Directory-based.

When a user has multiple ways to log in, you need to store information for all authentication types and associate this information with the user. To do this, use the @DevExpress.ExpressApp.Security.ISecurityUserWithLoginInfo (a descendant of @DevExpress.ExpressApp.Security.ISecurityUser and `IOAuthSecurityUser`) and @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo interfaces.

Additionally, if you want to support the user lockout feature (the capability to lock out users who fail to enter the correct password several times in a row), implement the @DevExpress.ExpressApp.Security.ISecurityUserLockout interface in your security system user class.

> [!NOTE]
> The [Template Kit](xref:405447) generates classes that implement these interfaces automatically. You can find these implementations in the following files within your solution:
> * _SolutionName.Module\BusinessObjects\ApplicationUser.cs_
> * _SolutionName.Module\BusinessObjects\ApplicationUserLoginInfo.cs_

Follow the steps below to implement the required classes from scratch.

1. Add a class to store user login information. In this class, implement the @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo interface. You can use the following code as a reference implementation (the [Template Kit](xref:405447) generates equivalent code).

    # [C# (EF Core)](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.ExpressApp.ConditionalAppearance;
    using DevExpress.ExpressApp.Security;
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    // ...
    [Table("PermissionPolicyUserLoginInfo")]
    public class ApplicationUserLoginInfo : ISecurityUserLoginInfo {

        public ApplicationUserLoginInfo() { }

        [Browsable(false)]
        public virtual Guid ID { get; protected set; }

        [Appearance("PasswordProvider", 
            Enabled = false, 
            Criteria = "!(IsNewObject(this)) and LoginProviderName == '" 
                + SecurityDefaults.PasswordAuthentication 
                + "'", 
            Context = "DetailView")]
        public virtual string LoginProviderName { get; set; }

        [Appearance("PasswordProviderUserKey", 
            Enabled = false, 
            Criteria = "!(IsNewObject(this)) and LoginProviderName == '" 
                + SecurityDefaults.PasswordAuthentication 
                + "'", 
            Context = "DetailView")]
        public virtual string ProviderUserKey { get; set; }

        [Browsable(false)]
        public virtual Guid UserForeignKey { get; set; }

        [Required]
        [ForeignKey(nameof(UserForeignKey))]
        public virtual ApplicationUser User { get; set; }

        object ISecurityUserLoginInfo.User => User;
    }
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.ExpressApp.ConditionalAppearance;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Xpo;
    // ...
    [DeferredDeletion(false)]
    [Persistent("PermissionPolicyUserLoginInfo")]
    public class ApplicationUserLoginInfo : BaseObject, ISecurityUserLoginInfo {
        private string loginProviderName;
        private ApplicationUser user;
        private string providerUserKey;
        public ApplicationUserLoginInfo(Session session) : base(session) { }

        [Indexed("ProviderUserKey", Unique = true)]
        [Appearance("PasswordProvider", Enabled = false, 
            Criteria = "!(IsNewObject(this)) and LoginProviderName == '" 
                + SecurityDefaults.PasswordAuthentication 
                + "'", 
            Context = "DetailView")]
        public string LoginProviderName {
            get { return loginProviderName; }
            set { SetPropertyValue(nameof(LoginProviderName), ref loginProviderName, value); }
        }

        [Appearance("PasswordProviderUserKey", Enabled = false, 
            Criteria = "!(IsNewObject(this)) and LoginProviderName == '" 
                + SecurityDefaults.PasswordAuthentication 
                + "'", 
            Context = "DetailView")]
        public string ProviderUserKey {
            get { return providerUserKey; }
            set { SetPropertyValue(nameof(ProviderUserKey), ref providerUserKey, value); }
        }

        [Association("User-LoginInfo")]
        public ApplicationUser User {
            get { return user; }
            set { SetPropertyValue(nameof(User), ref user, value); }
        }

        object ISecurityUserLoginInfo.User => User;
    }

    ```

    ***

2. Add an application user class that extends `PermissionPolicyUser` and implements the `ISecurityUserWithLoginInfo` interface required to associate multiple authentication methods with a user and the `ISecurityUserLockout` interface to support the user lockout feature. You can use the following code as a reference implementation ([Template Kit](xref:405447) generates equivalent code).

    # [C# (EF Core)](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using System.Collections.ObjectModel;
    using System.ComponentModel;
    // ...
    [DefaultProperty(nameof(UserName))]
    public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo, ISecurityUserLockout {
        [Browsable(false)]
        public virtual int AccessFailedCount { get; set; }

        [Browsable(false)]
        public virtual DateTime LockoutEnd { get; set; }

        [Browsable(false)]
        [DevExpress.ExpressApp.DC.Aggregated]
        public virtual IList<ApplicationUserLoginInfo> UserLogins { get; set; } 
            = new ObservableCollection<ApplicationUserLoginInfo>();

        IEnumerable<ISecurityUserLoginInfo> IOAuthSecurityUser.UserLogins 
            => UserLogins.OfType<ISecurityUserLoginInfo>();

        ISecurityUserLoginInfo ISecurityUserWithLoginInfo.CreateUserLoginInfo(string loginProviderName, string providerUserKey) {
            ApplicationUserLoginInfo result = ((IObjectSpaceLink)this).ObjectSpace.CreateObject<ApplicationUserLoginInfo>();
            result.LoginProviderName = loginProviderName;
            result.ProviderUserKey = providerUserKey;
            result.User = this;
            return result;
        }
    }
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.PermissionPolicy;
    using DevExpress.Xpo;
    using System.ComponentModel;
    // ...
    [MapInheritance(MapInheritanceType.ParentTable)]
    [DefaultProperty(nameof(UserName))]
    public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo, ISecurityUserLockout {
        private int accessFailedCount;
        private DateTime lockoutEnd;

        public ApplicationUser(Session session) : base(session) { }

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

        [Browsable(false)]
        [Aggregated, Association("User-LoginInfo")]
        public XPCollection<ApplicationUserLoginInfo> LoginInfo {
            get { return GetCollection<ApplicationUserLoginInfo>(nameof(LoginInfo)); }
        }

        IEnumerable<ISecurityUserLoginInfo> IOAuthSecurityUser.UserLogins 
            => LoginInfo.OfType<ISecurityUserLoginInfo>();

        ISecurityUserLoginInfo ISecurityUserWithLoginInfo.CreateUserLoginInfo(string loginProviderName, string providerUserKey) {
            ApplicationUserLoginInfo result = new ApplicationUserLoginInfo(Session);
            result.LoginProviderName = loginProviderName;
            result.ProviderUserKey = providerUserKey;
            result.User = this;
            return result;
        }
    }
    ```

    ***

3. Modify the Application Builder code as shown below so that XAF uses your custom classes to store security data:

    **File**: _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, MySolution.WebApi\Startup.cs

    # [C#](#tab/tabid-csharp)

    ```csharp{5-6}
    // ...
    builder.Security
        .UseIntegratedMode(options => {
            // ...
            options.UserType = typeof(MySolution.Module.BusinessObjects.ApplicationUser);
            options.UserLoginInfoType = typeof(MySolution.Module.BusinessObjects.ApplicationUserLoginInfo);
    // ...
    ```

    ***