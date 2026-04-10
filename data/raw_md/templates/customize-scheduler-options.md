```csharp{10-21}
using System.Drawing;
using DevExpress.Blazor;
using DevExpress.ExpressApp.Scheduler.Blazor;

namespace <:0:>.Blazor {
    public class Startup {
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                builder.Modules.AddScheduler(options => {
                    options.Events.OnSchedulerDataStorageCreated = context => {
                        context.SchedulerDataStorage.AppointmentLabelsSource = new DxSchedulerAppointmentLabelItem[] {
                            new DxSchedulerAppointmentLabelItem() { Id = 0, Caption = "Vacation", Color = Color.DeepPink },
                            new DxSchedulerAppointmentLabelItem() { Id = 1, Caption = "Personal", Color = Color.LightSeaGreen }
                        };
                        context.SchedulerDataStorage.AppointmentStatusSource = new DxSchedulerAppointmentStatusItem[] {
                            new DxSchedulerAppointmentStatusItem() { Id = 0, Caption = "Free", Color = Color.Yellow },
                            new DxSchedulerAppointmentStatusItem() { Id = 1, Caption = "Out of Office", Color = Color.MediumTurquoise }
                        };
                    };
                })
            })
        }
    }
}
```
[`DxSchedulerAppointmentLabelItem`]: xref:DevExpress.Blazor.DxSchedulerAppointmentLabelItem
[`DxSchedulerAppointmentStatusItem`]: xref:DevExpress.Blazor.DxSchedulerAppointmentStatusItem
