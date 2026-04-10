[Blazor's synchronization context](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/synchronization-context) implements a single-threaded model of execution. At any point in time, only one thread can execute code. XAF Blazor relies on this model. To safely invoke XAF code, this code must be executed on Blazor's synchronization context. Otherwise, the code will be prone to race conditions that can cause security issues, data loss, or other undesirable behavior.

### Error handling

If the delegate code throws an `IUserFriendlyException`, the user receives a user-friendly error notification, but the exception does not propagate to the caller method:

```csharp
using DevExpress.ExpressApp.Blazor;
// ...
async Task CallerMethod() {
    // Does not raise an exception.
    await blazorApplication.InvokeAsync(() => {
        // "An error occurred" message will be shown to the user.
        throw new UserFriendlyException("An error occurred");
    });
}
```

If any other type of exception is thrown, the user's application instance will crash, and the exception will be rethrown at the call site:

```csharp
using DevExpress.ExpressApp.Blazor;
// ...
async Task CallerMethod() {
    // Raises an InvalidOperationException.
    await blazorApplication.InvokeAsync(() => {
        // Crashes the user's application instance.
        throw new InvalidOperationException();
    });
}
```

To avoid crashing a user's application, wrap the delegate code with a `try-catch` block and handle the exceptions in the desired manner.

### Execution context

When your code calls `InvokeAsync`, XAF temporarily restores the [ExecutionContext](https://learn.microsoft.com/en-us/dotnet/api/system.threading.executioncontext) associated with a [BlazorApplication](xref:DevExpress.ExpressApp.Blazor.BlazorApplication) instance. This restoration has the following implications:

- [ValueManager](xref:DevExpress.Persistent.Base.ValueManager) can access data stored by the application.
- [Localized messages](xref:403669#caption-helper) are displayed in the user's selected language.
- [`AsyncLocal<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.asynclocal-1) values are restored to the state they were in when `ExecutionContext` was captured:

    ```csharp
    using System;
    using DevExpress.ExpressApp.Blazor;
    // ...
    static AsyncLocal<string> AsyncLocal { get; } = new();
    async Task CallerMethod() {
        AsyncLocal.Value = "not null";
        await blazorApplication.InvokeAsync(() => {
            Console.WriteLine(AsyncLocal.Value ?? "null"); // Prints `null`.
        });
    }
    ```

### Pitfalls

While Blazor's synchronization context guarantees single-threaded code execution, the order of operations is not guaranteed. Consider the following situation:

```csharp
using DevExpress.ExpressApp.Blazor;
// ...
if (View.CurrentObject is Order order) {
    var newDeliveryDate = await OrderTrackingService.CalculateDeliveryDate(order);
    order.DeliveryDate = newDeliveryDate; // May throw an `ObjectDisposedException`.
}
```

The user may navigate away from the current View before the new delivery date is assigned to the `order` object. In this case, the assignment statement fails with an `ObjectDisposedException`.

To avoid similar issues, validate the application state across `await` points. You can also use APIs such as [TaskCompletionSource](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcompletionsource) and [CancellationTokenSource](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtokensource) to signal when an asynchronous operation should proceed or be canceled.