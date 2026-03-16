---
uid: DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode
name: DatabaseUpdateMode
type: Property
summary: Specifies the database update mode.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(DatabaseUpdateMode.UpdateOldDatabase)]
    public DatabaseUpdateMode DatabaseUpdateMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DatabaseUpdateMode
    description: Update mode.
seealso:
- linkId: "113239"
---
Use this property to specify when the application database should be updated: at every application run, when its version is older than the application version, or never (manually).

The DevExpress [Template Kit](xref:405447) sets the `DatabaseUpdateMode` property for new applications to the `UpdateDatabaseAlways` value in Debug mode.

# [SolutionName.Blazor.Server\BlazorApplication.cs](#tab/tabid-blazor)
 
```csharp
protected override void OnSetupStarted() {
    base.OnSetupStarted();
    if(System.Diagnostics.Debugger.IsAttached && CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
        DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
    }
    // ...
```
 
# [SolutionName.Win\Startup.cs](#tab/tabid-win)
 
```csharp
builder.AddBuildStep(application => {
    application.ConnectionString = connectionString;
    if(System.Diagnostics.Debugger.IsAttached && application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
        application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
    }
    // ...
```
 
***

If your application includes [Middle Tier Application Server](xref:404640), the server application must update the database. Updating from client applications must be disabled. 

For new applications with a Middle Tier Server, the [Template Kit](xref:405447) disables the autoupdate in client applications and enables it in the Middle Tier server application.

# [SolutionName.MiddleTier\Startup.cs](#tab/tabid-mt)
 
```csharp
builder.AddBuildStep(application => {
    if (application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
        application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
        // ...
```

# [SolutionName.Blazor.Server\BlazorApplication.cs](#tab/tabid-blazor1)
 
```csharp
protected override void OnSetupStarted() {
    base.OnSetupStarted();
    DatabaseUpdateMode = DatabaseUpdateMode.Never;
}
```
 
# [SolutionName.Win\Startup.cs](#tab/tabid-win1)
 
```csharp
builder.AddBuildStep(application => {
    application.DatabaseUpdateMode = DatabaseUpdateMode.Never;
});
```
 
***