---
uid: "113480"
seealso: []
title: Custom Function Criteria Operators
owner: Eugeniy Burmistrov
---

# Custom Function Criteria Operators

Built-in [Function Criteria Operators](xref:113307) address the most common data management scenarios. Additionally, you can define custom Function Criteria Operators for those situations when built-in Operators do not suit your needs. For example, if you are frequently using a particular expression, and do not want to type it over and over again, you can implement a custom Function Criteria Operator.

## Implement the ICustomFunctionOperator Interface

You can define a Function Criteria Operator in a class that implements the [](xref:DevExpress.Data.Filtering.ICustomFunctionOperator) interface. 

> [!NOTE]
> The `ICustomFunctionOperator` implementation demonstrated in this section can only access the Security System through a static API (`SecuritySystem.Instance`). This API is not supported in some use cases (for example, in a [Web API Service](xref:403394)).
>
> See the following section for information on how to overcome this limitation: [Handle Criteria Customization Events (Access Security Information in the Web API Service)](#handle-criteria-customization-events-access-security-information-in-the-web-api-service).


The `ICustomFunctionOperator` interface exposes three members that allow you to specify a custom function and evaluate its value on the client side. The `Name` property specifies the name of the custom Operator. The `ResultType` method calculates the return type of the custom Function Criteria Operator, based on the types of passed arguments. The `Evaluate` method calculates the Function Criteria Operator's value based on the passed arguments.

# [C#](#tab/tabid-csharp)

```csharp
public class WeekAgoOperator : ICustomFunctionOperator {
    public string Name {
        get { return "WeekAgo"; }
    }
    public object Evaluate(params object[] operands) {
        return DateTime.Today.AddDays(-7);
    }
    public Type ResultType(params Type[] operands) {
        return typeof(DateTime);
    }
}
```

***

To use a custom Function Criteria Operator, you need to register it. To do this, first add a static constructor to the Operator. In the constructor, invoke the `CriteriaOperator.RegisterCustomFunction` method. The invocation of this method from the static constructor ensures that the Operator will not be registered twice accidentally.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
//...
public class WeekAgoOperator : ICustomFunctionOperator {
    //...
    static WeekAgoOperator() {
        WeekAgoOperator instance = new WeekAgoOperator();
        if (CriteriaOperator.GetCustomFunction(instance.Name) == null) {
            CriteriaOperator.RegisterCustomFunction(instance);
        }
    }
    public static void Register() { }
}
```

***

Next, invoke this constructor in the main module's static constructor.

**File:** _MySolution\Module.cs_

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MyModule : ModuleBase {
    static MyModule() {
        WeekAgoOperator.Register();
    }
}
```

***

After you register a Function Criteria Operator, you can use it anywhere it is required - in List View filters, Validation and Appearance rules, object-level security permissions, and so on. For example, you can configure a List View filter to use your Operator (for example, to select only the objects that were shipped within the last seven days).

``ShippingDate > WeekAgo()``

If your custom Function Criteria Operator is going to be used in server-side filtering, implement the [](xref:DevExpress.Data.Filtering.ICustomFunctionOperatorFormattable) interface as well.

Note that a custom Function Criteria Operator can be used in several applications. So, it is recommended that you implement all necessary custom Function Criteria Operators in a separate module.

> [!NOTE]
> See the [XAF - How to use data from a security user's property in a criterion](https://github.com/DevExpress-Examples/xaf-how-to-use-data-from-security-in-criterion) GitHub example for information on how to create a custom Function Criteria Operator.

## Handle Criteria Customization Events (Access Security Information in the Web API Service)

A Web API Service cannot use static API to access the security information from an `ICustomFunctionOperator` implementation. If your application contains a Web API Service and your use case scenario requires you to access the current user or get access to some additional services in criteria logic, use the following events to implement the function criteria operator:

[`OnCustomizeSecurityCriteriaOperator`](#use-the-oncustomizesecuritycriteriaoperator-event)
:   Allows you to write the criteria logic directly in the event handler.
[`OnCreateCustomSecurityFunctionPatcher`](#use-the-oncreatecustomsecurityfunctionpatcher-event-advanced)
:   Allows you to register your custom `SecurityFunctionPatcher` descendant (advanced).
 
You can access these events through the XAF Application Builder's `builder.Security.UseIntegratedMode` method parameter:

**File:** _MySolution.Blazor.Server\Startup.cs_ ( _MySolution.Win\Startup.cs_.)

# [C#](#tab/tabid-csharp)

```csharp
//..
builder.Security
    .UseIntegratedMode(options => {
        //...
        options.Events.OnCustomizeSecurityCriteriaOperator += (context) => { //...
        };
        options.Events.OnCreateCustomSecurityFunctionPatcher += (context) => { //...
        };
    })
    //...
```
***

### Use the OnCustomizeSecurityCriteriaOperator Event

The `OnCustomizeSecurityCriteriaOperator` delegate takes a parameter of the `CustomCriteriaOperatorPatcherContext` type. This parameter exposes the following properties:

`Security`
:   Gets a reference for the XAF Security (`ISecurityStrategyBase`).
`Operator`
:   Gets a source `CriteriaOperator`.
`Result` 
:   Gets or sets the resulting custom `CriteriaOperator`. If set to `null`, the source `CriteriaOperator` is used without any customizations. 
`ServiceProvider`
:   Gets a reference for the `IServiceProvider` service.

The code below demonstrates how to use the `OnCustomizeSecurityCriteriaOperator` event to customize a Function Criteria Operator in a basic use case scenario:

**File:** _MySolution.WebAPI\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
options.Events.OnCustomizeSecurityCriteriaOperator = context => {
    if(context.Operator is FunctionOperator functionOperator) {
        if(functionOperator.Operands.Count == 1 &&
        "CurrentOrgId".Equals((functionOperator.Operands[0] as ConstantValue)?.Value?.ToString(), StringComparison.InvariantCultureIgnoreCase)) {
            context.Result = new ConstantValue(((ApplicationUser)context.Security.User)?.Organization?.Oid ?? Guid.NewGuid());
        }
    }
};
```
***

This example code processes a custom `CurrentOrgId` function. You can use this function in a filter expression in a way similar to the `CurrentUserId` function as described in the [Function Criteria Operators](xref:113307) topic. The example code uses a custom `ApplicationUser` type with an additional `Organization` property. Data from that property is used in the custom function criteria operator's logic.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// or for XPO
using DevExpress.Persistent.BaseImpl.PermissionPolicy;

public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo {
    public Organization? Organization { get; set; }
    //...
}
```
***

The code sample below demonstrates how to use the custom `CurrentOrgId` function in a filter expression:

# [C#](#tab/tabid-csharp)

```csharp
IObjectSpace.FindObject<Organization>(CriteriaOperator.Parse("ID = CurrentOrgId()"))
```
***

In real applications, we recommend that you implement all required logic in a manner that allows you to reuse this implementation in an `OnCustomizeSecurityCriteriaOperator` event handler. This allows you to have a single Function Criteria Operator implementation that works across all platforms, including the Web API Service (with minimal additional configuration). The [Example](#example-reuse-an-icustomfunctionoperator-implementation-across-platforms) section demonstrates this technique.

### Use the OnCreateCustomSecurityFunctionPatcher Event (Advanced)

The `OnCreateCustomSecurityFunctionPatcherContext` delegate takes a parameter of the `OnCreateCustomSecurityFunctionPatcher` type. This parameter exposes the following properties:

`Security`
:   Gets a reference for the XAF Security (`ISecurityStrategyBase`).
`CustomSecurityFunctionPatcher`
:   Gets or sets a custom `ICriteriaOperatorPatcher`. If set to `null` the default `SecurityFunctionPatcher` is used.
`ServiceProvider`
:   Gets a reference for the `IServiceProvider` service.

The `OnCreateCustomSecurityFunctionPatcher` event allows you to create a custom `SecurityFunctionPatcher` descendant that implements the required criteria logic:

**File:** _MySolution.WebAPI\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
options.Events.OnCreateCustomSecurityFunctionPatcher = context => {
    context.CustomSecurityFunctionPatcher = new CustomSecurityFunctionPatcher(context.Security);
};
```
***

Where the `CustomSecurityFunctionPatcher` type extends the `SecurityFunctionPatcher` type:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;

public class CustomSecurityFunctionPatcher : SecurityFunctionPatcher {
    public CustomSecurityFunctionPatcher(ISecurityStrategyBase security) : base(security) { }
    //...
}
```
***

### Example: Reuse an ICustomFunctionOperator Implementation Across Platforms 

Assume you have the following `ICustomFunctionOperator` implementation in your solution:

# [C#](#tab/tabid-csharp)

```csharp{16}
public class GetCurrentUserName : ICustomFunctionOperator {
    static GetCurrentUserName() {
        GetCurrentUserName instance = new GetCurrentUserName();
        if (CriteriaOperator.GetCustomFunction(instance.Name) == null) {
            CriteriaOperator.RegisterCustomFunction(instance);
        }
    }
    public static void Register() { }

    public const string FUNCTION_NAME = "CurrentOrgId";
    public string Name {
        get { return FUNCTION_NAME; }
    }

    public object Evaluate(params object[] operands) {
        return ((ApplicationUser)SecuritySystem.Instance.User)?.Organization?.ID ?? Guid.Empty;
    }

    public Type ResultType(params Type[] operands) {
        return typeof(Guid);
    }
}
```

***

This custom function uses the static `SecuritySystem.Instance.User` property to access information about the currently logged in user (the user organization's ID). Because this static API is used, this custom function would not work in the Web API Service.

You can rewrite this implementation as follows so that the custom function can be reused in the Web API Service's [`OnCustomizeSecurityCriteriaOperator`](#use-the-oncustomizesecuritycriteriaoperator-event) event handler:

# [C#](#tab/tabid-csharp)

```csharp{18,23-29,33-35,40}
public class GetCurrentUserOrganizationIdFunction : ICustomFunctionOperator {
    static CurrentOrgIdFunction() {
        CurrentOrgIdFunction instance = new CurrentOrgIdFunction();
        if (CriteriaOperator.GetCustomFunction(instance.Name) == null) {
            CriteriaOperator.RegisterCustomFunction(instance);
        }
    }
    public static void Register() { }

    public const string FUNCTION_NAME = "CurrentOrgId";
    public string Name {
        get { return FUNCTION_NAME; }
    }

    // The `ICustomFunctionOperator.Evaluate` method implementation that accesses
    // security information through the static API (suitable for Blazor and WinForms).
    public object Evaluate(params object[] operands) {
        return CurrentOrgIdFunctionCore(SecuritySystem.Instance);
    }

    // Check if the current `ICustomFunctionOperator` can process a given custom function
    // specified by the `context` parameter passed from an `OnCustomizeSecurityCriteriaOperator` event handler.
    public static bool CanEvaluate(CustomCriteriaOperatorPatcherContext context) {
        if (context.Operator is FunctionOperator functionOperator) {
            return functionOperator.Operands.Count == 1 &&
                            FUNCTION_NAME.Equals((functionOperator.Operands[0] as ConstantValue)?.Value?.ToString(), StringComparison.InvariantCultureIgnoreCase);
        }
        return false;
    }

    // An additional `Evaluate` method overload that processes a custom function specified by the `context` parameter
    // passed from the Web API Service's `OnCustomizeSecurityCriteriaOperator` event handler.
    public static void Evaluate(CustomCriteriaOperatorPatcherContext context) {
        context.Result = new ConstantValue(CurrentOrgIdFunctionCore(context.Security));
    }

    // Implements logic used to obtain the required data from the Security System, process it,
    // and return the function's result
    // This method is called from both `Evaluate` method overloads.
    private static Guid CurrentOrgIdFunctionCore(ISecurityStrategyBase security) => ((ApplicationUser)security.User)?.Organization?.ID ?? Guid.Empty;

    public Type ResultType(params Type[] operands) {
        return typeof(Guid);
    }
}
```

***

With this refactoring, you can reuse your custom function from an [`OnCustomizeSecurityCriteriaOperator`](#use-the-oncustomizesecuritycriteriaoperator-event) event handler as shown below:

**File:** _MySolution.WebAPI\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{5-8}
builder.Security
    .UseIntegratedMode(options => {
        // ...
        options.Events.OnCustomizeSecurityCriteriaOperator = context => {
            if (GetCurrentUserOrganizationIdFunction.CanEvaluate(context)) {
                GetCurrentUserOrganizationIdFunction.Evaluate(context);
                return;
            }
            // if (OtherCustomFunction.CanEvaluate(context)) {
            //     OtherCustomFunction.Evaluate(context);
            //     return;
            // }
            // ...
        };
    })
    // ...
```
***

After this, the `CurrentOrgId` function will be available in the criteria operator syntax both on the Blazor/WinForms application side as well as the Web API Service side. For example, you can use it in the platform-agnostic module to define access permissions:

**File:** _MySolution.Module\DatabaseUpdate\Updater.cs_

# [C#](#tab/tabid-csharp)

```csharp
// ...
private PermissionPolicyRole CreateDefaultRole() {
    // ...
    defaultRole.AddObjectPermission<Employee>(SecurityOperations.ReadOnlyAccess, CriteriaOperator.Parse($"[{nameof(ApplicationUser.Organization.ID)}] == CurrentOrgId()").ToString(), SecurityPermissionState.Allow);
}
```
***

