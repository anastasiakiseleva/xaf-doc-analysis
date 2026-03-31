---
uid: "404488"
title: Add Endpoints for Business Object Methods
seealso:
- linkId: "403551"
- linkId: "403715"
---

# Add Endpoints for Business Object Methods

The Web API Service allows you to automatically generate endpoints for business object methods that are decorated with an [ActionAttribute](xref:DevExpress.Persistent.Base.ActionAttribute). Such endpoints can accept a required number of parameters and are automatically displayed in the Swagger UI.

For general information on how to use the [ActionAttribute](xref:DevExpress.Persistent.Base.ActionAttribute) to generate actions in an XAF application and how to design business object methods so that they can be used with this attribute, refer to the following topic: [](xref:112619).

> [!IMPORTANT]
>
> We intentionally disable endpoints for business object methods in our Web API Service for security reasons. Since these methods may make sensitive modifications to data, every Web API Service developer must be cautious and must verify every business object before exposing its methods to consumers. Refer to the [Hide Action Methods from Web API](#hide-action-methods-from-web-api) section to see how to hide only certain endpoints generated for business object methods.

## Enable Automatic Generation of Endpoints for Action Methods

To enable automatic generation of endpoints for action methods, specify the `WebApiOptions.ConfigureBusinessObjectActionEndpoints` delegate in the application's _Statup.cs_ file. In this delegate, enable the `EnableActionEndpoints` setting:

**File:** _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{5}
services.AddXafWebApi(builder => {
    builder.ConfigureOptions(options => {
        // ...
        options.ConfigureBusinessObjectActionEndpoints(options => {
            options.EnableActionEndpoints = true;
        });
    });
    // ...
});
```

***

Additionally, ensure that the `MapXafEndpoints` method is invoked within the `UseEndpoints` method call (the [Template Kit](xref:405447) generates the required code automatically).

**File:** _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{5}
public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
    // ...
    app.UseEndpoints(endpoints => {
        // ...
        endpoints.MapXafEndpoints();
    });
}
```

***

When the `EnableActionEndpoints` option is enabled, the Web API Service registers endpoints for all methods decorated with an [ActionAttribute](xref:DevExpress.Persistent.Base.ActionAttribute). For example, consider the following business object implementation:

**File:** _MySolution.WebApi\BusinessObjects\Task.cs_

# [C#](#tab/tabid-csharp)

```csharp{6-11}
public class Task : BaseObject {
    public virtual string Description { get; set; }
    public virtual bool IsComplete { get; set; }
    public virtual DateTime DueDate { get; set; }

    [Action(Caption = "Postpone a task for N days", 
        ToolTip = "Postpone a task. The \"Days\" parameter specifies the number of days the task should be postponed.", 
        TargetObjectsCriteria = "Not [IsComplete]")]
    public void Postpone(PostponeParameters parameters) {
        DueDate += TimeSpan.FromDays(parameters.Days);
    }
}

public class PostponeParameters {
    public PostponeParameters() { Days = 1; }
    public uint Days { get; set; }
}
```
***

The endpoints generated for the `Postpone` method are reflected by the Swagger UI as follows:

![Action Endpoints in the Swagger UI](~/images/web-api-action-endpoints-swagger.png)

The `ActionAttribute`'s [Caption](xref:DevExpress.Persistent.Base.ActionAttribute.Caption) and [ToolTip](xref:DevExpress.Persistent.Base.ActionAttribute.ToolTip) parameter values are used to fill the endpoint's summary and description respectively, and the request body example correctly renders the names of the action's parameters.

![Execute an Action from Swagger UI](~/images/web-api-action-endpoints-swagger-execute.png)

## Change the Endpoint Base Path

Use the `BusinessObjectActionEndpointOptions.BasePath` option to customize the base URL path for the generated endpoints (the default setting is `"/api/odata"`). For example:

**File:** _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{6}
services.AddXafWebApi(builder => {
    builder.ConfigureOptions(options => {
        // ...
        options.ConfigureBusinessObjectActionEndpoints(options => {
            // ...
            options.BasePath = "/my-actions";
        });
    });
    // ...
});
```

***

In this configuration, endpoints are generated as shown below:

![Endpoints with a Custom Base Path](~/images/web-api-action-endpoints-custom-base-path.png)

## Hide Action Methods from Web API

Use the `BusinessObjectActionEndpointOptions.MethodFilter` property to filter out methods that you do not want to be available through Web API endpoints. This property can accept a predicate that takes a [](xref:System.Reflection.MethodInfo) object as a parameter. In your implementation of the predicate, you can use the `MethodInfo` object to decide whether to hide (filter out) specific methods.

**File:** _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{7}
services.AddXafWebApi(builder => {
    builder.ConfigureOptions(options => {
        // ...
        options.ConfigureBusinessObjectActionEndpoints(options => {
            // ...
            options.MethodFilter = m => {
                return !m.Name.Contains("MethodToHide");
            };
        });
    });
    // ...
});
```

***

## Limitations

- The Web API Service does not currently support [validation](xref:113684) for action method endpoints.