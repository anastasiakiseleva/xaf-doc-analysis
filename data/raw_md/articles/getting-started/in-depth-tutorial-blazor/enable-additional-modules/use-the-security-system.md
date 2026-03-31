---
uid: "404204"
title: Use the Security System
---
# Use the Security System

This article explains how to implement the Security System in your application. The system applies the [](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex) security strategy. According to this strategy, application users have roles with different permission sets. For more information about permissions, see the following topic: [](xref:113366).

The instructions below describe how to do the following:

- Enable the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication type.
- Create an administrator user and a common user in code.
- Create a user and a role at runtime.

The administrator has a full-access permission set. The user has a limited permission set. The administrator can create **User** objects and **Role** objects, specify **Permissions** for them, and then assign **Roles** to **Users** at runtime.

With [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication type, the Security System uses the internal XAF authentication mechanism and stores user credentials in the application's database. Users need to input their name and password in the login form before application startup.

> [!NOTE]
> Before you proceed, take a moment to review this lesson:
> 
> * [Supply Initial Data](xref:402985)

## Implement Standard Authentication in Code

1. In the _MySolution.Module\BusinessObjects_ folder, create the `ApplicationUser` class. Replace the generated class declaration with the following code:

   ```csharp
   using System.Collections.ObjectModel;
   using System.ComponentModel;
   using DevExpress.ExpressApp;
   using DevExpress.ExpressApp.Security;
   using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;

   namespace MySolution.Module.BusinessObjects;

   [DefaultProperty(nameof(UserName))]
   public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo {
       public ApplicationUser() : base() {
           UserLogins = new ObservableCollection<ApplicationUserLoginInfo>();
       }

       [Browsable(false)]
       [DevExpress.ExpressApp.DC.Aggregated]
       public virtual IList<ApplicationUserLoginInfo> UserLogins { get; set; }

       IEnumerable<ISecurityUserLoginInfo> IOAuthSecurityUser.UserLogins => UserLogins.OfType<ISecurityUserLoginInfo>();

       ISecurityUserLoginInfo ISecurityUserWithLoginInfo.CreateUserLoginInfo(string loginProviderName, string providerUserKey) {
           ApplicationUserLoginInfo result = ((IObjectSpaceLink)this).ObjectSpace.CreateObject<ApplicationUserLoginInfo>();
           result.LoginProviderName = loginProviderName;
           result.ProviderUserKey = providerUserKey;
           result.User = this;
           return result;
       }
   }
   ```
   [`PermissionPolicyUser`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser

   You inherit this class from the [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser) class that defines an XAF user with a list of associated security roles.

2. In the same manner, create the `ApplicationUserLoginInfo` class. 

   ```csharp
   using DevExpress.ExpressApp.ConditionalAppearance;
   using DevExpress.ExpressApp.Security;
   using System.ComponentModel;
   using System.ComponentModel.DataAnnotations;
   using System.ComponentModel.DataAnnotations.Schema;

   namespace MySolution.Module.BusinessObjects;

   [Table("PermissionPolicyUserLoginInfo")]
   public class ApplicationUserLoginInfo : ISecurityUserLoginInfo {

       public ApplicationUserLoginInfo() { }

       [Browsable(false)]
       public virtual Guid ID { get; protected set; }

       [Appearance("PasswordProvider", Enabled = false, Criteria = 
	   "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
       public virtual string LoginProviderName { get; set; }

       [Appearance("PasswordProviderUserKey", Enabled = false, Criteria = 
	   "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
       public virtual string ProviderUserKey { get; set; }

       [Browsable(false)]
       public virtual Guid UserForeignKey { get; set; }

       [Required]
       [ForeignKey(nameof(UserForeignKey))]
       public virtual ApplicationUser User { get; set; }

       object ISecurityUserLoginInfo.User => User;
   }

   ```

3. Go to the _MySolution.Module\MySolutionDbContext_ file and add the following  properties to `DbSet`:

    ```csharp
    public class MySolutionEFCoreDbContext : DbContext {
        //...
        public DbSet<ApplicationUser> Users { get; set; }
        public DbSet<ApplicationUserLoginInfo> UserLoginInfos { get; set; }
        public DbSet<ModelDifference> ModelDifferences { get; set; }
        public DbSet<ModelDifferenceAspect> ModelDifferenceAspects { get; set; }
    }
    ```

    Note that the Security System requires that model differences be [stored in the database](xref:113698).

4. Enable Standard Authentication in the platform-specific _Startup_ files:

   # [C# (ASP.NET Core Blazor)](#tab/tabid-csharp-blazor)
 
   ```csharp{2-3,12-14,16-23,25-28,34-35}
   // ...
   using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
   using MySolution.Module.BusinessObjects;
   
   public class Startup {
   // ...
       public void ConfigureServices(IServiceCollection services) {
           // ...
           services.AddXaf(Configuration, builder => {
                // ...
                builder.ObjectSpaceProviders
                    .AddSecuredEFCore().WithDbContext<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext>((serviceProvider, options) => {
                        // ...
                    })
                    .AddNonPersistent();
                builder.Security
                    .UseIntegratedMode(options => {
                        options.RoleType = typeof(PermissionPolicyRole);
                        options.UserType = typeof(ApplicationUser);
                        options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
                        options.SupportNavigationPermissionsForTypes = false;
                    })
                .AddPasswordAuthentication(options => options.IsSupportChangePassword = true);
           });
           services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
               .AddCookie(options => {
                   options.LoginPath = "/LoginPage";
			   });
       }
	   public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
           //...
           app.UseRequestLocalization();
           //..
           app.UseAuthentication();
           app.UseAuthorization();
		   //...
       }
   }
   ```

   # [C# (Windows Forms)](#tab/tabid-csharp-xpo)

   ```csharp{2-3,10-12,14-21}
   // ...
   using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
   using MySolution.Module.BusinessObjects;
   
   public class ApplicationBuilder : IDesignTimeApplicationFactory {
       public static WinApplication BuildApplication(string connectionString) {
       var builder = WinApplication.CreateBuilder();
       builder.UseApplication<MySolutionWindowsFormsApplication>();
       builder.ObjectSpaceProviders
            .AddSecuredEFCore().WithDbContext<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext>((application, options) => {
                // ...
            })
            // ...
        builder.Security
            .UseIntegratedMode(options => {
                options.RoleType = typeof(PermissionPolicyRole);
                options.UserType = typeof(ApplicationUser);
                options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
                options.SupportNavigationPermissionsForTypes = false;
            })
        .UsePasswordAuthentication();				
        //...
       }
   }
   ```

   ***

5. Expand the _MySolution.Module_ project in the Solution Explorer and go to the _DatabaseUpdate_ folder. Open the _Updater.cs_ file and create the **Administrator** user in the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method.

    ```csharp{3-4,11-35}
    //...
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using MySolution.Module.BusinessObjects;

    public class Updater : DevExpress.ExpressApp.Updating.ModuleUpdater {
        //...
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();
            //...
        	ApplicationUser userAdmin = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "Admin");
        	if (userAdmin == null) {
            	userAdmin = ObjectSpace.CreateObject<ApplicationUser>();
            	userAdmin.UserName = "Admin";
            	// Set a password if the standard authentication type is used
            	userAdmin.SetPassword("");

            	/* The UserLoginInfo object requires a user object Id (Oid).
            	   Commit the user object to the database before you create a UserLoginInfo object.
                   This will correctly initialize the user key property. */

            	ObjectSpace.CommitChanges(); //This line persists created object(s).
            	((ISecurityUserWithLoginInfo)userAdmin).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, 
				ObjectSpace.GetKeyValueAsString(userAdmin));
        	}
        	// If a role with the Administrators name doesn't exist in the database, create this role.
        	PermissionPolicyRole adminRole = 
			ObjectSpace.FirstOrDefault<PermissionPolicyRole>(r => r.Name == "Administrators");
        	if (adminRole == null) {
            	adminRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
            	adminRole.Name = "Administrators";
        	}
			//Set the user's role to Administrative. This role has access to objects of all types.
        	adminRole.IsAdministrative = true;
        	userAdmin.Roles.Add(adminRole);

        	ObjectSpace.CommitChanges(); //Uncomment this line to persist created object(s).
        }
    }
    ```
	[`IsAdministrative`]: xref:DevExpress.Persistent.Base.IPermissionPolicyRole.IsAdministrative

6. In the same manner, create a common user.

    ```csharp{11-28}
    //...
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using MySolution.Module.BusinessObjects;

    public class Updater : DevExpress.ExpressApp.Updating.ModuleUpdater {
        //...
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();
            //...
			ApplicationUser commonUser = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "User");
        	if (commonUser == null) {
            	commonUser = ObjectSpace.CreateObject<ApplicationUser>();
            	commonUser.UserName = "User";
            	// Set a password if the standard authentication type is used
            	commonUser.SetPassword("");

            	/* The UserLoginInfo object requires a user object Id (Oid).
            	   Commit the user object to the database before you create a UserLoginInfo object.
				   This will correctly initialize the user key property.*/

            	ObjectSpace.CommitChanges(); //This line persists created object(s).

            	((ISecurityUserWithLoginInfo)commonUser).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, 
				ObjectSpace.GetKeyValueAsString(commonUser));
        	}
        	PermissionPolicyRole defaultRole = CreateDefaultRole();
        	commonUser.Roles.Add(defaultRole);
        }
    }
    ```   

7. Create a common user role and specify its permissions. This user only has access to the current user object.

   ```csharp{2,11-40}
    using MySolution.Module.BusinessObjects;
    using DevExpress.ExpressApp.SystemModule;
    //...

    public class Updater : DevExpress.ExpressApp.Updating.ModuleUpdater {
        //...
        public override void UpdateDatabaseAfterUpdateSchema() {
			base.UpdateDatabaseBeforeUpdateSchema();
		}

       private PermissionPolicyRole CreateDefaultRole() {
           PermissionPolicyRole defaultRole = 
		   ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
           if (defaultRole == null) {
               defaultRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
               defaultRole.Name = "Default";

               defaultRole.AddObjectPermissionFromLambda<ApplicationUser>(SecurityOperations.Read, 
			   cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
               defaultRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/MyDetails", 
			   SecurityPermissionState.Allow);
               defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, 
			   "ChangePasswordOnFirstLogon", cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), 
			   SecurityPermissionState.Allow);
               defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, 
			   "StoredPassword", cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), 
			   SecurityPermissionState.Allow);
               defaultRole.AddTypePermissionsRecursively<PermissionPolicyRole>(SecurityOperations.Read, 
			   SecurityPermissionState.Deny);
               defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.ReadWriteAccess, 
			   SecurityPermissionState.Allow);
               defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.ReadWriteAccess, 
			   SecurityPermissionState.Allow);
               defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.Create, 
			   SecurityPermissionState.Allow);
               defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.Create, 
			   SecurityPermissionState.Allow);
           }
           return defaultRole;
       }
	}
   ```

   > [!NOTE]
   > You can find more examples in the following topic: [](xref:113366).

8. Optionally, you can configure your application to store [user differences](xref:112580#application-model-layers) (individual user settings) in the database. Make the following changes in the _MySolution.Blazor.Server\\BlazorModule.cs_ (ASP.NET Core Blazor) and _MySolution.Win\\WinModule.cs_ (Windows Forms) files: 

    # [ASP.NET Core Blazor](#tab/tabid-blazor)

    ```cs{9,11-14}
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.BaseImpl;
    // ...

    public sealed class MySolutionBlazorModule : ModuleBase {
        // ...
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CreateCustomUserModelDifferenceStore += Application_CreateCustomUserModelDifferenceStore;
        }
        private void Application_CreateCustomUserModelDifferenceStore(object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), false, "Blazor");
            e.Handled = true;
        }
    }
    ```

    # [Windows Forms](#tab/tabid-winforms)

    ```cs{9,11-14}
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.BaseImpl;
    // ...

    public sealed class MySolutionWinModule : ModuleBase {
        // ...
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CreateCustomUserModelDifferenceStore += Application_CreateCustomUserModelDifferenceStore;
        }
        private void Application_CreateCustomUserModelDifferenceStore(object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), false, "Win");
            e.Handled = true;
        }
    }
    ```

    ***

    This way you can persist Detail View Layout changes made by individual users among other things. See the following help topic for more details: [Persist Layout Customization For Individual Users](xref:404353#persist-layout-customization-for-individual-users).

9. Run the application. Log in under _Admin_. Leave the password field empty (you did not specify the password when you created this user). When you click the **Log In** button, the user's credentials are authenticated and the application runs.

10. Select the **My Details** item in the navigation control and see the Detail View.

   ASP.NET Core Blazor
   
   :   ![|ASP.NET Core Blazor My Details|](~/images/tutorial-my-details-blazor.png)

   Windows Forms

   :   ![|Windows Forms My Details|](~/images/tutorial-my-details-winforms.png)

## Create a Role in the UI

Administrators and other users with **Role creation** permission can create roles at runtime.

1. Select the **Role** item in the navigation control and click the **New** button. In the invoked Detail View, set the name and permissions for the new role.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor New Role|](~/images/tutorial-create-role-blazor.png)

   Windows Forms

   :   ![Windows Forms New Role](~/images/tutorial-create-role-winforms.png)

   With the `Permission Policy` property, you can assign the following permission policies:

   * Deny all by default
   * Read only all by default
   * Allow all by default
   
   For each operation, you can explicitly specify the `Allow` or `Deny` modifier, or leave it blank. If you don't specify the modifier, the permission follows the role's permission policy.

## Create a User in the UI

Administrators and other users with **User creation** permission can create users at runtime.

1. Select the **Application User** item in the navigation control and click the **New** button. In the invoked Detail View, specify the **User Name** and assign one or more roles.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor New User|](~/images/tutorial-create-user-blazor.png)

   Windows Forms

   :   ![Windows Forms New User](~/images/tutorial-create-user-winforms.png)

   > [!TIP]
   > Deselect the **Is Active** checkbox if you need to deny user access to the application.