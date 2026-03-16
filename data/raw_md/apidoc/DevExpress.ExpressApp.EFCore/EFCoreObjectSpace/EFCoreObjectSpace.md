---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace
name: EFCoreObjectSpace
type: Class
summary: An [Object Space](xref:113707) used for data manipulation in [EF Core](https://learn.microsoft.com/en-us/ef/core/)-based applications that do not use the [Security System](xref:113366).
syntax:
  content: 'public class EFCoreObjectSpace : CompositeObjectSpace, IQuerySupport, ISupportServerViews, ISupportCriteriaCompiler, ISupportServerExpressionEvaluator, IDataLockingManager, IOptimisticLockHandlingManager'
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace._members
  altText: EFCoreObjectSpace Members
---
XAF creates Object Spaces of the `EFCoreObjectSpace` type if an application calls the @DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderBuilderExtensions.AddEFCore* method at startup.

In XAF application, use the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace) method to create this Object Space if the default Object Space Provider is @DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1.

The following example demonstrates how to use @DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 to create **EFCoreObjectSpace** in a non-XAF application. 

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.EFCore;
using Microsoft.EntityFrameworkCore;
using System;
// ...
class Program {
    static void Main() {
        var objectSpaceProvider = 
            new EFCoreObjectSpaceProvider<ApplicationDbContext>(
            (builder, _) => builder.UseConnectionString(
                ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString));
        IObjectSpace objectSpace = objectSpaceProvider.CreateObjectSpace();
        // ...
    }
}
```
***

You can find the full example in the following GitHub repository: [How to use the Integrated mode of the Security System in non-XAF applications (EF Core)](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/20.1.5+/EFCore). 

To learn more about Object Spaces, refer to the @DevExpress.ExpressApp.BaseObjectSpace class description.

### Important Note
The EF Core Object Space does not support top level [agregate functions](xref:4928#functions) in criteria. Use [Free Joins](xref:8130) instead.

# [C#](#tab/tabid-csharp1)
```csharp
// Invalid code:
// int totalNumber = (int)ObjectSpace.Evaluate(typeof(Department), CriteriaOperator.Parse("Sum([NumberOfEmployees])"), null);
// ...
// Valid code:
int totalNumber = (int)ObjectSpace.Evaluate(typeof(Department), CriteriaOperator.Parse("[<Department>].Sum([NumberOfEmployees])"), null);
```
***
