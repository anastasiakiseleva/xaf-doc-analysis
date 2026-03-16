---
uid: "404691"
title: General Security Considerations
owner: Vladimir Abadzhev
---
# General Security Considerations
 
## App Development Best Practices: General and DevExpress-Specific Information  

DevExpress UI components and development libraries undergo multiple security-related testing processes. These processes apply to XAF UI, Web API Service, and underlying components like XPO ORM and DevExpress UI controls for various platforms (ASP.NET Core Blazor and Windows Forms). DevExpress UI components and development libraries are scanned with external SAST tools (including [Veracode](https://www.veracode.com/verified/directory/devexpress) and CodeQL) and internal software. For additional information, review the following article:

[](xref:403365) 

XAF applications also rely on many third-party libraries, technologies, and app services (.NET, JavaScript & HTML, database and network management systems, and more). As such, you need to fully consider/apply app development best practices when using our products and those we rely upon. It’s up to you, the application developer, to follow security-related guidelines.

You may find the following security-related best practice links helpful as you seek to secure your app against the actions of threat actors.

- [Security Best Practices for DevExpress UI Components](xref:403365#best-practices)

Third-party security-related links:

- [Make secure .NET Microservices and Web Applications](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/secure-net-microservices-web-applications/) 
- [ASP.NET Core security topics](https://learn.microsoft.com/en-us/aspnet/core/security/) 
- [Security Considerations for a SQL Server Installation](https://learn.microsoft.com/en-us/sql/sql-server/install/security-considerations-for-a-sql-server-installation) 
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Microsoft's Security Engineering Portal](https://www.microsoft.com/en-us/securityengineering)
- [Secure development best practices on Azure](https://learn.microsoft.com/en-us/azure/security/develop/secure-dev-overview)  

## Content Security Policy (Web Apps) 

Content Security Policy (CSP) is a built-in browser mechanism that helps you protect your web application against certain types of attacks, such as Cross-Site Scripting (XSS), clickjacking, and data injection. CSP is supported in most modern browsers, including Chrome, Edge, Firefox, Opera, Safari, and mobile browsers. 

CSP applies to XAF applications for Blazor. Review the documents below for additional information: 

- [Content Security Policy (CSP) in XAF Blazor Apps](xref:404448)

## Authentication (User Logins and Passwords) 

### Authentication Strategies: Overview 

Applications based on XAF UI/Web API Service support both basic and advanced authentication options, including custom authentication strategies. 

1. Built-in authentication types include: **Forms** (user name and password), **Active Directory** (Windows user) and **Mixed** (several authentication providers). For more information, refer to [Authentication](xref:119064). 

2. XAF includes a robust password generation/validation algorithm. For more information, refer to [Passwords in the Security System](xref:112649) and [Validate Password Complexity](xref:401909). 

3. You can extend standard authentication methods or replace our implementation with custom authentication strategies and logon parameters. For instance, [our popular Blazor example](xref:402197#google-azure-and-github-providers) supports OAuth2 with Google or Microsoft cloud authentication providers. [Our Web API/OData example](xref:403394) protects a backend service using a JWT bearer authentication schema with Azure AD. 

### Storing Sensitive Password Information In Transit and At Rest

According to industry standards, XAF does not store passwords in plain text in the database, log files, or anywhere else. For more information, review [Password Encryption](xref:112649#password-encryption). 

When data is in transit (between calls from client to server), we use different methods to store authentication tokens (such as user ID) depending on the application type. XAF Blazor applications use cookies by default. For Web API applications, the [Template Kit](xref:405447) generates a template with JWT authentication.

We may store user ID and user name information in a cookie or a JWT token. We also store a serialized logon parameter object in a cookie. We do not store user passwords. Password information is removed from the logon parameter object before serialization. The logon parameters object type must implement the `IAuthenticationStandardLogonParameters` interface for this purpose. The default `AuthenticationStandardLogonParameters` type does implement this interface.

Review the following articles for additional information on how authentication works in XAF ASP.NET Core-based apps:

* [Authentication System Architecture (Blazor)](xref:404462)
* [Access Token Lifetime (Middle Tier Server)](xref:404401#access-token-lifetime)
* [Configure the JWT Authentication (Web API Service)](xref:403504)

You can also review the following classes in our source code: `UserTokenProcessor`, `LogonDataProtectorService`, and `SignInMiddleware`.  

### Change Predefined Roles, Users, and Passwords in the Updater Class 

An XAF application may create demo/test roles and users automatically. This only happens in **Debug** mode if you used the [Template Kit](xref:405447). (See the `#if DEBUG` preprocessor directive in _SolutionName.Module\DatabaseUpdate\Updater.xx_.) 

In **Release** mode, you must create users and roles according to your specific business needs. Modify code in _SolutionName.Module\DatabaseUpdate\Updater.xx_ and make sure that this code is not placed under the `#if DEBUG` preprocessor directive. You can also create new users and roles at runtime using your production application UI or access the database directly. 

For additional information, review the following articles: 

- [Security - Test roles are no longer assigned automatically to new users in Release mode and apps with the Windows Active Directory authentication](https://supportcenter.devexpress.com/ticket/details/t1105320/security-test-roles-are-no-longer-assigned-automatically-to-new-users-in-release-mode)
- [](xref:119065)


### Brute Force Attack Protection 

In ASP.NET Core apps, you can use standard Microsoft APIs to protect against brute force attacks, lock users, limit the number of failed login attempts, etc. Refer to the following article for additional information: 

[Configure ASP.NET Core Identity](https://learn.microsoft.com/en-us/aspnet/core/security/)

XAF UI for Blazor and WinForms and Web API Service include built-in "Brute Force" attack protection. Your apps can prevent unauthorized attempts to log in and access data by guessing user passwords multiple times. You can implement the [ISecurityUserLockout](xref:DevExpress.ExpressApp.Security.ISecurityUserLockout) interface in your application user class, and configure the maximum number of failed login attempts in settings.
 

## Authorization (Role-Based Access Control) 

XAF UI and Web API Service apps ship with built-in Role-based Access Control (RBAC) - a part of the **Security System** module. We recommend that you configure **Type**, **Record**, and **Field** level permissions for different user roles. This way, you implement proper data and UI authorization support (filter sensitive data automatically and authorize CRUD/custom operations). 

You can implement fine-grain access control for object relationships, individual objects, or columns. For example, a user may be able to read the _Name_ field, but not be able to modify _Salary_. 

Use straightforward API to check access permissions and customize UI accordingly. For example, you can mask protected editors or disable menu commands. 

In addition to access permissions, you must also choose and configure an appropriate security tier architecture for your application. Make sure that network access to the data store is secure. For more information, refer to the following article: 

[Security (Access Control & Authentication)](xref:113366) 


The **Security System** module implements a wide variety of data protection tools. The following image illustrates how this module integrates into your XAF applications.  

![Security System Diagram](~/images/xaf-security-system-diagram.png)


### Anonymous Business Objects (Bypass Security or User Login) 

The **Security System** module allows you to configure [Type Permissions](xref:404633#type-permissions) for persistent types only. [Non-persistent objects](xref:116516) **are not secured and users can access them freely**. If you want to protect a non-persistent object type, add this type to the static `SecurityStrategy.AdditionalSecuredTypes` collection and configure an associated permission. 

XAF's Security System also implements specialized API for advanced scenarios where certain data needs to remain unprotected or accessible without a user login. 

- [AllowAnonymousAccess](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AllowAnonymousAccess) 
- [AnonymousAllowedTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.AnonymousAllowedTypes)
- [SupportNavigationPermissionsForTypes](xref:DevExpress.ExpressApp.Security.SecurityStrategy.SupportNavigationPermissionsForTypes)

We do not recommended that you allow anonymous access to all data using the `AllowAnonymousAccess` property. Instead, use the `AnonymousAllowedTypes` property to grant access to select types. 


### Forced Browsing Protection 

This strategy applies to both public and private web apps that utilize a practice called “**security by obscurity**”. For instance, your application-level security system may hide certain navigation control items for non-Admin users. At the same time, you may not handle a scenario when a user guesses a web page URL and simply pastes that URL into a web browser address bar. One way a user can “guess” a URL is if you use recognizable patterns. For instance, you can use consecutive numbers to access specific web page sequences - `/contacts/1`, `/contacts/2`, etc.  

Proper protection against “forced browsing” is a solid security system. Such a system typically uses role-based access control permissions at the Type, Record, and even Field level. Protection from the “forced browsing” attack is especially critical for system objects such as Application Model differences, Audit Trail events, File Attachments, or Reports. See specific recommendations for these object types below. 

We recommend that developers of XAF UI and Web API Service apps enforce **Read** access permission for object types associated with navigation permissions (**Navigation** permission is insufficient). [Navigation permission](xref:404633#navigation-permissions) alone simply shows/hides navigation items in the navigation control and does not grant or deny access to business objects themselves. A user may type a URL to a detail form of a specific record. To avoid "forced browsing", you must use **Type** or **Object** permissions and deny **Read** access. This way users will not see the protected information on the form, even if they guessed the corresponding URL (the server will not transmit sensitive data to the client app). 

XAF attracts administrator attention to these settings - it displays validation warnings in the administrative UI. For additional information, refer to the following articles:

- [Security - Read access is enforced for object types associated with navigation permissions](https://supportcenter.devexpress.com/ticket/details/t1121892/security-read-access-is-enforced-for-object-types-associated-with-navigation-permissions)
- [Permissions for Associated Objects](xref:116170)

If this built-in validation/protection mechanism is insufficient for your business needs, you can implement custom solutions. Handle the [XafApplication.CustomProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.CustomProcessShortcut) or [XafApplication.ViewCreating](xref:DevExpress.ExpressApp.XafApplication.ViewCreating) event in a custom `ViewController`. You can use an [IsGrantedExtensions](xref:DevExpress.ExpressApp.Security.IsGrantedExtensions) object to determine user permissions. If you need to disable access, you can also display a service/placeholder View. Simply display an error page or disable editors using `PropertyEditor.AllowEdit` or `View.AllowEdit` properties. For more information, refer to the following article: 

[Determine if the Current User Has Specific Permissions](xref:403824) 

### File and Media Data Protection 

[FileData](xref:DevExpress.Persistent.Base.IFileData), `FileAttachmentBase`, [MediaDataObject](xref:DevExpress.Persistent.BaseImpl.MediaDataObject) (and their custom implementations) are regular business objects as far as XAF’s Security System is concerned. These objects may have their own security permissions. They are also not usually independent and form an aggregation (one-to-one or one-to-many relationship) with a parent business object. This means that related object permissions are normally enforced on them. For more information, refer to the following articles: 

- [Permissions for Associated Objects](xref:116170) 
- [Relationships Between Objects](xref:402958) 

Image properties declared [as a byte array](xref:113546) are an exception from the rule above. These properties fully derive their access permissions from the corresponding object. You're not supposed to configure their type and object permissions, unless you want to apply permissions to a specific property. 

Suppose your business object `Task` has a property `Attachment` of a `FileData` type or a property `Photo` of a `MediaDataObject` type. All tasks are visible to all application users; this allows all attachments or photos are to be visible to all users as well. Users can also browse all unprotected files. For example, they can run an XAF Blazor app and type "/FileData_ListView" or "/MediaDataObject_ListView" in the browser. If certain files should to be private, then such a file browsing method constitutes a “forced browsing” attack. XAF developers must take action to prevent this attack type. 

You can enforce permission rules where clients can only access files created by them or for them. Implement a custom descendant of a built-in file class or implement the `IFileData` interface from scratch. Provide additional fields such as `CreatedBy` or `ModifiedBy`. You can then implement standard XAF security permissions based on the `CurrentUserId` criteria function. For more information, review the following article:

[How to restrict inter-departmental data access using Security Permissions (EF Core)](https://github.com/DevExpress-Examples/xaf-separate-employees-data-in-different-departments-using-security-permissions)

To avoid a potential distributed denial-of-service (DDoS) attack (a malicious attempt to disrupt the normal traffic of a targeted web server, service, or network) by large media file attachments, configure the following option as your enterprise needs and typical customer scenarios dictate: [FileAttachmentsOptions.DefaultMaxFileSize](xref:DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions.DefaultMaxFileSize) (ASP.NET Core Blazor).

### Application Model Protection 

XAF developers should not store sensitive information in XAF’s Application Model. 

In an attempt to secure data, you may want to use the Application Model and hide select Navigation Items or disable individual Views and Editors. This practice is called “security by obscurity”. It prevents proper protection if used without Security System capabilities. 

You can store model differences in various mediums - file system, database, or custom storage. Depending on the storage type, XAF developers must implement additional measures to prevent unauthorized changes to the Application Model. This is especially important if related settings govern critical UI and behaviors of the application. For instance, an XAF WinForms application may store critical settings in the Model.XAFML file deployed to the client workstation. In such cases, end-users can view and edit this XAFML file on their machine. 

To ensure solid protection, store Application Model differences in the database. Configure security permissions for the `ModelDifference` and `ModelDifferenceAspect` business objects. (These are regular business objects as far as XAF’s Security System is concerned.) If you do not configure proper security permissions, end-users can open “/ModelDifference_ListView” and see user data in their web browser. For more information, refer to the following help topic:

[Store Application Model Differences in the Database](xref:113698)

We recommend that XAF developers prevent access to the runtime Model Editor in WinForms apps for regular users. This editor is available to administrators in Release mode or developers in Debug mode. 

XAF Blazor apps do not include a runtime Model Editor. A [standalone Model Editor](xref:113326#deploy-and-run-the-standalone-model-editor) is available to developers. You can control access to that editor with corresponding web server permissions. 

You may want to [disable runtime layout customizations](xref:112817#runtime-customization) based on security permissions. Apply restrictions globally or based on a specific View or user role. 
 

## Data Store Protection 

### Security Tiers 

XAF UI apps have access to two different security tiers. Choose on of the two security strategies for your application depending on your UI type and other project requirements: 

- [2-Tier Security](xref:113436) (Integrated and UI Level modes). **Integrated** mode is mostly applicable to XAF Blazor and Web API Service apps. This mode offers the highest protection level for these apps because the client application has no direct access to the database. **UI Level** mode is not recommended for use in new applications. It remains available for legacy application support. 
- [Middle Tier Security](xref:404389) (EF Core and XPO implementations). This strategy offers the highest protection level for XAF WinForms apps and any non-XAF apps. DevExpress [Web API Service](xref:403394) implements a variation of "Middle Tier Security" and targets non-XAF apps specifically. 

The main difference between security strategies is the location where protection takes place: the data source or the client app. Data source protection does not transfer any restricted data to the client. If an XAF app uses the Security System module, data on the client doesn't include restricted records and contains 'null' values in restricted fields. For instance, assume a data table contains 3 records, but permissions allow a user to view only 1 record. If your application queries records for this user, the data source returns only 1 record to the client. 

### Ways to protect database connection strings in desktop, web, or mobile clients  

There are application that may store database connection strings in plain and accessible form (for instance, in a configuration file). A user can then locate the connection string and access the database directly. When given direct access, users can modify data regardless of permissions granted to them through the application-level security system.  

To prevent users from accessing database connection information, implement an additional layer of protection. The following list outlines a few available options:  

- In ASP.NET Core (including Blazor apps), you can use the [Data Protection](https://learn.microsoft.com/en-us/aspnet/core/security/) mechanism, which may utilize [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/).  
- In SQL Server, you can enable [encrypted connections](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption) between the database engine and clients. Note that this method has known issues when used with Blazor WebAssembly and .NET MAUI mobile clients - [.NET SQL Client Issue 1662](https://github.com/dotnet/SqlClient/issues/1662), [.NET SQL Client Issue 1840](https://github.com/dotnet/SqlClient/issues/1840), [.NET Runtime Issue 77386](https://github.com/dotnet/runtime/pull/77386).   
- You can use a data service that filters out sensitive data. Connect client apps to this service. In this case, the user application doesn't obtain any restricted data and doesn't have direct access to the database. To learn more, review information about **Middle Tier Security** (see previous section) and **OData/Web API Service Integration** (see next section).   
  

### Integration of XAF app logic &amp; data with non-XAF apps or external systems 

Non-XAF apps that accompany XAF UI apps often need to access the same data and logic remotely. 

You can use standard ASP.NET Core solutions for authentication and authorization. A wide variety of resources is available on this subject. The list below contains just a few videos published on the DevExpress YouTube channel (Carl Franklin's Blazor Train series).  

- [Basic Authentication and Authorization in Blazor Web Assembly](https://www.youtube.com/watch?v=I3A1R-oBK7c) <br> Carl Franklin's Blazor Train, Ep. 27 
- [Adding Identity to Existing WASM Apps](https://www.youtube.com/watch?v=2V2tQU1kEOM)  <br> Carl Franklin's Blazor Train, Ep. 56 
- [MSAL Auth in Blazor Server](https://www.youtube.com/watch?v=AlRxwIOq4jQ) <br> Carl Franklin's Blazor Train, Ep. 89

Whether your XAF application uses DevExpress XPO or Microsoft EF Core for the data layer, you can configure a [middle-tier application server](xref:404389) or an [OData/Web API Service](xref:403394). The following examples show these best practices in action:  

- [Blazor WebAssembly App](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/23.1.1%2B/EFCore/ASP.NetCore/Blazor.WebAssembly) (uses DevExpress Blazor Data Grid, Reports and Editors)  
- [.NET MAUI (iOS/Android) App](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/23.1.1%2B/EFCore/MAUI) (uses FREE DevExpress .NET MAUI Data Grid, Reports and Editors)  
- [JavaScript with DevExtreme + ASP.NET Core Web API/OData App](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/23.1.1+/EFCore/ASP.NetCore/DevExtreme.OData)
- [JavaScript with Svelte + ASP.NET Core Web API/OData App](https://github.com/oliversturm/demo-dx-webapi-js/tree/stage-4)
- [Connect to an EF Core Middle Tier Security Application from Non-XAF Applications](xref:404398)

## Antiforgery Support

XAF Blazor and Web API apps with [XAF Security](xref:113366) have built-in [antiforgery](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery#antiforgery-in-aspnet-core) support.

* In Blazor apps, antiforgery applies mainly to Dashboards. 
* Web API apps secure all authenticated endpoints, such as DataController and MediaFileController. 

XAF uses the standard [ValidateAntiForgeryToken](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery#require-antiforgery-validation) attribute. It also registers key antiforgery services.

XAF secures IFileService URLs (such as images and attachments) with an [HMAC](https://en.wikipedia.org/wiki/HMAC) token. The encryption key is stored in the configuration file under the `UrlSigningKey` property. If the property is not specified, XAF generates a random in-memory key. We recommend that you use [Azure Key Vault integration](https://learn.microsoft.com/en-us/aspnet/core/security/key-vault-configuration) or a similar service to create and manage your access keys.

You can disable the HMAC token with the following code:

```csharp
builder.Security
    .UseIntegratedMode(options => {...})
    .ConfigureUrlSigning(opt => opt.UseHMAC = false)
    // ...
```

When you use JWT authentication, antiforgery validation does not apply.

> [!important]
> The Antiforgery mechanism in Web API apps with Windows authentication can result in error 400. You can use the `AntiforgeryOptions.ExcludeAuthenticationSchemes` property to disable antiforgery for Windows authentication:
> 
> ```csharp
> builder.Security
>     .UseIntegratedMode(options => {...})
>     .ConfigureAntiforgery(opt => {
>         opt.ExcludeAuthenticationSchemes.Add("NTLM"); // for Kestrel
>         opt.ExcludeAuthenticationSchemes.Add("Negotiate"); // for IIS
>     });
> ```

## Conditional Appearance Module 

Appearance rules work at the UI level and have no effect on editors that do not support [Conditional Appearance](xref:113286).  We do not recommend that you use the Conditional Appearance module as a security measure. This module was not designed for this task. The practice of appearance/visibility manipulation at the UI level is “security by obscurity”. Users can bypass such techniques with **forced browsing**. For example, a user may view hidden HTML elements and their data in web browser Developer Tools (F12). 

We recommend that XAF developers use the **Security System** to secure data on a per-user/per-role basis. 

## Report and Dashboard Modules  

### Query Builders 

DevExpress Dashboard and Report Designers include Query Builder components. These components allow end-users to create new or edit existing SQL queries. Note that the default validation mechanism only allows custom queries containing SELECT statements (except SELECT INTO clauses). You can't consider all such queries safe. A risk of potentially harmful requests does exist. 

You can also override default settings and enable unrestricted custom query execution. Be cautious as custom queries allow your users to modify the connected database. If you do enable custom SQL scripts, we recommend that you implement your own validation logic that permits only specific query types. For additional information, refer to the following articles:  

- [DevExpress Reports: Disable Custom SQL Queries](xref:119202#disable-custom-sql-queries)
- [DevExpress Dashboard: Custom SQL Queries](xref:117193)  

 

### C# Scripts in the Reports Module 

[Report scripts](xref:2593) are not secure. XAF’s Reports module keeps this feature disabled by default. We recommend that you use [expression bindings](xref:119236) instead. Enable scripts only if you trust your report source and cannot use expression bindings. 

 
### SQL Data Source

Reports and dashboards bound to [SqlDataSource](xref:DevExpress.DataAccess.Sql.SqlDataSource) and [DashboardSqlDataSource](xref:DevExpress.DashboardCommon.DashboardSqlDataSource) bypass XAF's Security System permissions and work directly with the underlying database using SQL. Review [reasons to use an SQL Data Source and associated limitations](xref:117720#use-the-sql-data-source).

In such advanced scenarios, you must protect data manually, exactly as you would do it in a non-XAF application. For instance, you need to use SQL Server settings to grant specific users access rights to required database tables. 

Security System rules are in effect if you use XAF’s built-in data sources powered by our `ObjectSpace` implementation: [CollectionDataSource](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource), [ViewDataSource](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource), and [Object Data Source](xref:117450).

## Audit Trail Module 

We recommend that XAF developers enable the **Audit Trail** module when security requirements dictate that they track data changes made by users. For more information, refer to [Audit Trail (History of Data Changes)](xref:112782). 

The **Audit Trail** module logs user operations in the application. It does not log modifications made directly in the database bypassing XAF application UI or our Web API Service. For example, a database administrator may use SQL Server Management Studio to run a direct SQL query. If an administrator deletes a record in that manner, the **Audit Trail** module would not log that operation. 

To log all database changes, consider native audit solutions at the database server level:

 [SQL Server Audit (Database Engine)](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine)


## Dynamic Module Registration, Debug Environments, and Other Risky Operations 

### Functional Testing & Debug Environments 

[EasyTest](xref:113211), XAF’s functional testing engine, is designed for use in development environments only (not in production). **EasyTest** may load external assemblies, use test databases, execute built-in and custom commands, and do other things not suitable for production environments. 

### Loading Assemblies Dynamically  

We recommend that you carefully review the code that loads assemblies and external data from the file system, network, a database, and other locations. Consider if users can intercept information.

<!--TODO: see if .NET replacement is necessary here -->

### Direct SQL in Middle Tier Security 

If your app uses XPO-based Middle Tier Security, the client may execute SQL scripts on a remote database server. A way to enable this functionality is described in the following article: [Execute Direct SQL Queries in Integrated Mode and with Middle Tier Security](xref:118741). XAF disables this functionality by default for security reasons. We recommend that you enable it only when no other options exist. 

If your app uses EF Core-based Middle Tier Security, this functionality is not available. We decided that such implementation would go against the latest security standards. (The standards changed since we implemented a similar feature in XPO many years ago.)

## Diagnostic / Tracing Information (Logs and Error Messaging) 

**XAF UI v23.2+** and **Web API Service v23.2+** do not store sensitive information (such as passwords) in log files. For more information and configuration options, review the following articles: 

- [v23.2 - Sensitive data is removed from log files](https://supportcenter.devexpress.com/ticket/details/t1182871/core-sensitive-data-is-removed-from-log-files)
- [Log Files](xref:112575)  

XAF apps also remove password information from the `XafApplication.ConnectionString` property value. As such, sensitive information is not exposed in logs, error messages, and so on. 

When your XAF UI app is ready for production, build it in Release mode. If built and run in this configuration, the application does not expose any information about API calls, error messages, and internal application structure. Diagnostic information is only available to developers in Debug mode. 

You can customize how the app displays error information to end-users in debug and release modes. For more information, refer to the following documents: 

- [ExceptionService](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService) (Blazor) 
- [HandleException](xref:DevExpress.ExpressApp.Win.WinApplication.HandleException(System.Exception)) (WinForms) 

## Storing Secrets in Version Control and CI/CD Systems

In your CI/CD development routines, you may store "secrets" in version control systems. A secret may be a private NuGet feed URL. For instance, DevExpress customers can use personalized URLs to access **NuGet.DevExpress.com** - a private NuGet server. Another example of a secret is a password for your database connection string. 

The “shift left” security initiative argues against secret storage in version control systems.  Many CI/CD systems include built-in mechanisms to store sensitive information. For instance, the following help topic describes a secure solution for Azure DevOps. In this example, your _NuGet.config_ contains a placeholder URL (no sensitive information). Azure DevOps securely stores your NuGet feed key as a password.

[Install DevExpress NuGet Packages: Azure DevOps](xref:400604#azure-devops)

Docker implements similar mechanisms for safe storage of sensitive information. Review the following example. It shows how to store your DevExpress NuGet feed URL and a database connection string password securely. 

[Use Azure Kubernetes Service to deploy and scale an XAF Blazor Server app: Build Docker Image](https://github.com/DevExpress/XAF-Blazor-Kubernetes-example#3-build-a-docker-image)  

We at DevExpress also rely on Azure and various vaults to store secrets and configure our virtual machines to have limited privileges by default.  
