---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.InstantFeedbackMappingMode
name: InstantFeedbackMappingMode
type: Property
summary: Specifies what properties should be mapped on a grid in [InstantFeedback or InstantFeedbackView](xref:118450) mode for all Object Spaces.
syntax:
  content: public XPInstantFeedbackSourceMappingMode InstantFeedbackMappingMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Xpo.XPInstantFeedbackSourceMappingMode
    description: A properties mapping mode in **InstantFeedback** or **InstantFeedbackView** mode.
seealso: []
---
In **InstantFeedback** and **InstantFeedbackView** modes, all property values are calculated at once regardless of grid columns settings. To calculate values only for visible columns, set the `InstantFeedbackMappingMode` property to @DevExpress.ExpressApp.Xpo.XPInstantFeedbackSourceMappingMode.RequiredProperties as follows:

# [C#](#tab/tabid-csharp)

```csharp
builder.ObjectSpaceProviders
    .AddSecuredXpo((serviceProvider, options) => {
        options.ConfigureObjectSpaceProvider = (objectSpaceProvider, serviceProvider)  => {
            objectSpaceProvider.InstantFeedbackMappingMode = XPInstantFeedbackSourceMappingMode.RequiredProperties;
        };
        // ...
```
***

To map other columns that do not appear in the grid, add them to the collection of displayed options. See the [CollectionSourceBase.DisplayableProperties](xref:DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties) topic for details.

To define which properties the grid should map for a specific View, use the [XPObjectSpace.InstantFeedbackMappingMode](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.InstantFeedbackMappingMode) property in the target Object Space.