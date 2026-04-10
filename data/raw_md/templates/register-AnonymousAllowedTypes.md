### WinForms

* In applications created in v22.1+:

    **File**: _MySolution.Win\\Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp{8-13}
    // ...
    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    options.Events.OnSecurityStrategyCreated = securityStrategyBase => {
                        // ...
                        var securityStrategy = (SecurityStrategy)securityStrategyBase;
                        securityStrategy.AnonymousAllowedTypes.Add(typeof(Company));
                        securityStrategy.AnonymousAllowedTypes.Add(typeof(ApplicationUser));
                    };
                })
            // ...
        }
    }
    ```
    ***
* In applications that do not use application builders:

    **File**: _MySolution.Win_ (the `WinApplication` descendant's constructor).

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Security;
    using DevExpress.ExpressApp.Win;
    // ...
    public partial class CustomLogonParametersExampleWindowsFormsApplication : WinApplication {
        // ...
        public CustomLogonParametersExampleWindowsFormsApplication() {
            // ...
            ((SecurityStrategy)Security).AnonymousAllowedTypes.Add(typeof(Company));
            ((SecurityStrategy)Security).AnonymousAllowedTypes.Add(typeof(ApplicationUser));
        }
        // ...
    }
    ```
    ***