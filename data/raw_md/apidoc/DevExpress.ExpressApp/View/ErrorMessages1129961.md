---
uid: DevExpress.ExpressApp.View.ErrorMessages
name: ErrorMessages
type: Property
summary: Allows access to the current [](xref:DevExpress.ExpressApp.View)'s message collection.
syntax:
  content: public ErrorMessages ErrorMessages { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.ErrorMessages
    description: An `ErrorMessages` object which is used to access the messages.
seealso: []
---
Each message contains an image and text associated with a specific property name. For example, the following code snippet adds a tooltip to the `Email` property in an XAF ASP.NET Core Blazor application:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using MySolution.Module.BusinessObjects;
namespace MySolution.Blazor.Server;
public class ErrorMessageController : ObjectViewController<DetailView, Employee> {
    protected override void OnActivated() {
        base.OnActivated();
        View.ErrorMessages.AddMessage(nameof(Employee.Email),
        View.CurrentObject,
        "Example: your@email.com");
    }
}
```
***

The following image demonstrates the result in an ASP.NET Core Blazor application:

![|XAF ASP.NET Core Blazor -- Message Associated with a Specific Property, DevExpress](~/images/blazor-property-specific-message-devexpress.png)

The [Validation Module](xref:113684)'s `ResultsHighlightController` uses the  `ErrorMessages` property. For more information, refer to the following topic: [](xref:113142).