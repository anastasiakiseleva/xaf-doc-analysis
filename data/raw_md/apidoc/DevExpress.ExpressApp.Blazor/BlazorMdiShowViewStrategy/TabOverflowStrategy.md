---
uid: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.TabOverflowStrategy
name: TabOverflowStrategy
type: Property
summary: Specifies how to handle overflowing tabs when the number of tabs reaches @DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.MaxTabLimit.
syntax:
  content: public static TabOverflowStrategy TabOverflowStrategy { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.TabOverflowStrategy
    description: The tab overflow strategy.
defaultMemberValue: 'BlockNewTab'
seealso: []
---
You can specify the `TabOverflowStrategy` property as follows: 

# [SolutionName.Blazor.Server\Program.cs](#tab/tabid-csharp)
 
```csharp
public static int Main(string[] args) {
    BlazorMdiShowViewStrategy.MaxTabLimit = 5;
    BlazorMdiShowViewStrategy.TabOverflowStrategy = TabOverflowStrategy.CloseLeastRecentTab;
    // ...
```
 
***