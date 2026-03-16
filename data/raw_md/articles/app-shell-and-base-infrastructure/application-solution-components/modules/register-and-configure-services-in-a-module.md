---
uid: "405025"
title: How to Register DI Services in a Custom Module with Application Builder Extensions
owner: Eugeniy Burmistrov
seealso:
  - linkId: '118046'
  - linkId: "118047"
---

# How to Register DI Services in a Custom Module with Application Builder Extensions

This topic describes how to implement an extension class that you can use to implement logic required to register and configure services within a module project. 

You can use this technique to achieve one of the following:

- In your [custom module](xref:405523), you can register and configure all services that the module requires in a centralized manner.
- In the application's main module (the _MySolution.Module_ project), you can register and configure all services that must be available across all platforms in the same configuration without the need to duplicate the registration code throughout the _Startup.cs_ files in platform-specific projects (_MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, and/or _MySolution.WebApi/Startup.cs_).

## Add Module Extensions to a Module

To implement module extensions, follow the steps described below: 

1. Add a static class (named `MySolutionModuleExtensions` in this example) to your module. Add a static `AddMySolutionModule` extension method to the class that extends the `IModuleBuilder` interface. This method will be used to register your module in the Application Builder code within the _Startup.cs_ files of application projects (see the [Register the Module in Platform-Specific Applications](#register-the-module-in-platform-specific-applications) section).

    **File**: _MySolution.Module/MySolutionModuleExtensions.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    public static class MySolutionModuleExtensions {
        public static IModuleBuilder<TBuilder> AddMySolutionModule<TBuilder>(
                this IModuleBuilder<TBuilder> builder)
                where TBuilder : IXafApplicationBuilder<TBuilder> {

            builder.Add<MySolutionModule>();
            IServiceCollection services = builder.Context.Services;
            services.AddScoped<MyService>();
            services.PostConfigure<MyServiceOptions>(options => {
                // ...
            });
            // ...
            // The method must return the `builder` instance.
            return builder;
        }
    }
    ```

    ***

    The `AddMySolutionModule` method receives the `builder` parameter, which is an instance of the Application Builder. Use `builder` to register the current module in the application and configure services.

2. For better abstraction, you can implement additional extension methods (for example, for `IServiceCollection`) to split the configuration logic based on the task.

   The following code snippet demonstrates how to implement a module extensions class that incapsulates logic required to configure application security and non-persistent object spaces. These two tasks are implemented as separate extension methods (`ConfigureSecurity` and `ConfigureNonPersistentDataProvider`).

    **File**: _MySolution.Module/MySolutionModuleExtensions.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp{9-10}
    public static class MySolutionModuleExtensions {
        public static IModuleBuilder<TBuilder> AddMySolutionModule<TBuilder>(
                this IModuleBuilder<TBuilder> builder)
                where TBuilder : IXafApplicationBuilder<TBuilder> {

            builder.Add<MySolutionModule>();

            IServiceCollection services = builder.Context.Services;
            services.ConfigureSecurity();
            services.ConfigureNonPersistentDataProvider();
            // ...

            return builder;
        }

        static IServiceCollection ConfigureSecurity(this IServiceCollection services) {
            services.PostConfigure<SecurityOptions>(options => {
                options.Lockout.Enabled = true;
                options.Lockout.MaxFailedAccessAttempts = 3;

                options.RoleType = typeof(PermissionPolicyRole);
                options.UserType = typeof(ApplicationUser);
                options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
                options.SupportNavigationPermissionsForTypes = false;
                options.Events.OnSecurityStrategyCreated += securityStrategy => {
                    ((SecurityStrategy)securityStrategy).PermissionsReloadMode = PermissionsReloadMode.CacheOnFirstAccess;
                };
            });
            return services;
        }

        static IServiceCollection ConfigureNonPersistentDataProvider(this IServiceCollection services) {
            services.AddSingleton<NonPersistentGlobalObjectStorage>();

            services.PostConfigure<ObjectSpaceProviderOptions>(options => {
                options.Events.OnObjectSpaceCreated += context => {
                    if(context.ObjectSpace is NonPersistentObjectSpace nonPersistentObjectSpace) {
                        new NonPersistentObjectSpaceExtender(context.ServiceProvider, nonPersistentObjectSpace);
                    }
                };
            });
            return services;
        }
    }
    ```

    ***

    You can find the full example in the _MainDemo.Module\NonPersistentObjects\MainModuleExtensions.cs_ file in the MainDemo demo that is located in the _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_ folder.

## Pass Services to a Module Constructor

If you need to access a service from code in a module's `Module.cs` file (for example, in your module class's `Setup` method), adjust your application code as follows:

1. Add an argument of the required service's type to your module's constructor:

    **File**: _MySolution.MyModule/Module.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    public sealed class MyModule : ModuleBase {
        MyService myService;
        public MyModule(MyService myService) {
            this.myService = myService;
            // ...
        }
        // ...
    }
    ```

    ***

2. Modify the module extensions code so that it passes the required service to the module constructor as shown below:

    **File**: _MySolution.Module/MySolutionModuleExtensions.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp{6-8}
    public static class MyModuleExtensions {
        public static IModuleBuilder<TBuilder> AddMyModule<TBuilder>(
                this IModuleBuilder<TBuilder> builder)
                where TBuilder : IXafApplicationBuilder<TBuilder> {

            builder.Add((serviceProvider) => {
                return new MyModule(serviceProvider.GetRequiredService<MyService>());
            });
            // ...
            return builder;
        }
    }
    ```

    ***

## Register the Module in Platform-Specific Applications

To register your module and execute all configuration logic implemented in the module's `MySolutionModuleExtensions` class within a platform-specific application's scope, add the following line to the Application Builder code in the application's _Startup.cs_ file:

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{4}
// ...
builder.Modules
    // ...
    .AddMySolutionModule()
```

***

If the _Startup.cs_ file already contains code that registers the module (`builder.Modules.Add<MySolutionModule>`), be sure to remove this code.