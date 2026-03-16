---
uid: "404668"
title: 'Get the Current Tenant in Code'
owner: Eugeniy Burmistrov
seealso:
- linkId: "404667"
---

# Get the Current Tenant in Code

## Code-Based (Programmatically)

To get the current tenant ID and/or name in application code, use the @DevExpress.ExpressApp.MultiTenancy.ITenantProvider service. You can use one of the following techniques to access this service:

- Use the application's Service Provider (available through `Application.ServiceProvider`, `ObjectSpace.ServiceProvider`, and so on).
    
    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp.MultiTenancy;
    // ...
    var tenantProvider = ObjectSpace.ServiceProvider.GetService<ITenantProvider>(); 
    Guid? currentTenantId = tenantProvider.TenantId;  
    string currentTenantName = tenantProvider.TenantName; 
    Tenant tenant = (Tenant)tenantProvider.TenantObject;
    ```
    ***

- Use [Dependency Injection](xref:404364) in constructors of controllers or custom services registered in the application.

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.MultiTenancy;
    // ...
    public class MyViewController : ViewController {
        ITenantProvider tenantProvider;
        // ...
        [ActivatorUtilitiesConstructor]
        public MyViewController(IServiceProvider serviceProvider) : base() {
            // ...
            tenantProvider = serviceProvider.GetService<ITenantProvider>();
        }
        protected override void OnActivated() {
            base.OnActivated();
            Guid? currentTenantId = tenantProvider.TenantId;
            string currentTenantName = tenantProvider.TenantName;
            Tenant tenant = (Tenant)tenantProvider.TenantObject;
            // ...
        }
    }
    ```
    ***

The @DevExpress.ExpressApp.MultiTenancy.ITenantProvider interface exposes the @DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantId and @DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantName properties, which return the current tenant's unique identifier and name respectively if a user is currently logged in to the [Tenant User Interface](xref:404436#glossary). If a user is not currently logged in or the [Host User Interface](xref:404436#glossary) is used, these properties return `null`.

The @DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantObject property returns the tenant object, which you can use to access the tenant data directly. Use this property to access additional fields of a custom tenant. For more information, refer to [Extend the Built-in Tenant Class with Custom Fields](xref:404667#extend-the-built-in-tenant-class-with-custom-fields). If a user is not currently logged in or the [Host User Interface](xref:404436#glossary) is used, this property returns `null`.

## Criteria-Based (Filtering)

In a [criteria operator expression](xref:4928), you can use the [CurrentTenantId](xref:113307#function-criteria-operators-basics) function to get the current tenant:

# [LINQ](#tab/tabid-csharp-linq)

```csharp
var criteria = CriteriaOperator.FromLambda<BusinessObject>(
    x => x.TenantId == (Guid?)CurrentTenantIdOperator.CurrentTenantId()
);
```

# [Typed](#tab/tabid-csharp-typed)

```csharp
var criteria = new BinaryOperator(
    new OperandProperty("TenantId"),
    new FunctionOperator(CurrentTenantIdOperator.OperatorName),
    BinaryOperatorType.Equal
);
```
# [String](#tab/tabid-csharp-string)

```csharp
'TenantId = CurrentTenantId()' 
```
***

This function returns the tenant ID if a user is logged in to the Tenant User Interface. If a user is not logged in or the Host User Interface is used, the function returns `null`.

[`ITenantProvider`]: xref:DevExpress.ExpressApp.MultiTenancy.ITenantProvider
[`TenantId`]: xref:DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantId
[`TenantName`]: xref:DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantName
[`TenantObject`]: xref:DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantObject