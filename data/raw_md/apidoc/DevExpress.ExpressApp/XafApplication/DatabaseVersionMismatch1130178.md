---
uid: DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch
name: DatabaseVersionMismatch
type: Event
summary: Occurs when the database should be synchronized with the application version.
syntax:
  content: public event EventHandler<DatabaseVersionMismatchEventArgs> DatabaseVersionMismatch
seealso:
- linkId: "112691"
- linkId: 113239#how-database-is-updated-in-debug-mode
  altText: How a Database is Updated in Debug Mode
---
XAF checks database and application compatibility when the application accesses the database. After checking, the `DatabaseVersionMismatch` event fires in the following cases:

* The database cannot be opened.  
   The @DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.CompatibilityError property returns `CompatibilityUnableToOpenDatabaseError`.
* The database version is older than the application version.  
   The @DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.CompatibilityError property returns `CompatibilityDatabaseIsOldError`.
* The @DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode property is set to `UpdateDatabaseAlways`.  
   The @DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.CompatibilityError property returns `null`.

Handle this event to update the database. Use the @DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.Updater parameter to access the Database Updater object. Set the @System.ComponentModel.HandledEventArgs.Handled parameter to `true`, to prevent other database version updates.

The DevExpress [Template Kit](xref:405447) handles the `DatabaseVersionMismatch` event in new Blazor, Web API, and WinForms projects to keep the application and database versions synchronized. If the database version is older than the application's version, the event triggers at startup, and the handler runs the Database Updater's `Update` method. Rewrite this event handler if you need to implement custom logic.

# [SolutionName.Blazor.Server\BlazorApplication.cs](#tab/tabid-Blazor)

```csharp
public class SolutionNameBlazorApplication : BlazorApplication {
    public SolutionNameBlazorApplication() {
       DatabaseVersionMismatch += SolutionNameBlazorApplication_DatabaseVersionMismatch;
       // ...
    }
    void SolutionNameBlazorApplication_DatabaseVersionMismatch(object sender, DatabaseVersionMismatchEventArgs e) {
       e.Updater.Update();
       e.Handled = true;
       // ...

```

# [SolutionName.WebApi\Startup.cs](#tab/tabid-WebAPI)

```csharp
public class Startup {
   public void ConfigureServices(IServiceCollection services) {
      services.AddXafWebApi(builder => {
            builder.AddBuildStep(application => {
               // ...
               if(System.Diagnostics.Debugger.IsAttached && application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
                  application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
                  application.DatabaseVersionMismatch += (s, e) => {
                        e.Updater.Update();
                        e.Handled = true;
                  };
               }
            });
         // ...

```

# [SolutionName.Win\WinApplication.cs](#tab/tabid-WinForms)

```csharp
public class SolutionNameWindowsFormsApplication : WinApplication {
   public SolutionNameWindowsFormsApplication() {
      DatabaseVersionMismatch += SolutionNameWindowsFormsApplication_DatabaseVersionMismatch;
      // ...
   }
   void SolutionNameWindowsFormsApplication_DatabaseVersionMismatch(object sender, DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs e) {
      e.Updater.Update();
      e.Handled = true;
      // ...
```

***

> [!important]
> If the application includes the [Middle Tier Server Application](xref:113439), the compatibility check must be performed at the server side. Client applications (Blazor, Web API, and WinForms) should throw an exception when the `DatabaseVersionMismatch` event occurs.

When you use the [Template Kit](xref:405447) to create an application with a Middle Tier Security server, the kit handles the `DatabaseVersionMismatch` event in the Middle Tier Application.

# [MiddleTier](#tab/tabid-middletier)

```csharp
// File: SolutionName.MiddleTier\Startup.cs
builder.AddBuildStep(application => {
   application.CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
   if (application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
      application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
      application.DatabaseVersionMismatch += (s, e) => {
            e.Updater.Update();
            e.Handled = true;
      };
   }
   //...
```
***

The `DatabaseVersionMismatch` event does not occur if you handle the @DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility event.