---
uid: DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor.SchedulerStorageService
name: SchedulerStorageService
type: Property
summary: A service that creates a @DevExpress.Blazor.DxSchedulerDataStorage object.
syntax:
  content: public ISchedulerStorageService SchedulerStorageService { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Scheduler.Blazor.ISchedulerStorageService
    description: An @DevExpress.ExpressApp.Scheduler.Blazor.ISchedulerStorageService object.
seealso: []
---

To access and customize a @DevExpress.Blazor.DxSchedulerDataStorage object, we recommend that you use the technique demonstrated in the following example: [XAF - How to Display an Event with Custom Fields in a Scheduler List View](https://github.com/DevExpress-Examples/xaf-how-to-display-an-event-with-custom-fields-in-a-scheduler-list-view).

Alternatively, you can implement your own `ISchedulerStorageService` or inherit from `SchedulerStorageService` as demonstrated in the following code sample:

```csharp
using System;
using DevExpress.Blazor;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Scheduler.Blazor;
using DevExpress.ExpressApp.Services.Localization;
using Microsoft.Extensions.Options;
using YourApplicationName.Module.BusinessObjects;

namespace YourApplicationName.Blazor.Server;

public class CustomSchedulerStorageService: SchedulerStorageService {
    public CustomSchedulerStorageService(IServiceProvider serviceProvider, 
    ICaptionHelperProvider captionHelperProvider, IOptions<SchedulerOptions> schedulerOptions) : base(serviceProvider, captionHelperProvider, schedulerOptions) { }

    protected override DxSchedulerDataStorage CreateSchedulerDataStorageCore(ITypeInfo typeInfo) {
        var schedulerStorage = base.CreateSchedulerDataStorageCore(typeInfo);
        if(typeInfo.Type == typeof(CustomEvent)) {
            ((DxSchedulerAppointmentLabelItem[])schedulerStorage.AppointmentLabelsSource)[0].Caption = "Custom";
        }
    
        return schedulerStorage;
    }
}
```
[`DxSchedulerAppointmentLabelItem`]: xref:DevExpress.Blazor.DxSchedulerAppointmentLabelItem

Use the `services` parameter of the `Startup.ConfigureServices` method in the _YourApplicationName.Blazor.Server\Startup.cs_ file to register your custom `SchedulerStorageService`:

```csharp
//...
using YourApplicationName.Blazor.Server.Services;

namespace YourApplicationName.Blazor.Server;

public class Startup {
    
    // ...

    public void ConfigureServices(IServiceCollection services) {
        // The default code.
        services.AddScoped<ISchedulerStorageService, CustomSchedulerStorageService>();
    }
    //...
}
```