---
uid: DevExpress.ExpressApp.WebApi.Services.WebApiOptions.UseResourceDelta
name: UseResourceDelta
type: Property
summary: Specifies the type Web API uses to track EF Core and non-persistent object changes.
syntax:
  content: public bool UseResourceDelta { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to use the `DevExpress.ExpressApp.WebApi.EFCore.ResourceDelta<T>` type;<br/>`false` to use the `Microsoft.AspNetCore.OData.Deltas.Delta<T>` type.'
seealso: []
---
XAF Web API Service uses the `DevExpress.ExpressApp.WebApi.EFCore.ResourceDelta<T>` class to track changes in EF Core and non-persistent objects. Disable the `UseResourceDelta` property to use the standard [`Delta<T>`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.odata.deltas.delta-1) class instead. In this case, some complex update scenarios, such as [Deep Update](xref:405468), may cause runtime exceptions.

# [SolutionName.WebApi\Startup.cs](#tab/tabid-csharp)
 
```csharp
builder.AddXafWebApi(webApiBuilder => {
    webApiBuilder.ConfigureOptions(options => {
        options.UseResourceDelta = false;
        // ... Other options
    });
});
```
 
***