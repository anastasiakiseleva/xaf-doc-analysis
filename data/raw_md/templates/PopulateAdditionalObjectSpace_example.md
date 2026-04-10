1. Handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code in the application's `Startup.cs` file.
2. In the event handler, call the @DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.Core.IObjectSpaceProviderService,DevExpress.ExpressApp.Core.IObjectSpaceCustomizerService) method to populate the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection with <:0:>.

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
//...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    CompositeObjectSpace compositeObjectSpace = context.ObjectSpace as CompositeObjectSpace;
    if (compositeObjectSpace != null) {
        if (!(compositeObjectSpace.Owner is CompositeObjectSpace)) {
            var objectSpaceProviderService = context.ServiceProvider.GetRequiredService<IObjectSpaceProviderService>();
            var objectSpaceCustomizerService = context.ServiceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
            compositeObjectSpace.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
        }
    }
}
```

***

[`/\.(ObjectSpaceCreated)/`]: xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
[`CompositeObjectSpace`]: xref:DevExpress.ExpressApp.CompositeObjectSpace 
[`Owner`]: xref:DevExpress.ExpressApp.IObjectSpace.Owner
[`PopulateAdditionalObjectSpaces`]: xref:DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.XafApplication)
[`ObjectSpaceCreatedEventArgs`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs
