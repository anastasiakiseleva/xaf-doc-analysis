---
uid: "404610"
title: 'How to: Access the Scheduler Control in Code'
owner: Anastasiya Kisialeva
---
# How to: Access the Scheduler Control in Code

To access the control in code, create a [View Controller](xref:112621) and override its `OnActivated` method. Set the Controller's [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) property to `ListView`. This way the Controller is activated for List Views only.

## ASP.NET Core Blazor

[!include[<YourApplicationName.Blazor.Server\Controllers\SchedulerController.cs>](~/templates/platform_specific_file_path.md)]

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler.Blazor;
using DevExpress.ExpressApp.Scheduler.Blazor.Editors;
using DevExpress.Persistent.Base.General;

namespace YourApplicationName.Module.Controllers {
    public partial class SchedulerController : ObjectViewController<ListView, IEvent> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if(View.Editor is SchedulerListEditor schedulerListEditor) {
                // Obtain an instance of the DxSchedulerModel type.
                schedulerListEditor.SchedulerModel.ActiveViewType = DevExpress.Blazor.SchedulerViewType.WorkWeek;
            }
        }
    }
}
```

For more information on how to access the Scheduler control in code, refer to the following examples:
* [XAF - Create Custom Event and Resource Classes for XAF Scheduler](https://github.com/DevExpress-Examples/xaf-how-to-display-an-event-with-custom-fields-in-a-scheduler-list-view/blob/23.1.4%2B/CS/EFCore/ExtendedEvents.Blazor.Server/Controllers/SchedulerCustomFieldMappingsController.cs).
* [XAF - How to Display an Event with Custom Fields in a Scheduler List View](https://github.com/DevExpress-Examples/xaf-how-to-display-an-event-with-custom-fields-in-a-scheduler-list-view/blob/23.1.4%2B/CS/EFCore/ExtendedEvents.Blazor.Server/Controllers/SchedulerCustomFieldMappingsController.cs).

## Windows Forms

[!include[<YourApplicationName.Win\Controllers\SchedulerController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler.Win;
using DevExpress.Persistent.Base.General;
using DevExpress.XtraScheduler;
namespace YourApplicationName.Module.Controllers {
    public partial class SchedulerController : ObjectViewController<ListView, IEvent> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if(View.Editor is SchedulerListEditor schedulerListEditor) {
                SchedulerControl scheduler = schedulerListEditor.SchedulerControl;
            }
        }
    }
}
```
***

> [!NOTE]
> If the `CrossThreadFailure` error occurs when you handle `SchedulerControl` events, set the control's [SchedulerOptionsBehavior.UseAsyncMode](xref:DevExpress.XtraScheduler.SchedulerOptionsBehavior.UseAsyncMode) option to `false`.

For more information on how to access the Scheduler control in code, refer to the following examples:
* [XAF - Create Custom Event and Resource Classes for XAF Scheduler](https://github.com/DevExpress-Examples/xaf-how-to-display-an-event-with-custom-fields-in-a-scheduler-list-view/blob/23.1.4%2B/CS/EFCore/ExtendedEvents.Win/Controllers/SchedulerCustomFieldMappingsController.cs).
* [XAF - How to Display an Event with Custom Fields in a Scheduler List View](https://github.com/DevExpress-Examples/xaf-how-to-display-an-event-with-custom-fields-in-a-scheduler-list-view/blob/23.1.4%2B/CS/EFCore/ExtendedEvents.Win/Controllers/SchedulerCustomFieldMappingsController.cs).

