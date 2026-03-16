---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.RestoreDB(System.String)
name: RestoreDB(String)
type: Method
summary: Restores the specified database from a backup. The database name must be registered with the [](xref:DevExpress.EasyTest.Framework.EasyTestFixtureContext.RegisterDatabases(DevExpress.EasyTest.Framework.IEasyTestDatabaseOptions[])) method.
syntax:
  content: public void RestoreDB(string dbName)
  parameters:
  - id: dbName
    type: System.String
    description: A restored database's name.
seealso: []
---
Call the **RestoreDB** method before running an application.

# [C#](#tab/tabid-csharp1)
 
```csharp
[Fact] 
public void Test() { 
    FixtureContext.RestoreDB(MainDemoDBName); 
    var appContext = FixtureContext.CreateApplicationContext(BlazorAppName); 
    appContext.RunApplication(); 
    // 
} 
```
***