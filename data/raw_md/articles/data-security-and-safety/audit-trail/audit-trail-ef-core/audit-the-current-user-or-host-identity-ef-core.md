---
uid: "403117"
title: Audit the Current User or Host Identity (EF Core)
owner: Yekaterina Kiseleva
---
# Audit the Current User or Host Identity (EF Core)

The Audit Trail Module gets information on the user who changed an object from the [Security System](xref:113366). If your application uses custom authentication instead of the Security System, you can use the following properties to determine the user:
* [IPrincipalProvider.User.Identity.Name](xref:System.Security.Principal.IIdentity.Name*) in ASP.NET Core Blazor applications 
* [WindowsIdentity.Name](xref:System.Security.Principal.WindowsIdentity.Name) in WinForms applications

## ASP.NET Core Blazor

1. In the ASP.NET Core Blazor application project (_MySolution.Blazor.Server_), create the following new classes: 
    * `MyUserProvider` that implements the `IAuditUserProvider` interface
    * `MyAuditDefaultStringProvider` that is an `AuditDefaultStringProvider` descendant

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp.Security;
    using DevExpress.ExpressApp.Services.Localization;
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    
    public class MyUserProvider : IAuditUserProvider {
        private readonly IPrincipalProvider principalProvider;
        public MyUserProvider(IPrincipalProvider principalProvider) {
            this.principalProvider = principalProvider;
        }
        public object GetUser() {
            return principalProvider.User.Identity.Name;
        }
        public object GetUserId() {
            return principalProvider.User.Identity.Name;
        }
        public Type GetUserType() {
            return typeof(string);
        }
    }
    
    public class MyAuditDefaultStringProvider : AuditDefaultStringProvider {
        public MyAuditDefaultStringProvider(ICaptionHelperProvider captionHelperProvider)
            : base(captionHelperProvider) { }
        public override string GetDefaultString(object targetObject, Type objectType, object objectKey) {
            if(targetObject.GetType().Equals(typeof(string))) {
                return targetObject.ToString();
            }
            return base.GetDefaultString(targetObject, objectType, objectKey);
        }
    }
    ```
    ***
2. In the `Startup.ConfigureServices` method (the _MySolution.Blazor.Server\\Startup.cs_ file), do the following: 
    * add the custom implementation of the `IPrincipalProvider` service (`HttpContextPrincipalProvider`);
    * set the `AuditUserProviderType` and `AuditDefaultStringProviderType` properties to the custom `MyUserProvider` and `MyAuditDefaultStringProvider` types.

    **File**: _MySolution.Blazor.Server\\Startup.cs_

    # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
    ```csharp{7,20-23}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddScoped(typeof(IPrincipalProvider), typeof(HttpContextPrincipalProvider));
            services.AddXaf(Configuration, builder => {
                // ...
                builder.ObjectSpaceProviders
                    .AddEFCore(options => options.PreFetchReferenceProperties())
                        .WithAuditedDbContext(contexts => {
                            contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                                (serviceProvider, businessObjectDbContextOptions) => {
                                    // ...
                                },
                                (serviceProvider, auditHistoryDbContextOptions) => {
                                    // ...
                                },
                                auditTrailOptions => {
                                    auditTrailOptions.AuditUserProviderType = typeof(MyUserProvider);
                                    auditTrailOptions.AuditDefaultStringProviderType = typeof(MyAuditDefaultStringProvider);
                                });
                        })
                    // ...
    ```
    ***

> [!NOTE]
> The `MyUserProvider` and `MyAuditDefaultStringProvider` types are registered as scoped services. You can use the `IAuditUserProvider` and `IAuditDefaultStringProvider` interfaces to access them.

## WinForms

1. In the WinForms application project (_MySolution.Win_), create the following new classes: 
    * `MyUserProvider` that implements the `IAuditUserProvider` interface
    * `MyAuditDefaultStringProvider` that is an `AuditDefaultStringProvider` descendant

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp.Services.Localization;
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    using System.Security.Principal;
    
    public class MyUserProvider : IAuditUserProvider {
        public object GetUser() {
            return WindowsIdentity.GetCurrent().Name;
        }
        public object GetUserId() {
            return WindowsIdentity.GetCurrent().Name;
        }
        public Type GetUserType() {
            return typeof(string);
        }
    }
    
    public class MyAuditDefaultStringProvider : AuditDefaultStringProvider {
        public MyAuditDefaultStringProvider(ICaptionHelperProvider captionHelperProvider)
            : base(captionHelperProvider) { }
        public override string GetDefaultString(object targetObject, Type objectType, object objectKey) {
            if(targetObject.GetType().Equals(typeof(string))) {
                return targetObject.ToString();
            }
            return base.GetDefaultString(targetObject, objectType, objectKey);
        }
    }
    ```
    ***
2. In the `ApplicationBuilder.BuildApplication` method (_MySolution.Win\\Startup.cs_ file), set the `AuditUserProviderType` and `AuditDefaultStringProviderType` properties to the custom `MyUserProvider` and `MyAuditDefaultStringProvider` types:

    **File**: _MySolution.Win\\Startup.cs_

    # [Windows Forms](#tab/tabid-csharp-win)
    ```csharp{16-19}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            // ...
            builder.ObjectSpaceProviders
                .AddEFCore(options => options.PreFetchReferenceProperties())
                    .WithAuditedDbContext(contexts => {
                        contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                            (application, businessObjectDbContextOptions) => {
                                // ...
                            },
                            (application, auditHistoryDbContextOptions) => {
                                // ...
                            },
                            auditTrailOptions => {
                                auditTrailOptions.AuditUserProviderType = typeof(MyUserProvider);
                                auditTrailOptions.AuditDefaultStringProviderType = typeof(MyAuditDefaultStringProvider);
                            });
                    })
                    // ...
        }
        // ...
    }
    ```
    ***
