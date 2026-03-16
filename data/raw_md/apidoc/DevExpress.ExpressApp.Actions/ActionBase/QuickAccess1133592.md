---
uid: DevExpress.ExpressApp.Actions.ActionBase.QuickAccess
name: QuickAccess
type: Property
summary: Specifies whether the current Action is accessible via the Quick Access Toolbar (this toolbar is available when the Ribbon UI is used).
syntax:
  content: |-
    [DefaultValue(false)]
    public bool QuickAccess { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, when the Action is accessible via the Quick Access Toolbar; otherwise - **false**.'
seealso: []
---
The code below demonstrates how to add the **New** [Action](xref:112622) to the [Quick Access Toolbar](xref:2496).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

// ...
public class NewObjectActionController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        NewObjectViewController newObjectViewController = Window.GetController<NewObjectViewController>();
        if(newObjectViewController != null) {
            newObjectViewController.NewObjectAction.QuickAccess = true;
        }
    }
}
```
***

The following image illustrates the **New** Action, accessible via the Quick Access Toolbar.

![QuickAccessToolbar](~/images/quickaccesstoolbar116629.png)

The Quick Access Toolbar can be located either above or below the Ribbon. Its default location is above the Ribbon. The location can be changed via the toolbar's context menu:

![QuickAccessToolbar2](~/images/quickaccesstoolbar2116632.png)
> [!NOTE]
> The Ribbon UI can be enabled in the Windows Forms application via the [Model Editor](xref:112582). To enable the Ribbon UI, set the **Options** node's [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Ribbon**.

