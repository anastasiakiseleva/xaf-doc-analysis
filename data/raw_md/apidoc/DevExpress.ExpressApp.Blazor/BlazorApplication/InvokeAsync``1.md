---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync``1(System.Func{System.Threading.Tasks.Task{``0}})
name: InvokeAsync<T>(Func<Task<T>>)
type: Method
summary: Executes code on [Blazor's synchronization context](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/synchronization-context).
syntax:
  content: public virtual Task<T> InvokeAsync<T>(Func<Task<T>> func)
  parameters:
  - id: func
    type: System.Func{System.Threading.Tasks.Task{{T}}}
    description: A delegate to invoke on Blazor's synchronization context.
  typeParameters:
  - id: T
    description: The type of the result produced by a task that the delegate function returns.
  return:
    type: System.Threading.Tasks.Task{{T}}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) object.
seealso:
- linkId: "405253"
---

The following code snippet demonstrates how to use this `InvokeAsync` method overload:

```csharp
using DevExpress.ExpressApp.Blazor;
// ...
var result = await blazorApplication.InvokeAsync(async () => {
    var message = await GetMessageAsync();
    return message;
});
```

[!include[blazor-application-invoke-async-extended-description](~/templates/blazor-application-invoke-async-extended-description.md)]