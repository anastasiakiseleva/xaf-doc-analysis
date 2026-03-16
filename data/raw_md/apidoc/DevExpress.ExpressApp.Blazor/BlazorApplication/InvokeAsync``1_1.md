---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync``1(System.Func{``0})
name: InvokeAsync<T>(Func<T>)
type: Method
summary: Executes code on [Blazor's synchronization context](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/synchronization-context).
syntax:
  content: public virtual Task<T> InvokeAsync<T>(Func<T> func)
  parameters:
  - id: func
    type: System.Func{{T}}
    description: A delegate to invoke on Blazor's synchronization context.
  typeParameters:
  - id: T
    description: The delegate's return value type.
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
var result = await blazorApplication.InvokeAsync(() => {
    var message = "Message";
    return message;
});
```

[!include[blazor-application-invoke-async-extended-description](~/templates/blazor-application-invoke-async-extended-description.md)]