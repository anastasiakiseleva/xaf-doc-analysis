---
uid: DevExpress.ExpressApp.Security.SecurityStrategyComplex.NewUserRoleName
name: NewUserRoleName
type: Property
summary: Specifies the name of role which is assigned to auto-created users.
syntax:
  content: public string NewUserRoleName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the name of the role assigned to auto-created users.
seealso: []
---
For instance, users are auto-created when [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication is used and the [AuthenticationActiveDirectory.CreateUserAutomatically](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically) property is set to **true**.

You can use this property to update existing applications with Active Directory authentication. For this purpose, follow the steps below:

1. In Release mode (for production purposes), you can create security users and roles (other than Admins) according to your specific business needs in _SolutionName.Module\DatabaseUpdate\Updater.xx_. In this case, ensure that this code is not placed under the `#if DEBUG` preprocessor directive. Alternatively, you can create new users and roles at runtime directly from your production application UI or database.

1. Set the `SecurityStrategyComplex.NewUserRoleName` property to the name of the role you want to assign to new users automatically.

### WinForms Applications

**File:** _MySolution.Win\ApplicationBuilder.cs_

```csharp{8-9,13}
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
                // Assign the role with the 'Default' name to new users.
                options.NewUserRoleName = "Default"; 
                // ...
            })
            .UseWindowsAuthentication(options => {
                options.CreateUserAutomatically();
                // ...
            });
        // ...
    }
}
```

### ASP.NET Core Blazor Applications

**File:** _MySolution.Blazor.Server\Startup.cs_

```csharp{10-11,16}
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    // Assign the role with the 'Default' name to new users.
                    options.NewUserRoleName = "Default";
                    // ...
                })
                // ...
                .AddWindowsAuthentication(options => {
                    options.CreateUserAutomatically();
                    // ...
                });
            // ...
        });
    }
}
```

### Web API Applications

**File:** _MySolution.WebApi\Startup.cs_

```csharp{9-10,15}
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXafWebApi(builder => {
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    // Assign the role with the 'Default' name to new users.
                    options.NewUserRoleName = "Default";
                    // ...
                })
                // ...
                .AddWindowsAuthentication(options => {
                    options.CreateUserAutomatically();
                    // ...
                });
            // ...
        }, Configuration);
    }
}
```

### Middle Tier Server Applications

**File:** _MySolution.MiddleTierWebApi\Startup.cs_

```csharp{10-11,15}
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXafMiddleTier(Configuration, builder => {
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    // Assign the role with the 'Default' name to new users.
                    options.NewUserRoleName = "Default";
                    // ...
                })
                .AddWindowsAuthentication(options => {
                    options.CreateUserAutomatically();
                    // ...
                });
            // ...
        });
    }
}
```
