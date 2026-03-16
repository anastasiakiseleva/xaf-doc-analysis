---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.CloseRunningApplications
name: CloseRunningApplications()
type: Method
summary: Closes all the applications started before. Must be called after test execution.
syntax:
  content: public void CloseRunningApplications()
seealso: []
---
After test execution, call the **CloseRunningApplications** method to close the started applications.

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
