---
uid: DevExpress.ExpressApp.Security.ISecurityUserLockout
name: ISecurityUserLockout
type: Interface
summary: Returns and stores information about user lockout.
syntax:
  content: public interface ISecurityUserLockout
seealso:
- linkId: DevExpress.ExpressApp.Security.ISecurityUserLockout._members
  altText: ISecurityUserLockout Members
---

User lockout is a technique that improves application security. The application locks out a user who fails to enter the correct password several times in a row. Such lockouts protect you against brute force attacks where an attacker repeatedly tries to guess the password.

The [Template Kit](xref:405447) generates the `ApplicationUser` class that implements this interface automatically.

To support user lockout in existing applications, implement the `ISecurityUserLockout` interface in the Application User class as demonstrated in the following example:

1. Implement the `ISecurityUserLockout` interface in the Application User class as demonstrated in the following example:

    # [EF Core](#tab/tabid-csharp-efcore)
    ```csharp
    using System.Collections.ObjectModel;
    using System.ComponentModel;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;

    namespace YourApplicationName.Module.BusinessObjects;

    public class ApplicationUser : PermissionPolicyUser, ISecurityUserLockout {

        [Browsable(false)]
        public virtual int AccessFailedCount { get; set; }
        
        [Browsable(false)]
        public virtual DateTime LockoutEnd { get; set; }
        //
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

    namespace YourApplicationName.Module.BusinessObjects;

    public class ApplicationUser : PermissionPolicyUser, ISecurityUserLockout {
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
    }
    ```
    ***

2. In _YourApplicationName.Blazor.Server\Startup.cs_ file (ASP.NET Core Blazor) or _YourApplicationName.Win\Startup.cs_ file (Windows Forms), set the [LockoutOptions.Enabled](xref:DevExpress.ExpressApp.Security.LockoutOptions.Enabled) property to `true`:

    # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
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
    # [Windows Forms](#tab/tabid-csharp-winforms)
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
