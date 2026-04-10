```csharp
namespace MySolution.Blazor.Server;

public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddRazorPages();
        services.AddServerSideBlazor();
        services.AddHttpContextAccessor();
        services.AddScoped<CircuitHandler, Services.Circuits.CircuitHandlerProxy>();
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            // ...
            builder.Modules
                // ...
                .AddNotifications(options => {
                    options.CanAccessPostponedItems = true;
                    options.NotificationsRefreshInterval = TimeSpan.FromSeconds(1);
                    options.NotificationsStartDelay = TimeSpan.FromSeconds(15);
                    options.ShowDismissAllAction = true;
                    options.ShowNotificationsWindow = false;
                    options.ShowRefreshAction = true;
                });
        });
    };
}
```