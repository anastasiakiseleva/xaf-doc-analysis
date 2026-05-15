---
uid: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.MaxTabLimit
name: MaxTabLimit
type: Property
summary: Limits the number of opened tabs.
syntax:
  content: public static int MaxTabLimit { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: The maximum number of opened tabs.
seealso: []
defaultMemberValue: '10'
---
You can specify the `MaxTabLimit` property as follows: 

# [SolutionName.Blazor.Server\Program.cs](#tab/tabid-csharp)
 
```csharp
public static int Main(string[] args) {
    BlazorMdiShowViewStrategy.MaxTabLimit = 5;
    BlazorMdiShowViewStrategy.TabOverflowStrategy = TabOverflowStrategy.CloseLeastRecentTab;
    // ...
```
 
***

When the @DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.TabOverflowStrategy property is set to `UnloadLeastRecentTab` or `CloseLeastRecentTab`, the total number of tabs can exceed the limit if the oldest tabs have unsaved changes. Such tabs are not unloaded or closed.