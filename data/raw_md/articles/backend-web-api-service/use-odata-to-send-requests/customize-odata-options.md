---
uid: "403719"
title: 'Change the Entity Data Model Structure Exposed in OData'
owner: Eugeniy Burmistrov
---

# Change the Entity Data Model Structure Exposed in OData

This article describes techniques that you can use to customize the Web API Service's OData interface including the availability of particular endpoints and the structure of data written to the service's responses. 

## Change the Expansion Depth for Related Business Objects

To specify the [ODataValidationSettings.MaxExpansionDepth](xref:Microsoft.AspNet.OData.Query.ODataValidationSettings.MaxExpansionDepth*) option, follow the steps below:

* Implement a custom _ODataQueryValidator_ service to set @Microsoft.AspNet.OData.Query.ODataValidationSettings.MaxExpansionDepth*:

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using Microsoft.AspNetCore.OData.Query.Validator;
    using Microsoft.AspNetCore.OData.Query;
    // ...
    public class MyODataQueryValidator : ODataQueryValidator {
        public override void Validate(ODataQueryOptions options, ODataValidationSettings validationSettings){
            validationSettings.MaxExpansionDepth = 3;
            base.Validate(options, validationSettings);
        }
    }

    ```
    ***
* Replace the default _ODataQueryValidator_ service with the custom service in the _ConfigureServices_ method:

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public void ConfigureServices(IServiceCollection services) {
    // ...
    services.AddControllers().AddOData((options, serviceProvider) => {
        options
            .EnableQueryFeatures(100)
            .AddRouteComponents("api/odata", new EdmModelBuilder(serviceProvider).GetEdmModel(), odataServices => {
                odataServices.AddSingleton<ODataQueryValidator, MyODataQueryValidator>();
            });
        });
        // ...
    }
    ```
    ***

## Enable/Disable Web Actions for Business Objects

Use the techniques described below to enable or disable specific combinations of OData endpoints and HTTP verbs for business objects in your Web API Service application.

> [!IMPORTANT]
> We recommend that you configure Type, Object, and Member security permissions for your business objects. Ensure that your API controls data access or CRUD operations depending on the user role. In addition, you can use the techniques described in this section to prevent execution of specific web actions on a business object at the Swagger UI and OData query levels.

- Use the `WebApiOptions.ConfigureDataControllers` extension method to enable/disable web actions globally for all business objects:

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

    # [C#](#tab/tabid-csharp)

    ```csharp
    services.AddXafWebApi(builder => {
        builder.ConfigureOptions(options => {
            options.ConfigureDataControllers(b => {
                // Place your logic to customize the availability of web actions here.
                // You can use one of the following methods:
                // - b.WithActions(a => !a.ActionName.Contains("Ref"));
                // - b.WithActions(WebApiActions.PostEntity | WebApiActions.GetEntity);
                // - b.ReadOnly();
            });
        });
    }, Configuration);
    ```
    ***

- Use the `BusinessObjectConfigurator.ConfigureController` method to enable/disable web actions for a specific business object. If this method is called for a business object, it overrides all effects of `WebApiOptions.ConfigureDataControllers` for this object.

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

    # [C#](#tab/tabid-csharp)

    ```csharp
    services.AddXafWebApi(builder => {
        builder.ConfigureOptions(options => {
            options.BusinessObject<MyEntity>().ConfigureController(b => {
                // Place your logic to customize the availability of web actions here.
                // You can use one of the following methods:
                // - b.WithActions(a => !a.ActionName.Contains("Ref"));
                // - b.WithActions(WebApiActions.PostEntity | WebApiActions.GetEntity);
                // - b.ReadOnly();
            });
        });
    }, Configuration);
    ```
    ***

Both methods take a delegate as a parameter. The delegate's argument exposes the `WithActions` method, which has two overloads that you can use in the following ways:

- Allow web actions based on an arbitrary predicate:

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

    # [C#](#tab/tabid-csharp)

    ```csharp{2}
    options.BusinessObject<MyEntity>().ConfigureController(b => { 
        b.WithActions(a => !a.ActionName.Contains("Ref"));
    });
    ```
    ***

- Use predefined bit flags:

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

    # [C#](#tab/tabid-csharp)

    ```csharp{2}
    options.BusinessObject<MyEntity>().ConfigureController(b => { 
        b.WithActions(WebApiActions.PostEntity | WebApiActions.GetEntity);
    });
    ```
    ***

The `WebApiActions` enumeration defines the following bit flags:

| Flag                   | Description                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `GetEntity`            | Gets the specified object.                                                                                    |
| `GetEntities`          | Gets multiple objects.                                                                                         |
| `PostEntity`           | Creates a new object.                                                                                         |
| `PutEntity`            | Overwrites the specified object.                                                                              |
| `PatchEntity`          | Updates the specified object.                                                                                 |
| `DeleteEntity`         | Deletes the specified object.                                                                                 |
| `GetReference`         | Gets an object or a list of objects from the specified navigation or collection property.                     |
| `CreateReference`      | Associates an object with a navigation property or adds an object to a list property.                          |
| `DeleteNavigation`     | Unlinks an object from a navigation property.                                                           |
| `DeleteFromCollection` | Removes an object from a list property.                                                                       |
| `ReadOnly`             | Equivalent to `GetEntity` \| `GetEntities` \| `GetReference`                                                 |
| `EntityActions`        | Equivalent to `GetEntity` \| `GetEntities` \| `PostEntity` \| `PutEntity` \| `PatchEntity` \| `DeleteEntity` |
| `ReferenceActions`     | Equivalent to `GetReference` \| `CreateReference` \| `DeleteNavigation` \| `DeleteFromCollection`            |

You can also use the `ReadOnly` method to only allow read actions. This method has the same effect as the `ReadOnly` bit flag.

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C#](#tab/tabid-csharp)

```csharp{2}
options.BusinessObject<MyEntity>().ConfigureController(b => { 
    b.ReadOnly();
    // The above line is equivalent to:
    // b.WithActions(WebApiActions.ReadOnly);
});
```
***

The `AllActions` method allows you to enable all web actions for a specific business class when some of the actions are prohibited globally.

# [C#](#tab/tabid-csharp)

```csharp{2}
options.BusinessObject<MyEntity>().ConfigureController(b => { 
    b.AllActions();
});
```
***

For example, the image below demonstrates how the Swagger UI reflects a business object configured in read-only mode.

> [!IMPORTANT]
> Keep in mind that the hidden endpoints are not only invisible in Swagger, but are entirely unavailable through the OData interface. 

![Customize Web Actions](~/images/customize-odata-web-actions.png)

## Configure an OData Entity Type

Use one of the following techniques to customize the OData entity data model structure.

### Use the OnCustomizeEdmModel property

The `WebApiEvents.OnCustomizeEdmModel` property allows you to customize the OData entity data model structure at runtime (change types, properties, actions, and so on).

For example, you can implement custom logic that adds a property that was removed from the model by the [IgnoreDataMemberAttribute](xref:System.Runtime.Serialization.IgnoreDataMemberAttribute).

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)

```csharp
services.AddXaf(Configuration, builder => {
    //...
    builder.AddXafWebApi(webApiBuilder => {
        webApiBuilder.ConfigureOptions(options => {
            options.Events.OnCustomizeEdmModel = context => {
                context.ODataModelBuilder.AddEntityType(typeof(MyEntity)).AddProperty(typeof(MyEntity).GetProperty(nameof(MyEntity.MyProperty)));
            };
            //...
        });
    });
});

public class MyEntity : BaseObject {
    [IgnoreDataMember]
    public virtual int MyProperty { get; set; }
    //...
}
```
***

### Use the ODataModelBuilder

Implement the `DevExpress.ExpressApp.WebApi.Services.IEdmModelCustomizer` interface in a custom class. In your implementation of the class `CustomizeEdmModel` method, use the [ODataModelBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnet.odata.builder.odatamodelbuilder) to customize the OData entity data model based on your requirements.

You can register your `IEdmModelCustomizer` implementation after the `services.AddXafWebApi` call in the `ConfigureServices` method:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C# (Standalone WEB API Service)](#tab/tabid-csharp-standalone)

```csharp
services.AddXafWebApi(options => { /* ... */  }, Configuration);
services.TryAddEnumerable(ServiceDescriptor.Transient<IEdmModelCustomizer, CustomEdmModelCustomizer>());
```

# [C# (XAF Application Builder)](#tab/tabid-csharp-builder)

```csharp
services.AddXaf(Configuration, builder => {
    //...
    builder.AddXafWebApi(webApiBuilder => { /* ... */  });
});
services.TryAddEnumerable(ServiceDescriptor.Transient<IEdmModelCustomizer, CustomEdmModelCustomizer>());
```
***

For more information, refer to the following resources:

* [Model builders overview](https://learn.microsoft.com/en-us/odata/webapi/model-builder-abstract)
* Code of the built-in `IEdmModelCustomizer` implementers (`DateTimeNullableEdmModelCustomizer`, `PersistentAliasEdmModelCustomizer`, etc.) within the `DevExpress.ExpressApp.WebApi` library sources
* Support articles: 
  - [Web API - The "400 Bad Request" error occurs when you use properties with NotMappedAttribute in EF Core-based apps](https://supportcenter.devexpress.com/ticket/details/t1096425/web-api-the-400-bad-request-error-occurs-when-you-use-properties-with-notmappedattribute) 
  - [Web API Service - How to return or serialize a business object in a custom method/endpoint of API controller?](https://supportcenter.devexpress.com/ticket/details/t1041495/web-api-service-how-to-return-or-serialize-a-business-object-in-a-custom-method-endpoint)
  - [Web API - How to create a custom ODataController for each business object type to create own custom endpoints](https://supportcenter.devexpress.com/ticket/details/t1101266/web-api-how-to-create-a-custom-odatacontroller-for-each-business-object-type-to-create)

### Use the EntityTypeConfiguration

The `EntityTypeConfigurator.ConfigureODataEntityType` method allows you to directly access an [EntityTypeConfiguration\<TEntityType\>](xref:System.Data.Entity.ModelConfiguration.EntityTypeConfiguration`1) instance for your business class. Use the API exposed through the instance to configure the entity type.

For example, you can add a property that was hidden from the Entity Data Model by the [IgnoreDataMemberAttribute](xref:System.Runtime.Serialization.IgnoreDataMemberAttribute) as shown below.

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C#](#tab/tabid-csharp)

```csharp{3-15}
services.AddXafWebApi(builder => {
    builder.ConfigureOptions(options => {
        options.BusinessObject<MyEntity>().ConfigureEntityType(b => {
            // Add the current business class ignored property.
            b.ConfigureODataEntityType(d => d.Property(o => o.IgnoredProperty));
            // Add the base class ignored property.
            b.ConfigureODataEntityType(
                // You can access the `BaseType` properties sequentially to get to
                // an arbitrary ancestor's configurator (`d.BaseType.BaseType ...`)
                d => d.BaseType.AddProperty(
                    typeof(MyEntity)
                        .GetProperty(nameof(BusinessEntityBase.BaseClassIgnoredProperty))
                )
            );
        });
    });
}, Configuration);
```
***
