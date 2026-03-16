---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.OptionsCustomization
name: OptionsCustomization
type: Property
summary: Provides access to the scheduler's customization options.
syntax:
  content: public abstract object OptionsCustomization { get; }
  parameters: []
  return:
    type: System.Object
    description: A @DevExpress.XtraScheduler.SchedulerOptionsCustomization object representing the scheduler's customization options.
seealso: []
---
For additional information, refer to the [SchedulerControl.OptionsCustomization](xref:DevExpress.XtraScheduler.SchedulerControl.OptionsCustomization) property description.

You may need to perform an additional cast. The following example demonstrates how to do this:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraScheduler;
// ...
((SchedulerOptionsCustomization)schedulerListEditor.OptionsCustomization).AllowInplaceEditor = UsedAppointmentType.All;
```
***
