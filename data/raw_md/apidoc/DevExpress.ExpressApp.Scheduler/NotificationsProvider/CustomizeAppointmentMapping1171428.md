---
uid: DevExpress.ExpressApp.Scheduler.NotificationsProvider.CustomizeAppointmentMapping
name: CustomizeAppointmentMapping
type: Event
summary: Occurs when the [](xref:DevExpress.ExpressApp.Scheduler.NotificationsProvider) is initialized by the scheduler storage (Windows Forms).
syntax:
  content: public event EventHandler<CustomizeAppointmentMappingEventArgs> CustomizeAppointmentMapping
seealso: []
---
Handle this event to change the list of data source fields that is used in the [](xref:DevExpress.ExpressApp.Scheduler.NotificationsProvider) in your Windows Forms application. To subscribe to `CustomizeAppointmentMapping`, override the `Setup ` method of the _MySolution\Module_ project.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Scheduler;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    //...
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        //...
        NotificationsProvider notificationsProvider = (NotificationsProvider)moduleManager.Modules.FindModule<SchedulerModuleBase>().NotificationsProvider;
        notificationsProvider.CustomizeAppointmentMapping += NotificationsProvider_CustomizeAppointmentMapping;
    }
    private void NotificationsProvider_CustomizeAppointmentMapping(object sender, DevExpress.ExpressApp.Scheduler.CustomizeAppointmentMappingEventArgs e) {
        e.AppointmentMappingInfo.ResourceId = null;
    }
}
```
***

> [!NOTE]
> To customize appointment mappings in an XAF ASP.NET Core Blazor application, use the @DevExpress.ExpressApp.Scheduler.Blazor.SchedulerEvents.OnSchedulerDataStorageCreated event. For more information, refer to the following topic: [](xref:404714#aspnet-core-blazor).