---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext.RegisterApplications(DevExpress.EasyTest.Framework.IEasyTestApplicationOptions[])
name: RegisterApplications(IEasyTestApplicationOptions[])
type: Method
summary: Registers configurations for tested applications.
syntax:
  content: public void RegisterApplications(params IEasyTestApplicationOptions[] options)
  parameters:
  - id: options
    type: DevExpress.EasyTest.Framework.IEasyTestApplicationOptions[]
    description: An array of application options.
seealso: []
---
The following code snippet registers a Blazor and WinForms application for testing purposes:

# [C#](#tab/tabid-csharp1)
 
```csharp
public class YourSolutionNameTests : IDisposable { 
    const string BlazorAppName = "YourSolutionNameBlazor"; 
    const string WinAppName = "YourSolutionNameWin"; 
    EasyTestFixtureContext FixtureContext { get; } = new EasyTestFixtureContext(); 
    // 
    public YourSolutionNameTests() { 
        FixtureContext.RegisterApplications( 
            new BlazorApplicationOptions(BlazorAppName, string.Format(@"{0}\..\..\..\..\YourSolutionName.Blazor.Server", Environment.CurrentDirectory)), 
            new WinApplicationOptions(WinAppName, string.Format(@"{0}\..\..\..\..\YourSolutionName.Win\bin\EasyTest\net8.0-windows\YourSolutionName.Win.exe", Environment.CurrentDirectory)) 
        ); 
        // 
    } 
    // 
} 
```
***