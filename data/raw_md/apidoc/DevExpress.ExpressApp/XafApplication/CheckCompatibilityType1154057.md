---
uid: DevExpress.ExpressApp.XafApplication.CheckCompatibilityType
name: CheckCompatibilityType
type: Property
summary: Specifies how database and application compatibility is checked.
syntax:
  content: |-
    [DefaultValue(CheckCompatibilityType.ModuleInfo)]
    public CheckCompatibilityType CheckCompatibilityType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.CheckCompatibilityType
    description: A value that specifies how database and application compatibility is checked.
seealso:
- linkId: 113239#how-database-is-updated-in-debug-mode
  altText: How Database is Updated in Debug Mode
---
The XAF application template is designed to create a database when the application is run for the first time and to update that application as new versions of it are released. Use the `CheckCompatibilityType` property to specify how database and application compatibility is checked.

You can use the following properties to specify the compatibility type individually for each Object Space Provider; for instance, in cases where you [use multiple databases](https://supportcenter.devexpress.com/ticket/details/e4896/how-to-connect-different-data-models-to-several-databases-within-a-single-application):
* [IObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.IObjectSpaceProvider.CheckCompatibilityType)
* [EFCoreObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1.CheckCompatibilityType)
* [XPObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.CheckCompatibilityType)

### DatabaseSchema Type

When the `CheckCompatibilityType` property is set to `DatabaseSchema`, XAF ensures that the database schema matches the business model. In particular, XAF checks to ensure that:

  * the database exists
  * all required tables exist
  * all required columns exist

  The @DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch event occurs if any of these checks fails. The DevExpress [Template Kit](xref:405447) handles this event in new Blazor, Web API, and WinForms projects to keep the application and database versions synchronized as follows:
  * If the database does not exist, XAF creates the database and required tables.
  * If the database exists, but it is empty, XAF creates the tables.
  * If a column does not exist, XAF adds it to the table.

The [Template Kit](xref:405447) sets the `CheckCompatibilityType` property to `DatabaseSchema` in new applications:

# [Blazor](#tab/tabid-Blazor)
 
```csharp
// File: SolutionName.Blazor.Server\BlazorApplication.cs
public class SolutionNameBlazorApplication : BlazorApplication {
    public SolutionNameBlazorApplication() {
        CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
        // ...
```
 
# [WinForms](#tab/tabid-Win)
 
```csharp
// File: SolutionName.Win\WinApplication.cs
public class SolutionNameWindowsFormsApplication : WinApplication {
    public SolutionNameWindowsFormsApplication() {
        CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
        // ...
```

# [WebApi](#tab/tabid-api)
 
```csharp
// File: SolutionName.WebApi\Startup.cs
builder.AddBuildStep(application => {
    application.CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
    // ...
```

# [MiddleTier](#tab/tabid-middletier)
 
```csharp
// File: SolutionName.MiddleTier\Startup.cs
builder.AddBuildStep(application => {
    application.CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
    // ...
```
***

### ModuleInfo Type

[!include[checkcompatibilitytype-moduleinfo](~/templates/checkcompatibilitytype-moduleinfo.md)]

When the `CheckCompatibilityType` property is set to `ModuleInfo`, XAF ensures that the database version matches the application version. In this mode, XAF creates a `ModuleInfo` table in the database to check the compatibility of an application and its database. This table stores information on the module versions used in the application. When XAF checks database and application compatibility, versions stored in the `ModuleInfo` table are compared with existing module versions. The @DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch event occurs in case of a mismatch.

If your application uses Entity Framework Core ORM, register the `ModuleInfo` type in `DbContext`.

# [SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs](#tab/tabid-cs)
 
```cs
public class SolutionNameEFCoreDbContext : DbContext {
    public DbSet<ModuleInfo> ModulesInfo { get; set; }
    // ...
```
***

Each module's default version value is "_1.0.*_" (specified by the [AssemblyVersion](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.assemblyversionattribute) attribute in the _Properties\AssemblyInfo.cs_ file). The asterisk in the version number indicates that build and revision numbers are incremented automatically. XAF updates the version number with each new build. As a result, module versions may become unsynchronized if you build Windows Forms or ASP.NET Core Blazor applications separately (for example, when you create a ClickOnce installation or deploy to IIS).

This mode is more complicated compared to `DatabaseSchema`, but it helps you ensure both business logic and data model compatibility.

#### Compatibility Check Steps

The mechanism XAF uses to check application and database version compatibility, and update the database, consists of the following steps:
1. Compare the application name in the database with the existing application name.  
    If they do not match, the following error message appears: _Database is designed for the 'A' application while you are running the 'B' application._
1. Compare module versions in the database with actual module versions.  
    If the database version is greater than the application version,  the following error message appears: _The database version is greater than the application version. The application needs to be updated._
1. Call the @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema method.
1. Collect all persistent classes. Update database schema.
1. Call the @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema method.
1. Set new module versions in the database.

You can override @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema and @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema methods to modify module database tables, both before and after updating the database schema. For instance, this can be necessary when applying the [Security System](xref:113366) in the application. A user with administrative rights should be added to a database using the `UpdateDatabaseAfterUpdateSchema` method. For details, refer to the following help topics: 

* [Using the Security System](xref:404204)
* [Supply Initial Data](xref:402985)

You can use the @DevExpress.ExpressApp.Updating.ModuleUpdater to implement complex updating logic that takes into account the differences between application versions.