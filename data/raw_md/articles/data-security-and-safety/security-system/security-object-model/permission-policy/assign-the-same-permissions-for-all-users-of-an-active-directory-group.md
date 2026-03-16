---
uid: "118740"
seealso: []
title: 'Assign the Same Permissions for All Users of an Active Directory Group'
owner: Ekaterina Kiseleva
---
# Assign the Same Permissions for All Users of an Active Directory Group

The [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication type does not support [Active Directory Security Groups](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups) out of the box. This topic demonstrates how to map XAF security roles to AD groups. When a user logs on for the first time, existing roles with names matching the user's AD group names are automatically assigned. If the user membership in AD groups was modified, the associated roles collection will be updated accordingly on the next logon.

> [!NOTE]
> ASP.NET Core Blazor applications do not support Active Directory authentication.

* In the [module project](xref:112569), reference the _System.DirectoryServices.AccountManagement.dll_ assembly, which provides the [UserPrincipal](https://learn.microsoft.com/en-us/dotnet/api/system.directoryservices.accountmanagement.userprincipal) class.
* Inherit **AuthenticationActiveDirectory** and override the  [AuthenticationActiveDirectory.Authenticate](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.Authenticate(DevExpress.ExpressApp.IObjectSpace)) method:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System.DirectoryServices.AccountManagement;
	using DevExpress.Data.Filtering;
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Security;
	using DevExpress.Persistent.BaseImpl.PermissionPolicy;
	// ...
	public class CustomAuthenticationActiveDirectory : AuthenticationActiveDirectory { 
	    public override object Authenticate(IObjectSpace objectSpace) { 
	        string userName = GetUserName(); 
	        ApplicationUser user = objectSpace.FirstOrDefault<ApplicationUser>(u => u.UserName == userName); 
	        if(user == null) { 
	            if(CreateUserAutomatically) { 
	                user = objectSpace.CreateObject<ApplicationUser>(); 
	                user.UserName = userName; 
	            }                 
	        } 
	        if(user != null) { 
	            foreach(PermissionPolicyRole role in user.Roles.ToArray()) { 
	                if(!UserPrincipal.Current.GetGroups().Any(p => p.Name == role.Name)) { 
	                    user.Roles.Remove(role); 
	                } 
	            } 
	            foreach(string groupName in UserPrincipal.Current.GetGroups().Select(x => x.Name)) { 
	                if(!user.Roles.Any(p => p.Name == groupName)) { 
	                    PermissionPolicyRole role = objectSpace.FirstOrDefault<PermissionPolicyRole>(r => r.Name == groupName); 
	                    if(role != null) { 
	                        user.Roles.Add(role); 
	                    } 
	                } 
	            } 
	        } 
	        if(user == null || user.Roles.Count == 0) { 
	            throw new AuthenticationException(userName); 
	        } 
	        objectSpace.CommitChanges(); 
	        return user; 
	    } 
	}
	```

	***

* Rebuild the solution.
* Run the Application Designer and replace the **AuthenticationActiveDirectory** component with the **CustomAuthenticationActiveDirectory** component from the toolbox (as it is demonstrated in the **Pass the Custom Classes to the Security System** section of the [How to: Use Custom Logon Parameters and Authentication](xref:404264) topic).
	
	![CustomAuthenticationActiveDirectory](~/images/customauthenticationactivedirectory128642.png)
