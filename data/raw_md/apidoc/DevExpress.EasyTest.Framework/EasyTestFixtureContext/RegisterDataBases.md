---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.RegisterDatabases(DevExpress.EasyTest.Framework.IEasyTestDatabaseOptions[])
name: RegisterDatabases(IEasyTestDatabaseOptions[])
type: Method
summary: Registers a set of data sources used for the testing purposes.
syntax:
  content: public void RegisterDatabases(params IEasyTestDatabaseOptions[] options)
  parameters:
  - id: options
    type: DevExpress.EasyTest.Framework.IEasyTestDatabaseOptions[]
    description: An array of data sources used to test XAF applications.
seealso: []
---
Databases registered in this method can be used in @DevExpress.EasyTest.Framework.EasyTestFixtureContext.RestoreDB(System.String) and @DevExpress.EasyTest.Framework.EasyTestFixtureContext.DropDB(System.String) methods.

# [C#](#tab/tabid-csharp1)
 
```csharp
public class YourSolutionNameTests : IDisposable {
    const string AppDBName = "YourSolutionName";
    EasyTestFixtureContext FixtureContext { get; } = new EasyTestFixtureContext();
 
    public YourSolutionNameTests() {
        FixtureContext.RegisterDatabases(new DatabaseOptions(AppDBName, "YourSolutionNameEasyTest", server: @"(localdb)\mssqllocaldb"));
        //
    }
    //
}
```
***