---
uid: DevExpress.ExpressApp.DC.OptimisticLockIgnoreAttribute
name: OptimisticLockIgnoreAttribute
type: Class
summary: Applies to EF Core business class. Disables [optimistic concurrency control](xref:405384).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property, Inherited = true)]
    public class OptimisticLockIgnoreAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.OptimisticLockIgnoreAttribute._members
  altText: OptimisticLockIgnoreAttribute Members
---
Use `OptimisticLockgnoreAttribute` to disable concurrency control in a business class or a property of an EF Core-based XAF application.

The following code snippet uses `OptimisticLockIgnoreAttribute` on a class level:

[!include[](~/templates/optimisticlockignoreclasslevel.md)]

The following code snippet uses `OptimisticLockIgnoreAttribute` on a property level:

[!include[](~/templates/optimisticlockignorepropertylevel.md)]

For more information about optimistic concurrency control in EF Core-based XAF applications, refer to the following topic: [](xref:405384).