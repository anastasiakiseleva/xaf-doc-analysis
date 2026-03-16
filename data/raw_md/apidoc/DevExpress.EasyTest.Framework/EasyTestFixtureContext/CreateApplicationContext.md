---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.CreateApplicationContext(System.String)
name: CreateApplicationContext(String)
type: Method
summary: Creates a context for a new application.
syntax:
  content: public IApplicationContext CreateApplicationContext(string applicationName)
  parameters:
  - id: applicationName
    type: System.String
    description: The application name
  return:
    type: DevExpress.EasyTest.Framework.IApplicationContext
    description: The application context.
seealso: []
---
After test execution, call the @DevExpress.EasyTest.Framework.EasyTestFixtureContext.CloseRunningApplications method to close the started applications.

# [C#](#tab/tabid-csharp1)
 
```csharp
[Fact]
public void Test() { 
    var appContext = FixtureContext.CreateApplicationContext(BlazorAppName); 
    appContext.RunApplication(); 
    // 
} 
public void Dispose() { 
    FixtureContext.CloseRunningApplications(); 
}
```
***
