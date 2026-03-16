---
uid: DevExpress.EasyTest.Framework.EasyTestFixtureContext
name: EasyTestFixtureContext
type: Class
summary: A test fixture context.
syntax:
  content: 'public class EasyTestFixtureContext : IDisposable'
seealso:
- linkId: DevExpress.EasyTest.Framework.EasyTestFixtureContext._members
  altText: EasyTestFixtureContext Members
---
To create a fixture context, call the static [EasyTestFixtureContext.CreateApplicationContext](xref:DevExpress.EasyTest.Framework.EasyTestFixtureContext.CreateApplicationContext(System.String)) method.

# [C#](#tab/tabid-csharp1)
 
```csharp
[Fact]
public void Test() { 
    var appContext = FixtureContext.CreateApplicationContext(BlazorAppName); 
    appContext.RunApplication(); 
    // 
} 
```
***
