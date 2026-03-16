---
uid: DevExpress.ExpressApp.MessageOptions.CancelDelegate
name: CancelDelegate
type: Property
summary: Specifies a delegate that is executed on a **Cancel** button click in WinForms applications or close button click in ASP.NET Core Blazor applications.
syntax:
  content: public Action CancelDelegate { get; set; }
  parameters: []
  return:
    type: System.Action
    description: A [](xref:System.Action) that is executed on a **Cancel** button click.
seealso: []
---
### WinForms UI

This parameter is supported in WinForms applications when the [WinMessageOptions.Type](xref:DevExpress.ExpressApp.WinMessageOptions.Type) property set to **Flyout**. The code snippet below demonstrates how to use this property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
public class ProjectTaskController : ViewController {
    //…
    MessageOptions options = new MessageOptions();
    options.CancelDelegate = () => {
        //Place here your code that is executed on a Cancel button click.
    };
    //…
    Application.ShowViewStrategy.ShowMessage(options);
}
```
***

### ASP.NET Core Blazor UI

Use the **CancelDelegate** property to specify a delegate that is executed when a user clicks the notification's close button.