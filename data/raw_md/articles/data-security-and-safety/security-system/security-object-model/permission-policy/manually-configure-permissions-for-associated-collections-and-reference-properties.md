---
uid: "113556"
seealso: []
title: 'Manually Configure Permissions for Associated Collections and Reference Properties'
seealso:
- linkId: "116170"
---
# Manually Configure Permissions for Associated Collections and Reference Properties

The [Security System](xref:113366) automatically configures permissions for one side of an association if the other side is specified. The [Permissions for Associated Objects](xref:116170) topic describes this behavior. You can also specify permissions for both sides of an association. This topic describes how to manually allow linking and unlinking of objects from a collection when a user has read-only access to objects in this collection. Here, it is assumed that you have:

* Two business classes called **Employee** and **Project**.
* A _many-to-many_ association between these classes using the **Employee.Projects** and **Project.Employees** collection properties (see [Set a Many-to-Many Relationship](xref:402983)).
* An enabled Security System (see [Client-Side Security (2-Tier Architecture)](xref:113436)).

The key concept is that you should grant _Write_ access to the collection properties on both sides of the association to allow linking and unlinking operations. These operations always lead to modifying both collections. That is why granting _Write_ on one side is insufficient.

> [!NOTE]
> In this example, the _many-to-many_ association is demonstrated. However, you can use the same approach with the _one-to-many_ association.

Follow the steps below to set up a security role that has read-only access to **Projects**, but can modify the **Employee.Projects** collection.

1. In the overridden [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method (located in the [!include[File_Updater](~/templates/file_updater111114.md)] file of the module project), create a user role. For this role, grant full access to the **Employee** object, and read-only access to the **Project** object.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	PermissionPolicyRole role = ObjectSpace.CreateObject<PermissionPolicyRole>();
	role.Name = "User role";
	role.AddTypePermission<Person>(SecurityOperations.CRUDAccess, SecurityPermissionState.Allow);
	role.AddNavigationPermission("Application/NavigationItems/Items/Default/Items/Employee_ListView", SecurityPermissionState.Allow);
	role.AddTypePermission<Project>(SecurityOperations.ReadOnlyAccess, SecurityPermissionState.Allow);
	```
	
	***
2. Currently, a user whose role is **User role** cannot link or unlink **Project** objects. Linking or unlinking **Project** objects causes a modification of the **Employees** property, which is read-only, because the **Project** object is read-only. The solution is to grant _Write_ access to this property.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	role.AddMemberPermission<Project>(SecurityOperations.Write, "Employees", "", SecurityPermissionState.Allow);
	```

	***
3. Add a user associated with the role that was configured in the previous steps.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	ApplicationUser user = ObjectSpace.CreateObject<ApplicationUser>();
	user.UserName = "User";
	user.SetPassword("");
	user.Roles.Add(role);
	```

	***
4. Run the application, log in as "User", and ensure that the **Project** objects can be linked to the **Employee.Projects** collection.
	
	![Associations_ManyToMany_LinkUnlinkReadonlyObjects](~/images/associations_manytomany_linkunlinkreadonlyobjects117316.png)