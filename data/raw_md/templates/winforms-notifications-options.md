```csharp{14-16}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;

namespace YourApplicationName.Win;

public class Startup {

  public class ApplicationBuilder : IDesignTimeApplicationFactory {
      public static WinApplication BuildApplication(string connectionString) {
          var builder = WinApplication.CreateBuilder();
          builder.UseApplication<MySolutionWindowsFormsApplication>();
          builder.Modules
              // ...
              .AddNotifications(options => {
                  options.CanAccessPostponedItems = true;
                  options.NotificationsRefreshInterval = TimeSpan.FromSeconds(1);
                  options.NotificationsStartDelay = TimeSpan.FromSeconds(15);
                  options.ShowDismissAllAction = true;
                  options.ShowNotificationsWindow = false;
                  options.ShowRefreshAction = true;
              })
          // ...
      }
      // ...
  }
  // ...
}
```