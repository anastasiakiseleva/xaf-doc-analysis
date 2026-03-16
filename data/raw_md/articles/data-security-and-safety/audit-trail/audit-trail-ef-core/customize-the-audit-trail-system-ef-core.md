---
uid: "403115"
title: 'Miscellaneous Customizations of the Audit Trail System (EF Core)'
owner: Yekaterina Kiseleva
seealso:
  - linkId: "112782"
---
# Miscellaneous Customizations of the Audit Trail System (EF Core)

## Track Changes in Objects of Specific Types

The `AuditTrailOptions.AuditedTypePolicy` property allows you to audit changes on all persistent objects or on a list of objects. You can set this property to one of the following `AuditedTypePolicy` values:

`AuditAllExceptDeniedTypes` (default)
:   The Module audits changes on all objects except objects listed in the `AuditTrailOptions.DeclaredTypes` collection.

`AuditAllAllowedTypes`
:   The Module audits changes on objects listed in the `AuditTrailOptions.DeclaredTypes` collection. 

The `AuditTrailOptions.DeclaredTypes` collection contains the following types: [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference) and [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifferenceAspect). The following code snippet customizes this collection and enable audit for `CustomClass` objects only:

**Files**: _MySolution.Blazor.Server\\Startup.cs_, _MySolution.Win\\Startup.cs_.

# [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
```csharp{19-23}
using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                    .WithAuditedDbContext(contexts => {
                        contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                            (serviceProvider, businessObjectDbContextOptions) => {
                                // ...
                            },
                            (serviceProvider, auditHistoryDbContextOptions) => {
                                // ...
                            },
                            auditTrailOptions => {
                                auditTrailOptions.AuditedTypePolicy = AuditedTypePolicy.AuditAllAllowedTypes;
                                auditTrailOptions.DeclaredTypes.Clear();
                                auditTrailOptions.DeclaredTypes.Add(typeof(CustomClass));
                            });
                    })
                // ...
        })
    }
}
```

# [Windows Forms](#tab/tabid-csharp-win)
```csharp{16-20}
using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        // ...
        builder.ObjectSpaceProviders
            .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                .WithAuditedDbContext(contexts => {
                    contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                        (application, businessObjectDbContextOptions) => {
                            // ...
                        },
                        (application, auditHistoryDbContextOptions) => {
                            // ...
                        },
                        auditTrailOptions => {
                            auditTrailOptions.AuditedTypePolicy = AuditedTypePolicy.AuditAllAllowedTypes;
                            auditTrailOptions.DeclaredTypes.Clear();
                            auditTrailOptions.DeclaredTypes.Add(typeof(CustomClass));
                        });
                })
                // ...
    }
    // ...
}
```

***

## Change the String Representation of Audited Objects

The Module stores the string representation of modified objects in the database. In the UI, the Module displays these strings in the **Audited Object** column of the **Audit Event** View:

**ASP.NET Core Blazor**

![Change the String Representation of Audited Objects](~/images/MyAuditDefaultStringProvider.png)

**WinForms**

![Change the String Representation of Audited Objects](~/images/MyAuditDefaultStringProvider_WinForms.png)

The following steps demonstrate how to customize the string representation of `Person` objects.

1. Create the `AuditDefaultStringProvider` descendant, as shown below.

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using DevExpress.ExpressApp.Services.Localization;
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    
    public class MyAuditDefaultStringProvider : AuditDefaultStringProvider {
        public MyAuditDefaultStringProvider(ICaptionHelperProvider captionHelperProvider)
            : base(captionHelperProvider) { }
        public override string GetDefaultString(object targetObject, Type objectType, object objectKey) {
            if (objectType.Equals(typeof(Person))) {
                Person person = (Person)targetObject;
                return $"{person.FullName}";
            }
            return base.GetDefaultString(targetObject, objectType, objectKey);
        }
    }
    ```
    
    ***

2. Register the **MyAuditDefaultStringProvider** class as a custom string representation provider: 

    **Files**: _MySolution.Blazor.Server\\Startup.cs_, _MySolution.Win\\Startup.cs_.

    # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
    ```csharp{19-21}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.ObjectSpaceProviders
                    .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                        .WithAuditedDbContext(contexts => {
                            contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                                (serviceProvider, businessObjectDbContextOptions) => {
                                    // ...
                                },
                                (serviceProvider, auditHistoryDbContextOptions) => {
                                    // ...
                                },
                                auditTrailOptions => {
                                    auditTrailOptions.AuditDefaultStringProviderType = typeof(MyAuditDefaultStringProvider);
                                });
                        })
                    // ...
    ```

    # [Windows Forms](#tab/tabid-csharp-win)
    ```csharp{16-18}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            // ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                    .WithAuditedDbContext(contexts => {
                        contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                            (application, businessObjectDbContextOptions) => {
                                // ...
                            },
                            (application, auditHistoryDbContextOptions) => {
                                // ...
                            },
                            auditTrailOptions => {
                                auditTrailOptions.AuditDefaultStringProviderType = typeof(MyAuditDefaultStringProvider);
                            });
                    })
                    // ...
        }
        // ...
    }
    ```

    ***

The following help topic demonstrates the full example: [Audit the Current User or Host Identity (EF Core)](xref:403117).


## Save Specific Audit Records

This section demonstrates customization of the Audit Trail mechanism to prevent the storage of audit records with specific information such as the following:
* Information on modifications of properties with "Password" in their names
* Information on object deletions

Follow the steps below to implement this customization:

1. Create a custom `CustomAuditFilterDataProvider` class that implements the `IAuditFilterDataProvider` interface. 
2. In the `NeedToSave` method, return `true` for records that the Audit Module saves to the database: 

    **File**: _MySolution.Module\CustomAuditFilterDataProvider.cs_.
    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    //...
    public class CustomAuditFilterDataProvider : IAuditFilterDataProvider {
        public bool NeedToSave(IAuditDataItemPersistent auditDataItemPersistent) {
            if(auditDataItemPersistent.PropertyName?.Contains("Password") == true 
                || auditDataItemPersistent.OperationType == "ObjectDeleted") {
                return false;
            }
            return true;
        }
    }
    ```
    ***

    The following help topic lists all operation types: [Tracked Changes](xref:112782#tracked-changes).
3. Register the `CustomAuditFilterDataProvider` class as a custom data filter provider:

    **Files**: _MySolution.Blazor.Server\\Startup.cs_, _MySolution.Win\\Startup.cs_.

    # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)
    ```csharp{19-21}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.ObjectSpaceProviders
                    .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                        .WithAuditedDbContext(contexts => {
                            contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                                (serviceProvider, businessObjectDbContextOptions) => {
                                    // ...
                                },
                                (serviceProvider, auditHistoryDbContextOptions) => {
                                    // ...
                                },
                                auditTrailOptions => {
                                    auditTrailOptions.AuditFilterDataProviderType = typeof(CustomAuditFilterDataProvider);
                                });
                        })
                    // ...
            })
        }
    }
    ```

    # [Windows Forms](#tab/tabid-csharp-win)
    ```csharp{16-18}
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;

    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            // ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
                    .WithAuditedDbContext(contexts => {
                        contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                            (application, businessObjectDbContextOptions) => {
                                // ...
                            },
                            (application, auditHistoryDbContextOptions) => {
                                // ...
                            },
                            auditTrailOptions => {
                                auditTrailOptions.AuditFilterDataProviderType = typeof(CustomAuditFilterDataProvider);
                            });
                    })
                    // ...
        }
        // ...
    }
    ```

    ***

> [!NOTE]
> Alternatively, you can inherit the `AuditFilterDataProvider` class and override its `NeedToSave` virtual method instead of implementing the `IAuditFilterDataProvider` interface.

## Add Custom Data to the Audit Log

The Audit Trail Module also allows you to track user activity not related to persistent object changes. For example, you can save information on the use of Actions in your application. 

The following code snippet saves an audit record when a user executes the **`CustomController.CustomAction`** @DevExpress.ExpressApp.Actions.SimpleAction:

1. In the Action's `Execute` event handler, use one of the following extension methods to get an instance of `AuditTrailService`: 
    * `EFCoreObjectSpace.GetAuditTrailService`
    * `DbContext.AuditTrailService`

2. In the `AuditTrailService.SaveCustomData` method's delegate parameter, specify custom information that the Audit Trail Module should save. This delegate has the following parameters:
    * The `data` parameter that is an `IAuditDataItemPersistent` object. The Audit Trail Module saves this object in the database. You can customize this object before the Module saves it.
    * The `getWeakReference` parameter that is a delegate. You can use it to convert a persistent object to an `IEFCoreWeakReference` object. The Module can save this converted object as `AuditedObject`.

    > [!NOTE]
    > `AuditTrailService` exposes the `UserName` and `ModifiedOn` data automatically.
# [C#](#tab/tabid-csharp)

```csharp{14-18}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.EFCore;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
// ...
public class CustomController : ViewController<DetailView> {
    public CustomController() {
        SimpleAction customAction = new SimpleAction(this, "CustomAction", PredefinedCategory.View);
        customAction.Execute += CustomAction_Execute;
    }
    private void CustomAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // ...
        AuditTrailService auditTrailService = ((EFCoreObjectSpace)ObjectSpace).GetAuditTrailService();
        auditTrailService.SaveCustomData((data, getWeakReference) => {
            data.Description = "CustomAction is executed.";
            data.AuditedObject = getWeakReference(View.CurrentObject);
        });
    }
}
```
***
