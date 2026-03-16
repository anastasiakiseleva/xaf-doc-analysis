---
uid: '113366'
title: Security (Access Control & Authentication)
owner: Ekaterina Kiseleva
---

# Security (Access Control & Authentication)

This section contains information on various aspects of the XAF Security System that offers you extensive permission management and access control capabilities out-of-the box. [See our demos](#see-demos) to research the Security System's functionality.

The Security System supports both XAF UI and non-XAF .NET applications, including [Backend Web API Service](xref:403394). As a registered DevExpress.com user, you are entitled to a free copy of .NET Role-based Access Control & Permission Management API powered by Entity Framework Core (EF Core) and DevExpress [XPO](https://www.devexpress.com/Products/NET/ORM/) ORM tools. For more information on this offer, refer to the following pages: [.NET App Security API (Role-based Access Control) – Free Offer from DevExpress](https://www.devexpress.com/security-api-free/), [GitHub examples](https://github.com/DevExpress-Examples/XAF_Security_E4908), [Technical FAQ](https://supportcenter.devexpress.com/ticket/details/t886740/faq-net-app-security-web-api-for-ef-core-xpo-orm), or [tutorial videos](https://www.youtube.com/playlist?list=PL8h4jt35t1wiM1IOux04-8DiofuMEB33G).

[!include[security-system-important-note-about-change-tracking](~/templates/security-system-important-note-about-change-tracking.md)]

## Prerequisites

To install the dependencies required to use the XAF Security System either standalone or as a part of an XAF application, use one of the following option:

### Option 1: Run the Installation

Download and run our [Unified Component Installer](https://www.devexpress.com/Products/Try/). The installer will copy all required assemblies to _"%PROGRAMFILES%\DevExpress XX.X"_ and register local NuGet package sources. **Note:** \*.BaseImpl.\* assemblies are required only if you use built-in PermissionPolicyXXX classes.

### Option 2: Use DevExpress NuGet Gallery (.NET)

[Register the DevExpress remote NuGet Feed](xref:116698#register) and install the following [DevExpress NuGet](https://nuget.devexpress.com/) packages for .NET. 

- EF Core: [DevExpress.ExpressApp.Api.EFCore.All](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Api.EFCore.All)
- XPO: [DevExpress.ExpressApp.Api.Xpo.All](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Api.Xpo.All)

Please click the NuGet package links above to see specific .NET assemblies.

## XAF Security System API Compared to Standard .NET Security Features

The security System's Authentication APIs can use ASP.NET authentication and other middleware – these simply provide an additional layer of customization and extensibility not tied to any particular framework. You can use the authentication engine in conjunction with built-in OAuth 2 (Microsoft, Google, Facebook, etc.) authentication providers or implement any custom authentication scheme.

Authorization APIs are similar to `IAsyncAuthorizationFilter` and `IAuthorizationFilter` or `AuthorizationHandler`, `IAuthorizationRequirement` and `IAuthorizationPolicyProvider` APIs offered by Microsoft (you can learn more about Microsoft’s API from [StackOverFlow](https://stackoverflow.com/questions/57800314/how-to-dynamically-adding-new-roles-with-permissions-in-asp-net-identity) or [Microsoft documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data)).

Our implementation differs in the following key areas:

- Our API ships built-in user, role and permission entities that help developers manage authorization configurations at runtime (because they are physically stored in the database using XPO or EF Core ORMs). With a fully dynamic permission policy, your apps can address changes to security requirements without the need for redeployment. If you build an administrative UI, [like we did in XAF's UI](xref:404633#type-permissions), developers can even delegate certain configuration responsibilities to application administrators or power users - these features are favorites among developers.

- Instead of hard-coded and narrow permissions for specific entities like _"See Documents Owned by Me"_, our API offers a general purpose Type, Object, Member-level and custom permissions that can be used by developers with any entity type to solve security-related tasks of any complexity

- Object and Member-level permissions include criteria support - a unique feature for fine-grain access control. You can specify [criteria expressions](xref:4928) using both string and strongly-typed formats. 

  # [C#](#tab/tabid-csharp)

  ```csharp
  // The following object permission addresses this business requirement: 
  // "allow 'Read' access to departments when title contains the word 'Development'".
  userRole.AddObjectPermissionFromLambda<Department>(
      SecurityOperations.Read, 
      t => t.Title.Contains("Development"), 
      SecurityPermissionState.Allow
  );

  // The following member permission addresses this business requirement:
  // "deny 'Write' access to an employee's Last Name property 
  // when his/her department title does not contain the word 'Development'".
  userRole.AddMemberPermissionFromLambda<Employee>(
      SecurityOperations.Write, 
      nameof(Employee.LastName), 
      t => !t.Department.Title.Contains(protectedDepartment), 
      SecurityPermissionState.Deny
  );
  ```
  ***

## Architecture

The image below illustrates the XAF Security System architecture:

![Security System Architecture](~/images/security-system-architechture.png)

For more information, see this overview video:

> [!video https://www.youtube.com/embed/sIhWOXRWlOw]

## See Demos

For code examples on Security System in _non-XAF apps_, refer to the following GitHub repository: [Role-based Access Control, Permission Management, and Web API for .NET App](https://github.com/DevExpress-Examples/XAF_Security_E4908).

For information on Security System in _XAF UI apps_, research the following demos:

- MainDemo, SecurityDemo (_c:\Users\Public\Documents\DevExpress Demos XX.X\Components\XAF\_);
- DentalClinic (_c:\Users\Public\Documents\DevExpress Demos XX.X\Components\WinForms\DevExpress.DentalClinic\CS\_);
For general information, please [review our landing page](https://www.devexpress.com/products/net/application_framework/security-web-api-service.xml).


