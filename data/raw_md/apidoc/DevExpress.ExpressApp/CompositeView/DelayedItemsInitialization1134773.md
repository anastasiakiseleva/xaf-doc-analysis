---
uid: DevExpress.ExpressApp.CompositeView.DelayedItemsInitialization
name: DelayedItemsInitialization
type: Property
summary: Indicates whether [View Items](xref:112612) controls of the [](xref:DevExpress.ExpressApp.CompositeView) are initialized immediately when the View is created.
syntax:
  content: public bool DelayedItemsInitialization { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if View Item controls are initialized once they are visible to end-users; `false` if View Item controls are initialized once the View is created.'
seealso: []
---
To change this property value, override the `OnActivated` method of a [](xref:DevExpress.ExpressApp.ViewController) descendant.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;

namespace SolutionName.Module.Controllers {
    public class DisablePerformanceOptimizationController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            View.DelayedItemsInitialization = false;
        }
    }
}
```
***

You can also change this setting globally for all Views using the [XafApplication.DelayedViewItemsInitialization](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization) property.
