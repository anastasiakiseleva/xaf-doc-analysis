---
uid: DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes
name: ViewTypes
type: Property
summary: View Types that the Scheduler uses to display its data.
syntax:
  content: public IList<SchedulerViewType> ViewTypes { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.Blazor.SchedulerViewType}
    description: A list of [DevExpress.Blazor.SchedulerViewType](xref:DevExpress.Blazor.SchedulerViewType) objects.
seealso: []
---
The following code snippet specifies type and display order of Views in am XAF ASP.NET Core Blazor Scheduler:

**File:** _YourApplicationName.Blazor.Server\Startup.cs_

```csharp
public class Startup {
// ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Modules
                // ...
                .AddScheduler(options => {
                    options.ViewTypes.Remove(DevExpress.Blazor.SchedulerViewType.Timeline);
                })
                     .AddScheduler(options => {
                        options.ViewTypes = new[] {
                            DevExpress.Blazor.SchedulerViewType.Month,
                            DevExpress.Blazor.SchedulerViewType.Week
                        };
                    })
        })
    }
}
```