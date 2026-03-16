---
uid: DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.Core.IObjectSpaceProviderService,DevExpress.ExpressApp.Core.IObjectSpaceCustomizerService)
name: PopulateAdditionalObjectSpaces(IObjectSpaceProviderService, IObjectSpaceCustomizerService)
type: Method
summary: Creates Object Spaces for registered Object Space Providers and adds them to the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection. Object Spaces in this collection are automatically disposed of with the owner Object Space.
syntax:
  content: public void PopulateAdditionalObjectSpaces(IObjectSpaceProviderService objectSpaceProvider, IObjectSpaceCustomizerService objectSpaceCustomizerService)
  parameters:
  - id: objectSpaceProvider
    type: DevExpress.ExpressApp.Core.IObjectSpaceProviderService
    description: An object that implements the `IObjectSpaceProviderService` interface.
  - id: objectSpaceCustomizerService
    type: DevExpress.ExpressApp.Core.IObjectSpaceCustomizerService
    description: An object that implements the `IObjectSpaceCustomizerService` interface.
seealso: []
---

The following code sample demonstrates how to use this method:

# [C#](#tab/tabid-csharp)

```csharp
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var objectSpaceProviderService = serviceProvider.GetRequiredService<IObjectSpaceProviderService>();
var objectSpaceCustomizerService = serviceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
objectSpace.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider