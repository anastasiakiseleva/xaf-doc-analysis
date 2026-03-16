---
uid: DevExpress.ExpressApp.XafApplication.LinkNewObjectToParentImmediately
name: LinkNewObjectToParentImmediately
type: Property
summary: Specifies whether or not a link between a master and child object is created immediately when the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) is executed in a nested List View with a non-aggregated collection.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(false)]
    public bool LinkNewObjectToParentImmediately { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if the link between a master and child object is created when the child object is committed; `false` if the link is created when the parent is committed.'
seealso: []
---
Since v20.2, the default `LinkNewObjectToParentImmediately` property value is `false` because the [Template Kit](xref:405447) generates new projects with the [FrameworkSettings.DefaultSettingsCompatibilityMode](xref:DevExpress.ExpressApp.FrameworkSettings.DefaultSettingsCompatibilityMode) property set to `Latest`.

The table below shows how the **New** Action behavior changes in a nested List View with a _non-aggregated_ collection depending on the `LinkNewObjectToParentImmediately` value.

| Value | Description |
|---|---|
| `true` | The new object linked to the master object is created and the master object is committed when the **New** Action is executed. The reference to the master object is available in the new child object immediately after creation. |
| `false` | The master object is not committed and the link is not created when the **New** Action is executed. The reference to the master object is not added to the new child object immediately. The link is created later when the child object is committed. To persist the link, a user should also save the master object. Otherwise, the unlinked child object is saved. |

To change the behavior for an entire application, set the `LinkNewObjectToParentImmediately` property in your [application project](xref:118045)'s @DevExpress.ExpressApp.XafApplication ([](xref:DevExpress.ExpressApp.Win.WinApplication) or [](xref:DevExpress.ExpressApp.Blazor.BlazorApplication)) descendant class constructor. 

# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            LinkNewObjectToParentImmediately = true;
        }
        // ...
    }
}

```
***

To change the behavior for a specific [View](xref:112611), set the [NewObjectViewController.LinkNewObjectToParentImmediately](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.LinkNewObjectToParentImmediately) property in a [Controller](xref:112621) that targets the View. The behavior of aggregated collections is not changed.

[!include[new-action-hidden-in-many-to-many-collection](~/templates/new-action-hidden-in-many-to-many-collection.md)]

> [!TIP]
> This property is hidden in the Application Designer. You can use it in code only.
