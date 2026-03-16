---
uid: DevExpress.EasyTest.Framework.DatabaseOptions
name: DatabaseOptions
type: Class
summary: Stores database configuration options for a tested application.
syntax:
  content: 'public class DatabaseOptions : IEasyTestDatabaseOptions'
seealso:
- linkId: DevExpress.EasyTest.Framework.DatabaseOptions._members
  altText: DatabaseOptions Members
---
Use the [](xref:DevExpress.EasyTest.Framework.DatabaseOptions.#ctor(System.String,System.String,System.String,System.String,System.String,System.String,System.String,System.String)) constructor to specify database configuration options.

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