```csharp{11-13}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
using DevExpress.Persistent.BaseImpl.EF;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<YourSolutionNameWindowsFormsApplication>();
        builder.Modules
            // ...
            .AddOffice(options => {
                <:0:>
            })
        // ...
    }
    // ...
}
```