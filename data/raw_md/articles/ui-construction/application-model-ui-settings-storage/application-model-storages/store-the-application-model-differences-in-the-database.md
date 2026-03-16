---
uid: "113698"
seealso: []
title: 'Store Application Model Differences in the Database'
owner: Anastasiya Kisialeva
---
# Store Application Model Differences in the Database

When you create a new application with the Security System enabled in the [Template Kit](xref:405447), XAF stores user settings (model differences) [in the database](xref:403527) with the help of the `ModelDifferenceDbStore` storage (the default setting). This topic describes how to enable this feature in an existing application and how to store shared model differences (administrator settings) in the database.

> [!NOTE]
> When the Security System is disabled, XAF passes the `System.Security.Principal.WindowsIdentity.GetCurrent().Name` value the [IModelDifference.UserId](xref:DevExpress.ExpressApp.IModelDifference.UserId) property to use as user identifier. You can use the technique described in this article to enable `ModelDifferenceDbStore` in unsecured Windows Forms applications. XAF supports shared model differences for ASP.NET Core Blazor and Windows Forms when the Security System is disabled.

1. Depending on the platform, navigate to one for the following files:

    * _YourApplicationName.Win\WinModule.cs_ file located in your Windows Forms module or application project.
    * _YourApplicationName.Blazor.Server\BlazorModule.cs_ file located in the ASP.NET Core Blazor module or application project
2. In the overridden [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method, subscribe to the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) and [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) events.
3. In these event handlers, pass the `ModelDifferenceDbStore` instance to the `e.Store` parameter. Pass the `ModelDifference` type to the `ModelDifferenceDbStore` constructor. Here, `ModelDifference` is a built-in persistent object from the [](xref:DevExpress.Persistent.BaseImpl) namespace (for XPO) or from the [](xref:DevExpress.Persistent.BaseImpl.EF) namespace (for Entity Framework Core) that implements the [](xref:DevExpress.ExpressApp.IModelDifference) interface.
4. Set the last parameter of the `ModelDifferenceDbStore` constructor (used to initialize the [IModelDifference.ContextId](xref:DevExpress.ExpressApp.IModelDifference.ContextId) property) to `"Blazor"` (ASP.NET Core Blazor) or `"Win"` (Windows Forms). This is necessary to distinguish between model differences created for the same user on different platforms.

    # [ASP.NET Core Blazor](#tab/tabid-blazor)

    ```csharp
    public sealed partial class MySolutionBlazorModule : ModuleBase {
        private void Application_CreateCustomModelDifferenceStore(Object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), true, "Blazor");
            e.Handled = true;
        }
        private void Application_CreateCustomUserModelDifferenceStore(Object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), false, "Blazor");
            e.Handled = true;
        }

        // ...
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CreateCustomModelDifferenceStore += Application_CreateCustomModelDifferenceStore;
            application.CreateCustomUserModelDifferenceStore += Application_CreateCustomUserModelDifferenceStore;
        }
    }
    ```

    # [Windows Forms](#tab/tabid-winforms)

    ```csharp
    public sealed partial class MySolutionWindowsFormsModule : ModuleBase {
        private void Application_CreateCustomModelDifferenceStore(Object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), true, "Win");
            e.Handled = true;
        }
        private void Application_CreateCustomUserModelDifferenceStore(Object sender, CreateCustomModelDifferenceStoreEventArgs e) {
            e.Store = new ModelDifferenceDbStore((XafApplication)sender, typeof(ModelDifference), false, "Win");
            e.Handled = true;
        }
        //...
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CreateCustomModelDifferenceStore += Application_CreateCustomModelDifferenceStore;
            application.CreateCustomUserModelDifferenceStore += Application_CreateCustomUserModelDifferenceStore;
        }
    }
    ```

    ***

    > [!NOTE]
    > When the `CreateCustomModelDifferenceStore` event is handled, the shared model differences (administrator settings) are stored in the database. XAF ignores changes in the _Model.xafml_ file in the application project if the database record already exists for the shared model differences. To reload settings from _Model.xafml_, enable the administrative UI and use the **Import Shared Model Difference** Action (or delete the "Shared Model Difference" record and restart). If this behavior is inappropriate, do not handle this event. Handle it in the RELEASE project configuration only.

4. Navigate to the _YourSolutionName.Module\Module.cs_ file and add the following code to the Module constructor:

    ```csharp
    using DevExpress.Persistent.BaseImpl;
    // ...
    namespace SimpleProjectManager.Module {
        public sealed partial class SimpleProjectManagerModule : ModuleBase {
            public SimpleProjectManagerModule() {
                // ...
                AdditionalExportedTypes.Add(typeof(ModelDifference));
                AdditionalExportedTypes.Add(typeof(ModelDifferenceAspect));
            }
        }
    }
    ```

5. If you use Entity Framework Core, additionally register [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference) and [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifferenceAspect) classes in  `DbContext`.

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    public class MyDbContext : DbContext {
        // ...
        public DbSet<ModelDifference> ModelDifferences { get; set; }
        public DbSet<ModelDifferenceAspect> ModelDifferenceAspects { get; set; }
    }
    ```

6. In the _MySolution.Module\DatabaseUpdate\Updater.cs_ file, check that all users have read/write access to `ModelDifference` and `ModelDifferenceAspect` types.

    ```csharp
    public class Updater : ModuleUpdater {
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();

            PermissionPolicyRole defaultRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
            if(defaultRole == null) {
                defaultRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
                defaultRole.Name = "Default";
                defaultRole.AddObjectPermissionFromLambda<ApplicationUser>(SecurityOperations.Read, u => u.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
                defaultRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/MyDetails", SecurityPermissionState.Allow);
                defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "ChangePasswordOnFirstLogon", u => u.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
                defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "StoredPassword", u => u.ID == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
                defaultRole.AddTypePermissionsRecursively<PermissionPolicyRole>(SecurityOperations.Read, SecurityPermissionState.Deny);
                defaultRole.AddObjectPermission<ModelDifference>(SecurityOperations.ReadWriteAccess, "UserId = ToStr(CurrentUserId())", SecurityPermissionState.Allow);
                defaultRole.AddObjectPermission<ModelDifferenceAspect>(SecurityOperations.ReadWriteAccess, "Owner.UserId = ToStr(CurrentUserId())", SecurityPermissionState.Allow);
                // The 'Create' permission is additionally required if you use the Middle Tier Application Server
                defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.Create, SecurityPermissionState.Allow);
                defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.Create, SecurityPermissionState.Allow);                
            }
            sampleUser.Roles.Add(defaultRole);
            // ...
            ObjectSpace.CommitChanges();
        }
        // ...
    }
    ```

> [!TIP]
> For information on how you can enable UI elements to manage Model Differences stored in the database, refer to the following article - [How to: Enable the Administrative UI for managing Users' Model Differences](xref:113704).

> [!NOTE]
> [!include[ThreadSafe_CustomFields_Note](~/templates/threadsafe_customfields_note111210.md)]
