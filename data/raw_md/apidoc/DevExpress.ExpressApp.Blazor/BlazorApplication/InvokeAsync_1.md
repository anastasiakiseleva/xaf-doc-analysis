---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync(System.Func{System.Threading.Tasks.Task})
name: InvokeAsync(Func<Task>)
type: Method
summary: Executes code on [Blazor's synchronization context](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/synchronization-context).
syntax:
  content: public virtual Task InvokeAsync(Func<Task> func)
  parameters:
  - id: func
    type: System.Func{System.Threading.Tasks.Task}
    description: A delegate to invoke on Blazor's synchronization context.
  return:
    type: System.Threading.Tasks.Task
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) object.
seealso:
- linkId: "405253"
---

The following code snippet demonstrates how to use this `InvokeAsync` method overload:

```csharp
using DevExpress.ExpressApp.Blazor;
// ...
await blazorApplication.InvokeAsync(async () => {
    var message = await GetMessageAsync();
    blazorApplication.ShowViewStrategy.ShowMessage(message);
});
```

[!include[blazor-application-invoke-async-extended-description](~/templates/blazor-application-invoke-async-extended-description.md)]