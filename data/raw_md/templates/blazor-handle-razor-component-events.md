Razor components usually have events implemented as properties of the [EventCallback\<T\>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.eventcallback-1) type. Examples include [DxTextBox.TextChanged](xref:DevExpress.Blazor.DxTextBox.TextChanged) or [InputBase.ValueChanged](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.forms.inputbase-1.valuechanged).

XAF can handle some of these events. To safely add your own event handler without overriding the default XAF implementation, we recommend that you use the following pattern:

```csharp
var defaultEventHandler = ComponentModel.SomeEvent;
ComponentModel.SomeEvent = EventCallback.Factory.Create<TArgument>(this, async eventArgument => {
    // Comment out the line below if you do not want XAF to handle this event.
    await defaultEventHandler.InvokeAsync(eventArgument);

    // Implement your custom logic here.
    // ...
});
```

See also:

* [EventCallback | ASP.NET Core Blazor event handling](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)