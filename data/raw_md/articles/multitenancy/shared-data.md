---
uid: "405451"
title: Shared Data Support in a Multi-Tenant Application
seealso:
- linkId: 403669
- linkId: 113707
- linkId: 403858
---
# Shared Data Support in a Multi-Tenant Application

In multi-tenant applications, the host database can maintain shared business objects accessible to tenants. Shared data is helpful when storing master tables, such as currency, tax, and other global application settings. Tenant users can read these shared data tables, but cannot modify table data. Host UI administrators have complete CRUD control over host and tenant data through code.

## Key Security Points
* The host admin has full access to tenant business objects.
* A tenant user has read-only access to host shared business objects.
* A tenant user does not have access to another tenant's business objects.

## Access Host Shared Business Objects from a Tenant

Register host object types as shared to indicate that all tenants have read-only access to corresponding data. Data types associated with shared types must also be registered as shared types. Otherwise, access to associated objects is denied.

1. Use the [WithSharedBusinessObjects (EF Core)](xref:DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithSharedBusinessObjects(System.Type[])) / [WithSharedBusinessObjects (XPO)](xref:DevExpress.ExpressApp.MultiTenancy.Xpo.IMultiTenancyApplicationBuilder.WithSharedBusinessObjects(System.Type[])) method to register shared host object types in the application builder.

    # [Startup.cs](#tab/tabid-csharp)
    
    ```csharp
    public class Startup { 
        public void ConfigureServices(IServiceCollection services) { 
            // ... 
            builder.AddMultiTenancy() 
                .WithSharedBusinessObjects(typeof(SharedEntityType1), typeof(SharedEntityType2), ...) 
                // ... 
        } 
    } 
    ``` 
    ***

    If an application uses [middle-tier security](xref:404640), the shared types should be registered on the server and client side.

2. The list below contains methods that return the Object Space for shared data. When calling these methods, set the generic type parameter to the shared object type and the `tenantName` parameter to `null`. Once you obtain the Object Space, access required data in the same manner as you would do with regular business objects.

    * [XafApplication.CreateObjectSpace&lt;T>(tenantName)](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace``1(System.String))
    * [ObjectSpaceFactoryExtensions.CreateObjectSpace&lt;T>(objectSpaceFactory,tenantName)](xref:DevExpress.ExpressApp.ObjectSpaceFactoryExtensions.CreateObjectSpace``1(DevExpress.ExpressApp.IObjectSpaceFactory,System.String))
    * `IDataService.GetObjectSpace<T>(tenantName)`

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    var objectSpace = Application.CreateObjectSpace<SharedEntityType1>(null));
    ```
    ***

> [!tip]
> In tenant accounts, you can use `CreateObjectSpace` methods without the `tenantName` parameter to get the same result.

### Example

The following code sample registers the `TaxRate` type as a shared type and accesses `TaxRate` objects in code:

# [Startup.cs](#tab/tabid-csharp)

```csharp
builder.AddMultiTenancy() 
    .WithSharedBusinessObjects(typeof(TaxRate)) 
    // ...
``` 
***

# [C#](#tab/tabid-csharp)

```csharp
decimal CalculateTax() { 
    using (var objectSpace = Application.CreateObjectSpace<TaxRate>(null)) { 
        var taxRate = objectSpace.GetObjectsQuery<TaxRate>().FirstOrDefault(t => t.State == Customer.BillingAddressState); 
        if (taxRate != null) { 
            return TotalAmount * taxRate.Rate; 
        } 
    } 
    return 0; 
} 
```
***

> [!tip]
> You can find examples on how to access business objects shared by the host from a tenant in our [Outlook Inspired Demo](xref:113577#net-winforms--blazor-outlook-inspired-demo-multi-tenancysaas-readyxref404669) installed with XAF. Files to review:
> * _[!include[MainDemoLocationNote](~/templates/path-to-all-xaf-demos.md)]\OutlookInspiredDemo.NET.EFCore\CS\OutlookInspiredDemo.Blazor.Server\Startup.cs_
> * _[!include[MainDemoLocationNote](~/templates/path-to-all-xaf-demos.md)]\OutlookInspiredDemo.NET.EFCore\CS\OutlookInspiredDemo.Win\Startup.cs_
> * _[!include[MainDemoLocationNote](~/templates/path-to-all-xaf-demos.md)]\OutlookInspiredDemo.NET.EFCore\CS\OutlookInspiredDemo.MiddleTier\Startup.cs_
> * _[!include[MainDemoLocationNote](~/templates/path-to-all-xaf-demos.md)]\OutlookInspiredDemo.NET.EFCore\CS\OutlookInspiredDemo.Module\BusinessObjects\Order.cs_

> [!important]
> Host user interface mode does not support the following standard modules: <xref:404695#standard-module-support>


### Shared Business Objects in Lookup and Calculated Properties

* You can use shared business objects in calculated properties as [operands in Free Joins](xref:8130). Specify a @DevExpress.Xpo.PersistentAliasAttribute.

    The following code sample uses the shared `TaxRate` object to calculate the `Tax` property value.

    ```csharp
    [PersistentAlias("[<TaxRate>][State = ^.Customer.BillingAddressState].Single(Rate) * TotalAmount")] 
    public decimal Tax => EvaluateAlias<decimal>(); 
    ```
* You can assign a shared type to a **non-persistent** reference property to display the shared business objects in the lookup property editor. 

> [!note]
> If you use shared types with business object types in calculated or lookup properties, you must populate additional object spaces as described in the following method description: @DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.XafApplication).

## Access Tenant Data from the Host

The host has full access to tenant data. The host can use the following methods to obtain an Object Space for a specific tenant. 

* [XafApplication.CreateObjectSpace&lt;T>(tenantName)](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace``1(System.String))
* [ObjectSpaceFactoryExtensions.CreateObjectSpace&lt;T>(objectSpaceFactory,tenantName)](xref:DevExpress.ExpressApp.ObjectSpaceFactoryExtensions.CreateObjectSpace``1(DevExpress.ExpressApp.IObjectSpaceFactory,System.String))
* `IDataService.GetObjectSpace<T>(tenantName)`

# [C#](#tab/tabid-csharp)

```csharp
var objectSpace = Application.CreateObjectSpace<Type>('tenantName'));
```
***

> [!note]
> To access tenant data, the tenant database must exist and be updated; you cannot access databases that are non-existent or uninitialized.


## Limitations

* A shared type cannot be used in associations with regular business object types.
* A shared type cannot be additionally registered as a regular business type.
* Calculated properties based on shared types are not supported in Server, InstantFeedback, ServerView, and DataView [list view data access modes](xref:113683).
* Avoid obtaining the `IServiceProvider` instance from the `ObjectSpace` or `Session` instance used to access shared business objects, as services retrieved in this manner may function incorrectly.