---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.DropDB(System.String)
name: DropDB(String)
type: Method
summary: Deletes the specified database. This method can potentially destroy a lot of valuable data and should be used with caution.
syntax:
  content: public void DropDB(string dbName)
  parameters:
  - id: dbName
    type: System.String
    description: A deleted database's name.
seealso: []
---
The database name must be registered with the [](xref:DevExpress.EasyTest.Framework.EasyTestFixtureContext.RegisterDatabases(DevExpress.EasyTest.Framework.IEasyTestDatabaseOptions[])) method.

Call the **DropDB** method before running an application.

# [C#](#tab/tabid-csharp1)
 
```csharp
public void Test() { 
    FixtureContext.DropDB(MainDemoDBName); 
    var appContext = FixtureContext.CreateApplicationContext(BlazorAppName); 
    appContext.RunApplication(); 
    // 
} 
```
***