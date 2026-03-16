---
uid: DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor.ViewTypes
name: ViewTypes
type: Property
summary: View Types that the Scheduler uses to display its data.
syntax:
  content: public IEnumerable<SchedulerViewType> ViewTypes { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.Blazor.SchedulerViewType}
    description: A @DevExpress.Blazor.SchedulerViewType enumeration type that specifies the Scheduler View type.
seealso: []
---

The following code snippet specifies `Day` and `Week` View Types for an individual View:

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler.Blazor.Editors;
using DevExpress.Persistent.Base.General;

namespace YourApplicationName.Blazor.Server.Controllers;

public class SchedulerViewTypesCustomizationController : ObjectViewController<ListView, IEvent> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is SchedulerListEditor schedulerListEditor) {
            schedulerListEditor.ViewTypes = new[] {
                    SchedulerViewType.Day,
                    SchedulerViewType.Week,
            };
        }
    }
}
```