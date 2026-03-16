---
uid: "113472"
title: 'Add a Security Operation that Can be Permitted or Denied for a Specific Type'
owner: Ekaterina Kiseleva
---
# Add a Security Operation that Can be Permitted or Denied for a Specific Type

In the XAF [Security System](xref:113366), you can permit _Read_, _Write_, _Create_, and _Delete_ operations for a specific type. This topic describes an implementation of the additional _Export_ operation and demonstrates the customization of the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) that determines whether the _Export_ operation is allowed or denied for the currently displayed object type.

![ExportOperation_Result](~/images/exportoperation_result117203.png)

> [!Tip]
> A complete sample project is available in the following GitHub Example: [XAF - How to implement a custom security operation that can be permitted at the type level](https://github.com/DevExpress-Examples/xaf-how-to-implement-a-custom-security-operation-that-can-be-permitted-at-the-type-level).

> [!NOTE]
> If you want to permit the export functionality for all types at once at the Role level, see the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic.

## Customize the Security System
* Extend the `PermissionPolicyTypePermissionObject` persistent object that is used to store permissions with the `ExportState` property.
	
	# [C# (EF Core)](#tab/tabid-csharp-ef)

	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
	// ...
	[XafDisplayName("Type Operation Permissions")]
	public class CustomTypePermissionObject : PermissionPolicyTypePermissionObject {
	    [XafDisplayName("Export")]
	    public virtual SecurityPermissionState? ExportState { get; set; }
	}
 	```

	# [C# (XPO)](#tab/tabid-csharp-xpo)
	
	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.BaseImpl.PermissionPolicy;
	// ...
	[XafDisplayName("Type Operation Permissions")]
	public class CustomTypePermissionObject : PermissionPolicyTypePermissionObject {
	    public CustomTypePermissionObject(Session session)
	        : base(session) {
	    }
	    [XafDisplayName("Export")]
	    public SecurityPermissionState? ExportState {
	        get {
	            return GetPropertyValue<SecurityPermissionState?>(nameof(ExportState));
	        }
	        set {
	            SetPropertyValue(nameof(ExportState), value);
	        }
	    }
	}
	```
	
	***

* If you are using the EF Core ORM, add a DbSet for the `CustomTypePermissionObject` type to the DbContext:

	**File:** _MySolution.Module\MySolutionDbContext.cs_ 

	# [C#](#tab/tabid-csharp)

	```csharp
	public class MySolutionEFCoreDbContext : DbContext {
		// ...
		public DbSet<CustomTypePermissionObject> CustomTypePermissionObjects { get; set; }
	}
	```

	***


* To implement a custom Operation Permission, add a class that supports the [](xref:DevExpress.ExpressApp.Security.IOperationPermission) interface.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Security;
	using DevExpress.Persistent.Base;
	// ...
	public class ExportPermission : IOperationPermission {
	    public ExportPermission(Type objectType, SecurityPermissionState state) {
	        ObjectType = objectType;
	        State = state;
	    }
	    public Type ObjectType { get; private set; }
	    public string Operation { get { return "Export"; } }
	    public SecurityPermissionState State { get; set; }
	}
	```
	
	***
* The Security System uses Permission Requests to determine whether or not a permission is granted. Add a Permission Request for the `ExportPermission` permission. Implement the [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) interface in the following manner:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Security;
	// ...
	public class ExportPermissionRequest : IPermissionRequest {
	    public ExportPermissionRequest(Type objectType) {
	        ObjectType = objectType;
	    }
	    public Type ObjectType { get; private set; }
	    public object GetHashObject() {
	        return ObjectType.FullName;
	    }
	}
	```
	
	***
* All Permission Requests should have an appropriate Permission Request Processor known by the Security Strategy. To implement such a processor, inherit the [](xref:DevExpress.ExpressApp.Security.PermissionRequestProcessorBase`1) class and pass the Permission Request type as the ancestor class's generic parameter.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.Linq;
	using System.Collections.Generic;
	using DevExpress.ExpressApp.Security;
	using DevExpress.Persistent.Base;
	// ...
	public class ExportPermissionRequestProcessor : PermissionRequestProcessorBase<ExportPermissionRequest> {
	    private IPermissionDictionary permissionDictionary;
	    public ExportPermissionRequestProcessor(IPermissionDictionary permissionDictionary) {
	        this.permissionDictionary = permissionDictionary;
	    }
	    public override bool IsGranted(ExportPermissionRequest permissionRequest) {
	        IEnumerable<ExportPermission> exportPermissions = 
	            permissionDictionary.GetPermissions<ExportPermission>().Where(p => p.ObjectType == permissionRequest.ObjectType);
	        if (exportPermissions.Count() == 0) {
	            return IsGrantedByPolicy(permissionDictionary);
	        }
	        else {
	            return exportPermissions.Any(p => p.State == SecurityPermissionState.Allow);
	        }
	    }
	    private bool IsGrantedByPolicy(IPermissionDictionary permissionDictionary) {
	        if (GetPermissionPolicy(permissionDictionary) == SecurityPermissionPolicy.AllowAllByDefault) {
	            return true;
	        }
	        return false;
	    }
	    private SecurityPermissionPolicy GetPermissionPolicy(IPermissionDictionary permissionDictionary) {
	        SecurityPermissionPolicy result = SecurityPermissionPolicy.DenyAllByDefault;
	        List<SecurityPermissionPolicy> permissionPolicies = 
	            permissionDictionary.GetPermissions<PermissionPolicy>().Select(p => p.SecurityPermissionPolicy).ToList();
	        if (permissionPolicies != null && permissionPolicies.Count != 0) {
	            if (permissionPolicies.Any(p => p == SecurityPermissionPolicy.AllowAllByDefault)) {
	                result = SecurityPermissionPolicy.AllowAllByDefault;
	            }
	            else {
	                if (permissionPolicies.Any(p => p == SecurityPermissionPolicy.ReadOnlyAllByDefault)) {
	                    result = SecurityPermissionPolicy.ReadOnlyAllByDefault;
	                }
	            }
	        }
	        return result;
	    }
	}
	```
	
	***

* Handle the [SecurityStrategy.CustomizeRequestProcessors](xref:DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors) event in the _Startup.cs_ file from the ASP.NET Core Blazor and WinForms application projects to register the `ExportPermissionRequestProcessor`. Subscribe to this event before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called. The same technique is applicable when the [Middle Tier](xref:113439) application server is in use.

    **ASP.NET Core Blazor**

	**File:** _MySolution.Blazor.Server\Startup.cs_

    # [C#](#tab/tabid-csharp1)
	
	```csharp
	public class Startup {
		// ...
		public void ConfigureServices(IServiceCollection services) {
			// ...
			services.AddXaf(Configuration, builder => {
				// ...
				builder.Security
					.UseIntegratedMode(options => {
						// ...
						options.Events.OnSecurityStrategyCreated += securityStrategy => {
							((SecurityStrategy)securityStrategy).CustomizeRequestProcessors += delegate (object sender, CustomizeRequestProcessorsEventArgs e) {
								List<IOperationPermission> result = new List<IOperationPermission>();
								SecurityStrategyComplex security = sender as SecurityStrategyComplex;
								if (security != null) {
									ApplicationUser user = security.User as ApplicationUser;
									if (user != null) {
										foreach (PermissionPolicyRole role in user.Roles) {
											foreach (PermissionPolicyTypePermissionObject persistentPermission in role.TypePermissions) {
												CustomTypePermissionObject customPermission = persistentPermission as CustomTypePermissionObject;
												if (customPermission != null && customPermission.ExportState != null) {
													SecurityPermissionState state = (SecurityPermissionState)customPermission.ExportState;
													result.Add(new ExportPermission(customPermission.TargetType, state));
												}
											}
										}
									}
								}
								IPermissionDictionary permissionDictionary = new PermissionDictionary(result);
								e.Processors.Add(typeof(ExportPermissionRequest), new ExportPermissionRequestProcessor(permissionDictionary));
								// ...
							};
						};
					})
					// ...
			});
			// ...
		}
		// ...
	}
	```
		
    ***

    **Windows Forms**

	**File:** _MySolution.Win\Startup.cs_

	# [C#](#tab/tabid-csharp)
	```csharp
	public class ApplicationBuilder : IDesignTimeApplicationFactory {
		public static WinApplication BuildApplication(string connectionString) {
			var builder = WinApplication.CreateBuilder();
			// ...
			builder.Security
				.UseIntegratedMode(options => {
					// ...
					options.Events.OnSecurityStrategyCreated += securityStrategy => {
						((SecurityStrategy)securityStrategy).CustomizeRequestProcessors += delegate (object sender, CustomizeRequestProcessorsEventArgs e) {
							List<IOperationPermission> result = new List<IOperationPermission>();
							SecurityStrategyComplex security = sender as SecurityStrategyComplex;
							if (security != null) {
								ApplicationUser user = security.User as ApplicationUser;
								if (user != null) {
									foreach (PermissionPolicyRole role in user.Roles) {
										foreach (PermissionPolicyTypePermissionObject persistentPermission in role.TypePermissions) {
											CustomTypePermissionObject customPermission = persistentPermission as CustomTypePermissionObject;
											if (customPermission != null && customPermission.ExportState != null) {
												SecurityPermissionState state = (SecurityPermissionState)customPermission.ExportState;
												result.Add(new ExportPermission(customPermission.TargetType, state));
											}
										}
									}
								}
							}
							IPermissionDictionary permissionDictionary = new PermissionDictionary(result);
							e.Processors.Add(typeof(ExportPermissionRequest), new ExportPermissionRequestProcessor(permissionDictionary));
						};
						// ...
					};
					// ...
				})
				// ...
		}
		// ...
	}
	```

	***

## Create Predefined Users And Roles
To check the implemented Export operation, add the predefined Admin and User users with appropriate roles to the application's database. Edit the _Updater.cs_ file located in the _DatabaseUpdate_ folder of your module project. Override the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method in the following manner.

**File:** _MySolution.Module\DatabaseUpdate\Updater.cs_

# [C#](#tab/tabid-csharp)

```csharp{13,51-64}
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// ...
public override void UpdateDatabaseAfterUpdateSchema() {
    base.UpdateDatabaseAfterUpdateSchema();
	ApplicationUser user = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "User");
	if(user == null) {
		user = ObjectSpace.CreateObject<ApplicationUser>();
		user.UserName = "User";
		user.SetPassword("");
		ObjectSpace.CommitChanges();
		((ISecurityUserWithLoginInfo)user).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(user));
	}
	PermissionPolicyRole userRole = CreateUserRole();
	user.Roles.Add(userRole);

	ApplicationUser userAdmin = ObjectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == "Admin");
	if(userAdmin == null) {
		userAdmin = ObjectSpace.CreateObject<ApplicationUser>();
		userAdmin.UserName = "Admin";
		userAdmin.SetPassword("");
		ObjectSpace.CommitChanges();
		((ISecurityUserWithLoginInfo)userAdmin).CreateUserLoginInfo(SecurityDefaults.PasswordAuthentication, ObjectSpace.GetKeyValueAsString(userAdmin));
	}
	PermissionPolicyRole adminRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(r => r.Name == "Administrators");
	if(adminRole == null) {
		adminRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
		adminRole.Name = "Administrators";
	}
	adminRole.IsAdministrative = true;
	userAdmin.Roles.Add(adminRole);
    ObjectSpace.CommitChanges();

    for (int i = 1; i <= 10; i++) {
        string subject = string.Format("Task {0}", i);
        EmployeeTask task = ObjectSpace.FirstOrDefault<EmployeeTask>(t => t.Subject == subject);
        if (task == null) {
            task = ObjectSpace.CreateObject<EmployeeTask>();
            task.Subject = subject;
            task.DueDate = DateTime.Today;
            task.Save();
        }
    }
    ObjectSpace.CommitChanges();
}

private PermissionPolicyRole CreateUserRole() {
	PermissionPolicyRole userRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
	if(userRole == null) {
		userRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
		userRole.Name = "User Role";
		CustomTypePermissionObject taskTypePermission = ObjectSpace.CreateObject<CustomTypePermissionObject>();
		taskTypePermission.TargetType = typeof(EmployeeTask);
		taskTypePermission.CreateState = SecurityPermissionState.Allow;
		taskTypePermission.DeleteState = SecurityPermissionState.Allow;
		taskTypePermission.ReadState = SecurityPermissionState.Allow;
		taskTypePermission.WriteState = SecurityPermissionState.Allow;
		taskTypePermission.ExportState = SecurityPermissionState.Allow;
		CustomTypePermissionObject userTypePermission = ObjectSpace.CreateObject<CustomTypePermissionObject>();
		userTypePermission.TargetType = typeof(ApplicationUser);
		userTypePermission.ReadState = SecurityPermissionState.Allow;
		userRole.TypePermissions.Add(taskTypePermission);
		userRole.TypePermissions.Add(userTypePermission);
		userRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/MyDetails", SecurityPermissionState.Allow);
        userRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/EmployeeTask_ListView", SecurityPermissionState.Allow);
		// ...
	}
	return userRole;
}
```

***

As you can see, the `User Role` role is allowed to export `EmployeeTask` objects. The role is not allowed to export `ApplicationUser` objects. Here, it is assumed that the `EmployeeTask` object from the business class library is added to your business model (see [](xref:404214)). In this example, you can use any other business class instead of `EmployeeTask`.

## Verify if the Custom Operation is Allowed for the Current User

To let the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and its [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) know about the presence of the Export operation, add the following View Controller.

**File:** _MySolution.Module\Controllers\SecuredExportController.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.SystemModule;
// ...
public class SecuredExportController : ObjectViewController {
    private ExportController exportController;
    protected override void OnActivated() {
        base.OnActivated();
        exportController = Frame.GetController<ExportController>();
        if (exportController  != null) {
            exportController.ExportAction.Executing += ExportAction_Executing;
        }
    }
    void ExportAction_Executing(object sender, System.ComponentModel.CancelEventArgs e) {
		if (!Application.GetSecurityStrategy().IsGranted(new ExportPermissionRequest(View.ObjectTypeInfo.Type))) {
			throw new UserFriendlyException("Export operation is prohibited.");
		}
    }
}
```

***

This Controller subscribes to the **Export** Action's [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) event and calls the [SecurityStrategy.IsGranted](xref:DevExpress.ExpressApp.Security.SecurityStrategy.IsGranted*) method to check whether or not the Export operation is allowed before export is executed. An exception will be thrown if the current user is not allowed to export objects displayed in the current View. To test it, run the application, log on as `User`, navigate to the list of users and try to execute the **Export** Action.

You may want to avoid the security exception and deactivate the **Export** Action when exporting is not allowed. In this instance, additionally override the `OnActivated` method and change the Action's visibility in accordance with the [SecurityStrategy.IsGranted](xref:DevExpress.ExpressApp.Security.SecurityStrategy.IsGranted*) method result.

**File:** _MySolution.Module\Controllers\SecuredExportController.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class SecuredExportController : ObjectViewController {
    // ....
    protected override void OnActivated() {
       	base.OnActivated();
       	exportController = Frame.GetController<ExportController>();

       	if (exportController != null) {
           	exportController.ExportAction.Active.SetItemValue("Security",
                Application.GetSecurityStrategy().IsGranted(new ExportPermissionRequest(View.ObjectTypeInfo.Type)));
       	}
   	}
}
```

***

If you run the application and log on as `User`, you will see that the **Export** action is active for `EmployeeTask` objects and is hidden for `ApplicationUser` objects.

## Adjust the Administrative UI

If you open the `Role` Detail View and select the **Type Permissions** tab, you will see no **Export** column in the nested List View. The object type of this List View is `PermissionPolicyTypePermissionObject`, while the `AllowExport` property is declared in the derived `CustomTypePermissionObject` class. To display the **Export** column, [use UpCasting](xref:112797). Invoke the [Model Editor](xref:112582), navigate to the **PermissionPolicyRoleBase_TypePermissions_ListView** node and add the `ExportState` column. Set the `PropertyName` to `\<CustomTypePermissionObject>ExportState` for this column. The image below illustrates this customization.

![ExportOperation_AddColumn](~/images/exportoperation_addcolumn117201.png)

Navigate to the **CustomTypePermissionObject_DetailView** node and make the following adjustments to its **Layout**:

* Group the operation checkboxes together.
* Move the `TargetType` property to the top.

The following image demonstrates the required layout:

![ExportOperation_Layout](~/images/exportoperation_layout117202.png)

You may notice that the **New** Action accompanying the **Type Permissions** List View contains duplicate **Type Operation Permissions** Action Items. One of these Items refer to the base `PermissionPolicyTypePermissionObject` type, and another - to your custom `CustomTypePermissionObject`. To hide the base class item, use the following Controller to [customize the New Action's items list](xref:112915).

**File:** _MySolution.Module\Controllers\RemoveBaseTypePermissionNewActionItemController.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// ...
public class RemoveBaseTypePermissionNewActionItemController :
    ObjectViewController<ObjectView, PermissionPolicyTypePermissionObject> {
    protected override void OnFrameAssigned() {
		NewObjectViewController newObjectViewController = Frame.GetController<NewObjectViewController>();
		if(newObjectViewController != null) {
			newObjectViewController.CollectDescendantTypes += (s, e) => {
				e.Types.Remove(typeof(PermissionPolicyTypePermissionObject));
			};
			newObjectViewController.ObjectCreating += (s, e) => {
				if(e.ObjectType == typeof(PermissionPolicyTypePermissionObject)) {
					e.NewObject = e.ObjectSpace.CreateObject(typeof(CustomTypePermissionObject));
				}
			};
		}
		base.OnFrameAssigned();
	}
}
```

***
