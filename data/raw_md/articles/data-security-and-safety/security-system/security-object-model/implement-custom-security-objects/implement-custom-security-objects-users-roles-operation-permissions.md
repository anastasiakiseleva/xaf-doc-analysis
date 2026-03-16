---
uid: "113384"
seealso:
- linkId: "404264"
- linkId: "113472"
title: 'Implement Custom Security Objects (Users, Roles, Operation Permissions)'
owner: Eugeniy Burmistrov
---

# Implement Custom Security Objects (Users, Roles, Operation Permissions)

This example illustrates how to create custom security objects such as permissions, roles, and users. You can implement a permission an administrator uses to allow or deny users to export data in an XAF application. Each role exposes the `CanExport` property (a custom role object is implemented for this purpose). When the corresponding checkbox is checked, users associated with this role have access to the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) Action. 

[!example[How to: Implement Custom Permission, Role and User Objects](https://github.com/DevExpress-Examples/XAF-implement-custom-permission-role-and-user-objects)]

## Implement a Custom Role Object

Extend the [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole) class with an additional `CanExport` property. This property indicates that a role has the `ExportPermission`.
    
# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[DefaultClassOptions,ImageName("BO_Role")]
public class ExtendedSecurityRole : PermissionPolicyRole {
    public virtual bool CanExport { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// ...
[DefaultClassOptions, ImageName("BO_Role")]
public class ExtendedSecurityRole : PermissionPolicyRole {
    public ExtendedSecurityRole(Session session) : base(session) { }
    public bool CanExport {
        get { return GetPropertyValue<bool>(nameof(CanExport)); }
        set { SetPropertyValue<bool>(nameof(CanExport), value); }
    }
}
```

***

To use the custom `ExtendedSecurityRole` role instead of the default role, modify the [SecurityStrategyComplex.RoleType](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.RoleType) values, as shown below:

**File**: _SolutionName.Blazor.Server/Startup.cs_, _SolutionName.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.Security
                .UseIntegratedMode(options => {
                    options.RoleType = typeof(ExtendedSecurityRole);
                    // ...
                }
        }
    }
}

```

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                options.RoleType = typeof(ExtendedSecurityRole);
                // ...
            }
    }
}
```

***

## Customize the ApplicationUser Object

For users, the [Template Kit](xref:405447) automatically generates an `ApplicationUser` persistent class. This class extends the default [PermissionPolicyUser](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser) class with the [](xref:DevExpress.ExpressApp.Security.ISecurityUserWithLoginInfo) interface that is required to associate multiple authentication methods with a user. 

Although this is not required to replicate this example, you can customize the `ApplicationUser` class according to your needs. For example, add an `AppplicationUser.Tasks` collection property so that each user can be assigned a list of tasks:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
// ...
public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo
{
    // ...
    [DevExpress.ExpressApp.DC.Aggregated]
    public virtual IList<Task> Tasks { get; set; } = new ObservableCollection<Task>();
}

[DefaultClassOptions]
[ImageName("BO_Task")]
public class Task : BaseObject {
    public virtual string Subject { get; set; }
    public virtual DateTime DueDate { get; set; }
    public virtual ApplicationUser AssignedTo { get; set; }
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
// ...
public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo
{
    // ...
    [Association("Employee-Task")]
    public XPCollection<Task> Tasks {
        get { return GetCollection<Task>("Tasks"); }
    }
}

[DefaultClassOptions]
[ImageName("BO_Task")]
public class Task : BaseObject {
    public Task(Session session)
        : base(session) { }
    private string subject;
    public string Subject {
        get { return subject; }
        set { SetPropertyValue("Subject", ref subject, value); }
    }
    private DateTime dueDate;
    public DateTime DueDate {
        get { return dueDate; }
        set { SetPropertyValue("DueDate", ref dueDate, value); }
    }
    private ApplicationUser assignedTo;
    [Association("Employee-Task")]
    public ApplicationUser AssignedTo {
        get { return assignedTo; }
        set { SetPropertyValue("AssignedTo", ref assignedTo, value); }
    }
}

```

***

## Implement Custom Operation Permission and Permission Request

Add a class that supports the [](xref:DevExpress.ExpressApp.Security.IOperationPermission) interface to implement a custom operation permission.
    
**File**: _SolutionName.Module/Security/ExportPermission.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
// ...
public class ExportPermission : IOperationPermission {
    public string Operation { 
        get { return "Export"; }
    }
}
```
***

The Security System uses permission requests to determine whether permission is granted. To add a permission request for the `ExportPermission`, implement the [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) interface as follows:
    
**File**: _SolutionName.Module/Security/ExportPermissionRequest.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class ExportPermissionRequest : IPermissionRequest {
    public object GetHashObject() {
        return this.GetType().FullName;
    }
}
```
***

## Implement the Permission Request Processor and Register it in the Security Strategy

All permission requests should have a permission request processor registered in the Security Strategy. Inherit the [](xref:DevExpress.ExpressApp.Security.PermissionRequestProcessorBase`1) class and pass the permission request type as the ancestor class's generic parameter to implement a processor.

**File**: _SolutionName.Module/Security/ExportPermissionRequestProcessor.cs_    

# [C#](#tab/tabid-csharp)

```csharp
public class ExportPermissionRequestProcessor : 
    PermissionRequestProcessorBase<ExportPermissionRequest> {
    private IPermissionDictionary permissions;
    public ExportPermissionRequestProcessor(IPermissionDictionary permissions) {
        this.permissions = permissions;
    }
    public override bool IsGranted(ExportPermissionRequest permissionRequest) {
        return (permissions.FindFirst<ExportPermission>() != null);
    }
}
```
***

Handle the [SecurityStrategy.CustomizeRequestProcessors](xref:DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors) event in the _Startup.cs_ files in the ASP.NET Core Blazor and WinForms application projects to register the `ExportPermissionRequestProcessor`. Subscribe to this event before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called. 

In the event handler, pass the `ExportPermission` object to the `PermissionDictionary` as shown below.

> [!NOTE]
> You do not need to handle this event on the client side if your XAF application uses the [Middle Tier](xref:113439) application server. Instead, subscribe to this event in the server's _Startup.cs_ file. 

**File**: _SolutionName.Blazor.Server/Startup.cs_, _SolutionName.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-blazor)

```csharp
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    options.Events.OnSecurityStrategyCreated = securityStrategy => {
                        ((SecurityStrategy)securityStrategy).CustomizeRequestProcessors += delegate (object sender, CustomizeRequestProcessorsEventArgs e) {
                            List<IOperationPermission> result = new List<IOperationPermission>();
                            SecurityStrategyComplex security = sender as SecurityStrategyComplex;
                            if (security != null) {
                                ApplicationUser user = security.User as ApplicationUser;
                                if (user != null) {
                                    foreach (ExtendedSecurityRole role in user.Roles) {
                                        if (role.CanExport) {
                                            result.Add(new ExportPermission());
                                        }
                                    }
                                }
                            }
                            IPermissionDictionary permissionDictionary = new PermissionDictionary((IEnumerable<IOperationPermission>)result);
                            e.Processors.Add(typeof(ExportPermissionRequest), new ExportPermissionRequestProcessor(permissionDictionary));
                        };
                    };
                }
         }
    }
}
```

# [C# (WinForms)](#tab/tabid-winforms)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
                options.Events.OnSecurityStrategyCreated = securityStrategy => {
                    ((SecurityStrategy)securityStrategy).CustomizeRequestProcessors += delegate (object sender, CustomizeRequestProcessorsEventArgs e) {
                        List<IOperationPermission> result = new List<IOperationPermission>();
                        SecurityStrategyComplex security = sender as SecurityStrategyComplex;
                        if (security != null) {
                            ApplicationUser user = security.User as ApplicationUser;
                            if (user != null) {
                                foreach (ExtendedSecurityRole role in user.Roles) {
                                    if (role.CanExport) {
                                        result.Add(new ExportPermission());
                                    }
                                }
                            }
                        }
                        IPermissionDictionary permissionDictionary = new PermissionDictionary((IEnumerable<IOperationPermission>)result);
                        e.Processors.Add(typeof(ExportPermissionRequest), new ExportPermissionRequestProcessor(permissionDictionary));
                    };
                };
            }
    }
}
```

# [C# (Middle Tier Server)](#tab/tabid-middletier)

```csharp
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXafAspNetCoreSecurity(Configuration, options => {
            // ...
            boptions.Events.OnSecurityStrategyCreated = securityStrategy => {
                ((SecurityStrategy)securityStrategy).CustomizeRequestProcessors += delegate (object sender, CustomizeRequestProcessorsEventArgs e) {
                    List<IOperationPermission> result = new List<IOperationPermission>();
                    SecurityStrategyComplex security = sender as SecurityStrategyComplex;
                    if (security != null) {
                        ApplicationUser user = security.User as ApplicationUser;
                        if (user != null) {
                            foreach (ExtendedSecurityRole role in user.Roles) {
                                if (role.CanExport) {
                                    result.Add(new ExportPermission());
                                }
                            }
                        }
                    }
                    IPermissionDictionary permissionDictionary = new PermissionDictionary((IEnumerable<IOperationPermission>)result);
                    e.Processors.Add(typeof(ExportPermissionRequest), new ExportPermissionRequestProcessor(permissionDictionary));
                };
            };
        }
}

```

***

## Apply the Custom Permission to the ExportController Controller

Add the following View Controller to inform the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) controller about the `ExportPermission`:

**File**: _SolutionName.Module/Security/SecuredExportController.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class SecuredExportController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        ExportController controller = Frame.GetController<ExportController>();
        if (controller != null) {
            controller.ExportAction.Executing += ExportAction_Executing;
            IRequestSecurity requestSecurity = (IRequestSecurity)Application.Security;
            controller.Active.SetItemValue("Security",
                requestSecurity.IsGranted(new ExportPermissionRequest()));
        }
    }
    void ExportAction_Executing(object sender, System.ComponentModel.CancelEventArgs e) {
        IRequestSecurity requestSecurity = (IRequestSecurity)Application.Security;
        if (!requestSecurity.IsGranted(new ExportPermissionRequest())) {
            throw new UserFriendlyException("Export operation is prohibited.");
        }
    }
}
```
***

The code above deactivates the controller for users who are not allowed to export data. The [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) event handler demonstrates how to throw an exception when a user attempts to perform a prohibited operation.

## Add Demo Data

Add the predefined user and role objects in the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method as shown below.

**File**: _SolutionName.Module/DatabaseUpdate/Updater.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    public Updater(IObjectSpace objectSpace, Version currentDBVersion) :
        base(objectSpace, currentDBVersion) {
    }
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
#if !RELEASE
        ExtendedSecurityRole defaultRole = CreateDefaultRole();
        ExtendedSecurityRole exportRole = CreateExporterRole();
        ApplicationUser sampleUser = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "User");
        if (sampleUser == null) {
            sampleUser = ObjectSpace.CreateObject<ApplicationUser>();
            sampleUser.UserName = "User";
            sampleUser.SetPassword("");
            ObjectSpace.CommitChanges();
            ((ISecurityUserWithLoginInfo)sampleUser).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(sampleUser));
            sampleUser.Roles.Add(defaultRole);
        }
        ApplicationUser exportUser = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "exportUser");
        if (exportUser == null) {
            exportUser = ObjectSpace.CreateObject<ApplicationUser>();
            exportUser.UserName = "exportUser";
            exportUser.SetPassword("");
            ObjectSpace.CommitChanges();
            ((ISecurityUserWithLoginInfo)exportUser).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(exportUser));
            exportUser.Roles.Add(defaultRole);
            exportUser.Roles.Add(exportRole);
        }

        ApplicationUser userAdmin = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "Admin");
        if (userAdmin == null) {
            userAdmin = ObjectSpace.CreateObject<ApplicationUser>();
            userAdmin.UserName = "Admin";
            userAdmin.SetPassword("");
            ObjectSpace.CommitChanges(); 
            ((ISecurityUserWithLoginInfo)userAdmin).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(userAdmin));
        }
        ExtendedSecurityRole adminRole = ObjectSpace.FirstOrDefault<ExtendedSecurityRole>(r => r.Name == "Administrators");
        if (adminRole == null) {
            adminRole = ObjectSpace.CreateObject<ExtendedSecurityRole>();
            adminRole.Name = "Administrators";
        }
        adminRole.IsAdministrative = true;
        userAdmin.Roles.Add(adminRole);


        var cnt = ObjectSpace.GetObjects<Contact>().Count;
        if (cnt > 0) {
            return;
        }
        for (int i = 0; i < 5; i++) {
            string contactName = "FirstName" + i;
            var contact = ObjectSpace.CreateObject<Contact>();
            contact.FirstName = contactName;
            contact.LastName = "LastName" + i;
            contact.Age = i * 10;

        }

        ObjectSpace.CommitChanges(); 
#endif
    }
    public override void UpdateDatabaseBeforeUpdateSchema() {
        base.UpdateDatabaseBeforeUpdateSchema();
    }
    private ExtendedSecurityRole CreateDefaultRole() {
        ExtendedSecurityRole defaultRole = ObjectSpace.FirstOrDefault<ExtendedSecurityRole>(role => role.Name == "Default");
        if (defaultRole == null) {
            defaultRole = ObjectSpace.CreateObject<ExtendedSecurityRole>();
            defaultRole.Name = "Default";

            defaultRole.AddObjectPermissionFromLambda<ApplicationUser>(SecurityOperations.Read, cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
            defaultRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/MyDetails", SecurityPermissionState.Allow);
            defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "ChangePasswordOnFirstLogon", cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
            defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "StoredPassword", cm => cm.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
            defaultRole.AddTypePermissionsRecursively<ExtendedSecurityRole>(SecurityOperations.Read, SecurityPermissionState.Deny);
            defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow);
            defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow);
            defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.Create, SecurityPermissionState.Allow);
            defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.Create, SecurityPermissionState.Allow);

            defaultRole.AddTypePermission<Contact>(SecurityOperations.CRUDAccess, SecurityPermissionState.Allow);
            defaultRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/Contact_ListView", SecurityPermissionState.Allow);

        }
        return defaultRole;
    }
    private ExtendedSecurityRole CreateExporterRole() {
        ExtendedSecurityRole exporterRole = ObjectSpace.FirstOrDefault<ExtendedSecurityRole>(role => role.Name == "Exporter");
        if (exporterRole == null) {
            exporterRole = ObjectSpace.CreateObject<ExtendedSecurityRole>();
            exporterRole.Name = "Exporter";
            exporterRole.CanExport = true;
            exporterRole.AddTypePermission<Contact>(SecurityOperations.CRUDAccess, SecurityPermissionState.Allow);
            exporterRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/Contact_ListView", SecurityPermissionState.Allow);
        }
        return exporterRole;
    }
}

```
***

## Ensure that the Application UI Changes Based on the Role

Run the application and log in as "Admin". Open the extended security role object's detail view. The **Can Export** checkbox is checked for the "Exporter" role.

![|custompermission_canexport117041](~/images/custompermission_canexport117041.png)

Log in again as "exportUser" who has the "Exporter" role. Ensure that the **Export** action is available for this user. If you log in as "User", the **Export** action is unavailable.

![custompermission_exportaction117042](~/images/custompermission_exportaction117042.png)

> [!NOTE]
> The **Export** action is available for the "Admin" user even though the "Can Export" option is not checked for the "Administrator" role. The "Is Administrative" option overrides all other permissions (built-in and custom) and grants full access to all operations.
